import pandas as pd
time_cols = ['birthday'] #which cols should be changed to datetime?
df = pd.read_csv(r'D:\Epam\Self_study\Python for Data Scientists\Exercise Files\Ch02\02_01\Example.csv',
                 parse_dates = time_cols) #changes data type for 'birthday'
print(df)
