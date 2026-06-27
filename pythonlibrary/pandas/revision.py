import pandas as pd

##Creation

# --- Creating a Series (1D - Just one column) ---
ages = pd.Series([25, 30, 35, 40], name="Age")

# --- Creating a DataFrame (2D - The full table) ---
# The most common way is from a Python dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}
df = pd.DataFrame(data)

# Creating from a list of lists (less common, but good to know)
list_data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London']
]
df2 = pd.DataFrame(list_data, columns=['Name', 'Age', 'City'])


## Inspection


print(df.head())        # Shows the first 5 rows (default)
print(df.tail(2))       # Shows the last 2 rows
print(df.shape)         # (4, 3) -> 4 rows, 3 columns
print(df.columns)       # Index(['Name', 'Age', 'City'])
print(df.dtypes)        # Shows data type of each column (object, int64, etc.)
print(df.info())        # The ultimate summary: columns, non-null counts, memory usage
print(df.describe())    # Statistical summary (mean, min, max, quartiles) for numerical columns


##I/O (Reading and Writing)
# --- READING ---
df = pd.read_csv('sales_data.csv')          # Read a CSV
df = pd.read_excel('sales_data.xlsx')       # Read an Excel file
df = pd.read_json('data.json')              # Read a JSON file

# --- WRITING ---
df.to_csv('cleaned_data.csv', index=False)  # Save to CSV (index=False prevents saving row numbers)
df.to_excel('cleaned_data.xlsx', index=False)



##Selection & Filtering
# --- Selecting Columns ---
age_col = df['Age']                 # Returns a Series (1 column)
subset = df[['Name', 'City']]       # Returns a DataFrame (2 columns) - Note the double brackets!

# --- Selecting Rows & Cells (.loc and .iloc) ---
# .loc is for LABELS (names)
# .iloc is for INTEGERS (index numbers)

val = df.loc[0, 'Name']             # Row index 0, 'Name' column -> 'Alice'
row = df.iloc[0]                    # Entire first row
cell = df.iloc[0, 1]                # Row 0, Column index 1 (Age) -> 25

# --- Filtering Rows (Boolean Indexing) ---
# "Give me everyone older than 28"
older_than_28 = df[df['Age'] > 28]

# Multiple conditions (Use parentheses! Use & for AND, | for OR)
specific_people = df[(df['Age'] > 25) & (df['City'] == 'London')]


##Modification
# --- Adding a new column ---
df['Salary'] = [50000, 60000, 70000, 80000]  # Assign a list
df['Tax'] = df['Salary'] * 0.2               # Math on existing columns!

# --- Deleting a column ---
# axis=1 means "columns" (axis=0 is rows). inplace=True saves it directly to df.
df.drop('Tax', axis=1, inplace=True)         

# --- Renaming columns ---
df.rename(columns={'Name': 'Full_Name', 'City': 'Location'}, inplace=True)


##Data Cleaning & Handling the Mess
# Find missing values (Returns True/False)
print(df.isnull())            
print(df['Age'].isnull().sum()) # Count how many missing values in the 'Age' column

# Drop missing values
df_dropped = df.dropna()                  # Drops ANY row with a NaN
df_dropped = df.dropna(subset=['Age'])    # Drops rows only if 'Age' is NaN

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())  # Fill NaNs with the average age
df['City'] = df['City'].fillna('Unknown')       # Fill NaNs with a specific string

# Find duplicates (Returns True for the 2nd, 3rd, etc. occurrence)
print(df.duplicated())

# Remove duplicates
df_clean = df.drop_duplicates()                 # Removes exact duplicate rows
df_clean = df.drop_duplicates(subset=['Name'])  # Keeps only the first occurrence of each Name

# Convert string numbers to actual integers/floats
df['Age'] = df['Age'].astype(int)

# Convert strings to Datetime objects (Crucial for time-series data!)
# Suppose df has a 'Join_Date' column like '2023-01-15'
df['Join_Date'] = pd.to_datetime(df['Join_Date'])

# Now you can extract the year, month, etc.!
df['Join_Year'] = df['Join_Date'].dt.year



##Advanced Library Features (Leveling Up)

# Suppose df has 'Department' and 'Salary' columns

# Group by Department and find the average salary
avg_salary = df.groupby('Department')['Salary'].mean()

# Group by Department and find multiple stats
dept_stats = df.groupby('Department')['Salary'].agg(['mean', 'max', 'min', 'count'])

# value_counts() - The fastest way to count occurrences (like a frequency table)
print(df['Department'].value_counts()) 


# --- pd.merge() (Like SQL Joins or VLOOKUP in Excel) ---
# Merges based on a common key column
employees = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
salaries = pd.DataFrame({'ID': [1, 2], 'Salary': [50k, 60k]})

merged_df = pd.merge(employees, salaries, on='ID', how='inner') # how can be 'left', 'right', 'outer'

# --- pd.concat() (Stacking tables on top of each other) ---
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'A': [3, 4]})

stacked_df = pd.concat([df1, df2], ignore_index=True) # ignore_index resets the row numbers



# --- .apply() (Best for row-by-row or column-by-column logic) ---
# Let's categorize ages into 'Young' and 'Senior'
def categorize_age(age):
    if age < 30:
        return 'Young'
    else:
        return 'Senior'

df['Age_Group'] = df['Age'].apply(categorize_age)

# Using a lambda function (anonymous, one-line function) for quick math
df['Bonus'] = df['Salary'].apply(lambda x: x * 0.10) # 10% bonus

# --- .map() (Best for simple 1-to-1 dictionary replacements) ---
city_mapping = {'New York': 'NYC', 'London': 'LDN'}
df['City_Code'] = df['City'].map(city_mapping)





import pandas as pd

# ==========================================
# PANDAS TOP 25 MASTER CHEAT SHEET
# ==========================================

# --- 1. SETUP & INSPECTION ---
df = pd.read_csv('file.csv')            # Load data
df.head(10)                             # First 10 rows
df.shape                                # (rows, columns)
df.info()                               # Columns, data types, non-null counts
df.describe()                           # Statistical summary of numbers
df.columns                              # List of column names
df.dtypes                               # Data types of each column

# --- 2. SELECTION & FILTERING ---
df['col_name']                          # Select one column (returns Series)
df[['col1', 'col2']]                    # Select multiple columns (returns DataFrame)
df.loc[0, 'col_name']                   # Select by label (row label, column label)
df.iloc[0, 1]                           # Select by integer index (row index, col index)
df[df['age'] > 30]                      # Filter rows based on condition
df[(df['age'] > 30) & (df['city'] == 'NY')] # Multiple conditions (Use & and |)

# --- 3. MODIFICATION ---
df['new_col'] = df['col1'] * 2          # Create new column via math
df.drop('col_name', axis=1, inplace=True) # Delete a column
df.rename(columns={'old': 'new'}, inplace=True) # Rename columns

# --- 4. CLEANING ---
df.isnull().sum()                       # Count missing values per column
df.dropna()                             # Drop rows with ANY missing values
df.fillna(0)                            # Fill missing values with 0
df.drop_duplicates()                    # Remove exact duplicate rows
df['col'] = df['col'].astype(int)       # Change data type
df['date'] = pd.to_datetime(df['date']) # Convert string to datetime

# --- 5. AGGREGATION & GROUPING ---
df['col'].mean() / .sum() / .max()      # Basic math on a column
df['col'].value_counts()                # Count occurrences of each unique value
df.groupby('category')['value'].mean()  # Group by category, calculate mean
df.groupby('cat')['val'].agg(['mean', 'sum']) # Multiple aggregations at once

# --- 6. COMBINING & APPLYING ---
pd.merge(df1, df2, on='key_col', how='left') # Merge two DataFrames (SQL Join)
pd.concat([df1, df2], ignore_index=True)     # Stack DataFrames vertically
df['col'].apply(lambda x: x * 10)            # Apply a custom function to a column
df['col'].map({'A': 1, 'B': 2})              # Map values using a dictionary