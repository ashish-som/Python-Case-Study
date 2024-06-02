# Project Outline: Country Extractor

# GitHub Link: https://github.com/ashish-som/Python-Case-Study

## Objective: This project extracts country names from PDF files and saves the extracted information into CSV files. It uses various Python libraries to read PDF files, extract text, identify country names, and handle data manipulation and storage. 

---

## Key Stages

1. **Setup Environment**
   - Install required libraries.
   - Set up directory structure.

2. **Develop PDF Text Extraction Function**
   - Create a function to read and extract text from PDF files.

3. **Extract Country Information**
   - Develop a function to identify country names from the extracted text using the `geograpy` library.

4. **Create DataFrame**
   - Convert the list of identified countries into a pandas DataFrame.

5. **Save DataFrame to CSV**
   - Save the DataFrame to a CSV file.

6. **Integrate Functions**
   - Combine all functions in a script to process all PDF files in a specified directory.

---

## Code Design:
- The main script consists of several functions, each responsible for a specific task:

### `extract_text_from_pdf(pdf_path)`
- **Description**: Reads a pdf file and converts it into readable text format.
- **Input**: `pdf_path` - Path to the pdf file.
- **Output**: Text extracted from the pdf file.

### `extract_country_info(text)`
- **Description**: Extracts country names from the given text.
- **Input**: `text` - Text extracted from the pdf file.
- **Output**: A list that contains the country names from the given text.

### `create_dataframe(countries)`
- **Description**: Converts the list of countries into a Pandas DataFrame.
- **Input**: `countries` - A list of countries.
- **Output**: A Pandas DataFrame that contains country names

### `def get_pdf_files_list(source_path)`
- **Description**: Retrieves a list of all PDF files in the specified directory.
- **Input**: `source_path` - The path of the folder that we have kept the pdf files in.
- **Output**: A list that contains the pdf file names.

### `dataframe_to_csv(df,destination_path,file_name)`
- **Description**: Saves the DataFrame to a CSV file with the specified destination path and file name.
- **Input**: 
    - `df` - The Pandas DataFrame that has to be converted to csv.
    - `destination_path`- The path of the destination folder that we want to store the csv files in.
    - `file_name`- Name of the pdf file
- **Output**: Creates a csv file from the Pandas DataFrame and stores it into the destination folderpip

## File Structure

Python-Case-Study/Task_3
│
├── country.py # Main script with all functions
├── PROJECT_OUTLINE.md # Project documentation
├── requirements.txt # List of required libraries
├── resources/ # Directory containing PDF files to process
│ └── pdf files
└── output/ # Directory where CSV files will be saved

---

## Choice of Libraries

1. **NumPy**
   - Provides support for large, multi-dimensional arrays and matrices.
   
2. **pandas**
   - Offers data structures and data analysis tools.
   
3. **PyPDF2**
   - A library for reading and manipulating PDF files.
  
4. **geograpy**
   - Extracts geographical information from text.
   
5. **os**
   - Provides functions for interacting with the operating system.
  
6. **re**
   - Offers support for regular expressions.
   
7. **warnings**
   - Used to manage warnings in Python.

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

- The primary storage requirement will be for the pdf input files and the resulting cleaned CSV file.
- Ensure there is sufficient disk space to accomodate these files.

---

## How to Run

1. **Install Required Libraries:**
    pip install -r requirements.txt

2. **Place PDF Files in resources/ Directory:**
    Add all the PDF files you want to process into the resources/ directory.

3. **Run the script:**
    country.py

4. **Check the output/ Directory:**
    The extracted country information will be saved as CSV files in the output/ directory.


