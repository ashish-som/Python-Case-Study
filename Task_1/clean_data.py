import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

def load_dataset(file_path):
    return pd.read_excel(file_path)

def handle_missing_values(df, strategy='drop'):

    if strategy == 'drop':
        df = df.dropna()

    elif strategy == 'fill':
        columns=df.columns
        imputation_mapping=list(zip(columns,map(lambda x:' ('+x+' is not available) ',df.columns)))

        def missing_values_imputation(col,value):
            df[col].fillna(value,inplace=True)
        
        for i in imputation_mapping:
            missing_values_imputation(*i)
    return df

def clean_data(df):
    
    cols=['Title','Abstract','Author Addresses']

    cd=df[cols[0]]
    for i in cols[1::]:
        cd=cd+' '+df[i]
    
    clean_df=pd.DataFrame({'ID':[i for i in range(1,len(df)+1)],'Text':cd})
    
    def clean_string(s):
        import unicodedata
        return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    
    clean_df['Text'] = clean_df['Text'].apply(clean_string)
    clean_df.to_csv(r"C:\Users\ashis\OneDrive\Documents\Case_Study\Task_1\Output\cleaned_tiabs.csv",index=False)
    
if __name__ == "__main__":
    
    file_path= r"C:\Users\ashis\OneDrive\Documents\Python_case_study\resources\tiabs.xlsx"
    df=load_dataset(file_path)
    cleaned_df = clean_data(handle_missing_values(df,strategy='fill'))
   