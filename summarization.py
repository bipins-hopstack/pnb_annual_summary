#!/usr/bin/env python
# coding: utf-8

# In[27]:


import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from PIL import Image


# In[49]:


# To get one day ago details

# current_datetime = datetime.now() - timedelta(days=1)
# formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Get current date and time
#current_datetime = datetime.now().strftime("%Y-%m-%d")


# In[50]:


def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo


# In[51]:


# Streamlit UI
st.title("Bank Report Summary")

# Sidebar with collapsible section for RBI News
#st.sidebar.image(add_logo(logo_path=r"C:\Users\5173707\News\PNBLogo.png", width=175, height=85)) 
#st.sidebar.markdown('#### Select Banks')

#
import streamlit as st
import pandas as pd

# Sidebar section for menu items
st.sidebar.title("Select Bank and Report Type")

# Define the options for banks and report types
options = [
    ('PNB', 'Annual Summary'),
    ('PNB', 'Quarterly Notes'),
    ('SBI', 'Annual Summary'),
    ('SBI', 'Quarterly Notes'),
    ('Indian Bank', 'Annual Summary'),
    ('Indian Bank', 'Quarterly Notes'),
    ('HDFC', 'Annual Summary'),
    ('HDFC', 'Quarterly Notes')
]

# Create a radio button for selecting the bank and report type
# Sidebar with collapsible section for RBI News
st.sidebar.image(add_logo(logo_path="PNBLogo.png", width=175, height=85), use_column_width=True)
selected_option = st.sidebar.radio('Select Bank and Report Type', options, format_func=lambda x: f"{x[0]} - {x[1]}")

# Load the data
a_summaries_df = pd.read_csv("https://github.com/bipins-hopstack/pnb_annual_summary/blob/main/a_summaries.csv?raw=true")
q_summaries_df = pd.read_csv("https://github.com/bipins-hopstack/pnb_annual_summary/blob/main/q_summaries.csv?raw=true")

# Extract summaries
summaries = {
    'annual': {bank: a_summaries_df.loc[a_summaries_df['Bank'] == bank, 'Summary'].values[0] for bank in a_summaries_df['Bank'].unique()},
    'quarterly': {bank: q_summaries_df.loc[q_summaries_df['Bank'] == bank, 'Summary'].values[0] for bank in q_summaries_df['Bank'].unique()}
}

# Display the selected summary
bank, report_type = selected_option
st.header(f"{bank} - {report_type}")

if report_type == 'Annual Summary':
    st.write(summaries['annual'].get(bank, 'Under Process . . .'))
elif report_type == 'Quarterly Notes':
    st.write(summaries['quarterly'].get(bank, 'Under Process . . .'))






# In[ ]:




