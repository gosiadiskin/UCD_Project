import pandas as pd
pd.set_option('display.expand_frame_repr', False)

debt=pd.read_csv('MunicipalDebtAnalysis.csv')

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
print(acccategory)

print(acccategory.index('Educational'))
print(Totalreceipt[2])

print(min(Totalbilling))
print(max(Totalbilling))

print(min(Totalreceipt))
print(max(Totalreceipt))
