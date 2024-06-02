# Project Outline: Data Manipulation and Cleaning

# GitHub Link: https://github.com/ashish-som/Python-Case-Study

## Objective: The objective of this project is to clean and prepare data from an existing dataset 'test.csv'. The goal is to identify and correct inconsistencies such as missing values, incorrect entries, and irregular formatting.

---

# Tasks Overview:
 - **1- Load the dataset.**
 - **2- Check the initial structure and shape of the data.***
 - **3- Handle missing values.**
 - **4- Convert specific columns to numeric types.**
 - **5- Replace specific values in categorical columns.**

 ---

 # Key Stages and Approach:

  ## 1- Setup Environment
   - Install required libraries.
   - Set up directory structure.

  ## 2- Data Loading
  - **Objective:-** Load the data into a pandas DataFrame for easy manipulation and analysis.
  - **Method:-** Use `pd.read_csv()` function to read the file.

  ## 3- Intial Data Exploration
  - **Objective:-** Understand the structure and content of the dataset.
  - **Method:-** Use `.shape` to get the number of rows and columns, and .head() to preview the data.

  ## 4- Handling Missing values
  - **Objective:-** Remove rows with missing values to prevent data quality issues.
  - **Approach Used:-** After checking the missing values, it was found out that there were some missing values in the Country column that makes the rest of the data in the rows irrelevant and incomplete so the rows that had missing values in the Country column had been drooped and the DataFrame got free from the missing values.
  - **Method:-** Use df.dropna(inplace=True) to drop any rows containing missing values.

  ## 5- Data Type Conversion
  - **Objective:-** Ensure columns intended to be numeric are correctly typed.
  - **Approach Used:-** First removed the special characters and converted the text into digit (where needed) then typecast to numeric (int)
  - **Method:-** Use `.astype()` function after removing the special characters and text to digit conversion.

 ## 6- Categorical Data Standardization
  - **Objective:-** Standardize values in categorical columns to ensure consistency.
  - **Approached Used:-** In some columns ('Country', 'Outcome') some different representations were used for the same entity so combined the different categories into one category. 
  - **Method:-** Use `.replace()` to replace specific values and `.strip()` function to get rid of the extra spaces in the categories.

## -7 Checking for Duplicate Values
  - **Objective:-** Ensure there are duplicate entries.
  - **Method:-** Use `.duplicated()` function to check for the suplicate values. `drop_duplicates()` to srop the missing values (if any) .

 ---

 # File Structure

 Python-Case_Study/
├── Task_2/
│   ├── Data_Manipulation.ipynb  # Jupyter notebook containing the code and documentation
├── resources/
│   ├── test.csv 
└── Data_Manipulation_Documentation.md  # Markdown file with project outline and documentation

  
- `Data_Manipulation.ipynb` - This Jupyter notebook contains the code for data cleaning and preparation, with markdown cells explaining each step.
- `test.csv` - The CSV file containing the raw data that needs to be cleaned.
- `Data_Manipulation_Documentation.md` - This Markdown file provides a comprehensive outline and documentation of the project,          including the objective, key stages, approach, and detailed steps with code snippets.

---

# Choice of Libraries:

- **Pandas**: For data manipulation and analysis.
- **Numpy**: For numerical operations (if needed).
- **Matplotlib**: For potential future visualisatin.
- **Seaborn**: For potential future visualisation.
- **Warnings**: To manage warning messages.
- **word2number**: To convert the words to digits.

---

## Requirements:
- To ensure that all necessary libraries are installed, use the `requirements.txt` file provided with the project. 
- Follow the steps below to set up your environment

1. ### Using Anaconda

1. **Download and Install Anaconda:**
   - Anaconda is a distribution of Python and R for scientific computing and data science. It simplifies package management and deployment.
   - Download from: [Anaconda Distribution](https://www.anaconda.com/products/distribution)

**Create a New Environment**
  conda create --name pdf_extractor python=3.11

2. **Activate the virtual environment**
   conda activate pdf_extractor
 
3. **Install Required Libraries**
  pip install -r requirements.txt

2. ### Using Visual Studio Code (VSCode)

1. **Download and Install VSCode:**
   - Visual Studio Code is a free code editor with support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring.

2. **Install Python Extension:**
   - Open VSCode and go to the Extensions view by clicking the Extensions icon in the Activity Bar on the side of the window.
   - Search for "Python" and install the extension by Microsoft.

3. **Open Project Folder:**
   - Open VSCode and go to File > Open Folder... to open your project directory.

4. **Select the Python Interpreter:**
   - Press Ctrl+Shift+P to open the command palette.
   - Type and select Python: Select Interpreter.
   - Choose the environment that was created with Anaconda (pdf_extractor).


## Storage Requirements:
- The primary storage requirement will be for the csv input file.

---

# How to Run
1- Open the Notebook File `Data_Manipulation_and_Cleaning`:
2. Run the Notebook:
    - Ensure your virtual environment is selected as the kernel.
    - Execute the notebook cells by pressing Shift + Enter or using the Run button.

---

# Funcions:

`word_to_num(text)` Converts a text ino digit