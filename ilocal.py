# ==========================================================
# iLocal
# Local Business Advertising Platform
# Streamlit + Supabase
# ==========================================================
import streamlit as st
from supabase import create_client

SUPABASE_URL = "https://xbdlzzjparnvrsvsjfca.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhiZGx6empwYXJudnJzdnNqZmNhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc5MzQ0NDYsImV4cCI6MjA5MzUxMDQ0Nn0.h0AxxjVJZWpTCkywH-Et30TCn4nKQwGXfvmPbVmgZJo"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------
st.set_page_config(
    page_title="iLocal",
    page_icon="📍",
    layout="wide"
)
# ----------------------------------------------------------
# Header
# ----------------------------------------------------------
st.title("📍 iLocal")
st.caption("Local Business Advertising Platform")
# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------
page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Shops",
        "Browse Ads",
        "My Ads",
        "My Profile",
    ]
)
# ==========================================================
# HOME
# ==========================================================
if page == "Home":
    st.header("Welcome to iLocal")
    search = st.text_input("Search")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("Restaurants", use_container_width=True)
        st.button("Home Services", use_container_width=True)
        st.button("Automotive", use_container_width=True)
    with col2:
        st.button("Shopping", use_container_width=True)
        st.button("Health", use_container_width=True)
        st.button("Beauty", use_container_width=True)
    with col3:
        st.button("Education", use_container_width=True)
        st.button("Real Estate", use_container_width=True)
        st.button("More", use_container_width=True)
    # ------------------------------------------------------
    # Current Businesses
    # ------------------------------------------------------
    st.subheader("🏪 Current Local Businesses")
    try:
        businesses = (
            supabase
            .table("ilocal_businesses")
            .select("*")
            .execute()
        )
        for business in businesses.data:
            st.write(
                "### " + business["business_name"]
            )
            if business.get("business_type"):
                st.write(
                    "Category:",
                    business["business_type"]
                )
            if business.get("city"):
                st.write(
                    "Location:",
                    business["city"]
                )
            if business.get("description"):
                st.write(
                    business["description"]
                )
            if st.button(
                "Delete",
                key=business["business_id"]
            ):
                try:
                    supabase.table(
                        "ilocal_businesses"
                    ).delete().eq(
                        "business_id",
                        business["business_id"]
                    ).execute()
                    st.success(
                        "Business deleted."
                    )
                    st.rerun()
                except Exception as e:
                    st.error(e)
            st.divider()
#        else:
#            st.info(
#                "No businesses registered yet."
#            )
    except Exception as e:
        st.error(e)
# ==========================================================
# SHOPS
# ==========================================================
elif page == "Shops":
    st.header("🏪 Local Shops")
    try:
        businesses = (
            supabase
            .table("ilocal_businesses")
            .select("*")
            .execute()
        )
        if businesses.data:
            for business in businesses.data:
                st.write(
                    "### " + business["business_name"]
                )
                if business.get("business_type"):
                    st.write(
                        "Category:",
                        business["business_type"]
                    )
                if business.get("city"):
                    st.write(
                        "Location:",
                        business["city"]
                    )
                st.divider()
        else:
            st.info(
                "No businesses registered yet."
            )
    except Exception as e:
        st.error(e)
# ==========================================================
# BROWSE ADS
# ==========================================================
elif page == "Browse Ads":
    st.header("Browse Ads")
    st.info("Advertisements will appear here.")
# ==========================================================
# MY ADS
# ==========================================================
elif page == "My Ads":
    st.header("My Advertisements")
    # ------------------------------------------------------
    # Check if any businesses exist
    # ------------------------------------------------------
    businesses = (
        supabase
        .table("ilocal_businesses")
        .select("*")
        .order("business_name")
        .execute()
    )
    if not businesses.data:
        st.warning(
            "Please create your Business Profile first."
        )
        st.stop()
    # ------------------------------------------------------
    # Select Business
    # ------------------------------------------------------
    business_names = [
        business["business_name"]
        for business in businesses.data
    ]
    selected_business = st.selectbox(
        "Select Your Business",
        business_names
    )
    st.divider()
    # ------------------------------------------------------
    # Subscription
    # ------------------------------------------------------
    st.subheader("Subscription")
    subscription_active = st.checkbox(
        "Subscription Active (Temporary)"
    )
    if not subscription_active:
        st.warning(
            "Please subscribe on the Profile page before posting advertisements."
        )
        st.stop()
    st.success("Subscription Active")
    st.divider()
    # ------------------------------------------------------
    # Advertisement Form
    # ------------------------------------------------------
    st.subheader("Post Advertisement")
    title = st.text_input("Title")
    category = st.selectbox(
        "Category",
        [
            "Restaurant",
            "Home Services",
            "Automotive",
            "Health",
            "Beauty",
            "Education",
            "Shopping",
            "Other"
        ]
    )
    description = st.text_area(
        "Description"
    )
    price = st.number_input(
        "Price",
        min_value=0.0,
        step=1.0
    )
    image = st.file_uploader(
        "Photo",
        type=["jpg", "jpeg", "png"]
    )
    if st.button("Post Advertisement"):
        # Save advertisement to Supabase here later
        st.success(
            "Advertisement posted successfully."
        )
    st.divider()
    # ------------------------------------------------------
    # Current Advertisements
    # ------------------------------------------------------
    st.subheader("My Current Advertisements")
    st.info(
        "Your advertisements will appear here once the ads table is connected."
    )
# ==========================================================
# MY PROFILE
# ==========================================================
elif page == "My Profile":
    st.header("Business Profile")
    business_name = st.text_input("Business Name")
    business_type = st.selectbox(
    "Business Type",
    [
        "Restaurant",
        "Home Services",
        "Automotive",
        "Shopping",
        "Health",
        "Beauty",
        "Education",
        "Real Estate",
        "Sports",
        "Other"
    ]                            )
    phone = st.text_input("Phone")
    website = st.text_input("Website")
    address = st.text_input("Address")
    city = st.text_input("City")
    description = st.text_area("Business Description")
    if st.button("Save Business"):
        try:
            result = supabase.table(
                "ilocal_businesses"
            ).insert(
                {
                    "business_name": business_name,
                    "business_type": business_type,
                    "description": description,
                    "phone": phone,
                    "website": website,
                    "address": address,
                    "city": city
                }
            ).execute()

            st.success(
                "Business saved successfully."
            )
        except Exception as e:
            st.error(e)
    # ------------------------------------------------------
    # SUBSCRIPTION
    # ------------------------------------------------------
    st.divider()
    st.subheader("Current Plan")
    st.info(
        "Free Business Profile"
    )
    st.subheader("Upgrade to Pro")
    st.write(
        """
        **Pro Subscription**
        • $100/month
        • Up to 100 active advertisements
        • Advertisements appear on Browse Ads
        • Ability to edit and delete advertisements
        """
    )
    st.subheader("Stripe Subscription")
    st.info(
        "Stripe payment"
    )
    st.link_button(
        "Pay $100 and Post Ads",
        "https://buy.stripe.com/3cIdR94mI6XyaG7aR9gIo01"
    )
    st.subheader("Subscription Status")
    st.warning(
        "Inactive"
    )





