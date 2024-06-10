# %%
import pandas as pd
import requests
from datetime import datetime, timedelta
import os
uri = os.environ.get('URI')

# %%
# obtaining the data
url = 'https://api.blockchain.info/charts/transactions-per-second?timespan=all&sampled=false&metadata=false&cors=true&format=json'
resp = requests.get(url)
data = pd.DataFrame(resp.json()['values'])

# %%
# parsing the date
# X - datetiem in UTC
# y - number of transactions added to the pool per minute
data['x'] = [datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S') for x in data['x']]
data['x'] = pd.to_datetime(data['x'])

# %%
data['x_hour'] = data['x'].dt.round('H')

# %%
data_grouped = data.groupby('x_hour').sum(['y']).reset_index()

# %%
new_column_names = ['datetime', 'trans_per_min']
data_grouped.columns=new_column_names

# %%
yesterday_date = datetime.now() - timedelta(days=1)
new_data = data_grouped.loc[data_grouped['datetime'] >= yesterday_date,:]

# %%
data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    
# %%
new_file_name = 'etl_' + datetime.now().strftime('%Y-%m-%d') + '.csv'
new_file_name = new_file_name.replace('-', '_')
new_file_path = os.path.join('data', new_file_name)

new_data.to_csv(new_file_path)


