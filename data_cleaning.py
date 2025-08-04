import pandas as pd

print(pd.__version__)
df = pd.read_csv('sales_data_sample.csv',encoding = 'latin1')
df.head()
df.info()
df.describe()
df['ORDERDATE']=pd.to_datetime(df['ORDERDATE'],errors='coerce')
df['ORDERDATE']=df['ORDERDATE'].dt.strftime('%d-%m-%y')
df.isnull().sum()
df['STATE']=df['STATE'].fillna('Unknown')
df['TERRITORY'] = df['TERRITORY'].fillna('Unknown')
df['POSTALCODE'].replace('nan', pd.NA, inplace=True)
df['POSTALCODE']=df['POSTALCODE'].fillna('00000')
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df['COUNTRY']=df['COUNTRY'].str.strip().str.title()
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
df.dtypes

# Convert if necessary
df['postalcode'] = df['postalcode'].astype(str)
df['year_id'] = df['year_id'].astype(int)
df['orderdate'] = pd.to_datetime(df['orderdate'], errors='coerce')
print(df)