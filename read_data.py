import pandas as pd

# Read Excel file
data = pd.read_excel("dataset/mutual_fund_nav.xlsx", header=4)

# Select only required columns
data = data[["Net Asset Value", "Date", "Plan", "Option"]]

# Keep only Direct Plan - Growth
data = data[
    (data["Plan"] == "Direct Plan") &
    (data["Option"] == "Growth")
]

# Rename columns
data = data.rename(columns={
    "Net Asset Value": "NAV"
})

# Convert Date to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Convert NAV to numeric
data["NAV"] = pd.to_numeric(data["NAV"], errors="coerce")

# Remove missing values
data = data.dropna(subset=["Date", "NAV"])

# Remove duplicate dates
data = data.drop_duplicates(subset=["Date"])

# Sort by date
data = data.sort_values("Date")

# Keep only Date and NAV
data = data[["Date", "NAV"]]

# Save cleaned dataset
data.to_csv("dataset/mutual_fund_nav_clean.csv", index=False)

# Display results
print("Cleaned Dataset:")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nNumber of Rows and Columns:")
print(data.shape)

print("\nFirst Date:", data["Date"].min())
print("Last Date:", data["Date"].max())