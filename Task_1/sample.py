import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

def load_dataset(file_path):
    return pd.read_csv(file_path)

def sample_data(df):
    state=222
    while True:
        sample=df.sample(n=100,replace=False,ignore_index=True,random_state=state)
        if False in sample.apply(lambda x:False if x.isna().sum()!=0 else True).values:
            state=np.random.randint(100,1000,1)
        elif sample.duplicated().sum()!=0:
            state=np.random.randint(100,1000,1)
        else:
            sample.to_csv(r"C:\Users\ashis\OneDrive\Documents\Case_Study\Task_1\Output\sample.csv",index=False)
            break
            

if __name__=='__main__':
    path=r"C:\Users\ashis\OneDrive\Documents\Case_Study\Task_1\Output\cleaned_tiabs.csv"
    sample_data(load_dataset(path))