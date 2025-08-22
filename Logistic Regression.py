import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


#Step 1: Create Sample Dataset
data = {
        'Hours_Studied':[1, 2, 2.5, 3, 3.5, 4, 5, 6, 6.5, 7, 8, 9],
        'Passed' : [0,0,0,0,0,1,1,1,1,1,1,1]
        }

df = pd.DataFrame(data)


# Step 2: Prepare features and labels

x = df[['Hours_Studied']]
y = df['Passed']

#Step 3: Split data
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 0)

# Step 4: Train Logistics Regression model
model = LogisticRegression()
model.fit(x_train, y_train)

# Step 5: Predict on test data
y_pred = model.predict(x_test)

# Step 6: Evaluate Performance
print("Accuracy: ",accuracy_score(y_test,y_pred))
print("Classification Reporty : \n", classification_report(y_test, y_pred))


# Step 7: Predict for a new student
hours = 4.5
prob = model.predict_proba([[hours]])[0][1]
prediction = model.predict([[hours]])[0]
print(f"Predicted Probability of Passing if studied {hours} hours: {prob:.2f}")
print("Prediction:", "Pass" if prediction == 1 else "Fail")

# Step 8: Visualization
x_plot = np.linspace(0, 10, 100).reshape(-1, 1)
y_probs = model.predict_proba(x_plot)[:, 1]

plt.figure(figsize = (8,5))
plt.scatter(x,y, color = 'blue', label = 'Actual Data')
plt.plot(x_plot, y_probs, color = 'red' , linewidth = 2, label = 'Logistic Curve')
plt.xlabel('Hours Studied')
plt.ylabel('Probability of Passing')
plt.title('Logistic Regression: Hours Studied vs Probability of Passing')
plt.legend()
plt.grid('true')
plt.show()







