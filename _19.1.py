import pandas as pd

df = pd.read_csv('sales_september_october.csv')

df['November Sales'] = [160, 210, 310]
df['December Sales'] = [170, 220, 330]

df.to_csv('sales_september_december.csv', index=False)

print("Data has been successfully updated and saved to 'sales_september_december.csv'.")

