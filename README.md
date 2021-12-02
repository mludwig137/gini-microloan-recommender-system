
# <a name="top"></a> Recommender System for Microloan Contributers:
## A Study of the Kiva Dataset

By: Brian Rubin, Matthew Ludwig, Terri John


This ReadMe contains:

* [Project Contents](#contents)
* [Problem Statement](#problemstatement)
* [Background](#background)
* [A description of the data and Project Requirements](#data)
* [Modeling and Analysis](#model)
* [Conclusion](#conclusion)
* [Sources](#sources)


## <a name="contents"></a>Project Contents:

|Name|File Type|Description|
|---|---|--|
|01_EDA_&_Cleaning|Jupyter Notebook|Provides an introduction to the project, including problem statement and background, and the code to perform initial cleaning of the non-NLP data for modeling.|
|02_Preprocessing|Jupyter Notebook|Processes NLP data for visualizations and modeling.|
|03_Modeling|Jupyter Notebook|Builds a content based recommender system.|
|04_User_Model|Jupyter Notebook|Builds a user based recommender system for groups.|
|05_Data_Visualizations|Jupyter Notebook|Explores the data through visualizations|
|data|folder|contains csv files of data used|
|streamlit|folder|contains streamlit.py file, folder with streamlit images, folder with streamlit data files|

## <a name="problemstatement"></a>Problem Statement

The microloan crowdfunding organization Kiva has a website that links entrepreneurs and lenders throughout 77 countries. On their website they state an interest in working with the data science community on various machine learning projects, including the need for recommender systems. With the goal of increasing repeat lender participation and to develop a sense of community among lenders to increase user retention, we set out to develop two distinct recommender systems that would increase loan contributions, thereby improving quality of life for millions of people around the globe.

## <a name="background"></a>Background

### What are microloans?

Microlending is defined as "small lending to the rural poor in developing countries." (https://www.pbs.org/frontlineworld/stories/uganda601/history.html) It enables individuals who may face challenges applying for and receiving traditional bank loans to receive a loan. While microlending has been in existence in some capacity since the 1700s, it began gaining momentum in the 1980s with the advent of several microlending organizations around the world, including the Grameen bank and ACCION International.

Grameen Bank and its founder, Muhammad Yunus, were awarded the Nobel Peace Price in 2006 "for their efforts to create economic and social development from below." (https://www.nobelprize.org/prizes/peace/2006/summary/)

### About Kiva

Kiva is a 501(c)3 U.S. nonprofit organization founded in 2005. It's website is a forum for crowdsourcing contributions to microloans for entrepreneurs around the world. Since 2005, Kiva has had 4.1 million borrower users and 2 million lender users.

Kiva loans can follow two models: partner and direct. "Direct loans on Kiva are currently only available to businesses in the US and social enterprises internationally." The vast majority of loans are facilitated by a field partner, which is an organization managing the loan locally. These types of loans are first approved by the field partner before being posted on Kiva.org. Field partners go through Kiva's vetting process and are monitored. While Kiva does not guarantee that lenders will be repaid, but boasts a 96.3% repayment rate.

Read more in Kiva's FAQ: https://www.kiva.org/about/how

Source: https://www.kiva.org/about


## <a name="data"></a>Data:
The data for this study was available on kiva.org:
https://www.kiva.org/build/data-snapshots

Download 'Snapshots' as a CSV.

This dataset consists of 3 csv files:

|Name|Description|
|---|---|
|lenders.csv|Kiva lender profiles|
|loans_lenders.csv|a list of loans and the contributing lenders|
|loans.csv|loans and their attributes|

#### Data Cleaning Steps


### Data Dictionaries:
#### lenders.csv


#### loans.csv

#### loans_lenders.csv

### Project Requirements:   
* streamlit==1.1.0
* joblib==1.1.0
* pandas==1.2.4
* scikit-learn==1.0.1

## <a name="model"></a>Modeling and Analysis
We created 2 main recommender system models:
1. [Content Based Model](#content)
2. [User Based Model](#user)


### <a name="content"></a>  Content Based Model



### <a name="user"></a> User Based Model




## <a name="conclusion"></a>Conclusion:



### Recommendations for next steps:
Throughout the course of this project, we observed the need for further actions in several capacities:

* coin
* recommender system improvements
* While we reached out to the Grameen Bank in the hopes of gaining access to data related to their microlending operation, we did not receive a response. We recommend gathering data from several microlending organizations to compare effectiveness of differying strategies. It would be particularly interesting to study data from Zidisha, an organization which focuses solely on direct lender to entrepreneur loans, without an intermediary such as a field partner.
(source: https://www.zidisha.org/how-it-works)



### <a name="sources"></a>Sources

* NobelPrize.org: https://www.nobelprize.org/prizes/peace/2006/summary/
* Muhammad Yunus biography: https://www.nobelprize.org/prizes/peace/2006/yunus/facts/
* PBS Frontline: https://www.pbs.org/frontlineworld/stories/uganda601/history.html
* Zidisha: https://www.zidisha.org/how-it-works
* Kiva: https://www.kiva.org/
