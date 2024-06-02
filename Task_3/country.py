import numpy as np
import pandas as pd
import PyPDF2
import geograpy
import warnings
import os
import re

warnings.filterwarnings('ignore')

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_country_info(text):
    places = geograpy.get_place_context(text=text)
    countries = places.countries
    return countries

def create_dataframe(countries):
    df = pd.DataFrame(countries, columns=['Country'])
    return df

def get_pdf_files_list(source_path):
    os.chdir(source_path)
    files=[]
    for i in os.listdir():
        if re.search(r'\.pdf$',i):
            files.append(i)
    return files

def datafraeme_to_csv(df,destination_path,file_name):
    path=destination_path+'\\'+file_name.replace('pdf','csv')
    df.to_csv(path,index=False)

if __name__=='__main__':

    source_path=r"C:\Users\ashis\OneDrive\Documents\Case_Study\Python-Case-Study\Task_3\resources"
    dest_path=r"C:\Users\ashis\OneDrive\Documents\Case_Study\Python-Case-Study\Task_3\Output"

    files=get_pdf_files_list(source_path)
    for i in files:
       text= extract_text_from_pdf(i)
       countries=extract_country_info(text)
       df=create_dataframe(countries)
       datafraeme_to_csv(df,dest_path,i)