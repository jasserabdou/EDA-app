import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
import base64


def main():
    st.title('EDA App 🚀')
    uploaded_file = st.file_uploader(
        "Upload your dataset ...", type=[
            ".csv", ".xls", ".xlsx)"])

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        if file_extension in ["csv", "xls", "xlsx"]:
            df = read_data(uploaded_file, file_extension)
            if df is not None:
                EDA_dataset = ProfileReport(df)
                st_profile_report(EDA_dataset)
            else:
                st.write("Error: Unable to read the uploaded file.")
        else:
            st.write("Please upload a valid CSV or Excel (.xls)")
    else:
        st.write("Upload a file to get started with EDA.")


def read_data(uploaded_file, file_extension):
    try:
        if file_extension == "csv":
            df = pd.read_csv(uploaded_file)
        elif file_extension == "xls":
            df = pd.read_excel(uploaded_file)
        else:
            st.write(
                "Error: JSON files are not supported in this version of the code.")
            return None
        return df
    except Exception as e:
        st.write("Error:", e)
        return None


def st_profile_report(profile_report):
    st.title("EDA Report")
    tmp_file = f"./temp_profile_report.html"
    profile_report.to_file(tmp_file)
    with open(tmp_file, "r") as f:
        data = f.read()
    st.components.v1.html(data, height=1000)
    st.text("Download the HTML report")
    with open(tmp_file, "rb") as f:
        href = f"<a href='data:file/html;base64,{base64.b64encode(f.read()).decode()}' download='profile_report.html'>Click here</a> (right-click and save as &lt;profile_report.html&gt;)"
    st.markdown(href, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
