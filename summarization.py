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
st.title("Annual Report Summary")

# Sidebar with collapsible section for RBI News
st.sidebar.image(add_logo(logo_path=r"C:\Users\5173707\News\PNBLogo.png", width=175, height=85)) 
#st.sidebar.markdown('#### Select Banks')

#
import streamlit as st

# Sidebar section for menu items
st.sidebar.title("Select Bank")
selected_bank = st.sidebar.radio('',['PNB', 'SBI', 'Indian Bank', 'HDFC'])
#selected_item = st.sidebar.selectbox('Select an Item', Banks[selected_category])

# Display the selected menu item
st.header(f"Bank : {selected_bank}")

summaries_df= pd.read_csv(r"C:\Users\5173707\Summarization\summaries.csv")

pnb_summary = summaries_df.loc[summaries_df['Bank'] == 'PNB', 'Summary'].values[0]
sbi_summary = summaries_df.loc[summaries_df['Bank'] == 'SBI', 'Summary'].values[0]

other='''Under Process'''

SBI='''

'''

if (selected_bank =='PNB'):
    st.write(f"{pnb_summary}")
elif(selected_bank=='SBI'):
    st.write(f"{sbi_summary}")
else:
    st.write(f"{other}")

  

# In[ ]:





# In[ ]:




