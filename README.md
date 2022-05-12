# Diamond Price Prediction using Feed-forward Neural Network
## Summary
##### The aim of this project is to predict the price of a diamond based on a few features. The data used in this project is obtained from [Kaggle: Diamonds](https://www.kaggle.com/datasets/shivam2503/diamonds)
##
### 1. IDE and Framework
##### This project is created using Google Colab. The frameworks used are Pandas, Numpy, Scikit-Learn, Tensorflow Keras.
### 2. Methodology
#### 2.1 Data Pipeline
##### Data is upload into the google drive using google.colab file upload. The data is analyzed for preprocessing. In this step, unwanted or unrelated feature is removed. Ordinal encoder is used to encode categorical features with ordinal data. The data is split into train-validation-test sets with ratio of 60:20:20.
##### ![data](https://github.com/HudaSani/Project2-repo/blob/main/img2/data.PNG?raw=True "Data")
#### 2.2 Model Pipeline
##### Feed-forward Neural Network is constructed for regression problem. The structure of the model is shown in the figure below.
##### ![model](https://github.com/HudaSani/Project2-repo/blob/main/img2/model.PNG?raw=True "model")
##### Model is trained with batch size of 60 for 100 iteration. Early stopping is applied and stopped at epoch 13. The graph of training process is visualize using TensorBoard. Training process of the model resulting in MAE = 564 and val_MAE = 435.
##### ![epoch loss](https://github.com/HudaSani/Project2-repo/blob/main/img2/epoch_loss.PNG?raw=True "epoch loss")
##### ![epoch mae](https://github.com/HudaSani/Project2-repo/blob/main/img2/epoch_mae.PNG?raw=True "epoch mae")
### 3. Result
##### Evaluation result on test data is shown below. Plotted graph of predictions against labels is shown and proportionality between x and y can be seen from the graph.
##### ![result](https://github.com/HudaSani/Project2-repo/blob/main/img2/test%20result.PNG?raw=True "test result")
##### ![graph](https://github.com/HudaSani/Project2-repo/blob/main/img2/Graph%20of%20predictions%20vs%20labels.PNG?raw=True "predictions vs labels")
