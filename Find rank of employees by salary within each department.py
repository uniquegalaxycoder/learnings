""" Find rank of employees by salary within each department """

import pandas as pd 

data = {
  
  'emp_id' : [1,2,3,4,5,6,7,8],
  'emp_name' : ['Rashi','Rakesh','Danial','Hari','Tommy','Saine','Som','Barbi'],
  'department' : ['IT','Sales','IT','IT','Sales','Tech','Tech','Tech'],
  'salary' : [5000,95000,85000,72000,65000,27000,29500,95000],
  'joining_date' : ['2025-01-12','2024-09-23','2025-05-12','2025-07-19',
                     '2024-10-12','2024-06-10','2024-11-28','2024-03-10']
}

df = pd.DataFrame(data)

df['joining_date'] = pd.to_datetime(df['joining_date'])
print(df)


df['ranks'] = df.groupby(['department'])['salary'].rank(method = 'dense', ascending = False)
# select *, dense_rank()over(partition by department order by salary desc) as salary_ranks
print(df)
