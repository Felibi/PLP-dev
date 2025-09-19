# Load dataset using pandas
import pandas as pd

# Load dataset
df = pd.read_csv("C:\\Users\\Felibi\\Desktop\\iris.data.csv")
print(df.head())
print(df.columns)

# Explore structure of the dataset
print(df.info())

# Cleaning the dataset
# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values
df_cleaned = df.dropna()

# compute basic statistics
print(df_cleaned.describe())

# perform  groupings on categorical columns
print(df_cleaned.groupby('species').mean())
print(df_cleaned.groupby('species').agg({'sepal_length': 'mean', 'sepal_width': 'mean'}))

# Identify any patterns or interesting findings
# For example, average sepal length and width by species
import matplotlib.pyplot as plt
df_cleaned.groupby('species')[['sepal_length', 'sepal_width']].mean().plot(kind='bar')
plt.title('Average Sepal Length and Width by Species')

# Create a line chart visualization
plt.plot(df_cleaned['sepal_length'], df_cleaned['sepal_width'], marker='o', linestyle='')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal Length vs Sepal Width')
plt.show()

# Create a Bar Chart plot visualization
df_cleaned['species'].value_counts().plot(kind='bar')
plt.xlabel('Species')
plt.ylabel('Count')
plt.title('Count of Each Species')
plt.show()

# Create a Histogram plot visualization
df_cleaned['sepal_length'].plot(kind='hist', bins=10)
plt.xlabel('Sepal Length')
plt.title('Distribution of Sepal Length')
plt.show()

# Create a Scatter Plot visualization
df_cleaned.plot(kind='scatter', x='sepal_length', y='sepal_width', c='species', colormap='viridis')
plt.title('Sepal Length vs Sepal Width by Species')
plt.show()

# Customize plots with labels, titles, and legends using matplotlib
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal Length vs Sepal Width by Species')
plt.legend(title='Species')
plt.show()

# Use seaborn for advanced visualizations
import seaborn as sns
sns.pairplot(df_cleaned, hue='species')
plt.show()
sns.heatmap(df_cleaned.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Error handling
try:
    # Attempt to read a non-existent file
    df_error = pd.read_csv("non_existent_file.csv")
except FileNotFoundError:
    print("File not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("File is empty. Please provide a valid CSV file.")
except pd.errors.ParserError:
    print("Error parsing file. Please check the file format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")