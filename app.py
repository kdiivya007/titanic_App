import streamlit as st
import pandas as pd
st.title('deploy new app')
df=pd.read_csv('titani_data.csv')
df['Embarked']=df['Embarked'].fillna('Unknown')
embarked_port=list(df['Embarked'].unique())
sex_port=list(df['Sex'].unique())


col1,col2=st.columns(2)
selected_port=col1.selectbox(label='selected_port',options=embarked_port)
selected_gender=col2.selectbox('selected_geander',options=sex_port)
df_plot=df[df['Embarked']==selected_port]
df_plot=df_plot[df_plot['Sex']==selected_gender]
