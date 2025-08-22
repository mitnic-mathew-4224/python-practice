import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


data = {
        'Area' : [500,1000,1500,2000,2500,3000,3500,4000],
        'Price' : [30,50,70,85,110,130,150,165]
}

df = pd.DataFrame(data)


# step 2 : Prepare Data
x = df[['Area']]
y = df['Price']


# Step 3: Split into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 42)

# STep 4: Create and train model
model = LinearRegression()
model.fit(x_train,y_train)


# Step 5: Make Predictions
y_pred = model.predict(x_test)

# Step 6: Evaluate the model

mse = mean_squared_error(y_test,y_pred)
print("Mean Squared Error:", mse)
print("Model Coefficient (Slope) :", model.coef_[0])
print("Model Intercept:", model.intercept_)


# Step 7: Predict for a new area
new_area = 3200
predicted_price = model.predict([[new_area]])
print(f"Predicted price for {new_area} sq ft:{predicted_price[0]:.2f} lakhs")


# Step 8: Plotting
plt.scatter(x,y, color = 'blue', label = 'Actual Data')
plt.plot(x, model.predict(x), color = 'red', linewidth = 2, label= 'Regression Line')
plt.xlabel('Area (sq ft)')
plt.ylabel('Price (lakhs)')
plt.title('Linear Regression: Area vs Price')
plt.legend()
plt.grid(True)
plt.show()



