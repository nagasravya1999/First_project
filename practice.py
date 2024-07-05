import streamlit as st   # importing the streamlit
import numpy as np
import pandas as pd
import altair as alt

st.title('_streamlit _ is :blue[cool]:sunglasses::smile::rose:')

st.subheader('this is a subheader with a divider', divider='rainbow')
st.divider() # it can be a line
st.write("hello world")  # it display the inside st.write   here print() ---> st.write
st.markdown("_streamlit_:smile:")  # it genrts for style the text and moreover if u r giving the paragraph and line by line sentanceit will be print .

# using ST.BUTTON  allows the display of button widget
# by default , the app prints Good bye
# upon clicking on the button, the app displays the alternative messgae "why hello there"

st.header('st.button')
if st.button('say hello'):
    st.write('why hello the')
else:
    st.write('Good Bye')

#pandas dataframes can be  displays a table
# text, graps,,figures, plots , matplootlib , altair
#numpy uses for created numerical operations , data structres , functionalities essential for data analysis.

st. header('st.writer')
#creating data frams and table
df = pd. DataFrame({
   'first column':[1,2,3,4],
   'second column':[12,121,1234,1234]

 })
st.write(df)
#st.write('below is dataframe:' , df, 'above is a dataframe')

st.text('THIS IS SRAVYA') # it is fixed - width and performatted tet.


