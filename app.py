import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Data Visualization App", page_icon=":bar_chart:", layout="wide")

df = pd.read_csv("india.csv")

list_of_state = list(df['State'].unique())
list_of_state.insert(0,'Overall India')

st.sidebar.title("Data Visualization App")

selected_state = st.sidebar.selectbox("Select a state", list_of_state)
primary = st.sidebar.selectbox("Select Primary Parameter",sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("Select Secondary Parameter",sorted(df.columns[5:]))

plot = st.sidebar.button("Generate Plot")

if plot:
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color=primary,size=secondary, hover_name="District",mapbox_style="open-street-map",
                                    color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=3)
        st.plotly_chart(fig)
    else:
        state_data = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_data, lat="Latitude", lon="Longitude", color=primary,size=secondary, hover_name="District",mapbox_style="open-street-map",
                                    color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=5)
        st.plotly_chart(fig)

    
    