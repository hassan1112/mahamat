
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from modules import *
from connection import *
import tkinter
from tkinter import *
from matplotlib.pyplot import *
from sklearn.metrics import r2_score
import pickle
from sklearn.metrics import mean_squared_error
con = Connection()
try:
    import numpy as np

    data= con.get_data()
    
except Exception as err:
    print("{0}".format(err))

finally:
    con.close()
    print("Database is  succesafuy closed ")
    
    
data = data.iloc[:,1:]    
print("\nEnd of Reading the data from sqlite3 house table ")
data.head()

data= data.sort_values(["price"],ascending=TRUE)
data.reset_index(drop=True,inplace=True)

data.to_csv("sorted_data.csv")



'''
defining the dependent variable and independent variables from the data set
clustered by kmeans module
'''

y = data['price']
x = data.iloc[:,1:]
clustered_data = x

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

class model_evaluation:
            
    def rmse(y_test, y_pred):
        '''Root Mean Square error :'''
        rmse = np.sqrt(sum((y_test - y_pred) ** 2) / len(y_test))
        return rmse
    
    
    def r2_score(y_test, y_pred):
        '''Model Evaluation - R2 Score :'''
        mean_y = np.mean(y)
        ss_tot = sum((y_test - mean_y) ** 2)
        ss_res = sum((y_test - y_pred) ** 2)
        r2 = 1 - (ss_res / ss_tot)
        return r2
     
    def sse(y_test, y_pred):
        '''Model Evaluation - sse Score :'''
        result = np.sum((y_test - y_pred) ** 2)
        
        return result



#train the model
model = LinearRegression()
model.fit(x_train,y_train)
y_pred1 = model.predict(x_test)

#evaluation of MLR mode


print("Multiple linear regression Evaluation")
print("----MLR without gradient descent----")
print("Residual errors")
print("\t\t MSE {0}".format(mean_squared_error(y_test, y_pred1)))
print("\t\t RMSE {0}".format(model_evaluation.rmse(y_test, y_pred1)))
print("\t\t SSE {0}".format(model_evaluation.sse(y_test, y_pred1)))
print("\n\nAccuracy/explained variance:")
print("\t\t r2 {0}".format(model_evaluation.r2_score(y_test, y_pred1)))

#plotting residual errors in test data
#plt.scatter(model.predict(x_test), model.predict(x_test) - y_test,color = "blue", s = 10, label = 'Test data')
 

        
evaluation = model_evaluation()
print("\n\n")
gradientdescent = ensemble.GradientBoostingRegressor()
gradientdescent.fit(x_train, y_train)
y_pred2 = gradientdescent.predict(x_test)
print("\n"*10)
print("----MLR with gradient descent----")
print("Residual errors")
print("\t\t MSE {0}".format(mean_squared_error(y_test, y_pred2)))
print("\t\t RMSE {0}".format(model_evaluation.rmse(y_test, y_pred2)))
print("\t\t SSE {0}".format(model_evaluation.sse(y_test, y_pred2)))
print("\n\n Explained variance\n")
print("\t\t r2 {0}".format(model_evaluation.r2_score(y_test, y_pred2)))

pickle.dump(gradientdescent, open("trained_model.pkl","wb"))

#print("\t\t sse {0}".format(model_evaluation.sse(y_test, y_pred2)))
 

# variance score: 1 means perfect prediction 
print("Variance score: {}".format(gradientdescent.score(x_test, y_test))) 



from sklearn.linear_model.stochastic_gradient import SGDRegressor
sgdr = SGDRegressor()
sgdr.fit(x_train,y_train)
predict_gd = sgdr.predict(x_test)
print(model_evaluation.r2_score(y_test,predict_gd))

data.plot.bar()
plt.show()
plt.style.use('fivethirtyeight') 

def residualerror():  
    ## plotting residual errors in training data 
    plt.scatter(gradientdescent.predict(x_train), gradientdescent.predict(x_train) - y_train, 
                color = "green", s = 10, label = 'Train data') 
    plt.scatter(gradientdescent.predict(x_test), gradientdescent.predict(x_test) - y_test, 
                color = "blue", s = 10, label = 'Test data') 
    plt.hlines(y = 0, xmin = 0, xmax = 50, linewidth = 4) 
    plt.legend(loc = 'upper right') 
    plt.title("Residual errors") 
    plt.show()
    

residualerror()


#Multi colinearity
import matplotlib

def multicolinarity():
    print("--------------Correlation plot----------")
    
    corr = x_train.corr(method='pearson')
    mask = np.zeros_like(corr)
    mask[np.tril_indices_from(mask)] = True
    sn.heatmap(corr,cmap="YlGnBu",vmax=1.0, vmin=1.0, mask = mask,linewidths=2.5)
    plt.yticks(rotation=0)
    plt.xticks(rotation = 90)
    plt.show()
    
multicolinarity()



def correlation_matrix():
    plt.title("Features correlation")
    names= data.columns
    correlation = data.corr()
    fig = plt.figure()
    fig.set_size_inches(9.5,9.5)
    ax = fig.add_subplot(111)
    cmap=cm.get_cmap('jet',100)
    color_bar = ax.imshow(correlation,cmap=cmap,vmin=-1,vmax=1)
    ax.grid(True)
    #ticks=np.arange(0,14,1)
    ax.set_xticks(np.arange(len(names)))
    ax.set_xticklabels(names,fontsize=8,rotation=90)
    ax.set_yticks(np.arange(len(names)))
    ax.set_yticklabels(names,fontsize=10)
    fig.colorbar(color_bar)
    plt.show()
#diognal shows prefect correlation 
.

print("*"*40)
def feature_Correlation():
    #price correlation with other columns
    cor = data.corr().iloc[1:]
    cor =cor.iloc[1:]
    print(cor)
    #a large -ve and +ve values signifies high correlation
    #plot the corelation
    cor.plot.bar()
    plt.title("Features Correlation with price")
    plt.legend("")
    plt.show()
 
feature_Correlation()

#Step wise regression
def backwardelimination():
    x_b0 = pd.read_csv("sorted_data.csv")
    y = data["price"]
    x_b0 = x_b0.iloc[:,2:]
    #add slop b0 to all the independent variables
    b0 = pd.DataFrame(np.zeros(2001))
    b0 = b0.astype(int)
    x_b0["b0"] = b0
    x_b0.to_csv("x_b0.csv")
    #x_b0['b0','bedrooms', 'bathrooms','sqft_living','sqft_lot','floors','condition','sqft_above','sqft_basement', 'yr_built', 'zipcode','cluster'] = x_b0['b0','bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors','condition', 'sqft_above', 'sqft_basement', 'yr_built', 'zipcode','cluster'].astype(np.int32)
    #x3 = pd.DataFrame(x_b0,columns=['b0','bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',   'condition', 'sqft_above', 'sqft_basement', 'yr_built', 'zipcode',    'lat', 'long', 'cluster'])

     
     
     
    #applying backward elimination formula to x_b0 dataset to optimize the model
    b0 = x_b0.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13]]
    
    x_optimal = x_b0.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11]]
    regressor_OLS = sm.OLS(endog = y, exog = x_optimal).fit()
    regressor_OLS.summary()
    
    #remove floors
    x_optimal = x_b0.iloc[:,[0,1,2,3,5,6,7,8,9,10,11]]
    regressor_OLS = sm.OLS(endog = y, exog = x_optimal).fit()
    regressor_OLS.summary()
    
    #remove sqf_lot
    x_optimal = x_b0.iloc[:,[0,1,2,5,6,7,8,9,10,11]]
    regressor_OLS = sm.OLS(endog = y, exog = x_optimal).fit()
    regressor_OLS.summary()
    
    x_optimal = x_b0.iloc[:,[0,1,2,5,6,7,8,9,10,11]]
    regressor_OLS = sm.OLS(endog = y, exog = x_optimal).fit()
    regressor_OLS.summary()
    

backwardelimination()


#training the MLR regressor
print("--------optimzed MLR after stepwise regression/OLS--------")
x_opt_train, x_opt_test, y_opt_train, y_opt_test = train_test_split(x_optimal, y, test_size = 0.2, random_state = 0)
regressor_opt = LinearRegression()
regressor_opt.fit(x_opt_train, y_opt_train)
y_opt_pred = regressor_opt.predict(x_opt_test)
print("---the predicted prices ----")
print(pd.DataFrame(y_opt_pred).astype(int))



print("*"*40)
#def Randomforest():
print("*"*40)
print("--------Random forest--------------")
from sklearn.metrics import explained_variance_score
from sklearn.ensemble import RandomForestRegressor
randforsetregressor = RandomForestRegressor(n_estimators=100,min_samples_leaf=4,random_state=4)
randforsetregressor.fit(x_train,y_train)
prediction = randforsetregressor.predict(x_test)
print("the mean sqaure error %2f"%mean_squared_error(y_test,randforsetregressor.predict(x_test)))
print("explained variance %3f"%explained_variance_score(y_test,prediction))
    
'''
try:
    file = open("trained_model.pkl","wb")
    pickle.dump(randforsetregressor,file )
except pickle.PicklingError as e:
    
    print(e)
'''