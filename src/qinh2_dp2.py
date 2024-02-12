import pyreadr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
transaction_rds = pyreadr.read_r('/data/IDEA_DeFi_Research/Data/Lending_Protocols/Aave/V2/Mainnet/transactions.rds')
df = transaction_rds[None]
df_pandas = pd.DataFrame(df) # set to pandas data frame
df.plot() # plot the data
transaction_rds_data_label = df_pandas.columns.tolist()
# print(transaction_rds_data_label) # use to check the data label
df_pandas.head() # check the basic data, know the sample of data
# create a 'DateTime' column from the 'timestamp' column 
df_pandas['DateTime'] = df_pandas['timestamp'].transform(lambda x: datetime.datetime.fromtimestamp(x))
df_pandas.head() # check the updated data


# start to draw the basic graph set x_axis is DateTime and y_axis is amount
df_pandas['DateTime'] = pd.to_datetime(df_pandas['DateTime'])

# convert DataFrame columns to numpy arrays
x = df_pandas["DateTime"].values
y = df_pandas["amount"].values

# plot the graph
plt.plot(x, y)
plt.title("Analysis Graph")
plt.xlabel("DateTime")
plt.ylabel("Amount")
plt.show()

'''
Combine DateTime in the same day together, and then i add their label(amount)
together to draw a curve graph, Y_axis is amount, X_axis is Datetime.
FE: DateTime 2021-07-01 11:46:58, amount 1 and DateTime 2021-07-01 12:46:58, amount 2
All belong to 2021-07-01, so i will add 1 and 2 together to draw the curve graph.
'''
# convert timestamp to datetime
df_pandas['DateTime'] = pd.to_datetime(df_pandas['timestamp'], unit='s')

# group by date and sum the amounts
grouped_df = df_pandas.groupby(df_pandas['DateTime'].dt.date)['amount'].sum().reset_index()
'''
df_pandas['DateTime'].dt.date: This part extracts the date component from the 'DateTime' column of the DataFrame df_pandas.
The .dt.date accessor is used to access the date component of each datetime value.

df_pandas.groupby(df_pandas['DateTime'].dt.date): This part groups the DataFrame df_pandas by the date extracted in the previous step.
It creates a GroupBy object where rows with the same date are grouped together.

['amount'].sum(): This part specifies that we want to sum the values in the 'amount' column for each group created in the previous step.
It calculates the total amount for each date.

.reset_index(): This part resets the index of the resulting DataFrame.
By default, when you perform operations like groupby and sum, the resulting DataFrame will have a hierarchical index.
The .reset_index() method is used to convert this hierarchical index into a simple DataFrame with a default integer index.
'''