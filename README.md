# audience-name-generator


This is an interactive web app built using Streamlit that allows users to input data and generate a unique audience name. The app uses various input fields, including EPC/GWI, Research, Date, Version/Revision, Target Type, and Target Data Source, and combines them into a structured audience name.

Features:
User Input Form: Users can input data for EPC/GWI, Research, Date, Version/Revision, Target Type, and Target Data Source.

Audience Name Generation: Automatically generates a unique audience name based on the inputs.

Data Table: Displays all input data and generated audience names in a table for easy tracking.

How to Use:
Open the app in your browser using the link provided.

Fill out the fields for EPC/GWI, Research, Date, Version/Revision, Target Type, and Target Data Source.

Click the Generate Audience Name button.

The app will display the generated Audience Name based on the inputs.

The table below will update with all inputs and the corresponding generated audience names.

Deployment:
This app is hosted on Streamlit Cloud for easy access and sharing. Anyone with the link can use the app without needing to install anything locally.

Access the App:
You can access the app using the following link:

Access the Audience Name Generator App

Requirements:
Python 3.x
Streamlit
Pandas

How to Deploy on Streamlit Cloud:
Create a GitHub repository and upload the Python script (audience_name_generator.py).

Log in to Streamlit Cloud and create a new app.

Select your GitHub repository and deploy the app.

Once deployed, Streamlit Cloud will provide a public link that can be shared with others.

To Run Locally:
If you prefer to run the app locally, you can follow these steps:

Clone the repository to your local machine.

Install the required libraries:

bash:
pip install -r requirements.txt

Run the app:
bash:
streamlit run audience_name_generator.py
