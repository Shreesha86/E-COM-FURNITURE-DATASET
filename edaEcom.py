import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cleaned_ecom.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Create calculated columns
df['Revenue'] = df['price'] * df['sold']  # Calculate revenue from price and sold
df['Units Sold'] = df['sold']  # Rename for clarity

sns.set(style="whitegrid")

# 1. Top 10 Products by Units Sold
top_products = df['productTitle'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette='Blues_d')
plt.title('Top 10 Products by Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Product Title')
plt.tight_layout()
plt.show()

# 2. Revenue by Product Category (tagText)
revenue_by_tag = df.groupby('tagText')['Revenue'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=revenue_by_tag.values, y=revenue_by_tag.index, palette='Greens')
plt.title('Revenue by Product Category')
plt.xlabel('Total Revenue')
plt.ylabel('Category (tagText)')
plt.tight_layout()
plt.show()

# 3. Price vs Units Sold
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='price', y='sold', hue='tagText')
plt.title('Price vs Units Sold')
plt.xlabel('Price')
plt.ylabel('Units Sold')
plt.tight_layout()
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(10, 6))
# Select only numeric columns that exist
numeric_cols = ['originalPrice', 'price', 'sold', 'Revenue']
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# Summary statistics
print("Dataset Summary:")
print(f"Total number of products: {len(df)}")
print(f"Total revenue: ${df['Revenue'].sum():,.2f}")
print(f"Average price: ${df['price'].mean():.2f}")
print(f"Average units sold per product: {df['sold'].mean():.2f}")
print(f"Product categories: {df['tagText'].unique()}")