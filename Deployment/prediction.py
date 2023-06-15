import pandas as pd
import streamlit as st
import pickle
import json

# Load the combined pipeline
with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

# Load the list of numeric columns
with open('num_cols.json', 'r') as file:
    num_cols = json.load(file)

# Load the list of categorical columns (object type)
with open('cat_cols_object.json', 'r') as file:
    cat_cols_object = json.load(file)

# Load the list of categorical columns (number type)
with open('cat_cols_number.json', 'r') as file:
    cat_cols_number = json.load(file)

def run():
    # membuat title
    st.title('FLIGHT DELAY PREDICTION')
    st.subheader('Predicting whether a certain flight will be delayed or not')
    st.markdown('---')
    st.write("# Flight Information")
    # Buat form
    with st.form(key='form_flight_delay'):
        airline = st.selectbox('Airline code', ('9E', 'AA', 'AS', 'B6', 'CO', 'DL', 'EV', 'F9', 'FL', 'HA', 'MQ', 'OH', 'OO', 'UA', 'US', 'WN', 'XE', 'YV'))

        flight = st.number_input('Flight number', min_value=0, max_value=10000, value=120, step=1, 
                                   help='Input the flight number between 1 - 7814')
        
        airportfrom = st.selectbox('Departure airport code', ('ABE', 'ABI', 'ABQ', 'ABR', 'ABY', 'ACT', 'ACV', 'ACY', 'ADK', 'ADQ', 'AEX', 
                                                              'AGS', 'ALB', 'AMA', 'ANC', 'ASE', 'ATL', 'ATW', 'AUS', 'AVL', 'AVP', 'AZO', 
                                                              'BDL', 'BET', 'BFL', 'BGM', 'BGR', 'BHM', 'BIL', 'BIS', 'BKG', 'BLI', 'BMI', 
                                                              'BNA', 'BOI', 'BOS', 'BQK', 'BQN', 'BRO', 'BRW', 'BTM', 'BTR', 'BTV', 'BUF', 
                                                              'BUR', 'BWI', 'BZN', 'CAE', 'CAK', 'CDC', 'CDV', 'CEC', 'CHA', 'CHO', 'CHS', 
                                                              'CIC', 'CID', 'CLD', 'CLE', 'CLL', 'CLT', 'CMH', 'CMI', 'CMX', 'COD', 'COS', 
                                                              'COU', 'CPR', 'CRP', 'CRW', 'CSG', 'CVG', 'CWA', 'CYS', 'DAB', 'DAL', 'DAY', 
                                                              'DBQ', 'DCA', 'DEN', 'DFW', 'DHN', 'DLH', 'DRO', 'DSM', 'DTW', 'EAU', 'ECP', 
                                                              'EGE', 'EKO', 'ELM', 'ELP', 'ERI', 'EUG', 'EVV', 'EWN', 'EWR', 'EYW', 'FAI', 
                                                              'FAR', 'FAT', 'FAY', 'FCA', 'FLG', 'FLL', 'FLO', 'FNT', 'FSD', 'FSM', 'FWA', 
                                                              'GCC', 'GEG', 'GFK', 'GGG', 'GJT', 'GNV', 'GPT', 'GRB', 'GRK', 'GRR', 'GSO', 
                                                              'GSP', 'GTF', 'GTR', 'GUC', 'GUM', 'HDN', 'HLN', 'HNL', 'HOU', 'HPN', 'HRL', 
                                                              'HSV', 'HTS', 'IAD', 'IAH', 'ICT', 'IDA', 'ILM', 'IND', 'IPL', 'ISP', 'ITH', 
                                                              'ITO', 'IYK', 'JAC', 'JAN', 'JAX', 'JFK', 'JNU', 'KOA', 'KTN', 'LAN', 'LAS', 
                                                              'LAX', 'LBB', 'LCH', 'LEX', 'LFT', 'LGA', 'LGB', 'LIH', 'LIT', 'LMT', 'LNK', 
                                                              'LRD', 'LSE', 'LWB', 'LWS', 'LYH', 'MAF', 'MBS', 'MCI', 'MCO', 'MDT', 'MDW', 
                                                              'MEI', 'MEM', 'MFE', 'MFR', 'MGM', 'MHK', 'MHT', 'MIA', 'MKE', 'MKG', 'MLB', 
                                                              'MLI', 'MLU', 'MMH', 'MOB', 'MOD', 'MOT', 'MQT', 'MRY', 'MSN', 'MSO', 'MSP', 
                                                              'MSY', 'MTJ', 'MYR', 'OAJ', 'OAK', 'OGG', 'OKC', 'OMA', 'OME', 'ONT', 'ORD', 
                                                              'ORF', 'OTH', 'OTZ', 'PAH', 'PBI', 'PDX', 'PHF', 'PHL', 'PHX', 'PIA', 'PIE', 
                                                              'PIH', 'PIT', 'PLN', 'PNS', 'PSC', 'PSE', 'PSG', 'PSP', 'PVD', 'PWM', 'RAP', 
                                                              'RDD', 'RDM', 'RDU', 'RIC', 'RKS', 'RNO', 'ROA', 'ROC', 'ROW', 'RST', 'RSW', 
                                                              'SAF', 'SAN', 'SAT', 'SAV', 'SBA', 'SBN', 'SBP', 'SCC', 'SCE', 'SDF', 'SEA', 
                                                              'SFO', 'SGF', 'SGU', 'SHV', 'SIT', 'SJC', 'SJT', 'SJU', 'SLC', 'SMF', 'SMX', 
                                                              'SNA', 'SPI', 'SPS', 'SRQ', 'STL', 'STT', 'STX', 'SUN', 'SWF', 'SYR', 'TEX', 
                                                              'TLH', 'TOL', 'TPA', 'TRI', 'TUL', 'TUS', 'TVC', 'TWF', 'TXK', 'TYR', 'TYS', 
                                                              'UTM', 'VLD', 'VPS', 'WRG', 'XNA', 'YAK', 'YUM'), key='departure_airport')
        
        airportto = st.selectbox('Departure airport code', ('ABE', 'ABI', 'ABQ', 'ABR', 'ABY', 'ACT', 'ACV', 'ACY', 'ADK', 'ADQ', 'AEX', 
                                                              'AGS', 'ALB', 'AMA', 'ANC', 'ASE', 'ATL', 'ATW', 'AUS', 'AVL', 'AVP', 'AZO', 
                                                              'BDL', 'BET', 'BFL', 'BGM', 'BGR', 'BHM', 'BIL', 'BIS', 'BKG', 'BLI', 'BMI', 
                                                              'BNA', 'BOI', 'BOS', 'BQK', 'BQN', 'BRO', 'BRW', 'BTM', 'BTR', 'BTV', 'BUF', 
                                                              'BUR', 'BWI', 'BZN', 'CAE', 'CAK', 'CDC', 'CDV', 'CEC', 'CHA', 'CHO', 'CHS', 
                                                              'CIC', 'CID', 'CLD', 'CLE', 'CLL', 'CLT', 'CMH', 'CMI', 'CMX', 'COD', 'COS', 
                                                              'COU', 'CPR', 'CRP', 'CRW', 'CSG', 'CVG', 'CWA', 'CYS', 'DAB', 'DAL', 'DAY', 
                                                              'DBQ', 'DCA', 'DEN', 'DFW', 'DHN', 'DLH', 'DRO', 'DSM', 'DTW', 'EAU', 'ECP', 
                                                              'EGE', 'EKO', 'ELM', 'ELP', 'ERI', 'EUG', 'EVV', 'EWN', 'EWR', 'EYW', 'FAI', 
                                                              'FAR', 'FAT', 'FAY', 'FCA', 'FLG', 'FLL', 'FLO', 'FNT', 'FSD', 'FSM', 'FWA', 
                                                              'GCC', 'GEG', 'GFK', 'GGG', 'GJT', 'GNV', 'GPT', 'GRB', 'GRK', 'GRR', 'GSO', 
                                                              'GSP', 'GTF', 'GTR', 'GUC', 'GUM', 'HDN', 'HLN', 'HNL', 'HOU', 'HPN', 'HRL', 
                                                              'HSV', 'HTS', 'IAD', 'IAH', 'ICT', 'IDA', 'ILM', 'IND', 'IPL', 'ISP', 'ITH', 
                                                              'ITO', 'IYK', 'JAC', 'JAN', 'JAX', 'JFK', 'JNU', 'KOA', 'KTN', 'LAN', 'LAS', 
                                                              'LAX', 'LBB', 'LCH', 'LEX', 'LFT', 'LGA', 'LGB', 'LIH', 'LIT', 'LMT', 'LNK', 
                                                              'LRD', 'LSE', 'LWB', 'LWS', 'LYH', 'MAF', 'MBS', 'MCI', 'MCO', 'MDT', 'MDW', 
                                                              'MEI', 'MEM', 'MFE', 'MFR', 'MGM', 'MHK', 'MHT', 'MIA', 'MKE', 'MKG', 'MLB', 
                                                              'MLI', 'MLU', 'MMH', 'MOB', 'MOD', 'MOT', 'MQT', 'MRY', 'MSN', 'MSO', 'MSP', 
                                                              'MSY', 'MTJ', 'MYR', 'OAJ', 'OAK', 'OGG', 'OKC', 'OMA', 'OME', 'ONT', 'ORD', 
                                                              'ORF', 'OTH', 'OTZ', 'PAH', 'PBI', 'PDX', 'PHF', 'PHL', 'PHX', 'PIA', 'PIE', 
                                                              'PIH', 'PIT', 'PLN', 'PNS', 'PSC', 'PSE', 'PSG', 'PSP', 'PVD', 'PWM', 'RAP', 
                                                              'RDD', 'RDM', 'RDU', 'RIC', 'RKS', 'RNO', 'ROA', 'ROC', 'ROW', 'RST', 'RSW', 
                                                              'SAF', 'SAN', 'SAT', 'SAV', 'SBA', 'SBN', 'SBP', 'SCC', 'SCE', 'SDF', 'SEA', 
                                                              'SFO', 'SGF', 'SGU', 'SHV', 'SIT', 'SJC', 'SJT', 'SJU', 'SLC', 'SMF', 'SMX', 
                                                              'SNA', 'SPI', 'SPS', 'SRQ', 'STL', 'STT', 'STX', 'SUN', 'SWF', 'SYR', 'TEX', 
                                                              'TLH', 'TOL', 'TPA', 'TRI', 'TUL', 'TUS', 'TVC', 'TWF', 'TXK', 'TYR', 'TYS', 
                                                              'UTM', 'VLD', 'VPS', 'WRG', 'XNA', 'YAK', 'YUM'), key='arrival_airport')
        
        selected_day = st.selectbox('Select Day of Week', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        # Determine the numeric value based on the selected day
        selected_day_numeric = None
        if selected_day == 'Monday':
            selected_day_numeric = 1
        elif selected_day == 'Tuesday':
            selected_day_numeric = 2
        elif selected_day == 'Wednesday':
            selected_day_numeric = 3
        elif selected_day == 'Thursday':
            selected_day_numeric = 4
        elif selected_day == 'Friday':
            selected_day_numeric = 5
        elif selected_day == 'Saturday':
            selected_day_numeric = 6
        elif selected_day == 'Sunday':
            selected_day_numeric = 7

        time = st.number_input('Input time of departure in minutes from midnight', min_value=0, max_value=1439, value=10, step=1, 
                                   help='example: if time of departure is 6:00 then input 360 (360 minutes from midnight)')
        length = st.number_input('Input length of flights in minutes', min_value=0, max_value=660, value=0, step=1, 
                                   help='minimum value = 0, maximum value = 660')

        submitted = st.form_submit_button('Predict')

        # dataframe
        st.write("# Flight summary")
        data_inf = {
            'Airline': airline,
            'Flight': flight,
            'AirportFrom': airportfrom,
            'AirportTo': airportto,
            'DayOfWeek': selected_day_numeric,
            'Time': time,
            'Length': length,
        }

        data_inf = pd.DataFrame([data_inf])
        st.dataframe(data_inf.T, width=800, height=495)

    if submitted:
        # Predict using created pipeline
        y_pred_inf = pipeline.predict(data_inf)
        if y_pred_inf == 0:
            pred = 'Not Delay'
        else:
            pred = 'Delay'
        st.markdown('---')
        st.write('# Prediction : ', (pred))
        st.markdown('---')
        st.write('# Disclaimer')
        st.write('Prediction only has 64% accuracy.')

if __name__ == '__main__':
    run()