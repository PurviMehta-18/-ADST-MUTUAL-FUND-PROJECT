import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned dataset
data = pd.read_csv("dataset/mutual_fund_nav_clean.csv")

# Convert Date to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Display first 5 rows
print("First 5 rows:")
print(data.head())

# Display last 5 rows
print("\nLast 5 rows:")
print(data.tail())

# Dataset shape
print("\nDataset Shape:")
print(data.shape)

# Dataset information
print("\nDataset Information:")
print(data.info())

# Statistical summary
print("\nStatistical Summary:")
print(data["NAV"].describe())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Minimum and Maximum NAV
print("\nMinimum NAV:", data["NAV"].min())
print("Maximum NAV:", data["NAV"].max())

# Average NAV
print("Average NAV:", data["NAV"].mean())

# Plot NAV over time
plt.figure(figsize=(10, 5))

plt.plot(data["Date"], data["NAV"])

plt.xlabel("Date")
plt.ylabel("NAV")

plt.title("SBI Large Cap Fund NAV Over Time")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# Moving average graph

data["MA_30"] = data["NAV"].rolling(30).mean()

plt.figure(figsize=(10, 5))

plt.plot(data["Date"], data["NAV"], label="Actual NAV")
plt.plot(data["Date"], data["MA_30"], label="30 Day Moving Average")

plt.xlabel("Date")
plt.ylabel("NAV")

plt.title("NAV and 30 Day Moving Average")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# Calculate 30 day moving average
data["MA_30"] = data["NAV"].rolling(30).mean()

# Plot NAV and moving average
plt.figure(figsize=(10, 5))

plt.plot(data["Date"], data["NAV"], label="Actual NAV")
plt.plot(data["Date"], data["MA_30"], label="30 Day Moving Average")

plt.xlabel("Date")
plt.ylabel("NAV")

plt.title("NAV and 30 Day Moving Average")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()