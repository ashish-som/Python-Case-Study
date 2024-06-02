# Project Title: Data Cleaning Automation Tool

# GitHub Link: https://github.com/ashish-som/Python-Case-Study

## Objective:

This project aims to provide an automated tool to clean datasets by identifying and correcting data inconsistencies, such as duplicate records, missing entries, and improper formatting. The tool will also generate a report summarizing the issues found and the actions taken.

---

## Key Stages

1. **1- Setup Environment**
   - Install required libraries.
   - Set up directory structure.
2. **Loading Data**: Load the dataset from a specified file path.
3. **Checking for Duplicates**: Identify and remove duplicate rows in the dataset.
4. **Handling Missing Values**: Detect missing values and fill them using a specified strategy.
5. **Checking Formatting Issues**: Identify columns with improper formatting (dates and numerics).
6. **Fixing Formatting Issues**: Correct the formatting issues in the identified columns.
7. **Saving Cleaned Data**: Save the cleaned dataset to a specified output file.
8. **Generating Report**: Generate a summary report of the issues found and fixes applied.

---

## Code Design

### Functions

- **`load_data(file_path)`**: Loads data from a CSV or Excel file from the given path.
- **`check_duplicates(df)`**: Identifies duplicate rows in the dataframe.
- **`remove_duplicates(df)`**: Removes duplicate rows from the dataframe.
- **`check_missing_values(df)`**: Checks for missing values in the dataframe.
- **`fill_missing_values(df, strategy='mean')`**: Fills missing values in the dataframe using the specified strategy.
- **`check_improper_formatting(df, column_formats)`**: Checks for improper formatting in specified columns.
- **`fix_formatting(df, column_formats)`**: Fixes the formatting of specified columns.
- **`generate_report(report_path, issues)`**: Generates a report of the data cleaning process.
- **`main(file_path, output_path, report_path, column_formats)`**: Main function to execute the data cleaning process.

---

### Main Function Workflow

1. Load the dataset.
2. Check and remove duplicates.
3. Check and fill missing values.
4. Check and fix formatting issues.
5. Save the cleaned dataset.
6. Generate a summary report.

---

## File Structure

Case_Study/Data Cleaning and Summary Report
│
├── clean_and_summary.py               # Script for data cleaning and concatenation
├── requirements.txt                   # List of required libraries
├── resources/
│   ├── test.csv                       # Input dataset
│
├── output/
│   ├── clean_data.csv                  # Output cleaned dataset
|   ├── summary.txt                     # Summary report
│
└── PROJECT_OUTLINE.md                  # Project documentation

---

## Requirements:
- To ensure that all necessary libraries are installed, use the `requirements.txt` file provided with the project. 
- Follow the steps below to set up your environment

1. **Create a Virtual Environment**
  
    python -m venv venv  

2. **Activate the virtual environment**
 **On Windows:**
   venv\Scripts\activate
 **On Mac:**
   source/bin/activate

3. **Install Required Libraries**
  pip install -r requirements.txt


## Storage Requirements:

- The primary storage requirement will be for the Excel or CSV input file and the resulting clean_data.csv file and summary.txt.
- Ensure there is sufficient disk space to accomodate these files.

---

## Choice of Libraries:

- **Numpy**: For numerical operations (if needed).
- **Pandas**: For data manipulation and analysis.
- **OS**: To ensure directories exist and to handle file paths more robustly. 
- **Datetime**: To handle and manipulate datetime data 
---

## How to Run

Follow these steps to run the data cleaning script:

1. **Prepare Your Files**: Place your input data file in the `resources` directory. 

2. **Configure Column Formats**: Update the `column_formats` dictionary in the `main` function to reflect the expected formats of your columns. Supported formats are `date`, and `numeric`.

3. **Run the Script**: Execute the script using Python. You can do this by running the following command in your terminal or command prompt:

    clean_and_summary.py

    Ensure to update the paths and column formats if needed:

    ```if __name__ == "__main__":
        file_path = r"path\to\your\input\file.csv"
        output_path = r"path\to\your\output\clean_data.csv"
        report_path = r"path\to\your\output\summary.txt"
        column_formats = {
            'Column1': 'object',
            'Column2': 'object',
            'Column3': 'date',
            'Column4': 'numeric',
            'Column5': 'object',
            'Column6': 'numeric'
        }
        main(file_path, output_path, report_path, column_formats)
    ```

    Replace the file paths and column formats with your specific requirements.

5. **View Output**: After running the script, you can find the cleaned data in the specified output file (e.g., `output/clean_data.csv`) and the summary report in the specified report file (e.g., `output/summary.txt`).

This will execute the data cleaning process and generate the cleaned data and summary report as described.
