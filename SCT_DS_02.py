import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set seaborn theme for consistency
sns.set_theme(style="whitegrid")

# ---------------------------------------
# 1. Load and Inspect Titanic Dataset
# ---------------------------------------
df = sns.load_dataset('titanic')

print("Dataset Overview:")
print(df.head(), "\n")

print("Data Summary:")
print(df.info(), "\n")

print("Missing Values:")
print(df.isnull().sum(), "\n")

# ---------------------------------------
# 2. Data Cleaning
# ---------------------------------------

# Drop columns with excessive missing values or redundancy
df.drop(columns=['deck', 'embark_town', 'alive'], inplace=True)

# Handle missing values
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

# Verify cleaning
print("Missing Values After Cleaning:")
print(df.isnull().sum(), "\n")

# ---------------------------------------
# 3. Feature Engineering
# ---------------------------------------

# Create family size feature
df['family_size'] = df['sibsp'] + df['parch'] + 1

# Group age into categories
df['age_group'] = pd.cut(
        df['age'],
            bins=[0, 12, 18, 35, 60, 80],
                labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior']
)

# ---------------------------------------
# 4. Exploratory Data Analysis (EDA)
# ---------------------------------------

# --- Univariate Analysis ---
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='survived')
plt.title('Passenger Survival Count')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.histplot(df['age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.tight_layout()
plt.show()

# --- Bivariate Analysis ---

plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='sex', y='survived')
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='pclass', y='survived')
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='age_group', y='survived', order=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior'])
plt.title('Survival Rate by Age Group')
plt.ylabel('Survival Rate')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='embarked', y='survived')
plt.title('Survival Rate by Embarkation Port')
plt.xlabel('Embarked')
plt.tight_layout()
plt.show()

# --- Correlation Matrix ---
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# ---------------------------------------
# 5. Summary of Insights
# ---------------------------------------

print("Summary Statistics:\n")

print("Survival Rate by Gender:")
print(df.groupby('sex')['survived'].mean(), "\n")

print("Survival Rate by Passenger Class:")
print(df.groupby('pclass')['survived'].mean(), "\n")

print("Survival Rate by Embarked Port:")
print(df.groupby('embarked')['survived'].mean(), "\n")

print("Survival Rate by Age Group:")
print(df.groupby('age_group')['survived'].mean(), "\n")

print("Average Age and Fare by Class:")
print(df.groupby('pclass')[['age', 'fare']].mean(), "\n")

)