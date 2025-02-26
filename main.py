import streamlit as st
import pandas as pd 
import seaborn as sns 





st.title('Data Analysis Application')
st.subheader('This is a simple data Analysis application created By Qamar !')


dataset_options = ['iris', 'titanic', 'tips', 'diamonds']
selected_dataset = st.selectbox('Select a dataset', dataset_options)

if selected_dataset == 'iris':
    df = sns.load_dataset('iris')
elif selected_dataset == 'titanic':
    df = sns.load_dataset('titanic')
elif selected_dataset == 'tips' :
    df = sns.load_dataset('tips')
elif selected_dataset == ('diamonds'):
    df = sns.load_dataset('diamonds') 


uploaded_file = st.file_uploader('upload a custom data set', type = ['csv', 'xlsx'])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file, engine='openpyxl')

st.write(df)

st.write('Number of Rows : ', df.shape[0])
st.write('Number of Columns : ', df.shape[1])


#display the column names of selected data with their types 

st.write('Column Names and Data Types: ', df.dtypes)

#print the null values

if df.isnull().sum().sum() > 0:
    st.write('Null values:', df.isnull().sum().sort_values(ascending=False))
else:
    st.write('No Null Values')


st.write('Summary Statistics:', df.describe())

st.subheader('pairplot')
hue_column = st.selectbox('Select a Columnto be used as Hue', df.columns)
fig = sns.pairplot(df, hue=hue_column)
st.pyplot(fig)