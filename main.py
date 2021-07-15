import requests
data=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=Ebay&interval=5min&apikey=ES1AY6YOZU33WUST')
parsed_data=data.json()
print(parsed_data)


import pandas as pd
pd.set_option('display.expand_frame_repr', False)

debt=pd.read_csv('Data source/MunicipalDebtAnalysis.csv')

print(debt.info())

print(debt.head())

print(debt.shape)

print(debt.describe())

print(debt.isnull().sum())

print(debt.sort_values(['propertyvalue','totalbilling'], ascending=[False, False]))

drop_duplicates = debt.drop_duplicates()
print(drop_duplicates)

debt1=drop_duplicates
print(debt1)

debt1_ind= debt1.set_index('accountcategory')
print(debt1_ind.loc['Residential'])

print(debt1_ind.loc['Residential'].sort_values(['propertyvalue','totalbilling'], ascending=[False, False]))

debt1_by_type=debt1.groupby('accountcategory')[['totalbilling', 'totalreceipting']].sum()
print(debt1_by_type)



acccategory=['Agricultural', 'Business', 'Educational', 'Environ_Mgt', 'Goverment', 'Industry', 'Infrastr', 'Municipal'
             'Place of Worship']

Totalbilling=[93422565, 268518615, 61766651, -78, 84775936, 36659427, 781720, 34681517, 6022630, 2015056, 842190849, 55500199]

Totalreceipt=[92347204, 264463444, 58506195, 557, 86178940, 37124307, 872206,21232184, 5146218, 2196426, 687093780, 53902550]

acccategory.extend(['Public Benefit', 'Residential', 'Unknown'])


for x in [93422565, 268518615, 61766651, -78, 84775936, 36659427, 781720, 34681517, 6022630, 2015056, 842190849, 55500199]:
    if x == -78:
        continue
    print(x)



Data=pd.read_csv('Data source/indexData.csv')
print(Data)
print(Data.shape)

Info=pd.read_csv('Data source/indexInfo.csv')
print(Info)
print(Info.shape)

Data_Info=Data.merge(Info, on='Index', suffixes=('_Dat', '_Inf'))
print(Data_Info)



acccategory=['Agricultural', 'Business', 'Educational', 'Environ_Mgt', 'Goverment', 'Industry', 'Infrastr', 'Municipal'
             'Place of Worship']

Totalbilling=[93422565, 268518615, 61766651, -78, 84775936, 36659427, 781720, 34681517, 6022630, 2015056, 842190849, 55500199]

Totalreceipt=[92347204, 264463444, 58506195, 557, 86178940, 37124307, 872206,21232184, 5146218, 2196426, 687093780, 53902550]

acccategory.extend(['Public Benefit', 'Residential', 'Unknown'])
print(acccategory)

print(acccategory.index('Educational'))
print(Totalreceipt[2])

print(min(Totalbilling))
print(max(Totalbilling))

print(min(Totalreceipt))
print(max(Totalreceipt))




import numpy as np
property_value=[7375000, 325000, 1785000, 2200000, 100000, 1350000, 920000, 635000, 26500, 1735000, 50000, 2900000, 95000 ]
property_value_array=np.array(property_value)

print(np.mean(property_value))
print(np.std(property_value))

print(property_value_array[0:13:2])

total_billing=[13275, 585, 1366, 3960, 180, 1337, 911, 629, 477, 3123, 90, 5220, 171]

value_vs_billing_array=np.array([property_value, total_billing])
print(value_vs_billing_array)
print(value_vs_billing_array.size)
print(value_vs_billing_array.shape)

value_vs_billing_transposed=np.transpose(value_vs_billing_array)
print(value_vs_billing_transposed)






bank_clients=pd.read_csv('Data source/Churn Modeling.csv')
print(bank_clients)

a={'CustomerId':15634602, 'Surname':'Hargrave', 'Gender':'Female', 'Age':42, 'EstimatedSalary':101348.88, 'CreditScore':619}
b={'CustomerId':15647311, 'Surname':'Hill', 'Gender':'Female', 'Age':41, 'EstimatedSalary':112542.58, 'CreditScore':608}
c={'CustomerId':15619304, 'Surname':'Onio', 'Gender':'Female', 'Age':42, 'EstimatedSalary':113931.57, 'CreditScore':502}
d={'CustomerId':15701354, 'Surname':'Boni', 'Gender':'Female', 'Age':39, 'EstimatedSalary':93826.63, 'CreditScore':699}
e={'CustomerId':15737888, 'Surname':'Mitchell', 'Gender':'Female', 'Age':43, 'EstimatedSalary':79084.1, 'CreditScore':850}
f={'CustomerId':15574012, 'Surname':'Chu', 'Gender':'Male', 'Age':44, 'EstimatedSalary':149756.71, 'CreditScore':645}
g={'CustomerId':15592531, 'Surname':'Barlett', 'Gender':'Male', 'Age':50, 'EstimatedSalary':10062.8, 'CreditScore':822}


print(a)
print(e['Surname'])
print(f['CustomerId'])
print(g['CreditScore'])


