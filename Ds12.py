import pandas as pd
import numpy as np
data = {
'First Name': ['Aryan', 'Rohan', 'Riya', 'Yash', 'Siddini'],
'Last Name': ['Singh', 'Agarwal', 'Shah', 'Bhatia', 'Khanna'],
'Type': ['Full-time employee', 'Intern', 'Full-time employee',
'Part-time employee', 'Full-time employee'],
'Department': ['Administration', 'Technical', 'Administration',
'Technical', 'Technical'],
'Yoe': [2, 3, 5, 7, 6],
'Salary': [20000, 5000, 10000, 10000, 20000]
}
df = pd.DataFrame(data)
print(df)
table = pd.pivot_table(df, index=['Type', 'Department'],values='Salary', aggfunc='mean')
print(table)
pivot = pd.pivot_table(df, index='Type', values='Salary',aggfunc=['mean', 'sum'])
print(pivot)
pivot_count = df.pivot_table(index='Type', values='Salary',aggfunc='count')
print(pivot_count)
pivot_std = df.pivot_table(index='Type', values='Salary',aggfunc='std')
print(pivot_std)
