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

## About the dataset 

The dataset consist of resale flat prices in Singapore from 1990 to 1999 obtained from Kaggle.

Number of rows: 287196

Columns:
* month - yyyy-mm of resale transaction
* town - the town in which the resale flat belong to
* flat type - type of flat in which the hdb unit
* block - blk number in address of flat
* street_name - street in address of flat
* floor_area_sqm - size of flat in square meters
* lease_commence_date - yyyy in which flat lease begin
* resale_price - price at which the resale flat was sold

## Conclusions from EDA

**Month**

1. The resale prices increases over the years as expected - **Year of transaction will be an important feature**
2. The quarter (Q1- Q4) in which the sale is made seems to have minimal effect on resale price

**Town**

3. The resale prices vary largely according to the town as expected - **Town will be an important feature**
4. Some towns have fewer data points and may lead to poorer predictions (e.g. Bukit Timah, Lim Chu Kang, Sembawang, Sengkang)
5. Grouping the towns by region (North, North-East, East, West, Central) according to [this](https://en.wikipedia.org/wiki/Planning_Areas_of_Singapore) helps to solve point 4. However, this also removes the variance in point 3 as the resale flat prices balance each other out

**Flat type**

6. The resale prices vary largely according to flat types as expected - **Flat type will be an important feature**
7. Some flat types have fewer data points and may lead to poorer predictions (i.e. 1-room, 2-room and Multigeneration)

**Storey range**

8. The resale prices vary largely according to storey range as expected - **Storey range will be an important feature**
9. Some storey ranges have fewer data points and may lead to poorer predictions (i.e. > 16 storey)
10. Grouping the storey ranges into 4 groups - low, mid, high and very high help to improve the numbers and also help to preserve the trends in resale price

**Floor area**

11. The resale prices vary largely according to floor area as expected - **Floor area will be an important feature**
12. There are some rows with floor areas that are rather large (> 200 sqm), these belong to old HDB Maisonettes and Terraces

**Flat model**

13. The resale prices vary largely according to flat model as expected - **Flat model will be an important feature**
14. There are some models which are under represented (e.g. Improved-maisoneete, Multi-Generation, Premium Apartment, etc.)

**Lease commence date**

15. The resale prices vary proportionately according to lease commence date - **Lease commence date will be an important feature**

**Resale price**

16. The resale prices appear to follow a right skewed distribution as expected - probabilities of higher resale price decreases