#import modules
from functions import translate_df
import re
import pandas as pd
import numpy as np
import googletrans as gt
from googletrans import Translator
translator = Translator()



data=pd.read_csv("oel_poland_working.csv")

print(data)

#use translate_df function to translate the dataframe
translated_df = translate_df(data)
