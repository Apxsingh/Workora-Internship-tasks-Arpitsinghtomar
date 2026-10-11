from pathlib import Path
import warnings

import pandas as pd
# pyrefly: ignore [missing-import]
import plotly.express as px
# pyrefly: ignore [missing-import]
import plotly.graph_objects as go
# pyrefly: ignore [missing-import]
import streamlit as st

warnings.filterwarnings("ignore", category=FutureWarning)

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Workora | Business Intelligence Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"

FILES = {
    "traffic": DATA_DIR / "web_traffic.csv",
    "churn": DATA_DIR / "customer_churn.csv",
    "ab": DATA_DIR / "checkout_ab_test.csv",
    "market": DATA_DIR / "regional_market.csv",
}

st.markdown(
    """
    <style>
      .block-container {padding-top: 1.5rem; padding-bottom: 2rem;}
      div[data-testid="stMetric"] {
        background: rgba(128,128,128,0.08);
        border: 1px solid rgba(128,128,128,0.20);
        padding: 16px 18px;
        border-radius: 12px;
      }
      .small-note {font-size: 0.88rem; opacity: 0.8;}
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# DATA LOADING AND CLEANING
# ============================================================
@st.cache_data
def load_data(file_path: str):
    """Load CSV and return a copy-ready DataFrame plus basic file metadata."""
    path = Path(file_path)
    if not path.exists():
        return pd.DataFrame(), f"File not found: {path}"
    try:
        df = pd.read_csv(path)
        return df, None
    except Exception as exc:
        return pd.DataFrame(), f"Could not read {path.name}: {exc}"


def normalize_yes_no(series):
    """Normalize common yes/no values while preserving missing values."""
    mapping = {
        "yes": "Yes", "y": "Yes", "true": "Yes", "1": "Yes",
        "no": "No", "n": "No", "false": "No", "0": "No",
    }
    return series.astype("string").str.strip().str.lower().map(mapping).fillna(
        series.astype("string").str.strip()
    )


def clean_traffic(raw):
    df = raw.copy()
    if df.empty:
        return df, {"rows_loaded": 0, "duplicate_rows_removed": 0}
    original_rows = len(df)
    duplicate_count = int(df.duplicated().sum())
    df = df.drop_duplicates()
    if "SessionID" in df:
        df = df.drop_duplicates(subset=["SessionID"], keep="first")
    if "Date" in df:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    for col in ["SessionDurationSec", "PageViews"]:
        if col in df:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    for col in ["StartedRegistration", "Registered", "Bounced"]:
        if col in df:
            df[col] = normalize_yes_no(df[col])
    if "Region" in df:
        df["Region"] = df["Region"].fillna("Unknown").astype(str).str.strip()
    return df, {
        "rows_loaded": original_rows,
        "duplicate_rows_removed": duplicate_count,
        "rows_after_cleaning": len(df),
    }


def clean_churn(raw):
    df = raw.copy()
    if df.empty:
        return df, {"rows_loaded": 0, "duplicate_rows_removed": 0}
    original_rows = len(df)
    duplicate_count = int(df.duplicated().sum())
    # CustomerID is documented as unique. Keep the first occurrence per ID.
    df = df.drop_duplicates()
    if "CustomerID" in df:
        df = df.drop_duplicates(subset=["CustomerID"], keep="first")
    numeric_cols = [
        "Age", "TenureMonths", "MonthlyChargesINR", "TotalChargesINR",
        "SupportTickets", "LatePayments",
    ]
    for col in numeric_cols:
        if col in df:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    if "Region" in df:
        df["Region"] = df["Region"].fillna("Unknown").astype(str).str.strip()
    for col in ["Churn", "AutoPay"]:
        if col in df:
            df[col] = normalize_yes_no(df[col])
    # No rows are removed solely for numeric outliers; these are disclosed
    # and can be explored without silently changing the population.
    return df, {
        "rows_loaded": original_rows,
        "duplicate_rows_removed": duplicate_count,
        "rows_after_cleaning": len(df),
        "missing_region_filled": int(raw["Region"].isna().sum()) if "Region" in raw else 0,
    }


def clean_ab(raw):
    df = raw.copy()
    if df.empty:
        return df, {"rows_loaded": 0, "duplicate_rows_removed": 0}
    original_rows = len(df)
    duplicate_count = int(df.duplicated().sum())
    df = df.drop_duplicates()
    if "VisitorID" in df:
        df = df.drop_duplicates(subset=["VisitorID"], keep="first")
    if "Timestamp" in df:
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    if "OrderValueINR" in df:
        df["OrderValueINR"] = pd.to_numeric(df["OrderValueINR"], errors="coerce")
    for col in ["CheckoutStarted", "Converted"]:
        if col in df:
            df[col] = normalize_yes_no(df[col])
    return df, {
        "rows_loaded": original_rows,
        "duplicate_rows_removed": duplicate_count,
        "rows_after_cleaning": len(df),
    }


def clean_market(raw):
    df = raw.copy()
    if df.empty:
        return df, {"rows_loaded": 0, "duplicate_rows_removed": 0}
    original_rows = len(df)
    duplicate_count = int(df.duplicated().sum())
    df = df.drop_duplicates()
    if "RegionID" in df:
        df = df.drop_duplicates(subset=["RegionID"], keep="first")
    numeric_cols = [
        "Latitude", "Longitude", "MonthlySearchDemand", "ExistingCompetitors",
        "MedianAnnualIncomeINR", "LeadConversionRate", "EstimatedAcquisitionCostINR",
    ]
    for col in numeric_cols:
        if col in df:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    if {"Latitude", "Longitude"}.issubset(df.columns):
        df = df[
            df["Latitude"].between(-90, 90) &
            df["Longitude"].between(-180, 180)
        ].copy()
    return df, {
        "rows_loaded": original_rows,
        "duplicate_rows_removed": duplicate_count,
        "rows_after_cleaning": len(df),
    }


raw_traffic, err_traffic = load_data(str(FILES["traffic"]))
raw_churn, err_churn = load_data(str(FILES["churn"]))
raw_ab, err_ab = load_data(str(FILES["ab"]))
raw_market, err_market = load_data(str(FILES["market"]))

load_errors = [
    error for error in [err_traffic, err_churn, err_ab, err_market] if error
]
if load_errors:
    st.error("Some datasets could not be loaded. Check that the CSV files are inside the data folder.")
    for error in load_errors:
        st.code(error)
    st.stop()

traffic, traffic_audit = clean_traffic(raw_traffic)
churn, churn_audit = clean_churn(raw_churn)
ab, ab_audit = clean_ab(raw_ab)
market, market_audit = clean_market(raw_market)


# ============================================================
# REUSABLE HELPERS
# ============================================================
def money(value):
    if pd.isna(value):
        return "₹0"
    return f"₹{value:,.0f}"


def pct(value):
    if pd.isna(value):
        return "—"
    return f"{value:.1f}%"


def multiselect_filter(label, options, key):
    options = sorted([str(x) for x in options if pd.notna(x)])
    return st.sidebar.multiselect(
        label, options, default=options, key=key
    )


def filter_by_values(df, col, selected):
    if df.empty or col not in df.columns or not selected:
        return df.iloc[0:0].copy() if not selected and col in df.columns else df.copy()
    return df[df[col].astype(str).isin(selected)].copy()


def date_filter(df, date_col, label):
    if df.empty or date_col not in df.columns:
        return df.copy(), None, None
    valid_dates = pd.to_datetime(df[date_col], errors="coerce").dropna()
    if valid_dates.empty:
        return df.copy(), None, None
    min_date = valid_dates.min().date()
    max_date = valid_dates.max().date()
    chosen = st.sidebar.date_input(
        label,
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        key=f"date_{date_col}",
    )
    if isinstance(chosen, (tuple, list)) and len(chosen) == 2:
        start_date, end_date = chosen
    else:
        start_date = end_date = chosen
    date_values = pd.to_datetime(df[date_col], errors="coerce")
    mask = date_values.dt.date.between(start_date, end_date)
    return df.loc[mask].copy(), start_date, end_date


def show_empty(message):
    st.info(message)


# ============================================================
# SIDEBAR FILTERS
# ============================================================
st.sidebar.title("📊 Dashboard Controls")
st.sidebar.caption("Filters apply to the relevant dataset and section.")

pages = [
    "Executive Overview",
    "Web Traffic & Acquisition",
    "Customer Churn",
    "Checkout A/B Test",
    "Regional Market",
    "Data Quality & Assumptions",
]
page = st.sidebar.radio("Dashboard page", pages)

st.sidebar.divider()
st.sidebar.subheader("Shared filters")

traffic_regions = traffic["Region"].dropna().astype(str).unique() if "Region" in traffic else []
traffic_region_selection = multiselect_filter(
    "Traffic region", traffic_regions, "traffic_regions"
)
traffic_sources = traffic["Source"].dropna().astype(str).unique() if "Source" in traffic else []
traffic_source_selection = multiselect_filter(
    "Traffic source", traffic_sources, "traffic_sources"
)
traffic_categories = traffic["LandingPage"].dropna().astype(str).unique() if "LandingPage" in traffic else []
traffic_category_selection = multiselect_filter(
    "Traffic landing page", traffic_categories, "traffic_pages"
)

traffic_filtered = traffic.copy()
if "Region" in traffic_filtered:
    traffic_filtered = filter_by_values(traffic_filtered, "Region", traffic_region_selection)
if "Source" in traffic_filtered:
    traffic_filtered = filter_by_values(traffic_filtered, "Source", traffic_source_selection)
if "LandingPage" in traffic_filtered:
    traffic_filtered = filter_by_values(traffic_filtered, "LandingPage", traffic_category_selection)
traffic_filtered, traffic_start, traffic_end = date_filter(
    traffic_filtered, "Date", "Traffic date range"
)

churn_regions = churn["Region"].dropna().astype(str).unique() if "Region" in churn else []
churn_region_selection = multiselect_filter(
    "Customer region", churn_regions, "churn_regions"
)
churn_categories = churn["SubscriptionType"].dropna().astype(str).unique() if "SubscriptionType" in churn else []
churn_category_selection = multiselect_filter(
    "Subscription category", churn_categories, "churn_categories"
)
churn_filtered = churn.copy()
if "Region" in churn_filtered:
    churn_filtered = filter_by_values(churn_filtered, "Region", churn_region_selection)
if "SubscriptionType" in churn_filtered:
    churn_filtered = filter_by_values(churn_filtered, "SubscriptionType", churn_category_selection)

ab_devices = ab["Device"].dropna().astype(str).unique() if "Device" in ab else []
ab_device_selection = multiselect_filter("Checkout device", ab_devices, "ab_devices")
ab_sources = ab["TrafficSource"].dropna().astype(str).unique() if "TrafficSource" in ab else []
ab_source_selection = multiselect_filter("Checkout source", ab_sources, "ab_sources")
ab_filtered = ab.copy()
if "Device" in ab_filtered:
    ab_filtered = filter_by_values(ab_filtered, "Device", ab_device_selection)
if "TrafficSource" in ab_filtered:
    ab_filtered = filter_by_values(ab_filtered, "TrafficSource", ab_source_selection)
ab_filtered, ab_start, ab_end = date_filter(
    ab_filtered, "Timestamp", "Checkout date range"
)

market_states = market["State"].dropna().astype(str).unique() if "State" in market else []
market_state_selection = multiselect_filter("Market state", market_states, "market_states")
market_categories = market["PopulationSegment"].dropna().astype(str).unique() if "PopulationSegment" in market else []
market_segment_selection = multiselect_filter(
    "Population segment", market_categories, "market_segments"
)
market_filtered = market.copy()
if "State" in market_filtered:
    market_filtered = filter_by_values(market_filtered, "State", market_state_selection)
if "PopulationSegment" in market_filtered:
    market_filtered = filter_by_values(market_filtered, "PopulationSegment", market_segment_selection)

st.sidebar.divider()
st.sidebar.caption("All records are synthetic learning data, not actual Workora business results.")


# ============================================================
# KPI CALCULATIONS
# ============================================================
revenue = 0.0
average_ticket = 0.0
active_users = 0
if not ab_filtered.empty and {"Converted", "OrderValueINR"}.issubset(ab_filtered.columns):
    converted_mask = ab_filtered["Converted"].astype(str).str.lower().eq("yes")
    converted_orders = ab_filtered.loc[converted_mask]
    revenue = pd.to_numeric(converted_orders["OrderValueINR"], errors="coerce").fillna(0).sum()
    positive_orders = converted_orders[
        pd.to_numeric(converted_orders["OrderValueINR"], errors="coerce").fillna(0) > 0
    ]
    average_ticket = (
        pd.to_numeric(positive_orders["OrderValueINR"], errors="coerce").mean()
        if not positive_orders.empty else 0.0
    )
if not traffic_filtered.empty:
    active_users = (
        traffic_filtered["SessionID"].nunique()
        if "SessionID" in traffic_filtered else len(traffic_filtered)
    )

churn_rate = 0.0
if not churn_filtered.empty and "Churn" in churn_filtered:
    churn_labels = churn_filtered["Churn"].astype(str).str.lower()
    valid_churn = churn_labels.isin(["yes", "no"])
    if valid_churn.any():
        churn_rate = churn_labels[valid_churn].eq("yes").mean() * 100


# ============================================================
# HEADER AND PAGES
# ============================================================
st.title("📊 Workora Business Intelligence Dashboard")
st.caption(
    "Interactive analytics for acquisition, engagement, customer retention, "
    "checkout experiments, and regional market demand."
)
st.warning(
    "Synthetic educational data only. Metrics describe these supplied datasets and must not be interpreted as real Workora business results."
)

if page == "Executive Overview":
    st.subheader("Executive Overview")
    st.caption("Each KPI uses its own relevant dataset; the figures are not a joined customer-level view.")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Revenue", money(revenue))
    c2.metric("Active Sessions*", f"{active_users:,}")
    c3.metric("Customer Churn Rate", pct(churn_rate))
    c4.metric("Average Order Value", money(average_ticket))

    st.caption(
        "*Active Sessions is the number of distinct filtered SessionIDs in web traffic, "
        "not a deduplicated count of people. Average Order Value is used as the available "
        "proxy for the requested Average Ticket Size."
    )

    left, right = st.columns(2)
    with left:
        st.markdown("#### Web traffic over time")
        if not traffic_filtered.empty and "Date" in traffic_filtered:
            daily = traffic_filtered.dropna(subset=["Date"]).groupby(
                pd.Grouper(key="Date", freq="D")
            ).agg(Sessions=("SessionID", "nunique"), PageViews=("PageViews", "sum")).reset_index()
            fig = px.line(daily, x="Date", y="Sessions", markers=True, title="Sessions by date")
            fig.update_layout(legend_title_text="")
            st.plotly_chart(fig, use_container_width=True)
        else:
            show_empty("No web traffic records match the current filters.")

    with right:
        st.markdown("#### Checkout conversion by variant")
        if not ab_filtered.empty and {"Variant", "Converted"}.issubset(ab_filtered.columns):
            conversion = ab_filtered.assign(
                ConvertedFlag=ab_filtered["Converted"].astype(str).str.lower().eq("yes")
            ).groupby("Variant", as_index=False).agg(
                Visitors=("VisitorID", "nunique"),
                Conversions=("ConvertedFlag", "sum"),
            )
            conversion["ConversionRatePct"] = (
                conversion["Conversions"] / conversion["Visitors"].replace(0, pd.NA) * 100
            )
            fig = px.bar(
                conversion, x="Variant", y="ConversionRatePct", text="ConversionRatePct",
                title="Conversion rate by A/B variant",
                labels={"ConversionRatePct": "Conversion rate (%)", "Variant": "Variant"},
            )
            fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
            st.plotly_chart(fig, use_container_width=True)
        else:
            show_empty("No checkout records match the current filters.")

    left, right = st.columns(2)
    with left:
        st.markdown("#### Churn by subscription type")
        if not churn_filtered.empty and {"SubscriptionType", "Churn"}.issubset(churn_filtered.columns):
            temp = churn_filtered.assign(
                ChurnFlag=churn_filtered["Churn"].astype(str).str.lower().eq("yes")
            )
            grouped = temp.groupby("SubscriptionType", as_index=False).agg(
                Customers=("CustomerID", "nunique"),
                Churned=("ChurnFlag", "sum"),
            )
            grouped["ChurnRatePct"] = grouped["Churned"] / grouped["Customers"].replace(0, pd.NA) * 100
            fig = px.bar(
                grouped, x="SubscriptionType", y="ChurnRatePct", color="SubscriptionType",
                title="Churn rate by subscription",
                labels={"ChurnRatePct": "Churn rate (%)", "SubscriptionType": "Subscription"},
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            show_empty("No churn records match the current filters.")

    with right:
        st.markdown("#### Regional market demand")
        if not market_filtered.empty and {"State", "MonthlySearchDemand"}.issubset(market_filtered.columns):
            grouped = market_filtered.groupby("State", as_index=False)["MonthlySearchDemand"].sum()
            grouped = grouped.sort_values("MonthlySearchDemand", ascending=False).head(10)
            fig = px.bar(
                grouped, x="State", y="MonthlySearchDemand",
                title="Top states by monthly search demand",
                labels={"MonthlySearchDemand": "Monthly search demand", "State": "State"},
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            show_empty("No market records match the current filters.")

elif page == "Web Traffic & Acquisition":
    st.subheader("Web Traffic & Acquisition")
    if traffic_filtered.empty:
        show_empty("No web traffic records match the selected filters.")
    else:
        sessions = traffic_filtered["SessionID"].nunique() if "SessionID" in traffic_filtered else len(traffic_filtered)
        registration_rate = (
            traffic_filtered["Registered"].astype(str).str.lower().eq("yes").mean() * 100
            if "Registered" in traffic_filtered else 0
        )
        bounce_rate = (
            traffic_filtered["Bounced"].astype(str).str.lower().eq("yes").mean() * 100
            if "Bounced" in traffic_filtered else 0
        )
        avg_duration = pd.to_numeric(traffic_filtered.get("SessionDurationSec"), errors="coerce").mean()
        avg_pages = pd.to_numeric(traffic_filtered.get("PageViews"), errors="coerce").mean()
        k1, k2, k3, k4, k5 = st.columns(5)
        k1.metric("Sessions", f"{sessions:,}")
        k2.metric("Registration rate", pct(registration_rate))
        k3.metric("Bounce rate", pct(bounce_rate))
        k4.metric("Avg. duration", f"{avg_duration:.0f} sec" if pd.notna(avg_duration) else "—")
        k5.metric("Avg. page views", f"{avg_pages:.2f}" if pd.notna(avg_pages) else "—")

        left, right = st.columns(2)
        with left:
            daily = traffic_filtered.dropna(subset=["Date"]).groupby(
                pd.Grouper(key="Date", freq="D")
            ).agg(Sessions=("SessionID", "nunique")).reset_index()
            fig = px.line(daily, x="Date", y="Sessions", markers=True, title="Daily sessions")
            st.plotly_chart(fig, use_container_width=True)
        with right:
            by_source = traffic_filtered.groupby("Source", as_index=False).agg(
                Sessions=("SessionID", "nunique"),
                Registrations=("Registered", lambda s: s.astype(str).str.lower().eq("yes").sum()),
            ).sort_values("Sessions", ascending=False)
            fig = px.bar(by_source, x="Source", y="Sessions", color="Source", title="Sessions by acquisition source")
            st.plotly_chart(fig, use_container_width=True)

        left, right = st.columns(2)
        with left:
            by_page = traffic_filtered.groupby("LandingPage", as_index=False).agg(
                Sessions=("SessionID", "nunique"),
                AvgPageViews=("PageViews", "mean"),
            ).sort_values("Sessions", ascending=False)
            fig = px.bar(by_page, x="LandingPage", y="Sessions", title="Landing page sessions")
            st.plotly_chart(fig, use_container_width=True)
        with right:
            source_registration = traffic_filtered.assign(
                RegisteredFlag=traffic_filtered["Registered"].astype(str).str.lower().eq("yes")
            ).groupby("Source", as_index=False).agg(
                Sessions=("SessionID", "nunique"),
                Registered=("RegisteredFlag", "sum"),
            )
            source_registration["RegistrationRatePct"] = (
                source_registration["Registered"] / source_registration["Sessions"].replace(0, pd.NA) * 100
            )
            fig = px.bar(source_registration, x="Source", y="RegistrationRatePct",
                         title="Registration rate by source",
                         labels={"RegistrationRatePct": "Registration rate (%)"})
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("#### Filtered session data")
        st.dataframe(traffic_filtered, use_container_width=True, hide_index=True)
        st.download_button(
            "Download filtered web traffic CSV",
            data=traffic_filtered.to_csv(index=False).encode("utf-8"),
            file_name="filtered_web_traffic.csv",
            mime="text/csv",
        )

elif page == "Customer Churn":
    st.subheader("Customer Churn & Retention")
    if churn_filtered.empty:
        show_empty("No customer records match the selected filters.")
    else:
        valid = churn_filtered["Churn"].astype(str).str.lower().isin(["yes", "no"])
        clean_churn_labels = churn_filtered.loc[valid].copy()
        churn_flag = clean_churn_labels["Churn"].astype(str).str.lower().eq("yes")
        total_customers = clean_churn_labels["CustomerID"].nunique()
        churned = int(churn_flag.sum())
        local_rate = churned / len(clean_churn_labels) * 100 if len(clean_churn_labels) else 0
        avg_monthly = pd.to_numeric(churn_filtered["MonthlyChargesINR"], errors="coerce").mean()
        avg_tenure = pd.to_numeric(churn_filtered["TenureMonths"], errors="coerce").mean()

        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Customers", f"{total_customers:,}")
        k2.metric("Churned customers", f"{churned:,}")
        k3.metric("Churn rate", pct(local_rate))
        k4.metric("Avg. monthly charges", money(avg_monthly))

        left, right = st.columns(2)
        with left:
            by_contract = churn_filtered.assign(
                ChurnFlag=churn_filtered["Churn"].astype(str).str.lower().eq("yes")
            ).groupby("ContractType", as_index=False).agg(
                Customers=("CustomerID", "nunique"), Churned=("ChurnFlag", "sum")
            )
            by_contract["ChurnRatePct"] = by_contract["Churned"] / by_contract["Customers"].replace(0, pd.NA) * 100
            fig = px.bar(by_contract, x="ContractType", y="ChurnRatePct", color="ContractType",
                         title="Churn rate by contract type",
                         labels={"ChurnRatePct": "Churn rate (%)"})
            st.plotly_chart(fig, use_container_width=True)
        with right:
            fig = px.box(churn_filtered, x="Churn", y="TenureMonths", color="Churn",
                         title="Customer tenure by churn status")
            st.plotly_chart(fig, use_container_width=True)

        left, right = st.columns(2)
        with left:
            fig = px.histogram(churn_filtered, x="MonthlyChargesINR", color="Churn",
                               nbins=25, barmode="overlay", title="Monthly charges by churn status")
            st.plotly_chart(fig, use_container_width=True)
        with right:
            by_payment = churn_filtered.assign(
                ChurnFlag=churn_filtered["Churn"].astype(str).str.lower().eq("yes")
            ).groupby("PaymentMethod", as_index=False).agg(
                Customers=("CustomerID", "nunique"), Churned=("ChurnFlag", "sum")
            )
            by_payment["ChurnRatePct"] = by_payment["Churned"] / by_payment["Customers"].replace(0, pd.NA) * 100
            fig = px.bar(by_payment, x="PaymentMethod", y="ChurnRatePct",
                         title="Churn rate by payment method",
                         labels={"ChurnRatePct": "Churn rate (%)"})
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("#### Customer data after cleaning")
        st.caption("Missing regions are labeled Unknown. Duplicate CustomerIDs retain their first row. Numeric outliers are not automatically removed.")
        st.dataframe(churn_filtered, use_container_width=True, hide_index=True)
        st.download_button(
            "Download filtered customer churn CSV",
            data=churn_filtered.to_csv(index=False).encode("utf-8"),
            file_name="filtered_customer_churn.csv",
            mime="text/csv",
        )

elif page == "Checkout A/B Test":
    st.subheader("Checkout A/B Test")
    if ab_filtered.empty:
        show_empty("No checkout records match the selected filters.")
    else:
        ab_analysis = ab_filtered.copy()
        ab_analysis["ConvertedFlag"] = ab_analysis["Converted"].astype(str).str.lower().eq("yes")
        ab_analysis["CheckoutStartedFlag"] = ab_analysis["CheckoutStarted"].astype(str).str.lower().eq("yes")
        visitors = ab_analysis["VisitorID"].nunique()
        conversions = int(ab_analysis["ConvertedFlag"].sum())
        conversion_rate = conversions / visitors * 100 if visitors else 0
        started = int(ab_analysis["CheckoutStartedFlag"].sum())
        checkout_rate = started / visitors * 100 if visitors else 0
        converted_values = pd.to_numeric(
            ab_analysis.loc[ab_analysis["ConvertedFlag"], "OrderValueINR"], errors="coerce"
        ).fillna(0)
        revenue_ab = converted_values.sum()
        avg_order = converted_values[converted_values > 0].mean() if (converted_values > 0).any() else 0

        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Visitors", f"{visitors:,}")
        k2.metric("Conversions", f"{conversions:,}")
        k3.metric("Conversion rate", pct(conversion_rate))
        k4.metric("Converted order revenue", money(revenue_ab))

        summary = ab_analysis.groupby("Variant", as_index=False).agg(
            Visitors=("VisitorID", "nunique"),
            Conversions=("ConvertedFlag", "sum"),
            CheckoutStarts=("CheckoutStartedFlag", "sum"),
            Revenue=("OrderValueINR", "sum"),
        )
        summary["ConversionRatePct"] = summary["Conversions"] / summary["Visitors"].replace(0, pd.NA) * 100
        summary["CheckoutStartRatePct"] = summary["CheckoutStarts"] / summary["Visitors"].replace(0, pd.NA) * 100
        summary["RevenuePerVisitorINR"] = summary["Revenue"] / summary["Visitors"].replace(0, pd.NA)

        left, right = st.columns(2)
        with left:
            fig = px.bar(summary, x="Variant", y="ConversionRatePct", color="Variant",
                         text="ConversionRatePct", title="Conversion rate by variant",
                         labels={"ConversionRatePct": "Conversion rate (%)"})
            fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
            st.plotly_chart(fig, use_container_width=True)
        with right:
            fig = px.bar(summary, x="Variant", y="CheckoutStartRatePct", color="Variant",
                         title="Checkout-start rate by variant",
                         labels={"CheckoutStartRatePct": "Checkout-start rate (%)"})
            st.plotly_chart(fig, use_container_width=True)

        left, right = st.columns(2)
        with left:
            fig = px.bar(summary, x="Variant", y="RevenuePerVisitorINR", color="Variant",
                         title="Revenue per visitor",
                         labels={"RevenuePerVisitorINR": "INR per visitor"})
            st.plotly_chart(fig, use_container_width=True)
        with right:
            fig = px.histogram(ab_analysis, x="OrderValueINR", color="Variant", barmode="overlay",
                               title="Order value distribution")
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("#### A/B variant summary")
        st.dataframe(summary, use_container_width=True, hide_index=True)
        st.info(
            "Interpret conversion differences descriptively. No claim of statistical significance is made. "
            "A formal test would need a pre-defined hypothesis, randomization checks, and a significance test."
        )
        st.download_button(
            "Download filtered A/B test CSV",
            data=ab_filtered.to_csv(index=False).encode("utf-8"),
            file_name="filtered_checkout_ab_test.csv",
            mime="text/csv",
        )

elif page == "Regional Market":
    st.subheader("Regional Market Demand & Opportunity")
    if market_filtered.empty:
        show_empty("No market records match the selected filters.")
    else:
        total_demand = pd.to_numeric(market_filtered["MonthlySearchDemand"], errors="coerce").sum()
        avg_conversion = pd.to_numeric(market_filtered["LeadConversionRate"], errors="coerce").mean() * 100
        avg_competitors = pd.to_numeric(market_filtered["ExistingCompetitors"], errors="coerce").mean()
        avg_acquisition = pd.to_numeric(market_filtered["EstimatedAcquisitionCostINR"], errors="coerce").mean()

        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Monthly search demand", f"{total_demand:,.0f}")
        k2.metric("Avg. lead conversion", pct(avg_conversion))
        k3.metric("Avg. competitors", f"{avg_competitors:.1f}" if pd.notna(avg_competitors) else "—")
        k4.metric("Avg. acquisition cost", money(avg_acquisition))

        st.markdown("#### Geographic demand map")
        map_df = market_filtered.dropna(subset=["Latitude", "Longitude"]).copy()
        if not map_df.empty:
            fig = px.scatter_map(
                map_df,
                lat="Latitude",
                lon="Longitude",
                color="MonthlySearchDemand",
                size="MonthlySearchDemand",
                hover_name="City",
                hover_data={
                    "State": True,
                    "MonthlySearchDemand": ":,",
                    "ExistingCompetitors": True,
                    "LeadConversionRate": ":.1%",
                    "EstimatedAcquisitionCostINR": ":,",
                    "Latitude": False,
                    "Longitude": False,
                },
                zoom=3.4,
                height=520,
                title="Market locations sized and colored by monthly search demand",
                map_style="open-street-map",
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            show_empty("No valid latitude/longitude pairs are available for the current selection.")

        left, right = st.columns(2)
        with left:
            state_demand = market_filtered.groupby("State", as_index=False)["MonthlySearchDemand"].sum()
            state_demand = state_demand.sort_values("MonthlySearchDemand", ascending=False).head(15)
            fig = px.bar(state_demand, x="MonthlySearchDemand", y="State", orientation="h",
                         title="Top states by search demand")
            st.plotly_chart(fig, use_container_width=True)
        with right:
            fig = px.scatter(
                market_filtered,
                x="ExistingCompetitors",
                y="LeadConversionRate",
                size="MonthlySearchDemand",
                color="PopulationSegment",
                hover_name="City",
                hover_data=["State", "EstimatedAcquisitionCostINR"],
                title="Competition vs. lead conversion",
                labels={"LeadConversionRate": "Lead conversion rate"},
            )
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("#### Highest-demand locations")
        top_locations = market_filtered.sort_values("MonthlySearchDemand", ascending=False).head(20)
        st.dataframe(top_locations, use_container_width=True, hide_index=True)
        st.download_button(
            "Download filtered regional market CSV",
            data=market_filtered.to_csv(index=False).encode("utf-8"),
            file_name="filtered_regional_market.csv",
            mime="text/csv",
        )

elif page == "Data Quality & Assumptions":
    st.subheader("Data Quality, Cleaning & Assumptions")
    st.markdown(
        """
        This dashboard uses four synthetic datasets supplied for learning. Each dataset represents a different
        analytical domain. They are not joined into a single customer-level table because no shared,
        documented key connects the records across all four files.
        """
    )

    audit_rows = []
    for name, audit in [
        ("web_traffic.csv", traffic_audit),
        ("customer_churn.csv", churn_audit),
        ("checkout_ab_test.csv", ab_audit),
        ("regional_market.csv", market_audit),
    ]:
        row = {"Dataset": name}
        row.update(audit)
        audit_rows.append(row)
    st.markdown("#### Cleaning audit summary")
    st.dataframe(pd.DataFrame(audit_rows).fillna("—"), use_container_width=True, hide_index=True)

    st.markdown("#### Missing values after cleaning")
    missing_rows = []
    for name, df in [
        ("web_traffic.csv", traffic),
        ("customer_churn.csv", churn),
        ("checkout_ab_test.csv", ab),
        ("regional_market.csv", market),
    ]:
        for col, count in df.isna().sum().items():
            if count:
                missing_rows.append({
                    "Dataset": name,
                    "Column": col,
                    "Missing values": int(count),
                    "Missing percentage": round(count / len(df) * 100, 2) if len(df) else 0,
                })
    if missing_rows:
        st.dataframe(pd.DataFrame(missing_rows), use_container_width=True, hide_index=True)
    else:
        st.success("No missing values remain in the loaded cleaned tables.")

    st.markdown("#### Documented rules and assumptions")
    st.markdown(
        """
        - **Web traffic:** parse `Date` as a date; convert session duration and page views to numeric;
          normalize Yes/No fields; fill missing regions with `Unknown`; remove exact duplicate rows and
          repeated `SessionID` values, retaining the first occurrence.
        - **Customer churn:** remove exact duplicate rows and repeated `CustomerID` values, retaining the first
          occurrence; convert numeric fields; fill missing `Region` values with `Unknown`; normalize `Churn`
          and `AutoPay` values. Numeric outliers are not automatically removed because the correct business
          thresholds are not specified.
        - **Checkout experiment:** parse `Timestamp`; convert `OrderValueINR` to numeric; normalize the
          `Converted` and `CheckoutStarted` fields; remove exact duplicate rows and repeated `VisitorID` values,
          retaining the first occurrence.
        - **Regional market:** convert metric columns to numeric; remove exact duplicate rows and repeated
          `RegionID` values, retaining the first occurrence; exclude records with invalid latitude/longitude.
        - **Revenue:** sum `OrderValueINR` for rows where `Converted` is Yes. The data pack does not provide
          a separate general ledger or transaction table.
        - **Average ticket size:** interpreted as average positive order value among converted visitors.
          Zero/non-positive order values are excluded from this average, but remain in the source data.
        - **Active users:** displayed as distinct filtered `SessionID` values and labeled **Active Sessions**,
          because the traffic dataset has no user identifier.
        - **Churn rate:** churned customers divided by records with a valid Yes/No churn label in the filtered
          customer dataset.
        - **Filters:** traffic dates/regions/sources/landing pages filter traffic analysis; checkout dates/devices/
          sources filter experiment analysis; customer region/subscription filters churn analysis; state/segment
          filters regional market analysis. Dates are not shared across unrelated datasets.
        - **No cross-dataset joins:** IDs such as `SessionID`, `CustomerID`, `VisitorID`, and `RegionID` identify
          records in different domains and are not assumed to match each other.
        - **A/B test:** conversion rates are descriptive. This dashboard does not claim statistical significance.
        - **Synthetic data:** all records are synthetic and must not be represented as real Workora business results.
        """
    )

    st.markdown("#### Dataset previews")
    with st.expander("Preview web traffic data"):
        st.dataframe(traffic.head(100), use_container_width=True, hide_index=True)
    with st.expander("Preview customer churn data"):
        st.dataframe(churn.head(100), use_container_width=True, hide_index=True)
    with st.expander("Preview checkout A/B test data"):
        st.dataframe(ab.head(100), use_container_width=True, hide_index=True)
    with st.expander("Preview regional market data"):
        st.dataframe(market.head(100), use_container_width=True, hide_index=True)

st.divider()
st.caption(
    "Workora Dashboard Data Pack · Synthetic data for educational use · "
    "Built with Streamlit, Pandas, and Plotly"
)
