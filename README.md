# Singapore-Resale-Flat-Price-Prediction

Project plan:

1. EDA.ipynb

For each column:
* explore blank rows
* distribution of data
* effect on resale price (Engineer features if required)
* Provide visualizations

2. model_training.ipynb
* Feature engineering and selection 
* Dummy regressor (baseline)
* RandomForest (with optimized parameters)
* XGBoost 

3. app.py
* Flask app to host prediction front-end

## Conclusions from EDA

1. The resale prices increases over the years as expected - **Year of transaction will be an important feature**
2. The quarter (Q1- Q4) in which the sale is made seems to have minimal effect on resale price
3. The resale prices vary largely according to the town as expected - **Town will be an important feature**
4. Some towns have fewer data points and may lead to poorer predictions (E.g. Bukit Timah, Lim Chu Kang, Sembawang, Sengkang)
5. Grouping the towns by region (North, North-East, East, West, Central) according to [this](https://en.wikipedia.org/wiki/Planning_Areas_of_Singapore) helps to solve point 4. However, this also removes the variance in point 3 as the resale flat prices balance each other out