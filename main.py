# imports
import streamlit as st
import pandas as pd 
import os
from io import BytesIO

# set up our app
st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization")

# file uploader
uploaded_file = st.file_uploader("Upload your files (CSV or Excel Files):", type=["csv", "xlsx"], accept_multiple_files=True) 

if uploaded_file:
    for file in uploaded_file:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue
   
        # display info about the file 
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File size:** {file.size/1024:.2f} KB")

        # Show 5 rows of our dataframe 
        st.write("Preview the Head of the DataFrame")
        st.dataframe(df.head())

        # options for data cleaning 
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove duplicates from the file : {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates removed!")

            with col2:
                if st.button(f"Fill missing values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing values have been filled!")
        
            st.subheader("Select Columns to keep")
            columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=list(df.columns))
            df = df[columns]

            # Data visualization 
            st.subheader("📊 Data Visualization")
            if st.checkbox(f"Show visualization for {file.name}"):
                numeric_cols = df.select_dtypes(include=['number'])
                if not numeric_cols.empty:
                    st.bar_chart(numeric_cols.iloc[:, :2])
                else:
                    st.warning("No numeric columns available for visualization")

            # File Conversion options
            st.subheader("Conversion Options")
            conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
            if st.button(f"Convert {file.name}"):  
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False) 
                    file_name = file.name.replace(file_ext, ".csv")
                    mime_type = "text/csv"
                elif conversion_type == "Excel":
                    df.to_excel(buffer, index=False) 
                    file_name = file.name.replace(file_ext, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                buffer.seek(0)

                st.download_button(
                    label=f"Download {file.name} as {conversion_type}",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type
                )

    st.success("All files processed successfully!")
