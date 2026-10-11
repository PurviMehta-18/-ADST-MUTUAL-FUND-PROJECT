import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Read dataset
data = pd.read_csv("../dataset/mutual_fund_nav_clean.csv")
# Convert Date
data["Date"] = pd.to_datetime(data["Date"])

# Convert date into a number
data["Date_Number"] = data["Date"].map(pd.Timestamp.toordinal)

# Input and output
X = data[["Date_Number"]]
y = data["NAV"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Training Completed")

print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)

# Save model
with open("mutual_fund_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")