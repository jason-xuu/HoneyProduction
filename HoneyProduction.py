import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the data
df = pd.read_csv("honeyproduction.csv")

# Display the first few rows to understand the data structure
print(df.head())

# Group by year and calculate mean of totalprod
prod_per_year = df.groupby('year').totalprod.mean().reset_index()
print(prod_per_year)

# Extract the year column as X and reshape it
X = prod_per_year["year"].values.reshape(-1, 1)

# Extract the totalprod column as y
y = prod_per_year["totalprod"].values

# Create the linear regression model
regr = LinearRegression()

# Fit the model to the data
regr.fit(X, y)

# Print the slope and intercept
print("Slope (regr.coef_):", regr.coef_[0])
print("Intercept (regr.intercept_):", regr.intercept_)

# Create the predictions using the model
y_predict = regr.predict(X)

# Plot the scatterplot of y vs X and the regression line
plt.scatter(X, y)
plt.plot(X, y_predict, color='red')  # Red line for the regression
plt.xlabel('Year')
plt.ylabel('Total Production')
plt.title('Total Honey Production per Year')
plt.show()

# Predict the honey production for the years 2013 to 2050
X_future = np.array(range(2013, 2051)).reshape(-1, 1)  # Range from 2013 to 2050

# Check the X_future before and after reshaping (optional)
print("X_future before reshaping:", range(2013, 2051))
print("X_future after reshaping:", X_future)

# Generate predictions for future years
future_predict = regr.predict(X_future)

# Plot the future predictions on a new plot
plt.plot(X_future, future_predict, color='green')
plt.xlabel('Year')
plt.ylabel('Predicted Honey Production')
plt.title('Predicted Honey Production (2013-2050)')
plt.show()

# Predict honey production for the year 2050
production_2050 = future_predict[-1]  # The last value corresponds to 2050
print(f"Predicted honey production for 2050: {production_2050}")
