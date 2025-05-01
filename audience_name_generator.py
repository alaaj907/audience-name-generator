import streamlit as st
import pandas as pd

# Initialize a pandas DataFrame to hold the data
columns = ["System Source", "Audience", "Target Type", "Data Source", "Purpose", "Create Date", "Version", "Audience Name"]
data = pd.DataFrame(columns=columns)

# Function to generate the audience name
def generate_audience_name(system_source, audience, target_type, data_source, purpose, create_date, version):
    # Generate the audience name
    audience_name = f"{system_source}_{audience}_{target_type}_{data_source}_{purpose}_{create_date}_V{version}"

    # Add the input and generated audience name to the dataframe
    global data
    new_row = pd.DataFrame([[system_source, audience, target_type, data_source, purpose, create_date, version, audience_name]],
                           columns=columns)
    data = pd.concat([data, new_row], ignore_index=True)

    return audience_name

# Streamlit app layout
st.title('Audience Name Generator')

# Input form
system_source = st.selectbox('System Source', ['EPC PRSP', 'EPC DSC', 'GWI'])  # Dropdown for System Source (EPC PRSP, EPC DSC, GWI)
audience = st.text_input('Audience')  # Text input for short, descriptive name of the audience
target_type = st.selectbox('Target Type', ['BEH', 'CON', 'DEM', 'GEO', 'Multi'])  # Dropdown for Target Type (BEH, CON, DEM, GEO, Multi)
data_source = st.selectbox('Data Source', ['1P', '1P3P', '2P', '3P', 'NA'])  # Dropdown for Data Source (1P, 1P3P, 2P, 3P, NA)
purpose = st.selectbox('Purpose', ['ACT', 'RND', 'TST'])  # Dropdown for Purpose (ACT, RND, TST)
create_date = st.text_input('Create Date')  # Text input for sequential number indicating audience version (e.g., V1, V2)
version = st.text_input('Version')  # Text input for the version of the audience (e.g., V1, V2)

# Button to generate the audience name
if st.button('Generate Audience Name'):
    if system_source and audience and target_type and data_source and purpose and create_date and version:
        audience_name = generate_audience_name(system_source, audience, target_type, data_source, purpose, create_date, version)
        st.success(f'Generated Audience Name: {audience_name}')
    else:
        st.error("Please fill in all fields.")

# Display the table with all input data
st.subheader('Data Table')
st.dataframe(data)
