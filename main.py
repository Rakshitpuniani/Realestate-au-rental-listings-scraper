import pandas as pd
import streamlit as st
from streamlit_tags import st_tags
import pydeck as pdk
def filters():
    st.subheader('Price Range:')
    price = st.slider(label='price', min_value=0, max_value=5000, value=(0, 5000), step=50, label_visibility='hidden')
    st.write('Price Range:', price)
    st.subheader('Bedrooms: ')
    bedroom = st.slider(label='bedroom', min_value=0, max_value=10, value=(0, 10), step=1, label_visibility='hidden')
    st.write('Bedroom Range:', bedroom)
    st.subheader('Bathrooms:')
    bathroom = st.slider(label='bathroom', min_value=0, max_value=10, value=(0, 10), step=1, label_visibility='hidden')
    st.write('Bathroom Range:', bathroom)

def select_postcode():
    postcode_data = pd.read_csv('')
    selected_postcode = []
def button(name):
    name
st.markdown("<h1 style='text-align: center; '>Real Estate AU Listings Scraper</h1>", unsafe_allow_html=True)
st.markdown("***")

option, col1, col2= st.columns (3)
with option:
    st.subheader('Choose view: ')
with col1:
    a = st.button("Map", type="primary")

with col2:
    st.button("Text", type="primary")
col3, col4 = st.columns(2)
with col3:
    filters()
if a:
    with col4:
        # st.map()
        def hex_to_rgb(h):
            h = h.lstrip('#')
            return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


        view_state = pdk.ViewState(
            latitude=-33.8688,
            longitude=151.2093,
            zoom=10
        )

        layer = pdk.Layer(
            type='PathLayer',
            pickable=True,
            get_color='color',
            width_scale=20,
            width_min_pixels=2,
            get_path='path',
            get_width=5
        )

        r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={'text': '{name}'})

        st.pydeck_chart(r)
else:
    with col4:
        keyword = st_tags(
            label='# Enter postodes:',
            text='Press enter to add more',
            value=['2000', '2110'],
            maxtags=32,
            key='2')

st.markdown('***')
col5, col6 = st.columns(2)
with col5:
    st.subheader('Download csv:')
with col6:
    st.button('Click here to Download',type="primary")










