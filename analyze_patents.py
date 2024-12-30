import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('特実_国内文献 .csv')

# Convert the date columns to datetime format
df['出願日'] = pd.to_datetime(df['出願日'], format='%Y/%m/%d')
df['公知日'] = pd.to_datetime(df['公知日'], format='%Y/%m/%d')

# Extract the year from the date columns
df['出願年'] = df['出願日'].dt.year
df['公知年'] = df['公知日'].dt.year

# Generate a bar graph for the number of patents per year
plt.figure(figsize=(10, 6))
sns.countplot(x='出願年', data=df, palette='viridis')
plt.title('Number of Patents per Year')
plt.xlabel('Year')
plt.ylabel('Number of Patents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('patents_per_year.png')
plt.show()

# Generate a bar graph for the number of patents by company
plt.figure(figsize=(12, 8))
top_companies = df['出願人/権利者'].value_counts().nlargest(10).index
sns.countplot(y='出願人/権利者', data=df[df['出願人/権利者'].isin(top_companies)], palette='viridis', order=top_companies)
plt.title('Number of Patents by Company')
plt.xlabel('Number of Patents')
plt.ylabel('Company')
plt.tight_layout()
plt.savefig('patents_by_company.png')
plt.show()

# Generate a pie chart for the number of patents by status
plt.figure(figsize=(8, 8))
status_counts = df['ステージ'].value_counts()
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', len(status_counts)))
plt.title('Number of Patents by Status')
plt.axis('equal')
plt.tight_layout()
plt.savefig('patents_by_status.png')
plt.show()
