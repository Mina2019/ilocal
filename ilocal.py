
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
        "Browse Ads",
        "Post Ad",
        "My Ads",
        "My Business",
        "Profile"
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


st.subheader("🏪 All Local Businesses")

businesses = supabase.table("ilocal_businesses").select("*").execute()

if businesses.data:

    for business in businesses.data:

        st.write("###", business["business_name"])

        if business.get("business_type"):
            st.write("Category:", business["business_type"])

        if business.get("city"):
            st.write("Location:", business["city"])

        if business.get("description"):
            st.write(business["description"])

        st.divider()

else:
    st.info("No businesses registered yet.")

    

# ==========================================================
# BROWSE ADS
# ==========================================================

elif page == "Browse Ads":

    st.header("Browse Ads")

    st.info("Advertisements will appear here.")

# ==========================================================
# POST AD
# ==========================================================

elif page == "Post Ad":

    st.header("Post Advertisement")

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

    description = st.text_area("Description")

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

        st.success("Advertisement submitted.")

# ==========================================================
# MY ADS
# ==========================================================

elif page == "My Ads":

    st.header("My Advertisements")

    st.info("Your advertisements will appear here.")

# ==========================================================
# MY BUSINESS
# ==========================================================

elif page == "My Business":

    st.header("Business Profile")

    business_name = st.text_input("Business Name")

    phone = st.text_input("Phone")

    website = st.text_input("Website")

    address = st.text_input("Address")

    city = st.text_input("City")

    description = st.text_area("Business Description")

    if st.button("Save Business"):

        st.success("Business profile saved.")

# ==========================================================
# PROFILE
# ==========================================================

elif page == "Profile":

    st.header("Profile")

    st.info("User profile coming soon.")

