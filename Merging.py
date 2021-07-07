import pandas as pd
pd.set_option('display.expand_frame_repr', False)
Data=pd.read_csv('indexData.csv')
print(Data)
print(Data.shape)

Info=pd.read_csv('indexInfo.csv')
print(Info)
print(Info.shape)

Data_Info=Data.merge(Info, on='Index', suffixes=('_Dat', '_Inf'))
print(Data_Info)
