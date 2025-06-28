import pandas as pd

# Load CSV
df = pd.read_csv("ecom.csv")

# Clean price columns: remove '$' and convert to float
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
df['originalPrice'] = df['originalPrice'].replace('[\$,]', '', regex=True)

# Handle missing originalPrice: fill with price if originalPrice is missing
df['originalPrice'] = df['originalPrice'].fillna(df['price'])

# Convert to float
df['originalPrice'] = df['originalPrice'].astype(float)

# Fill missing tagText with 'No Tag'
df['tagText'] = df['tagText'].fillna("No Tag")

# Save cleaned file
df.to_csv("cleaned_ecom.csv", index=False)

print("✅ Cleaning complete. Cleaned file saved as 'cleaned_ecom.csv'")
print(df.head())

