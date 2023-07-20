# EDA App 🚀

## Overview

This is a simple Exploratory Data Analysis (EDA) web application built using Streamlit. The app allows users to upload datasets in CSV, Excel (.xls, .xlsx), or JSON format and generates a pandas profiling report using `pandas-profiling` library. The EDA report provides valuable insights into the dataset, including data types, missing values, statistics, and visualizations.

## Setup

To run the EDA App, follow these steps:

1. Install the required libraries by running the following command:

```bash
pip install pandas streamlit pandas-profiling
```

2. Clone or download the project files from the GitHub repository:

```bash
git clone https://github.com/jasserabdou/EDA-app.git
```

3. Open a terminal or command prompt and navigate to the project directory.

4. Run the app using the following command:

```bash
streamlit run app.py
```

5. The app will start running, and you will see a message with a local URL (e.g., `http://localhost:8501`). Open this URL in your web browser to access the app.

## How to Use

1. Once the app is running, you will see a title "EDA App 🚀" displayed at the top.

2. Use the "Upload your dataset ..." button to select and upload your dataset. The app accepts CSV or Excel (.xls, .xlsx).

3. After uploading the dataset, the app will generate an EDA report using `pandas-profiling` and display it on the web page.

4. The report includes information about the dataset's columns, data types, missing values, summary statistics, and interactive visualizations.

5. If there are any issues during the data reading process or unsupported file types, appropriate error messages will be displayed.

6. You can also download the HTML report by clicking the "Download the HTML report" link.

## Supported File Types

The app supports the following file types for dataset uploads:

- CSV (Comma Separated Values)
- Excel (.xls, .xlsx)
- JSON (Unsupported in this version of the app)

## Note

- If you encounter any problems or errors, please ensure that the uploaded dataset is in the correct format and that the required libraries are installed.

- This version of the app does not support JSON files. If you have a JSON dataset, consider converting it to CSV or Excel format before using the app.

- For JSON datasets with complex nested structures, additional handling might be required. Consider using `pd.read_json()` with the appropriate options to read the data correctly.

## Author

This EDA App was created by Jasser as a simple tool for performing exploratory data analysis.

Feel free to enhance and customize the app as per your specific requirements. Happy data exploration! 📊

---

