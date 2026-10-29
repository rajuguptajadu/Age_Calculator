import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

# Set up page configuration
st.set_page_config(page_title="Advanced Age Calculator", page_icon="📅", layout="centered")

st.title("📅 Lifetime Age Calculator")
st.title("Design and Develop by RK Gupta")
st.write("Enter your date of birth (DD/MM/YYYY) to calculate your exact age. Supports dates over 100 years ago!")

# Get today's date
today = date.today()

# Configure the date input to allow selections up to 120 years back
min_date = date(today.year - 120, 1, 1)
default_date = date(today.year - 25, today.month, today.day)

# Date input component
dob = st.date_input(
    label="Select or type your Date of Birth (DD/MM/YYYY):",
    value=default_date,
    min_value=min_date,
    max_value=today,
    format="DD/MM/YYYY" # Enforces the DD/MM/YYYY display format
)

if dob:
    # Calculate the exact difference using relativedelta (handles varying month lengths & leap years)
    age_diff = relativedelta(today, dob)
    
    st.markdown("---")
    
    # Display the primary metric breakdown
    st.subheader("Your Exact Age Breakdown:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Years", value=age_diff.years)
    with col2:
        st.metric(label="Months", value=age_diff.months)
    with col3:
        st.metric(label="Days", value=age_diff.days)
        
    # Additional total stats for perspective
    st.markdown("### Total Time Elapsed:")
    total_days = (today - dob).days
    total_weeks = total_days // 7
    
    st.info(f"💡 You have lived for approximately **{total_days:,} days** (or about **{total_weeks:,} weeks**).")
    
    # Check if today is their birthday
    if dob.month == today.month and dob.day == today.day:
        st.balloons()
        st.success("🎉 Happy Birthday! Wishing you an incredible year ahead!")
