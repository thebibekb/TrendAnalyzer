import pandas as pd

# Function to calculate the trending score
def calculate_trending_score(row):
    return (row['stars'] * 0.5) + (row['num_ratings'] * 0.3) + (row['num_reviews'] * 0.1) + (row['final_score'] * 0.1)

# Load t-shirts dataset and calculate trending score
tshirt_df = pd.read_csv('tshirts_csv_final.csv')
tshirt_df['trending_score'] = tshirt_df.apply(calculate_trending_score, axis=1)
top_20_tshirts = tshirt_df.sort_values(by='trending_score', ascending=False).head(20)

# Load dresses dataset and calculate trending score
dresses_df = pd.read_csv('dresses_csv_final.csv')
dresses_df['trending_score'] = dresses_df.apply(calculate_trending_score, axis=1)
top_20_dresses = dresses_df.sort_values(by='trending_score', ascending=False).head(20)

# Load skirts dataset and calculate trending score
skirts_df = pd.read_csv('skirts_csv_final.csv')
skirts_df['trending_score'] = skirts_df.apply(calculate_trending_score, axis=1)
top_20_skirts = skirts_df.sort_values(by='trending_score', ascending=False).head(20)

# Save the top 20 items for each category
top_20_tshirts.to_csv('top_20_tshirts.csv', index=False)
top_20_dresses.to_csv('top_20_dresses.csv', index=False)
top_20_skirts.to_csv('top_20_skirts.csv', index=False)

print("Top 20 T-shirts, Dresses, and Skirts saved.")
