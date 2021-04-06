import pandas as pd
import numpy as np

#LOAD DATASET INTO FRAME
df = pd.read_excel('xlsxfile.xlsx')

#REPLACE ZERO/NaN VALUES WITH COLUMN AVG
df['DATLFMW'].fillna(value=df['DATLFMW'].mean(), inplace = True)
df['ATLMW'].fillna(value=df['ATLMW'].mean(), inplace = True)

#REPLACE NaN VALUES USING THE GIVEN DATA
i = 0
while i < 4:

    pos1 = df.iloc[(i+8456),1]
    pos2 = df.iloc[(i+8456),2]

    newVal1 = pos1-pos2
    newVal2 = (newVal1/df.iloc[(i+8456),2])

    df.iloc[(i+8456),3] = newVal1
    df.iloc[(i+8456),4] = newVal2
    
    i += 1


#SUM DATA
sumExpected = df['DATLFMW'].sum(axis=0) #works
