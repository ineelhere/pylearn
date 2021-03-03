# SIMPLE LINEAR REGRESSION
# let us use this eqn for reference y = a₀ + a₁(x)

#Import packages and classes
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Define the data
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1)) #regressors(input), .reshape(-1,1) makes it a 2D array that has 1 column and as many rows as possible
y = np.array([5, 20, 14, 32, 22, 38]) #predictor(output)

#Model creation
model = LinearRegression()

#Fit/Start using the model
model.fit(x,y) #could have directly used model = LinearRegression().fit(x, y)

#Get results
score = model.score(x,y) #Coeff of determination - R square
print(f"Coeff of determination (R Square) = {score}")

intercept = model.intercept_ #this is a₀
print(f"Intercept (response predicted by model when x is 0) = {intercept}")

slope = model.coef_ #this is a₁
print(f"Slope (how many times the predicted response rises when x is increased by one) {slope}")

#Predict response
y_pred = model.predict(x)  #pass the regressor as the argument and get the corresponding predicted response
print(f"The predicted response = {y_pred} ")


#optional -- alternative
y_pred_alt = model.intercept_ + model.coef_ * x # y = a₀ + a₁(x) >>> multiply each element of x with model.coef_ and add model.intercept_ to the product.
print(y_pred_alt) 
#The output here differs from the previous example only in dimensions. 
#The predicted response is now a two-dimensional array, while in the previous case, it had one dimension.


#use fitted model to calculate outputs for new inputs
m = np.random.rand(65).reshape((-1, 1)) # the input (independent)
print(f"Prediction for new data = {model.predict(m)}") #the output (dependent)

#make a plot of the new data
plt.scatter(m,model.predict(m), alpha=0.1);
plt.plot(m,model.predict(m));
