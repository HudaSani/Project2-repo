# Diamond Price Prediction using FNN
## Summary
##### The aim of this project is to predict the price of a diamond based on a few features. The data used in this project is obtained from [Kaggle: Diamonds](https://www.kaggle.com/datasets/shivam2503/diamonds)
##
### 1. IDE and Framework
##### This project is created using Google Colab. The frameworks used are Pandas, Numpy, Scikit-Learn, Tensorflow Keras.
### 2. Methodology
#### 2.1 Data Pipeline
##### Data is upload into the google drive using google.colab file upload. The data is analyzed for preprocessing. In this step, unwanted or unrelated feature is removed. Ordinal encoder is used to encode categorical features with ordinal data. The data is split into train-validation-test sets with ratio of 60:20:20.
#### 2.2 Model Pipeline
##### Feed-forward Neural Network is construction for regression problem. The structure of the model is shown in the figure below.
##### Model is trained with batch size of 60 for 100 iteration. Early stopping is applied and stopped at epoch 13. The graph of training process is visualize using TensorBoard. Training process of the model resulting in MAE = 564 and val_MAE = 435.
### 3. Result
##### Evaluation result on test data is shown in the figure below. Plotted graph of predictions against labels shows proportionality between x and y.
