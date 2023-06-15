import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(
    page_title = 'FLIGHT DELAY PREDICTION' ,
    initial_sidebar_state= 'expanded',
)

def run():

    # membuat title
    st.title('FLIGHT DELAY PREDICTION')
    st.subheader('EXPLORATORY DATA ANALYSIS')
    st.markdown('---')

    # menambahkan gambar
    image = Image.open('delay.jpg')
    st.image(image)
    st.write('## Background')
    st.write('''The airline industry is a critical component of the global transportation network, 
                connecting people and goods across the world. However, flight delays and disruptions 
                continue to pose significant challenges for both airlines and passengers. Delays can 
                lead to increased costs, missed connections, decreased customer satisfaction, and 
                operational inefficiencies. As a result, airlines are constantly seeking innovative 
                solutions to predict and manage flight delays effectively.''')
    st.write('## Problem Statement')
    st.write('''Analyze the airline's comprehensive dataset and develop a predictive model to accurately 
                forecast flight delays. The goal is to create a reliable tool that can predict whether a 
                given flight will be delayed based on the scheduled departure information.''')

    # membuat garis lurus
    st.markdown('---')

    # show dataframe
    st.write('# The Dataset')
    data = pd.read_csv('h8dsft_P1M2__ali_aufa.csv')
    st.dataframe(data)

    markdown_text = '''
    ## Variable Descriptions

    | Variable     | Description                                                |
    |--------------|------------------------------------------------------------|
    | id           | The unique identifier for each flight record                |
    | Airline      | The airline associated with the flight                      |
    | Flight       | The flight number                                          |
    | AirportFrom  | The code for the departure airport                         |
    | AirportTo    | The code for the arrival airport                           |
    | DayOfWeek    | The day of the week when the flight is scheduled           |
    | Time         | The departure time measured in minutes from midnight       |
    | Length       | The duration of the flight in minutes                      |
    | Delay        | The delay status of the flight (0 = not delayed, 1 = delayed) |
    '''

    st.markdown(markdown_text)

    st.markdown('---')
    # Buat visualisasi
    st.write('# Data Visualization')
    ## Target Plot
    st.write('### Flight Delay Ratio')
    fig = plt.figure(figsize=(10,10))
    delay_count = data['Delay'].value_counts()


    plt.pie(delay_count, 
            labels=['Not Delayed', 'Delayed'], startangle=90,
            colors=['limegreen','firebrick'],
            autopct='%1.1f%%', explode=[0,0.1])
    plt.axis('equal')
    plt.title('Flight Delay Ratio')
    st.pyplot(fig)
    st.write('The data seems balanced between Delayed and not delayed. It seems that 44.5% of \
             flights from the data are delayed flights.')

    ## Categorical Data Plot
    st.write('### Categorical Data Ratio')
    pilihan_kategori = st.selectbox('Pick Categorical Column : ', ('Airline', 'AirportFrom', 'AirportTo', 'DayOfWeek'))

    fig= plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x=pilihan_kategori, hue='Delay', palette=['limegreen', 'firebrick'])

    plt.xlabel(pilihan_kategori.capitalize())
    plt.ylabel('Count')
    plt.title(pilihan_kategori.capitalize()+' Ratio')
    plt.legend(title='Delay')

    st.pyplot(fig)
    st.markdown('''
                    These airline have more delayed flights than not delayed:
                    - Continental Airlines (CO)
                    - Southwest Airlines (WN)

                    Airline with most flight is Southwest Airlines, airline with most not delayed 
                    flight is Delta Airlines (DL), and some airlines with lowest delay ratio seems 
                    to be US Airways (US), Hawaiian Airlines (HA), PSA Airlines (OH), Mesa Airlines(YV), 
                    and AirTran Airways(FL).
                ''')
    st.markdown('''
                    Most flights are from Hartsfield-Jackson Atlanta International Airport - Georgia (ATL).
                    Most destination also seems to be Hartsfield-Jackson Atlanta International Airport - Georgia. 
                    We can conclude that ATL is the busiest airport.
                ''')

    ## Numerical Data Plot
    # Select the numerical column
    pilihan_numerik = st.selectbox('Pick Numerical Column:', ('Time', 'Length'))

    # Plot the numerical data distribution
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data=data, x=pilihan_numerik, hue='Delay', kde=True, ax=ax)

    ax.set_xlabel(pilihan_numerik.capitalize())
    ax.set_ylabel('Count')
    ax.set_title(pilihan_numerik.capitalize() + ' Distribution')
    st.pyplot(fig)

if __name__ == '__main__':
    run()