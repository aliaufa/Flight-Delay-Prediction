import streamlit as st

import eda
import prediction

navigation = st.sidebar.radio('Page : ', ('EDA', 'Predict Heart Failure'))

if navigation == 'EDA':
    eda.run()
else:
    prediction.run()