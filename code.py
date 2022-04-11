import pandas as pd
pd.set_option('display.max_rows', None)
file = pd.read_csv('drones.csv', sep=';', skipinitialspace = True, header=None)

#define a dataframe
df = pd.DataFrame(file)

# make lower case
df = df.astype(str).apply(lambda x: x.str.lower())

#filter bad data
filtered=df.replace({'phatom': 'phantom', '2.0': 'NaN', '1.0': 'NaN', 'professional': 'pro'}, regex=True)
print(filtered)
# #count all variables
# count_drones=df.stack().value_counts()
# print(count_drones)