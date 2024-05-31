import pandas as pd
import os
from datetime import datetime

def load_data(file_path):
    try:
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            return pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format")
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def check_duplicates(df):
    duplicate_rows = df[df.duplicated()]
    return duplicate_rows

def remove_duplicates(df):
    df_no_duplicates = df.drop_duplicates()
    return df_no_duplicates

def check_missing_values(df):
    missing_values = df.isnull().sum()
    return missing_values

def fill_missing_values(df, strategy='mean'):
    if strategy == 'mean':
        df_filled = df.fillna(df.mean())
    elif strategy == 'median':
        df_filled = df.fillna(df.median())
    elif strategy == 'mode':
        df_filled = df.fillna(df.mode().iloc[0])
    elif strategy == 'ffill':
        df_filled = df.fillna(method='ffill')
    elif strategy == 'bfill':
        df_filled = df.fillna(method='bfill')
    else:
        df_filled = df.fillna(0)
    return df_filled

def check_improper_formatting(df, column_formats):
    formatting_issues = {}
    for column, fmt in column_formats.items():
        if fmt == 'date':
            invalid_dates = pd.to_datetime(df[column], errors='coerce').isna().sum()
            formatting_issues[column] = invalid_dates
        elif fmt == 'numeric':
            invalid_numerics = pd.to_numeric(df[column], errors='coerce').isna().sum()
            formatting_issues[column] = invalid_numerics
    return formatting_issues

def fix_formatting(df, column_formats):
    for column, fmt in column_formats.items():
        if fmt == 'date':
            df[column] = pd.to_datetime(df[column], errors='coerce')
        elif fmt == 'numeric':
            df[column] = pd.to_numeric(df[column], errors='coerce')
    return df

def generate_report(report_path, issues):
    with open(report_path, 'w') as file:
        file.write("Data Cleaning Report\n")
        file.write("====================\n\n")
        file.write(f"Report generated on: {datetime.now()}\n\n")
        
        for issue, details in issues.items():
            file.write(f"{issue}:\n")
            for detail, count in details.items():
                file.write(f"  {detail}: {count}\n")
            file.write("\n")

def main(file_path, output_path, report_path, column_formats):
    df = load_data(file_path)
    if df is None:
        return
    
    issues = {}

    # Check and remove duplicates
    duplicates = check_duplicates(df)
    issues['Duplicates'] = {'Total Duplicates': len(duplicates)}
    df = remove_duplicates(df)

    # Check and fill missing values
    missing_values = check_missing_values(df)
    issues['Missing Values'] = missing_values.to_dict()
    df = fill_missing_values(df, strategy='drop')

    # Check and fix improper formatting
    formatting_issues = check_improper_formatting(df, column_formats)
    issues['Improper Formatting'] = formatting_issues
    df = fix_formatting(df, column_formats)

    # Save cleaned data
    if file_path.endswith('.csv'):
        df.to_csv(output_path, index=False)
    elif file_path.endswith('.xlsx'):
        df.to_excel(output_path, index=False)
    
    # Generate report
    generate_report(report_path, issues)
    print(f"Data cleaning completed. Report saved to {report_path}")

if __name__ == "__main__":
    # Example usage
    file_path = r"C:\Users\ashis\OneDrive\Documents\Case_Study\Data Cleaning and Summary Report\resources\test.csv"
    output_path = r"C:\Users\ashis\OneDrive\Documents\Case_Study\Data Cleaning and Summary Report\Output\clean_data.csv"
    report_path = r"C:\Users\ashis\OneDrive\Documents\Case_Study\Data Cleaning and Summary Report\Output\summary.txt"
    column_formats=dict(zip(load_data(file_path).columns,['object','object','object','numeric','object','numeric']))
    main(file_path, output_path, report_path, column_formats)