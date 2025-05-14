import pandas as pd

spacex_df = pd.read_csv("spacex_launch_dash.csv")

success_counts = spacex_df[spacex_df['class'] == 1]['Launch Site'].value_counts()
largest_success_site = success_counts.idxmax()
largest_success_count = success_counts.max()

print(f"Largest number of successful launches: {largest_success_site} with {largest_success_count} successes.")

site_success_rate = spacex_df.groupby('Launch Site')['class'].mean()
highest_rate_site = site_success_rate.idxmax()
highest_rate = site_success_rate.max()

print(f"Highest launch success rate: {highest_rate_site} with success rate of {highest_rate:.2%}")

bins = list(range(0, 11000, 1000))
spacex_df['Payload Bin'] = pd.cut(spacex_df['Payload Mass (kg)'], bins)

payload_success_rate = spacex_df.groupby('Payload Bin')['class'].mean()
highest_payload_bin = payload_success_rate.idxmax()
lowest_payload_bin = payload_success_rate.idxmin()

print(f"Highest success rate payload range: {highest_payload_bin} with rate {payload_success_rate.max():.2%}")
print(f"Lowest success rate payload range: {lowest_payload_bin} with rate {payload_success_rate.min():.2%}")

booster_success_rate = spacex_df.groupby('Booster Version Category')['class'].mean()
top_booster = booster_success_rate.idxmax()
top_booster_rate = booster_success_rate.max()

print(f"Highest success rate booster: {top_booster} with success rate {top_booster_rate:.2%}")
