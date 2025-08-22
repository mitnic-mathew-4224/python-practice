import pandas as pd

#creating Dataframes
print('----------creating Dataframes----------')
data = {
        'Name':['Alice','Bob','Charlie'],
        'Marks':[89,90,42]
       }

df = pd.DataFrame(data)
print(df)
print()

#Reading from CSV
print('----------Reading from CSV----------')
df = pd.read_csv('students.csv')
print(df.head())
print()


#Filtering and Aggregation
print('----------Filtering and Aggregation----------')
print(df[df['Marks']>80])
print(df['Marks'].mean())
print()


#Exporting to Excel
print('----------Exporting to Excel----------')
df.to_excel('student.xlsx', index = False)
print()