import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("Geovisor operación Apartadó")

st.markdown(
    """
    Se encuentran desplegados los diferentes geovisores para el proyecto de actualización catastral en el municipio de Apartadó
    """
)

st.header("Apartadó")

markdown = """


"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True, center=[7.882293365998897 , -76.6249929671165],  # Coordinates for Colombia
        zoom=13,  )
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=700)
