import streamlit as st
import pandas as pd

# Initialize a pandas DataFrame to hold the data
columns = ["EPC/GWI", "Research", "Date", "Version/Revision", "Target Type", "Target Data Source", "Audience Name"]
data = pd.DataFrame(columns=columns)

# Function to generate the audience name
def generate_audience_name(epc_gwi, research, date, version, target_type, target_data_source):
    # Generate the audience name
    audience_name = f"{epc_gwi}_{research}_{date}_{target_type}_{target_data_source}_{version}"

    # Add the input and generated audience name to the dataframe
    global data
    new_row = pd.DataFrame([[epc_gwi, research, date, version, target_type, target_data_source, audience_name]],
                           columns=columns)
    data = pd.concat([data, new_row], ignore_index=True)

    return audience_name

# Streamlit app layout
st.title('Audience Name Generator')

# Input form
epc_gwi = st.text_input('EPC/GWI:')
research = st.text_input('Research:')
date = st.text_input('Date:')
version = st.text_input('Version/Revision:')
target_type = st.selectbox('Target Type', ['Behavioral', 'Contextual', 'Demographic', 'Geographic'])
target_data_source = st.text_input('Target Data Source:')

# Button to generate the audience name
if st.button('Generate Audience Name'):
    if epc_gwi and research and date and version and target_type and target_data_source:
        audience_name = generate_audience_name(epc_gwi, research, date, version, target_type, target_data_source)
        st.success(f'Generated Audience Name: {audience_name}')
    else:
        st.error("Please fill in all fields.")

# Display the table with all input data
st.subheader('Data Table')
st.dataframe(data)
