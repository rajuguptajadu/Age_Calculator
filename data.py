import streamlit as st
import pandas as pd
from datetime import datetime

# Set up the application page configuration
st.set_page_config(page_title="User Data Entry App", layout="centered")

st.title("📝 Employee Data Entry Portal")
st.write("Fill out the form below to register new records in the system.")

# Initialize an in-memory data store using session state
if "data_store" not in st.session_state:
    st.session_state.data_store = pd.DataFrame(
        columns=["Timestamp", "Full Name", "Department", "Experience (Years)", "Employment Status", "Join Date"]
    )

# 1. Create a containerized Data Entry Form
with st.form(key="entry_form", clear_on_submit=True):
    st.subheader("New Employee Information")
    
    # Text input for alphanumeric characters
    full_name = st.text_input("Full Name *", placeholder="John Doe")
    
    # Dropdown select box for pre-defined categories
    department = st.selectbox(
        "Department", 
        ["Human Resources", "Engineering", "Marketing", "Finance", "Sales"]
    )
    
    # Numeric input step widget
    experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=1, step=1)
    
    # Radio buttons for mutually exclusive selection
    status = st.radio("Employment Status", ["Full-Time", "Part-Time", "Contractor"], horizontal=True)
    
    # Date calendar picker element
    join_date = st.date_input("Target Join Date", min_value=datetime.today())
    
    # Form submission activator button
    submit_button = st.form_submit_button(label="Save Record")

# 2. Form processing execution 
if submit_button:
    if not full_name.strip():
        st.error("Submission failed: 'Full Name' is a required field.")
    else:
        # Create a dictionary of the newest entry row
        new_row = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Full Name": full_name,
            "Department": department,
            "Experience (Years)": int(experience),
            "Employment Status": status,
            "Join Date": join_date.strftime("%Y-%m-%d")
        }
        
        # Append the new row data into the existing DataFrame
        st.session_state.data_store = pd.concat(
            [st.session_state.data_store, pd.DataFrame([new_row])], 
            ignore_index=True
        )
        st.success(f"Success! Record for '{full_name}' has been captured safely.")

# 3. Display collected records dashboard
st.markdown("---")
st.subheader("📋 Registered Data Registry")

if not st.session_state.data_store.empty:
    # Render the interactive pandas dataframe table directly on screen
    st.dataframe(st.session_state.data_store, use_container_width=True)
    
    # Convert data log to CSV string formatting for browser export download
    csv_data = st.session_state.data_store.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="📥 Download Data Entry Log as CSV",
        data=csv_data,
        file_name="employee_records_log.csv",
        mime="text/csv",
    )
else:
    st.info("The local registry database is currently empty. Submit the form above to add logs.")
