#functions for data extraction and cleaning

#import modules
import regex as re
import pandas as pd
import numpy as np
import googletrans as gt
from googletrans import Translator
translator = Translator()


#function to highlight rows with duplicate CAS values
def highlight_dup(dataframe, CAS_column):
    '''
    function to highlight rows with duplicate values in one column
    '''
    #create a copy of the dataframe
    df = dataframe.copy()
    #create a new column to highlight duplicates
    df['highlight'] = np.where(df[CAS_column].duplicated(), 'background-color: yellow', '')
    #return the highlighted dataframe
    return df.style.apply(lambda x: x.highlight, axis=1)

#Once highlighted, user can filter the dataframe to show only the highlighted rows
#df[df['highlight'] == 'background-color: yellow']
#If CAS numbers are same but values in limit columns are different, user must use own intuition to combine rows into 1 CAS number.



#function to remove rows of duplicate CAS numbers when limit values are also the same
def remove_dup(dataframe, CAS_column):
    '''
    function to only remove rows of duplicate CAS numbers when the rows for limit values are also duplicates
    '''
    #create a copy of the dataframe
    df = dataframe.copy()
    #create a new column to highlight duplicates
    df['highlight'] = np.where(df[CAS_column].duplicated(), 'background-color: yellow', '')
    #return the highlighted dataframe
    df = df[df['highlight'] == 'background-color: yellow']
    #drop the highlighted rows
    df = df.drop_duplicates(subset=['CAS Number', 'Limit Value'])
    #return the dataframe with highlighted rows removed
    return df


#function to translate csv file into a dataframe
def csv_to_df(csv_file):
    '''
    function to translate csv file into a dataframe
    '''
    #read csv file into a dataframe
    df = pd.read_csv(csv_file)
    #return the dataframe
    return df


#function to separate CAS number from chemical name in a dataframe
def sep_cas(df, column):
    '''
    function to separate CAS number from chemical name in a dataframe
    '''
    #create a copy of the dataframe
    df = df.copy()
    #create a new column for CAS number
    df['CAS Number'] = df[column].str.extract(r'(\d{2,7}-\d{2}-\d)')
    #create a new column for chemical name
    df['Chemical Name'] = df[column].str.replace(r'(\d{2,7}-\d{2}-\d)', '')
    #return the dataframe
    return df

#function to translate all columns in a dataframe from a detected language to english 
def translate_df(df):
    '''
    function to translate all columns in a dataframe from a detected language to english 
    '''
    #create a copy of the dataframe
    df = df.copy()
    #translate all columns in the dataframe
    df = df.applymap(lambda x: translator.translate(x).text)
    #return the dataframe
    return df


