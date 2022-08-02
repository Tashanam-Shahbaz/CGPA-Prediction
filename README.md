# CGPA-Prediction

 
Prediction of Cumulative Grade Point Average
INTRODUCTION:
In this project, we were asked to experiment with a real world dataset of grades with CGPA, and to explore how machine learning algorithms can be used to find the patterns in data. 
For the given problem statement and dataset we have 42 features of different courses. In corresponding to these we are required to predict CGPA. We can solve this problem using SUPERVISED LEARNING algorithms.

LIBRARIES USED:
•	Numpy (Python library used for working with arrays)
•	Pandas (Python package that is most widely used for data science/data analysis and machine learning tasks)
•	Matplotlib (a comprehensive library for creating static, animated, and interactive visualizations in Python)
•	Seaborn (Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics)
•	Sklearn (It provides a selection of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction via a consistence interface in Python)
•	Joblib (Joblib is a set of tools to provide lightweight pipelining in Python). We used it to store our models weights in .joblib files

DATASET:
 




VISUALIZATION AND PREPROCESSING DATA:
Describe Data	Columns:	Numbers of Missing Values:
 	 	 

INSIGHTS:
•	'CGPA' is the target column/variable.
•	'Seat No' doesn't contribute to the target variable 'CGPA'. So, we can remove it from the data.
•	As there are a lot of missing values in the columns 'CS-412' and 'CS-406', we can remove it from the data.
•	'PH-121' , 'HS-101' , 'CS-105' , 'CGPA' doesn't have any missing values. 
•	Other Columns has less number of missing value. We have to impute those using different techniques.
1. VISUALIZATION OF INDIVIDUAL FEATURES:
INSIGHTS:
These bar charts show in each courses, average numbers of students get which grade.
 
 
2.  ENCODING TECHNIQUES:
As most of machine learning algorithm of sklearn cannot manipulate categorical dataset so we are required to convert categorical data into numerical values using appropriate encoding techniques. For this purpose we have four most common techniques.
1.	DUMMY ENCODING: Not suitable as we have multiple grades.
2.	NUMRICAL ENCODING: Not suitable as we can find relationship among grade points.
3.	ONE-HOT ENCODING: It would complicate the dataset as we have already 42 columns.
4.	ORDINAL ENCODING: Grades points have relations and order with each other. (i.e A+ has much importance than D -).
We have assigned greater numerical values to greater grade points. 
 
DATASET AFTER ENCODING:
 

3.  CORRELATIONS BTWEENS COLUMNS:
Calculation of correlation between columns is important in dataset. It is recommended to avoid having correlated features in the dataset. Indeed, a group of highly correlated features will not bring additional information (or just very few), but will increase the complexity of the algorithm, thus increasing the risk of errors.
 
 INSIGHTS:
•	We know that every subject from different year are marked separately, advances courses are not included previous related course marks.
•	That’s why there is no positive or negative high correlations among courses.
•	Every feature is unique and bring new information. 
4. HANDLING MISSING VALUES:
1.	Impute all Columns of all Years Courses with its majority class (MODE).
•	At First place, given data is categorical.
•	Second, Dataset has a skewed (very little).
•	That’s why filling missing data with mode is the best option.
2.	Removing features:
•	In CS-406 and CS-412 there are 85 and 79 students are absent which is quit a big number. 
•	Dropping these two columns from dataset.
5. NORMALIZATION AND STANDARIZATION:
Not Required. As our dataset contain only grade points (categorical dataset ) so outliers cannot be presents

MODELS AND PREDICTIONS:
We have to predict CGPA which is a continuous values so we will apply REGRESSION ALGORITHMS.
Model 1: Predict final CGPA based on GPs of first year only.
We implement two algorithms using sklearn library.
a.	Decision Tree Regression:
It breaks down a dataset into smaller and smaller subsets while at the same time an associated decision tree is incrementally developed. The final result is a tree with decision nodes and leaf nodes.
For better visualization we set maximum depth to 3 levels. (We have to compromise with accuracy of the model.)
  

b.	Linear Regression:
Linear Regression is a machine learning algorithm based on supervised learning. It performs a regression task. Regression models a target prediction value based on independent variables. It is mostly used for finding out the relationship between variables.
 





Model 2: predict final CGPA based on GPs of first two years.
a.	K Nearest Neighbors Regressor :
KNN regression is a non-parametric method that, in an intuitive manner, approximates the association between independent variables and the continuous outcome by averaging the observations in the same neighborhood.
 
b.	Random Forest Regressor:
A random forest regressor. A random forest is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.
 
On zooming in this tree we can observed that CS-214 is a root node.
Model 3: predict final CGPA based on GPs of all years.
a.	Feed Forward Neural Network using TensorFlow:
Feedforward neural networks are also known as Multi-layered Network of Neurons (MLN). These network of models are called feedforward because the information only travels forward in the neural network, through the input nodes then through the hidden layers (single or many layers) and finally through the output nodes.




Layers:
 
 
Activation Function: First we use RELU and linear activation function but its performance with our data do not satisfied us. We switch to SWISH activation Function. We observe less error using swish.
Early Stopping: To prevent our model from over fitting we call the built-in early stopping function of keras.
Optimizer: Adam is a replacement optimization algorithm for stochastic gradient descent for training deep learning models. Adam combines the best properties of the AdaGrad and RMSProp algorithms to provide an optimization algorithm that can handle sparse gradients on noisy problems
History: With the increasing epoch we can observe the loss is decreasing. 
 
Following graph shows;
•	Loss function also decrease with increasing epoch.
•	Model work great with validation set also.
 
b.	Gradient Boosting Regressor

Gradient boosting is a type of machine learning boosting. It relies on the intuition that the best possible next model, when combined with previous models, minimizes the overall prediction error. The key idea is to set the target outcomes for this next model in order to minimize the error.
Following graph shows;
•	Deviance also decrease with increasing iterations
•	Model work good with test set also.
 

COMPARISION BTWEEN MODELS:
We use R square score for the calculation of accuracy of models. Models having high R2 Score will considered better.
Model 1: Predict final CGPA based on GPs of first year only
Decision Tree Regression	Linear Regression
R2 SCORE = 0.6446	R2 SCORE = 0.85
Model 2: predict final CGPA based on GPs of first two years.
K Nearest Neighbor	Random Forest Regressor
R2 SCORE = 0.7982	R2 SCORE = 0.8560
Model 3: predict final CGPA based on GPs of all years
Feed Forward Neural Network using TensorFlow:	Gradient Boosting Regressor
R2 SCORE = 0.737	R2 SCORE = 0.960
ISSUES:
The issue we found with dataset as this dataset does not have enough rows to cover all scenarios. 
For example 
1.	Some one enter all grades point as A+. Any model cannot predict 4.00 CGPA.
2.	Entering all F, any model cannot predict 0.00 CGPA.
SOLUTION: In future we can add these rows by our self to cover all senerios.
DEPLOYMENT OF MODELS:
We have created a small user interface,  so any one can find the CGPA using grade points.
MODEL SELECTED:
We use those algorithms that give us best r2 score. We have stored the weights into pickle files. 
FOR MODEL 1:  Linear Regression.pkl
FOR MODEL 2: Random Forest Regressor.pkl
FOR MODEL 3: Gradient Boosting Regressor.pkl
FLASK: Use for the backend Purpose.
DOCKER: We use Docker for creation of image of our project.
HEROKU: at the end we deploy our website on heroku.

DEPLOYED LINK :  https://cgpa-prediction-3.herokuapp.com/
