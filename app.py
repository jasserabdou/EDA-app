import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report as st_pp_report


@st.cache_data
def read_data(uploaded_file, file_extension):
    try:
        if file_extension == "csv":
            df = pd.read_csv(uploaded_file)
        elif file_extension == "xls":
            df = pd.read_excel(uploaded_file)
        else:
            st.warning(
                "Error: JSON files are not supported in this version of the app."
            )
            return None
        return df
    except Exception as e:
        st.error(f"Error: {e}")
        return None


def main():
    st.title("EDA App for Datasets 📊")
    st.write("Upload a dataset (CSV, Excel) to perform exploratory data analysis.")

    uploaded_file = st.file_uploader(
        "Upload your dataset ...", type=[".csv", ".xls", ".xlsx"]
    )

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        if file_extension in ["csv", "xls", "xlsx"]:
            df = read_data(uploaded_file, file_extension)
            if df is not None:
                st.subheader("Exploratory Data Analysis")
                EDA_dataset = ProfileReport(df)
                st_pp_report(EDA_dataset)
            else:
                st.error("Error: Unable to read the uploaded file.")
        else:
            st.error("Please upload a valid CSV or Excel file.")
    else:
        st.info("Upload a file to get started with EDA.")


if __name__ == "__main__":
    main()
