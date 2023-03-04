import pandas as pd
from openpyxl.workbook import Workbook
# salary parsing
# company name text only
# state field 
# company age
# parsing of job description
df = pd.read_csv('D:\kaggle data analyst\DataAnalyst.csv')



# salary parsing

# removing thr row which doesnt have salary value // i had an error because of this
df = df[df['Salary Estimate'] != '-1']

# cleaning salary
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x : x.replace('K', "").replace('$' , ""))

# defining minimun and maximun salary
df['min_salary'] = minus_kd.apply(lambda x: x.split('-')[0])
df['max_salary'] = minus_kd.apply(lambda x: x.split('-')[1])            

# defining average salary
df['avg_salary'] = (df['min_salary'].astype(int) + df['max_salary'].astype(int))/2
# df['avg_salary'] = df['avg_salary'].apply(lambda x: '{}K'.format(x))


# todo company name text only

# company_name = df['Company Name'].apply(lambda x: x.split("\n")[0])
# AttributeError: 'float' object has no attribute 'split' . had this error , 
# was resolved by converting whole to string and then performing all the functions

company_name = df['Company Name'].apply(lambda x: str(x).split('\n')[0])
df['company_txt'] = company_name
# company_name.to_excel(r'test.xlsx',index=False)

# todo state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1]) 

# had this error , AttributeError: 'Series' object has no attribute 'Location',
# solved by providing axis info.
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)
# print(df.job_state.value_counts())


# todo company age
company_age = df['Founded'].apply(lambda x: 2023 - int(x) if int(x)!= -1 else x)
df['age'] = company_age

# todo description
#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
 
#r studio 
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)


#spark 
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)


#aws 
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)


#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)



df_out = df.drop(['Unnamed: 0'], axis =1)
df_out.to_csv('cleanerd.csv', index = False)
# print(df_out)