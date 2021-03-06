import streamlit as st
import requests

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from PIL import Image
from io import BytesIO
import re

from sklearn.metrics.pairwise import cosine_similarity

#silence deprecationwarnings
st.set_option('deprecation.showPyplotGlobalUse', False)


#setting a seaborn color µ
colors = "gist_earth_r"
sns.set_palette("gist_earth_r")


st.sidebar.title('Kiva Analysis & Recommender System')
st.sidebar.subheader('Data Science for Good')



page = st.sidebar.selectbox( 'Select a page', ('Home Page', 'Visualizations', 'Content Based Filtering', 'Kiva Teams'))

if page == 'Home Page':
    st.header('Kiva Analysis & Recommender System')
    st.subheader('Data Science for Good')
    #streamlit forum solution on how to create images with embedded links : https://discuss.streamlit.io/t/how-can-i-add-a-url-link-to-an-image/13997
    st.markdown("[![Foo](https://www-kiva-org.global.ssl.fastly.net/cms/kiva_logo_1.png)](https://www.kiva.org/)")



    #Kiva Introduction Video
    st.video('https://www.youtube.com/watch?v=WCraaM6PAos')

    git, slides = st.columns(2)
    git.success('Project GitHub Source')
    git.markdown("[![Foo](https://img.icons8.com/material-outlined/96/000000/github.png)](https://github.com/mludwig137/gini-microloan-recommender-system)")
    slides.success('Project Slides')
    slides.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Google_Slides_logo_%282014-2020%29.svg/72px-Google_Slides_logo_%282014-2020%29.svg.png)](https://docs.google.com/presentation/d/1tLYIMdbjOniqPUQpQOYjEvaOj-24g1e41QbFLGiLISc/edit#slide=id.p)")

    st.sidebar.write('Team Members :')

    #inspired by this personal website : https://github.com/v4gadkari/vgpersonalwebsite/blob/main/streamlit_app.py
    st.sidebar.info('Terri John')
    cols1, cols2 = st.sidebar.columns(2)
    cols1.markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/terri-john/)")
    cols2.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/tjohn07)")

    st.sidebar.info('Matthew Ludwig')
    cols3, cols4 = st.sidebar.columns(2)
    cols3.markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/matthewjwjludwig/)")
    cols4.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/mludwig137)")

    st.sidebar.info('Brian Rubin')
    cols5, cols6 = st.sidebar.columns(2)
    cols5.markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/brian-f-rubin/)")
    cols6.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/brianfrubin)")

if page == 'Visualizations':
    st.sidebar.write('Overview:')
    st.sidebar.info('Data by Country')
    st.sidebar.info('Data by Sector')
    st.sidebar.info('Compare Two Countries')
    st.sidebar.info('General Visualizations')

    #inspiration for several plots on this page came from: https://practicaldatascience.co.uk/data-science/how-to-visualise-categorical-data-in-seaborn

    #read in the csv as a pandas dataframe
    streamlit_df = pd.read_csv('./streamlit_data/streamlit_df.csv')

    user_choice = st.selectbox('What would you like to visualize?', ['Data by Country','Data by Sector', 'Compare Two Countries',
    'General Visualizations'])

    if user_choice == 'Data by Country':
        country_name = st.selectbox('Select a Country', sorted(['Mexico', 'Kenya', 'Philippines', 'Cambodia', 'Togo', 'Palestine',
           'Bolivia', 'Sierra Leone', 'Mozambique', 'Madagascar',
           'Kyrgyzstan', 'Indonesia', 'Samoa', 'Tajikistan', 'Uganda',
           'Haiti', 'Nicaragua', 'Solomon Islands', 'Ecuador', 'Tonga',
           'India', 'Vietnam', 'Peru', 'Armenia', 'Costa Rica', 'Azerbaijan',
           'Paraguay', 'Ghana', 'Liberia', 'Kosovo', 'Lebanon', 'Pakistan',
           'South Sudan', 'Moldova', 'Egypt', 'Dominican Republic', 'Lesotho',
           'Albania', 'El Salvador', 'Guatemala', 'Rwanda', 'Colombia',
           'Georgia', 'Burkina Faso', 'Mongolia', 'Tanzania', 'Senegal',
           'Jordan', 'Fiji', 'Zimbabwe', 'Cameroon', 'Mali', 'Honduras',
           'Nigeria', 'The Democratic Republic of the Congo', 'Zambia',
           'Ukraine', 'United States', 'Iraq', 'Turkey', 'Papua New Guinea',
           'Burundi', 'Congo', 'Timor-Leste', 'Malawi', 'Benin', 'Nepal',
           'Brazil', 'South Africa', 'Chile', 'Thailand', 'Yemen',
           'Afghanistan', 'China', 'Puerto Rico', 'Israel', 'Vanuatu',
           'Myanmar (Burma)', 'Panama', "Cote D'Ivoire",
           'Bosnia and Herzegovina', 'Belize', 'Sri Lanka', 'Bulgaria',
           "Lao People's Democratic Republic", 'Suriname', 'Somalia',
           'Namibia', 'Canada', 'Saint Vincent and the Grenadines',
           'Bangladesh', 'Mauritania', 'Guam', 'Bhutan', 'Uruguay']),
            index=0)

        # functions to create country specific visualizations
        df = streamlit_df[streamlit_df['COUNTRY_NAME'] == country_name]

        def country_by_sector_bar(country_name):

            plt.figure(figsize=(12, 6))
            sns.histplot(df['SECTOR_NAME'])
            plt.xticks(rotation=20, fontsize=12)
            plt.xlabel('Sector', fontsize=14)
            plt.xticks(fontsize=12)
            plt.xlabel('Loan Count', fontsize=14)
            plt.title(f'Loans by Sector in {country_name}', fontsize=16);


        def country_by_gender(country_name):

            plt.figure(figsize=(12, 8))
            ax = sns.countplot(x="FEMALE_OPERATED", data=df)
            plt.title(f'Female Operated Loans in {country_name}', fontsize=16)

            x1 = [0, 1]
            xlabels = ['No', 'Yes']

            ax.set_xticks(x1)
            ax.set_xticklabels(xlabels, minor=False)

            plt.xlabel('Female Operated', fontsize=14)
            plt.ylabel('Number of Loans', fontsize=14);


        def country_by_loan_amount(country_name):

            plt.figure(figsize=(14, 6))
            sns.histplot(df['LOAN_AMOUNT'], multiple="dodge", shrink = 0.8, common_norm=False,
                            stat='probability', bins=20)
            plt.title(f'Loan Amount Range: {country_name}', fontsize=16)

            plt.xlabel('Loan', fontsize=14)
            plt.ylabel('Percentage of Loans', fontsize=14);


        def loan_average(country_name):
            plt.figure(figsize=(12, 8))
            sns.violinplot(x="COUNTRY_NAME", y="LOAN_AMOUNT", hue="FEMALE_OPERATED", data=df, split=True)
            plt.title(f'Average Loan Amount in {country_name}', fontsize=16)
            plt.ylabel('Loan Amount', fontsize=14)
            plt.xlabel('Country Name', fontsize=14)

        def time_trend_by_country(country_name):
            time_df = df.copy()
            time_df['POSTED_TIME'] = pd.to_datetime(time_df['POSTED_TIME'], utc=True)
            time_df.set_index('POSTED_TIME', inplace=True)
            time_df.sort_index(inplace=True)
            # df = time_df[time_df['COUNTRY_NAME'] == country_name]
            plt.figure(figsize=(12, 8))
            plt.plot(df['COUNTRY_NAME'].groupby([time_df.index.year]).agg('count'))
            plt.title(f'Loans Per Year from 2006-2021 in {country_name}', fontsize=16)
            plt.xlabel('Year', fontsize=14)
            plt.ylabel('Loans Counts', fontsize=14);


        if df.empty:
            st.write('Sorry, we don\'t have enough data on that country yet. Please select another.')
        else:
            st.pyplot(time_trend_by_country(country_name))
            st.pyplot(country_by_sector_bar(country_name))
            st.pyplot(loan_average(country_name))
            st.pyplot(country_by_gender(country_name))
            st.pyplot(country_by_loan_amount(country_name))





    if user_choice == 'Data by Sector':

        sector = st.selectbox('Select a Sector', sorted(['Food', 'Housing', 'Services', 'Agriculture', 'Education',
       'Retail', 'Clothing', 'Entertainment', 'Arts', 'Manufacturing',
       'Transportation', 'Health', 'Construction', 'Personal Use',
       'Wholesale']),index=0)

        df = streamlit_df[streamlit_df['SECTOR_NAME'] == sector]

        def get_ten_countries_sector(sector):
            #get top ten by value counts
            top_10_values = df['COUNTRY_NAME'].value_counts().to_frame()[:10]
            ten_df = df[df['COUNTRY_NAME'].isin(top_10_values.index)]

            plt.figure(figsize=(12, 6))
            sns.histplot(ten_df['COUNTRY_NAME'])
            plt.xticks(rotation=20, fontsize=12)
            plt.xlabel('Sector', fontsize=14)
            plt.xticks(fontsize=12)
            plt.xlabel('Country', fontsize=14)
            plt.title(f'Top Ten Countries for {sector} Loans', fontsize=16);

        def time_trend_by_sector(sector):
            time_df = df.copy()
            time_df['POSTED_TIME'] = pd.to_datetime(time_df['POSTED_TIME'], utc=True)
            time_df.set_index('POSTED_TIME', inplace=True)
            time_df.sort_index(inplace=True)
            # df = time_df[time_df['COUNTRY_NAME'] == country_name]
            plt.figure(figsize=(12, 8))
            plt.plot(df['COUNTRY_NAME'].groupby([time_df.index.year]).agg('count'))
            plt.title(f'Loans Per Year from 2006-2021: {sector}', fontsize=16)
            plt.xlabel('Year', fontsize=14)
            plt.ylabel('Loans Counts', fontsize=14);


        def loan_amount_by_sector(sector):

            plt.figure(figsize=(12, 6))
            sns.stripplot(x="ACTIVITY_NAME", y="LOAN_AMOUNT", data=df, palette="gist_earth_r")
            plt.title('Loan Amount by Activity', fontsize=16)
            plt.xlabel('Activity', fontsize=14)
            plt.ylabel('Loan Amount', fontsize=14)
            plt.xticks(rotation=20)


        def get_activities(sector):

            plt.figure(figsize=(12, 6))
            sns.histplot(df['ACTIVITY_NAME'], palette="gist_earth_r")
            plt.xticks(rotation=20, fontsize=12)
            plt.xlabel('Count', fontsize=14)
            plt.xticks(fontsize=12)
            plt.xlabel('Activity', fontsize=14)
            plt.title(f'Activity Breakdown for {sector} Loans', fontsize=16);

        st.pyplot(get_ten_countries_sector(sector))
        st.pyplot(time_trend_by_sector(sector))
        st.pyplot(loan_amount_by_sector(sector))
        st.pyplot(get_activities(sector))

        sector_country = st.selectbox('If you\'d like to see activity breakdown for this sector in a certain country, select that country here',
         sorted(['Mexico', 'Kenya', 'Philippines', 'Cambodia', 'Togo', 'Palestine',
           'Bolivia', 'Sierra Leone', 'Mozambique', 'Madagascar',
           'Kyrgyzstan', 'Indonesia', 'Samoa', 'Tajikistan', 'Uganda',
           'Haiti', 'Nicaragua', 'Solomon Islands', 'Ecuador', 'Tonga',
           'India', 'Vietnam', 'Peru', 'Armenia', 'Costa Rica', 'Azerbaijan',
           'Paraguay', 'Ghana', 'Liberia', 'Kosovo', 'Lebanon', 'Pakistan',
           'South Sudan', 'Moldova', 'Egypt', 'Dominican Republic', 'Lesotho',
           'Albania', 'El Salvador', 'Guatemala', 'Rwanda', 'Colombia',
           'Georgia', 'Burkina Faso', 'Mongolia', 'Tanzania', 'Senegal',
           'Jordan', 'Fiji', 'Zimbabwe', 'Cameroon', 'Mali', 'Honduras',
           'Nigeria', 'The Democratic Republic of the Congo', 'Zambia',
           'Ukraine', 'United States', 'Iraq', 'Turkey', 'Papua New Guinea',
           'Burundi', 'Congo', 'Timor-Leste', 'Malawi', 'Benin', 'Nepal',
           'Brazil', 'South Africa', 'Chile', 'Thailand', 'Yemen',
           'Afghanistan', 'China', 'Puerto Rico', 'Israel', 'Vanuatu',
           'Myanmar (Burma)', 'Panama', "Cote D'Ivoire",
           'Bosnia and Herzegovina', 'Belize', 'Sri Lanka', 'Bulgaria',
           "Lao People's Democratic Republic", 'Suriname', 'Somalia',
           'Namibia', 'Canada', 'Saint Vincent and the Grenadines',
           'Bangladesh', 'Mauritania', 'Guam', 'Bhutan', 'Uruguay']),
            index=0)
        df = streamlit_df[(streamlit_df['SECTOR_NAME'] == sector) & (streamlit_df['COUNTRY_NAME'] == sector_country)]
        def get_activities_by_country(sector, sector_country):
            # df = streamlit_df[(streamlit_df['SECTOR_NAME'] == sector) & (streamlit_df['COUNTRY_NAME'] == sector_country)]
            plt.figure(figsize=(12, 6))
            sns.histplot(df['ACTIVITY_NAME'], palette="gist_earth_r")
            plt.xticks(rotation=20, fontsize=12)
            plt.xlabel('Count', fontsize=14)
            plt.xticks(fontsize=12, rotation=20)
            plt.xlabel('Activity', fontsize=14)
            plt.title(f'Activity Breakdown for {sector} Loans in {sector_country}', fontsize=16);

        def loan_average_sector_country(sector, sector_country):
            # df = streamlit_df[(streamlit_df['SECTOR_NAME'] == sector) & (streamlit_df['COUNTRY_NAME'] == sector_country)]
            sns.barplot(x="ACTIVITY_NAME", y="LOAN_AMOUNT", data=df, estimator=np.mean, ci=None, palette="gist_earth_r")
            plt.title(f'Average Loan Amount in {sector_country} Per {sector} Activity', fontsize=16)
            plt.ylabel('Average Loan Amount', fontsize=14)
            plt.xlabel('Activity Name', fontsize=14)
            plt.xticks(rotation=20)

        def loan_average_sector_gender(sector, sector_country):
            df = streamlit_df[(streamlit_df['SECTOR_NAME'] == sector) & (streamlit_df['COUNTRY_NAME'] == sector_country)]
            plt.figure(figsize=(12, 8))
            sns.violinplot(x="ACTIVITY_NAME", y="LOAN_AMOUNT", data=df, split=True, palette="gist_earth_r")
            plt.title(f'Average Loan Amount in {sector_country}', fontsize=16)
            plt.ylabel('Loan Amount', fontsize=14)
            plt.xlabel('Activity Name', fontsize=14)

        st.pyplot(get_activities_by_country(sector, sector_country))
        st.pyplot(loan_average_sector_country(sector, sector_country))
        st.pyplot(loan_average_sector_gender(sector, sector_country))

    if user_choice == 'Compare Two Countries':

        country_name_1 = st.selectbox('Select a Country', sorted(['Mexico', 'Kenya', 'Philippines', 'Cambodia', 'Togo', 'Palestine',
        'Bolivia', 'Sierra Leone', 'Mozambique', 'Madagascar',
        'Kyrgyzstan', 'Indonesia', 'Samoa', 'Tajikistan', 'Uganda',
        'Haiti', 'Nicaragua', 'Solomon Islands', 'Ecuador', 'Tonga',
        'India', 'Vietnam', 'Peru', 'Armenia', 'Costa Rica', 'Azerbaijan',
        'Paraguay', 'Ghana', 'Liberia', 'Kosovo', 'Lebanon', 'Pakistan',
        'South Sudan', 'Moldova', 'Egypt', 'Dominican Republic', 'Lesotho',
        'Albania', 'El Salvador', 'Guatemala', 'Rwanda', 'Colombia',
        'Georgia', 'Burkina Faso', 'Mongolia', 'Tanzania', 'Senegal',
        'Jordan', 'Fiji', 'Zimbabwe', 'Cameroon', 'Mali', 'Honduras',
        'Nigeria', 'The Democratic Republic of the Congo', 'Zambia',
        'Ukraine', 'United States', 'Iraq', 'Turkey', 'Papua New Guinea',
        'Burundi', 'Congo', 'Timor-Leste', 'Malawi', 'Benin', 'Nepal',
        'Brazil', 'South Africa', 'Chile', 'Thailand', 'Yemen',
        'Afghanistan', 'China', 'Puerto Rico', 'Israel', 'Vanuatu',
        'Myanmar (Burma)', 'Panama', "Cote D'Ivoire",
        'Bosnia and Herzegovina', 'Belize', 'Sri Lanka', 'Bulgaria',
        "Lao People's Democratic Republic", 'Suriname', 'Somalia',
        'Namibia', 'Canada', 'Saint Vincent and the Grenadines',
        'Bangladesh', 'Mauritania', 'Guam', 'Bhutan', 'Uruguay']),
         index=0)

        country_name_2 = st.selectbox('Select Another Country', sorted(['Mexico', 'Kenya', 'Philippines', 'Cambodia', 'Togo', 'Palestine',
        'Bolivia', 'Sierra Leone', 'Mozambique', 'Madagascar',
        'Kyrgyzstan', 'Indonesia', 'Samoa', 'Tajikistan', 'Uganda',
        'Haiti', 'Nicaragua', 'Solomon Islands', 'Ecuador', 'Tonga',
        'India', 'Vietnam', 'Peru', 'Armenia', 'Costa Rica', 'Azerbaijan',
        'Paraguay', 'Ghana', 'Liberia', 'Kosovo', 'Lebanon', 'Pakistan',
        'South Sudan', 'Moldova', 'Egypt', 'Dominican Republic', 'Lesotho',
        'Albania', 'El Salvador', 'Guatemala', 'Rwanda', 'Colombia',
        'Georgia', 'Burkina Faso', 'Mongolia', 'Tanzania', 'Senegal',
        'Jordan', 'Fiji', 'Zimbabwe', 'Cameroon', 'Mali', 'Honduras',
        'Nigeria', 'The Democratic Republic of the Congo', 'Zambia',
        'Ukraine', 'United States', 'Iraq', 'Turkey', 'Papua New Guinea',
        'Burundi', 'Congo', 'Timor-Leste', 'Malawi', 'Benin', 'Nepal',
        'Brazil', 'South Africa', 'Chile', 'Thailand', 'Yemen',
        'Afghanistan', 'China', 'Puerto Rico', 'Israel', 'Vanuatu',
        'Myanmar (Burma)', 'Panama', "Cote D'Ivoire",
        'Bosnia and Herzegovina', 'Belize', 'Sri Lanka', 'Bulgaria',
        "Lao People's Democratic Republic", 'Suriname', 'Somalia',
        'Namibia', 'Canada', 'Saint Vincent and the Grenadines',
        'Bangladesh', 'Mauritania', 'Guam', 'Bhutan', 'Uruguay']),
         index=0)

        df1 = streamlit_df[streamlit_df['COUNTRY_NAME'] == country_name_1]
        df2 = streamlit_df[streamlit_df['COUNTRY_NAME'] == country_name_2]


        def loan_average_comparison(country_name_1, country_name_2):

            df = streamlit_df[(streamlit_df['COUNTRY_NAME'] == country_name_1) | (streamlit_df['COUNTRY_NAME'] == country_name_2)]
            sns.barplot(x="COUNTRY_NAME", y="LOAN_AMOUNT", data=df, estimator=np.mean, ci=None)
            plt.title(f'Average Loan Amounts in {country_name_1} and {country_name_2}')
            plt.ylabel('Average Loan Amount')
            plt.xlabel('Country')


        def side_by_side_gender(country_name_1, country_name_2):

            fig, axes = plt.subplots(1,2, figsize=(14, 6))

            x1 = [0, 1]
            xlabels = ['No', 'Yes']

            ax=sns.histplot(df1['FEMALE_OPERATED'], multiple="dodge",
                          stat = 'probability', bins=2, shrink = 0.8, common_norm=False,
                            ax=axes[0], palette='gist_earth_r')
            ax.set_title(f'Gender Breakdown: {country_name_1}', fontsize=16)

            ax.set_xticks(x1)
            ax.set_xticklabels(xlabels, minor=False)

            ax=sns.histplot(df2['FEMALE_OPERATED'], multiple="dodge",
                          stat = 'probability', bins=2, shrink = 0.8, common_norm=False, ax=axes[1])
            ax.set_title(f'Gender Breakdown: {country_name_2}', fontsize=16)
            ax.set_xticks(x1)
            ax.set_xticklabels(xlabels, minor=False)

            for ax in fig.axes:
                ax.tick_params(axis='x')
                ax.set_xlabel('Female Operated', fontsize=14)
                ax.set_ylabel('Percentage of Loans', fontsize=14)
                ax.set_ylim(0, 1.0);

        def side_by_side_sector(country_name_1, country_name_2):
            df1 = streamlit_df[streamlit_df['COUNTRY_NAME'] == country_name_1].sort_values(by=['SECTOR_NAME'], ascending=True)
            df2 = streamlit_df[streamlit_df['COUNTRY_NAME'] == country_name_2].sort_values(by=['SECTOR_NAME'], ascending=True)

            fig, axes = plt.subplots(2,1, figsize=(16, 18))

            #code for normalizing count data found on stackoverflow: https://stackoverflow.com/questions/34615854/seaborn-countplot-with-normalized-y-axis-per-group
            ax = sns.histplot(df1['SECTOR_NAME'], multiple="dodge",
                          stat = 'density', shrink = 0.8, common_norm=False, ax=axes[0])

            ax.set_title(f'Sector Breakdown: {country_name_1}', fontsize=16)
            plt.xticks(rotation=20);

            ax = sns.histplot(df2['SECTOR_NAME'], multiple="dodge",
                          stat = 'density', shrink = 0.8, common_norm=False, ax=axes[1])

            ax.set_title(f'Sector Breakdown: {country_name_2}', fontsize=16)
            plt.xticks(rotation=20)

            for ax in fig.axes:
                ax.tick_params(axis='x', labelrotation=20)
                ax.set_xlabel('Sector', fontsize=14)
                ax.set_ylabel('Percentage of Loans per Sector', fontsize=14)
                ax.set_ylim(0, 1.0);

        def side_by_side_loan_amount(country_name_1, country_name_2):
            df = streamlit_df[(streamlit_df['COUNTRY_NAME'] == country_name_1) | (streamlit_df['COUNTRY_NAME'] == country_name_2)]
            plt.figure(figsize=(12, 8))
            sns.violinplot(x="COUNTRY_NAME", y="LOAN_AMOUNT", hue="FEMALE_OPERATED", data=df, split=True)
            plt.title(f'Average Loan Amounts in {country_name_1} and {country_name_2}', fontsize=16)
            plt.ylabel('Loan Amount', fontsize=14)
            plt.xlabel('Country Name', fontsize=14)

        if df1.empty:
            st.write(f'Sorry, we don\'t have enough data on {country_name_1} yet. Please select another option.')
        if df2.empty:
            st.write(f'Sorry, we don\'t have enough data on {country_name_2} yet. Please select another option.')
        else:
            st.subheader(f'Here you can see a comparison of average loan amounts between {country_name_1} and {country_name_2}')
            st.pyplot(loan_average_comparison(country_name_1, country_name_2))
            st.write('\n')
            st.subheader('This plot compares the percentage of loans that are solely female operated versus those that are for male lendees or a group of men and women')
            st.pyplot(side_by_side_gender(country_name_1, country_name_2))
            st.subheader('Comparison by Sectors (%)')
            st.pyplot(side_by_side_sector(country_name_1, country_name_2))
            st.subheader('A comparison of Loan Amounts')
            st.pyplot(side_by_side_loan_amount(country_name_1, country_name_2))

    if user_choice == 'General Visualizations':
        st.write('The number of loans funded per year shows an upward trend from 2006-2018. There appears to be a slight decrease in 2018, followed by a sharp decrease that appears to precede the onset of the COVID-19 pandemic.')
        st.image('./streamlit_images/loans_over_time.png')
        st.write('According to Kiva\'s website, field partners have the option to distribute loans before, during, or after a loan is posted on the site. 93% of loans are disbursed before they are even posted. Read more about this process on Kiva\'s site: https://www.kiva.org/about/how#faq-hkw-section')
        st.image('./streamlit_images/loan_dist_pie_chart.png')
        st.write('66% of all Kiva loans go to individual women, vs. individual men(20%) and groups(13%).')
        st.image('./streamlit_images/borrower_comp.png')
        st.image('./streamlit_images/loans_by_sector.png')
        st.image('./streamlit_images/sector_and_country.png')
        st.image('./streamlit_images/loans_per_lender.png')
        st.image('./streamlit_images/top_10_female.png')
        st.image('./streamlit_images/low_fem_sec.png')
        st.image('./streamlit_images/low_fem_sec2.png')

if page == 'Kiva Teams':
    st.title('Kiva Teams')
    st.subheader('User Based Recommender System')
    st.write('------------------------------------')

    @st.cache
    def load_rec():
        recommender = pd.read_csv('./streamlit_data/team_recommender.csv')
        recommender.set_index('LENDERS', inplace=True)
        return recommender
        
    st.caption('User Matrix Visualization')
    recommender = load_rec()
    st.dataframe(recommender.head())
    st.write(recommender.shape)
    st.write('------------------------------------')

    user_text = st.text_input('Please enter your Kiva User ID:', value='Enter User ID')
    st.write('------------------------------------')

    def team_rec(input):
        search = input
        output = recommender[search].sort_values()[1:25]
        top_users = []
        for user in output.index:
            top_users.append(user)

        import requests
        count = 0
        print("Kiva Teams we think you might you like:")
        print('\n')  #make space between print statements - https://stackoverflow.com/questions/10081538/how-do-i-make-spaces-between-paragraphs-in-my-python-script
        st.subheader('We Found These 5 Kiva Teams For You:')
        st.write('------------------------------------')
        for user in top_users:
            base_url = f'https://api.kivaws.org/v1/lenders/{user}/teams.json'

            try:
                r = requests.get(base_url)
                r = r.json()
                team_name = r['teams'][0]['name']
                description = r['teams'][0]['description']
                loan_because = r['teams'][0]['loan_because']
                loans_made = r['teams'][0]['loan_count']
                how_much = r['teams'][0]['loaned_amount']
                count += 1

                container = st.container()
                container.write(f'Team {count}')
                container.write(f'Team Name : {team_name}')
                container.write(f'Description : {description}')
                container.write(f'Why We Loan : {loan_because}')
                container.write(f'Number of Loans Made : {loans_made}')
                container.write(f'How Much We Loaned : ${how_much}')
                container.write('\n')
                st.write('------------------------------------')
                if count == 5:
                    break
            except Exception:
                pass

    if st.text_input:
        try:
            print(team_rec(user_text))
        except Exception:
            pass


# Content Based Filtering

if page == "Content Based Filtering":


    # read in dataframes
    #loan_id_df = pd.read_csv("../data/transformed/loan_id.csv")
    model_df = pd.read_csv("./streamlit_data/processed_content_filter_data.csv")
    X = pd.read_csv("./streamlit_data/X_df.csv")

    # X = model_df.drop(["user_favorite", "volunteer_like", "volunteer_pick", "rancor", "DESCRIPTION",
    #                    "LOAN_AMOUNT", "LOAN_USE", "TAGS", "TAGS+", "TEXT", "PROCESSED_TEXT", "LOAN_ID"],
    #                   axis = 1).astype(np.uint8)
    X = X.to_numpy()

    # st.set_page_config(layout="wide")

    @st.cache()


    def recommend(user):
        """
        user : numpy array

        Takes a user interests array and finds the cosine similarity between user user_interests
        and available loans.

        Sorts cosine similarity scores by greatest to least and returns the top 5 matching loan ids
        """

        # reshape user to column vector
        user = np.reshape(user, (1, -1))

        # find cosine similarity
        rec = cosine_similarity(X, user)

        # creates an ordinal that will stand in for the dataframe index to track which scores pair with
        # which index in the dataframe
        ordinals = [i for i in range(len(rec.ravel()))]
        rec_ordinal = list(zip(rec.ravel(), ordinals))

        # sorts by cosine similarity score
        sorted_index = sorted(rec_ordinal, key = lambda x: x[0], reverse=True)

        # slice
        top_loan_ids = [(x, model_df.iloc[y][0]) for x, y in sorted_index[0:5]]

        return top_loan_ids

    st.title("Content Based Filter")
    st.write("Tell us which sector interests you the most.")

    cols = st.columns(5)
    agro_sector = cols[0].checkbox("Agriculture")
    retail_sector = cols[1].checkbox("Retail")
    it_sector = cols[2].checkbox("Computers and Technology")
    education_sector = cols[3].checkbox("Education")
    health_sanitation_sector = cols[4].checkbox("Health and Sanitation")

    cols2 = st.columns(5)
    arts_sector =  cols2[0].checkbox("Arts")
    construction_sector = cols2[1].checkbox("Construction")
    entertainment_sector = cols2[2].checkbox("Entertainment")
    health_sector = cols2[3].checkbox("Health")
    manufacturing_sector = cols2[4].checkbox("Manufacturing")

    st.write("Tell us about the projects and people you are interested in by selecting 5 or more items below.")

    cols3 = st.columns(5)
    livestock = cols3[0].checkbox("Livestock")
    water = cols3[1].checkbox("Water-Filtration")
    women_owned = cols3[2].checkbox("Women-Owned Business")
    blacksmith = cols3[3].checkbox("Blacksmith")
    rrr = cols3[4].checkbox("Repair Renew Replace")

    cols4 = st.columns(5)
    dream = cols4[0].checkbox("Dream")
    female_operated = cols4[1].checkbox("Female Operated")
    school_fees_children = cols4[2].checkbox("School Fees(Young Children)")
    single_mother = cols4[3].checkbox("Single Mother")
    well_digging = cols4[4].checkbox("Well Digging")

    cols5 = st.columns(5)
    orphan = cols5[0].checkbox("Orphan")
    medical_expenses = cols5[1].checkbox("Medical: Expenses")
    textile = cols5[2].checkbox("Textiles")
    dairy = cols5[3].checkbox("Dairy")
    expand_business = cols5[4].checkbox("Expand Business")

    cols7 = st.columns(5)
    repeat_borrower = cols7[0].checkbox("Repeat Borrower")
    family = cols7[1].checkbox("Support Families")
    sanitation = cols7[2].checkbox("Sanitation")
    c19 = cols7[3].checkbox("Covid-19 Relief")
    vegan = cols7[4].checkbox("Vegan")

    cols8 = st.columns(5)
    latin = cols8[0].checkbox("Hispanic/Latinx Owned Business")
    school_fees_adoles = cols8[1].checkbox("School Fees(Adolescent)")
    sustainable = cols8[2].checkbox("Sustainable Agriculture")
    senior = cols8[3].checkbox("Senior Person(s)")
    job_creator = cols8[4].checkbox("Job Creator")

    if st.button("Fund an entrepeneur."):
        print(agro_sector)

        # an array of zeros equal in length to numbero f columns in x to examine cosine similarity with user/user user_interests
        # and available loans
        user = np.zeros(X.shape[1])

        # Pairing column number with column name allowing for manual selection and grouping user interests
        # [print(f"{i} {j}") for i, j in enumerate(X_df.columns)]

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
        # Sector and Industry                                                                   #
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


        if agro_sector == True: # = cols[0].checkbox("Agriculture")
            user[[10, 172]] = 1

        elif retail_sector == True: # = cols[1].checkbox("Retail")
            user[[16, 19, 23 , 43, 70, 92]] = 1

        elif it_sector == True: #= cols[2].checkbox("Computers and Technology")
            user[[46, 47, 91, 183]] = 1

        elif education_sector == True: #= cols[3].checkbox("Education")
            user[[176, 132]] = 1

        elif health_sanitation_sector == True: #= cols[4].checkbox("Health and Sanitation")
            user[[179, 85]] = 1

        elif arts_sector == True: # =  cols2[0].checkbox("Arts")
            user[[14, 173, 61]] = 1

        elif construction_sector == True:# = cols2[1].checkbox("Construction")
            user[[48, 49, 175]] = 1

        elif entertainment_sector == True:#= cols2[2].checkbox("Entertainment")
            user[[80, 177, 63]] = 1

        elif health_sector == True: #= cols2[3].checkbox("Health")
            user[179, 132, 102] = 1

        elif manufacturing_sector == True: #= cols2[4].checkbox("Manufacturing")
            user[[181, 101]] = 1

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Projects and People                                                                   #
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

        elif livestock == True: #= cols3[0].checkbox("Livestock")
            user[[187, 129, 131, 20]] = 1

        elif water == True: #= cols3[1].checkbox("Water-Filtration")
            user[[240, 228]] = 1

        elif women_owned == True: #= cols3[2].checkbox("Women-Owned Business")
            user[[222]] = 1

        elif blacksmith == True: #= cols3[3].checkbox("Blacksmith")
            user[[24]] = 1

        elif rrr == True: #= cols3[4].checkbox("Repair Renew Replace")
            user[[206, 48, 49, ]] = 1

        elif dream == True: #= cols4[0].checkbox("Dream")
            user[[227]] = 1

        elif female_operated == True: #= cols4[1].checkbox("Female Operated")
            user[[0]] = 1

        elif school_fees_children == True: #= cols4[2].checkbox("School Fees(Young Children)")
            user[[223, 224, 238, 224, 208]] = 1

        elif single_mother == True: #= cols4[3].checkbox("Single Mother")
            user[[239]] = 1

        elif well_digging == True: #= cols4[4].checkbox("Well Digging")
            user[[170]] = 1

        elif orphan == True: #= cols5[0].checkbox("Orphan")
            user[[202]] = 1

        elif medical_expenses == True: #= cols5[1].checkbox("Medical: Expenses")
            user[[236]] = 1

        elif textile == True: #= cols5[2].checkbox("Textiles")
            user[[154]] = 1

        elif dairy == True: #= cols5[3].checkbox("Dairy")
            user[[53]] = 1

        elif expand_business == True: #= cols5[4].checkbox("Expand Business")
            user[[229, 230]] = 1

        elif repeat_borrower == True: #= cols7[0].checkbox("Repeat Borrower")
            user[[207]] = 1

        elif family == True: #= cols7[1].checkbox("Support Families")
            user[[239, 235, 203, 210, 211]] = 1

        elif sanitation == True: #= cols7[2].checkbox("Sanitation")
            user[[194, 237, 234]] = 1

        elif c19 == True: #= cols7[3].checkbox("Medical: Covid-19")
            user[[225]] = 1

        elif vegan == True: #= cols7[4].checkbox("Vegan")
            user[[220]] = 1

        elif latin == True: #= cols8[0].checkbox("Hispanic/Latinx Owned Business")
            user[[199]] = 1

        elif school_fees_adoles == True: #= cols8[1].checkbox("School Fees(Adolescent)")
            user[[233, 238, 208]] = 1

        elif sustainable == True: #= cols8[2].checkbox("Sustainable Agriculture")
            user[[189, 212]] = 1

        elif senior == True: #= cols8[3].checkbox("Senior Person")
            user[[190]] = 1

        elif job_creator == True: #= cols8[4].checkbox("Job Creator")
            user[[198]] = 1


        recommendations = recommend(user)

        for i in range(0, 4):
            loan_id = recommendations[i][1]
            base_url = 'https://api.kivaws.org/graphql?query='
            graphql_query = '{lend {loan (id: %s){id name gender image {id url} description use geocode{country{name}} loanAmount sector{name}}}}'   %loan_id

            r = requests.post(base_url + graphql_query)
            r = r.json()
            url = r['data']['lend']['loan']['image']['url']
            url_600 = re.sub("s100", "s600", url)

            response = requests.get(url_600)
            img = Image.open(BytesIO(response.content))
            img.resize((500,500), Image.ANTIALIAS)

            if i in [0, 1]:
                cols = st.columns(2)
                cols[i].image(img)
                cols[i].write(f'Name: {r["data"]["lend"]["loan"]["name"]}')
                cols[i].write(f'Country: {r["data"]["lend"]["loan"]["geocode"]["country"]["name"]}')
                cols[i].write(f'Sector: {r["data"]["lend"]["loan"]["sector"]["name"]}')
                cols[i].write(f'Use: {r["data"]["lend"]["loan"]["use"].capitalize()}')
                cols[i].write(f'Loan Amount: {r["data"]["lend"]["loan"]["loanAmount"]}')
                cols[i].write("Description:")
                cols[i].write(re.sub("\\r|\\n|\\t|---|<br />", "", r["data"]["lend"]["loan"]["description"])[0:1000] + "...")


            if i in [2, 3]:
                i = i - 2
                cols2 = st.columns(2)
                cols2[i].image(img)
                cols2[i].write(f'Name: {r["data"]["lend"]["loan"]["name"]}')
                cols2[i].write(f'Country: {r["data"]["lend"]["loan"]["geocode"]["country"]["name"]}')
                cols2[i].write(f'Sector: {r["data"]["lend"]["loan"]["sector"]["name"]}')
                cols2[i].write(f'Use: {r["data"]["lend"]["loan"]["use"].capitalize()}')
                cols2[i].write(f'Loan Amount: {r["data"]["lend"]["loan"]["loanAmount"]}')
                cols2[i].write("Description:")
                cols2[i].write(re.sub("\\r|\\n|\\t|---|<br />", "", r["data"]["lend"]["loan"]["description"])[0:500] + "...")


        # for i in range(5):
        #     loan_id = recommendations[i][1]
        #     base_url = 'https://api.kivaws.org/graphql?query='
        #     graphql_query = '{lend {loan (id: %s){id name gender image {id url}  }}}'   %loan_id
        #
        #     r = requests.post(base_url+ graphql_query)
        #     r = r.json()
        #     url = r['data']['lend']['loan']['image']['url']
