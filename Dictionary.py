import pandas as pd
pd.set_option('display.expand_frame_repr', False)

bank_clients=pd.read_csv('Churn Modeling.csv')
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
