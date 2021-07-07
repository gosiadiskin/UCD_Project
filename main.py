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
