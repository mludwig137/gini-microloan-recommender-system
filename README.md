
# Kiva Analysis & Recommender System:
## Data for Good

By: Brian Rubin, Matthew Ludwig, Terri John


This ReadMe contains:

* [Project Contents](#contents)
* [Problem Statement](#problemstatement)
* [Background](#background)
* [A description of the data and Project Requirements](#data)
* [Modeling and Analysis](#model)
* [Conclusion](#conclusion)
* [Sources](#sources)
* [Data Dictionary](#dict)


## <a name="contents"></a>Project Contents:

|Name|File Type|Description|
|---|---|--|
|01_Cleaning_and_Data_Visualizations|Jupyter Notebook|Cleans the data to prepare for modeling. Data Visualizations.|
|02_Preprocessing|Jupyter Notebook|Processes NLP data for visualizations and modeling.|
|03_Modeling|Jupyter Notebook|Builds a content based recommender system.|
|04_User_Model|Jupyter Notebook|Builds a user based recommender system for groups.|
|data|folder|contains csv files of data used|
|images|folder|contains saved plot images|
|streamlit|folder|contains streamlit.py file, folder with streamlit images, folder with streamlit data files|

## <a name="problemstatement"></a>Problem Statement

The microloan crowdfunding organization Kiva has a website that links entrepreneurs and lenders throughout 77 countries. On their website they state an interest in working with the data science community on various machine learning projects, including the need for recommender systems. With the goal of increasing repeat lender participation and to develop a sense of community among lenders to increase user retention, we set out to develop two distinct recommender systems that would increase loan contributions, thereby improving quality of life for millions of people around the globe.

## <a name="background"></a>Background

### What are microloans?

Microlending is defined as "small lending to the rural poor in developing countries." (https://www.pbs.org/frontlineworld/stories/uganda601/history.html) It enables individuals who may face challenges applying for and receiving traditional bank loans to receive a loan. While microlending has been in existence in some capacity since the 1700s, it began gaining momentum in the 1980s with the advent of several microlending organizations around the world, including the Grameen bank and ACCION International.

Grameen Bank and its founder, Muhammad Yunus, were awarded the Nobel Peace Price in 2006 "for their efforts to create economic and social development from below." (https://www.nobelprize.org/prizes/peace/2006/summary/)

### About Kiva

Kiva is a 501(c)3 U.S. nonprofit organization founded in 2005. It's website is a forum for crowdsourcing contributions to microloans for entrepreneurs around the world. Since 2005, Kiva has had 4.1 million borrower users and 2 million lender users.

Kiva loans can follow two models: partner and direct. "Direct loans on Kiva are currently only available to businesses in the US and social enterprises internationally." The vast majority of loans are facilitated by a field partner, which is an organization managing the loan locally. These types of loans are first approved by the field partner before being posted on Kiva.org. Field partners go through Kiva's vetting process and are monitored. Kiva does not guarantee that lenders will be repaid, but boasts a 96.3% repayment rate.

Read more in Kiva's FAQ: https://www.kiva.org/about/how

Source: https://www.kiva.org/about


## <a name="data"></a>Data:

### Get the Data:
* The data for this study is available on kiva.org:
https://www.kiva.org/build/data-snapshots
* Download 'Snapshots' as a CSV: http://s3.kiva.org/snapshots/kiva_ds_csv.zip
* Save the unzipped csv files to the 'raw' folder inside of the 'data' folder
  * (data --> raw)

This dataset consists of 3 csv files:

|Name|Description|Data Dictionary|
|---|---|---|
|lenders.csv|Kiva lender profiles|[Jump to the data dictionary](#lendersdict)|
|loans_lenders.csv|a list of loans and the contributing lenders|[Jump to the data dictionary](#lldict)|
|loans.csv|loans and their attributes|[Jump to the data dictionary](#loansdict)|


#### Data Cleaning Steps: loans.csv
1. Dropped nulls:  Nulls banded by age and rows with majority missing values.
2. Combined Description and Description translated columns to have one Description column in English.
3. Engineered a binarized column based on the BORROWER_GENDERS column. This column is a 1 if all borrowers are female, and is otherwise a 0.
4. get_dummies of columns ORIGINAL_LANGUAGE, ACTIVITY_NAME, and SECTOR_NAME to prepare for modeling.
5. Dropped columns that were unneeded for our recommender system:


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
### Limitations and Recommendations for next steps:
Throughout the course of this project, we observed the need for further actions in several capacities:

* True P2P Microloan future utilizing decentralized financial systems.
* Recommender system improvements - data size constraints limiting the ability to process all the data at once. Downsampled to create proof of concept systems.  
* While we reached out to the Grameen Bank in the hopes of gaining access to data related to their microlending operation, we did not receive a response. We recommend gathering data from several microlending organizations to compare effectiveness of differing strategies. It would be particularly interesting to study data from Zidisha, an organization which focuses solely on direct lender to entrepreneur loans, without an intermediary such as a field partner.

(source: https://www.zidisha.org/how-it-works)



### <a name="sources"></a>Sources

* NobelPrize.org: https://www.nobelprize.org/prizes/peace/2006/summary/
* Muhammad Yunus biography: https://www.nobelprize.org/prizes/peace/2006/yunus/facts/
* PBS Frontline: https://www.pbs.org/frontlineworld/stories/uganda601/history.html
* Zidisha: https://www.zidisha.org/how-it-works
* Kiva: https://www.kiva.org/

### <a name="dict"></a>Data Dictionaries:
[Jump back to the Data Description](#data)
#### <a name="loansdict"></a>loans.csv

|Column|Data Type|Description|
|---|---|---|
LOAN_ID|int|unique loan ID number|
LOAN_NAME|object|name of lendee(s)|
ORIGINAL_LANGUAGE|object|original language of description column|
DESCRIPTION|object|description of the loan|
DESCRIPTION_TRANSLATED|object|English translation of description if original is in another language|
FUNDED_AMOUNT|float|Amount of loan that has been funded to date|
LOAN_AMOUNT|float|amount of requested loan|
STATUS|object|status of loan: funded, refunded, expired|
IMAGE_ID|float|ID number of lendee profile photo|
VIDEO_ID|float|ID number of lendee video|
ACTIVITY_NAME|object|Activity category of loan. During cleaning for modeling, this column was dummified.|
SECTOR_NAME|object|Sector category of loan within a certain Activity. During cleaning for modeling, this column was dummified.|
LOAN_USE|object|description of how the loan would be used.|
COUNTRY_CODE|object|a numerical value associated with a given country for ID purposes.|
COUNTRY_NAME|object|lendee's country.|
TOWN_NAME|object|lendee's town.|
CURRENCY_POLICY|object|unused column|
CURRENCY_EXCHANGE_COVERAGE_RATE|float|unused column|
CURRENCY|object|unused column|
PARTNER_ID|int|unused column|
POSTED_TIME|object|Date and time when a loan was posted on the site.|
PLANNED_EXPIRATION_TIME|object|expiration time of loan|
DISBURSE_TIME|object|date/time when a loan was disbursed.|
RAISED_TIME|object|date/time when a loan was fully funded.|
LENDER_TERM|float|used column|
NUM_LENDERS_TOTAL|int|the number of lenders who contributed to a given loan.|
NUM_JOURNAL_ENTRIES|int|unused column|
NUM_BULK_ENTRIES|int|unused column|
TAGS|object|hashtags associated with the loan.|
BORROWER_NAMES|object|names of lendees.|
BORROWER_GENDERS|object|genders of lendees.|
BORROWER_PICTURED|object|unused column|
REPAYMENT_INTERVAL|object|unused column|
DISTRIBUTION_MODEL|object|unused column|
FEMALE_OPERATED|int|engineered column - binarized form of BORROWER_GENDERS. 1 if borrower(s) all female, otherwise 0.|

[Jump back to the Data Description](#data)
#### <a name="lldict"></a>loans_lenders.csv

|Column|Data Type|Description|
|---|---|---|
|LOAN_ID|int|unique loan ID number|
|LENDERS|object|list of lenders who contributed to a loan.|
</details>

#### <a name="lendersdict"></a>lenders.csv

|Column|Data Type|Description|
|---|---|---|
|PERMANENT_NAME|object|username|
|DISPLAY_NAME|object|lender's display name on site.|
|MAIN_PIC_ID|float|used column|
|CITY|object|lender's city|
|STATE|object|lender's state|
|COUNTRY_CODE|object|lender's country|
|MEMBER_SINCE|int|when lender joined kiva.org|
|PERSONAL_URL|object|lender's URL|
|OCCUPATION|object|lender's occupation|
|LOAN_BECAUSE|object|a lender's description of why they contribute to loans with Kiva.|
|OTHER_INFO|object|unused column|
|LOAN_PURCHASE_NUM|int|loans contributed to|
|INVITED_BY|object|username of lender who invited new user|
|NUM_INVITED|int|number of people a user has invited to join the site|

[Jump back to the Data Description](#data)
