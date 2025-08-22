
# 1 Import libraries and load dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Titanic.csv')




# 2 Explore the dataset
print("First 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nStatistical summary:")
print(df.describe(include='all'))



# 3 Clean the dataset
# Drop irrelevant columns
df.drop(columns=['PassengerId', 'Ticket', 'Cabin'], inplace=True)

# Handle missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

print("\nNull values after cleaning:")
print(df.isnull().sum())



# 4 Descriptive statistics
print("\nAge mean:", df['Age'].mean())
print("Age median:", df['Age'].median())
print("Age mode:", df['Age'].mode().values)

print("\nValue counts for Sex:")
print(df['Sex'].value_counts())

print("\nValue counts for Pclass:")
print(df['Pclass'].value_counts())

print("\nValue counts for Embarked:")
print(df['Embarked'].value_counts())

print("\nValue counts for Survived:")
print(df['Survived'].value_counts())

print("\nSurvival rate by Sex:")
print(df.groupby('Sex')['Survived'].mean())

print("\nSurvival rate by Pclass:")
print(df.groupby('Pclass')['Survived'].mean())




#5 Visualization

# Distribution of Age

plt.figure(figsize = (8,5))
sns.histplot(df['Age'], bins = 30, kde=True)
plt.title('Age Distribution')
plt.show()

# count by gender

plt.figure(figsize = (6,4))
sns.countplot(x='Sex', data = df)
plt.title('Count by Gender')
plt.show()

# survival Rate by Gender

plt.figure(figsize = (6,4))
sns.barplot(x = 'Sex', y='Survived', data = df)
plt.title('Survival Rate by Gender')
plt.show()

#Survival Rate by Class
plt.figure(figsize=(6,4))
sns.barplot(x='Pclass', y = 'Survived', data = df)
plt.title('Survival Rate by Class')
plt.show()

# Age vs Survival (boxplot)
plt.figure(figsize=(8,5))
sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Age vs Survival')
plt.show()


# Heatmap of correlations
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# 6 Stretch activities

# create FamilySize feature

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

print("\nSurvival rate by FamilySize:")
print(df.groupby('FamilySize')['Survived'].mean())


#Violin plot for Survival by FamilySize

plt.figure(figsize = (10,6))
sns.violinplot(x='Survived', y = 'FamilySize', data=df)
plt.title('Survival by Family Size')
plt.show()


#Survival across sex and Pclass
plt.figure(figsize = (10,6))
sns.barplot(x= 'Pclass', y='Survived', hue='Sex', data=df)
plt.title('Survival Rate by Class and Gender')
plt.show()





















