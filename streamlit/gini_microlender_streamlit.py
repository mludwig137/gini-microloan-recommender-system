import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#silence deprecationwarnings
st.set_option('deprecation.showPyplotGlobalUse', False)


#setting a seaborn color µ
colors = "gist_earth_r"
sns.set_palette(sns.color_palette(colors))


st.sidebar.title('Data Science for Good \n Kiva Analysis & Recommender System')



page = st.sidebar.selectbox( 'Select a page', ('Home Page', 'Visualizations', 'Content Based', 'Kiva Teams'))

if page == 'Home Page':
    st.title('A Data Science for Good Project')
    st.header('Kiva Analysis & Recommender System')

    #Kiva Introduction Video
    st.video('https://www.youtube.com/watch?v=WCraaM6PAos')


    #base64_pdf = base64.b64encode(f.read('./Project 3 - Reddit NLP Classification.pdf')).decode('utf-8')
    #pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    #st.markdown(pdf_display, unsafe_allow_html=True)


    #resource https://discuss.streamlit.io/t/how-to-link-a-button-to-a-webpage/1661
    import webbrowser
    url = 'https://github.com/mludwig137/gini-microloan-recommender-system'
    if st.button('View our Project on GitHub'):
        webbrowser.open_new_tab(url)

    st.sidebar.write('Team Members :')

    #inspired by this personal website : https://github.com/v4gadkari/vgpersonalwebsite/blob/main/streamlit_app.py
    st.sidebar.info('Terri John')
    links_terri = ['https://www.linkedin.com/in/terri-john/', 'https://github.com/tjohn07']
    cols1, cols2 = st.sidebar.columns(2)
    linkedIn_terri = cols1.button('LinkedIn', key='a')
    github_terri = cols2.button('Github', key='b')

    if linkedIn_terri == True:
        webbrowser.open_new_tab(links_terri[0])
        #st.sidebar.markdown(links_terri[0])
    if github_terri == True:
        webbrowser.open_new_tab(links_terri[1])

    st.sidebar.info('Matthew Ludwig')
    links_matthew = ['https://www.linkedin.com/in/matthewjwjludwig/', 'https://github.com/mludwig137']
    cols3, cols4 = st.sidebar.columns(2)
    linkedIn_matthew = cols3.button('LinkedIn', key='c')
    github_matthew = cols4.button('Github', key='d')

    if linkedIn_matthew == True:
        webbrowser.open_new_tab(links_matthew[0])
    if github_matthew == True:
        webbrowser.open_new_tab(links_matthew[1])

    st.sidebar.info('Brian Rubin')
    links_brian = ['https://www.linkedin.com/in/brian-f-rubin/', 'https://github.com/brianfrubin']
    cols5, cols6 = st.sidebar.columns(2)
    linkedIn = cols5.button('LinkedIn', key='e')
    github = cols6.button('Github', key='f')

    if linkedIn == True:
        webbrowser.open_new_tab(links_brian[0])
    if github == True:
        webbrowser.open_new_tab(links_brian[1])

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


        if df.empty:
            st.write('Sorry, we don\'t have enough data on that country yet. Please select another.')
        else:
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


        def loan_amount_by_sector(sector):

            plt.figure(figsize=(12, 6))
            sns.stripplot(x="ACTIVITY_NAME", y="LOAN_AMOUNT", data=df, palette="gist_earth_r")
            plt.title('Loan Amount by Activity', fontsize=16)
            plt.xlabel('Activity', fontsize=14)
            plt.ylabel('Loan Amount', fontsize=14)
            plt.xticks(rotation=20)


        def get_activities(sector):

            plt.figure(figsize=(12, 6))
            sns.histplot(df['ACTIVITY_NAME'])
            plt.xticks(rotation=20, fontsize=12)
            plt.xlabel('Count', fontsize=14)
            plt.xticks(fontsize=12)
            plt.xlabel('Activity', fontsize=14)
            plt.title(f'Activity Breakdown for {sector} Loans', fontsize=16);

        st.pyplot(get_ten_countries_sector(sector))
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
            sns.histplot(df['ACTIVITY_NAME'])
            plt.xticks(rotation=20, fontsize=12)
            plt.xlabel('Count', fontsize=14)
            plt.xticks(fontsize=12, rotation=20)
            plt.xlabel('Activity', fontsize=14)
            plt.title(f'Activity Breakdown for {sector} Loans in {sector_country}', fontsize=16);

        def loan_average_sector_country(sector, sector_country):
            # df = streamlit_df[(streamlit_df['SECTOR_NAME'] == sector) & (streamlit_df['COUNTRY_NAME'] == sector_country)]
            sns.barplot(x="ACTIVITY_NAME", y="LOAN_AMOUNT", data=df, estimator=np.mean, ci=None)
            plt.title(f'Average Loan Amount in {sector_country} Per {sector} Activity', fontsize=16)
            plt.ylabel('Average Loan Amount', fontsize=14)
            plt.xlabel('Activity Name', fontsize=14)
            plt.xticks(rotation=20)

        def loan_average_sector_gender(sector, sector_country):
            df = streamlit_df[(streamlit_df['SECTOR_NAME'] == sector) & (streamlit_df['COUNTRY_NAME'] == sector_country)]
            plt.figure(figsize=(12, 8))
            sns.violinplot(x="ACTIVITY_NAME", y="LOAN_AMOUNT", data=df, split=True)
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
            df = streamlit_df[(streamlit_df['COUNTRY_NAME'] == 'Afghanistan') | (streamlit_df['COUNTRY_NAME'] == 'Pakistan')]
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
        st.image('./images/loans_over_time.png')
        st.write('According to Kiva\'s website, field partners have the option to distribute loans before, during, or after a loan is posted on the site. 93% of loans are disbursed before they are even posted. Read more about this process on Kiva\'s site: https://www.kiva.org/about/how#faq-hkw-section')
        st.image('./images/loan_dist_pie_chart.png')
        st.write('66% of all Kiva loans go to individual women, vs. individual men(20%) and groups(13%).')
        st.image('./images/borrower_comp.png')
        st.image('./images/loans_by_sector.png')
        st.image('./images/sector_and_country.png')
        st.image('./images/loans_per_lender.png')
        st.image('./images/top_10_female.png')
        st.image('./images/low_fem_sec.png')
        st.image('./images/low_fem_sec2.png')

if page == 'Kiva Teams':
    st.title('Kiva Teams')
    st.subheader('User Based Recommender System')
    st.write('------------------------------------')

    @st.cache
    def load_rec():
        recommender = pd.read_csv('./streamlit_data/team_recommender.csv')
        recommender.set_index('LENDERS', inplace=True)
        return recommender

    recommender = load_rec()
    st.dataframe(recommender.head())
    st.write(recommender.shape)
    st.write('------------------------------------')

    user_text = st.text_input('Please enter your Kiva User ID:', value='2viljoens')
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


    team_rec(user_text)
