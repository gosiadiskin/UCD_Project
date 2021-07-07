import pandas as pd
pd.set_option('display.expand_frame_repr', False)
Data=pd.read_csv('indexData.csv')
print(Data)

Info=pd.read_csv('indexInfo.csv')
print(Info)

Data_Info=Data.merge(Info, on='Index', suffixes=('_Dat', '_Inf'))
print(Data_Info)
