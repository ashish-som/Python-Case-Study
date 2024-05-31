# Project Outline: Text Data Cleaning, Concatenation and Sampling

## Objective: Develop a Python script to handle and clean a provided dataset.

- In an Excel file (‘tiabs.xlsx’) containing 1,000 titles and abstracts (tiabs) along with other metadata. 
The task is to:- 
**(a)**	
- Combine the 'Title', 'Abstract', and 'Author Addresses' columns into one column named 'Text'. Then, assign a unique, random ID to each entry—sequential numbering is fine. The final dataset should contain just two columns: 'ID' and 'Text'. The new file can be named as ‘cleaned_tiabs.csv’
**(b)**
  - Create a random subset of 100 tiabs from ‘tiabs.xlsx’, ensuring the data is free from duplicates and formatting errors.

---

## Key Stages:
**1- Setup Environment**
   - Install required libraries.
   - Set up directory structure.

- After this two main stages for two different files ('clean_data.py','sample.py') in this project- 

### (a) Cleaning and Concatenation
  **1- Loading the dataset-**
    - Use `load_data` function that reads an excel file into a Pandas Dataframe
  **2- Handling missing values-**
    - Implement the `handle_missing_values` function to handle missing values either by dropping them or by filling with a specified value.
  **3- Column concatenation**
    - Develop the `clean_data` function to merge specific columns (Title, Abstract, Author Addresses), clean the text data by removing non-ASCII characters, and save the cleaned data to a CSV file named as `cleaned_tiabs.csv`.

  ### (b) Sampling
  **1- Loading the cleaned dataset-**
    - Use `load_dataset` function to load the dataset (It takes the cleaned dataset created in stage 'a')
  **2- Data Sampling**
    - Implement the `sample_data` function to obtain a random sample of the dataset, ensuring no missing values or duplicate values in the sample.


---

## Code Design:

### (a) clean_data.py
### `load_dataset(file_path)`
- **Description**: Loads the dataset from an Excel file.
- **Input**: `file_path` - Path to the excel file.
- **Output**: Pandas DataFrame containing the dataset.

### `handle_missing_values(df, strategy='drop', fill_value=None)`
- **Description**: Handles missing values in the DataFrame.
- **Input**: 
   - `df` - Pandas DataFrame
   - `strategy` - Method fo handling missing values ('drop' or 'fill').
- **Output**: - DataFrame with the missing values handled.

### `clean_data(df)`
- **Description**: Concatenates the specified columns ('Title','Abstarct','Author Addresses') into 'Text' column, It also cleans the text by removing non-ASCII characters.
- **Input**: `df`- Pandas DataFrame
- **Output**: Saves cleaned data into a csv file ("cleaned_tiabs.csv").

### (b) sample.py
### `load_dataset(file_path)`
- **Description**: Loads the dataset from a csv file.
- **Input**: `file_path` - Path to the csv file.
- **Output**: Pandas DataFrame containing the dataset.

### `sample_data(df)`
- **Description**: Obtains a random sample of the dataset, ensuring no missing values or duplicates.
- **Input**: `df` - Pandas DataFrame.
- **Output**: Saves the sample in a csv file ("sample_data.csv").

---

## File Structure:

Case_Study/Task_1
│
├── clean_data.py               # Script for data cleaning and concatenation
|── sample.py                   # Script for data sampling
├── requirements.txt            # List of required libraries
├── resources/
│   ├── tiabs.xlsx               # Input dataset
│
├── output/
│   ├── cleaned_tiabs.csv        # Output cleaned dataset
|   ├── sample_data.csv          # Sample data
│
└── PROJECT_OUTLINE.md           # Project documentation

---

## Choice of Libraries:

- **Pandas**: For data manipulation and analysis.
- **Numpy**: For numerical operations (if needed).
- **Matplotlib**: For potential future visualisatin.
- **Seaborn**: For potential future visualisation.
- **Warnings**: To manage warning messages.
- **unicodedata**: To handle text processing and encoding

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

- The primary storage requirement will be for the Excel input file and the resulting cleaned CSV file.
- Ensure there is sufficient disk space to accomodate these files.

---

## Documetataion:

### Project Title:Text Data cleaning and Concatenation

### Description:
- This project aims to automate the preprocessing of bibliographic text data by loading the dataset, handling missing values, and cleaning and concatenating the specified columns. The cleaned data is saved in a CSV file for easy access and further use.

### How to Run:
1. Place the input Excel file (`tiabs.xlsx`) in the `resources` directory.
2. Run the main script (`clean_data.py`).


### Example Usage of clean_data.py:
if __name__ == "__main__":
    file_path= r"C:\Users\ashis\OneDrive\Documents\Python_case_study\resources\tiabs.xlsx"
    df=load_dataset(file_path)
    cleaned_df = clean_data(handle_missing_values(df, strategy='fill'))

### Example Usage of sample_data.py:
if __name__=='__main__':
    path=eval(input('Enter the path in the correct format- '))
    sample_data(load_dataset(path))



### Functions in `clean_data.py`:
  `load_dataset(file_path)`: Loads an Excel file into a DataFrame.
  `handle_missing_values(df, strategy='drop', fill_value=None)`: Handles missing values in the DataFrame.
  `clean_data(df)`: Cleans and preprocesses the data, then saves it to a CSV file.

### Functions in `sample.py`:
  `load_dataset(file_path)`: Loads a CSV file into a DataFrame.
  `sample_data(df)`: Obtains a random sample of the dataset and saves it in a csv file ("sample_data.csv"), ensuring no missing values or duplicates.

      
