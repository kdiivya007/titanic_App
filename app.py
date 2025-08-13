import streamlit as st
import pandas as pd
import plotly.express as px
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

plot=px.histogram(data_frame=df_plot,template='seaborn',color='Survived',title='Distributuin of age',facet_col='Survived',x='Age')
col1.plotly_chart(plot)

df_plot_pie=df_plot.loc[:,['PassengerId','Survived']].groupby(['Survived']).count().reset_index()
df_plot_pie.rename({'PassengerId':'count of passengers survived'},axis='columns',inplace=True)
pie_plot=px.pie(data_frame=df_plot_pie,template='seaborn',title='count of pass survided',values='count of passengers',names='Survived')
col2.plotly_chart(pie_plot)