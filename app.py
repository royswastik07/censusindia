import streamlit as st
import numpy as np
import pandas as pd 
import plotly_express as px

st.set_page_config(layout='wide')

df=pd.read_csv("india.csv")

list_of_states=list(df["State"].unique())
list_of_states.insert(0,"Overall India")


st.sidebar.title("India Census Data Vizualization")

selected_state= st.sidebar.selectbox("Select a State",list_of_states)
primary= st.sidebar.selectbox("Select Primary Data",sorted(df.columns[5:]))
secondary= st.sidebar.selectbox("Select secondary Data",sorted(df.columns[5:]))

plot = st.sidebar.button("Plot")

if plot:

    st.text(f'Size represent {primary}')
    st.text(f'Color represents {secondary}')

    if selected_state == "Overall India":
        # plot for india
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=3,size_max=30,
                                mapbox_style="carto-positron",width=600,height=500,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        # plot state
        state_df=df[df["State"]==selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=5,size_max=30,
                                mapbox_style="carto-positron",width=600,height=500,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    
