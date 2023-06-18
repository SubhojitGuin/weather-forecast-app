import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast fot the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days:", min_value=1, max_value=5,
                 help="Select the number of forecasted days:")
option = st.selectbox("Select data to view:", options=("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

try:
    if place:
        filtered_data = get_data(place, days)
        dates = [dic["dt_txt"] for dic in filtered_data]

        if option == "Temperature":
            temperatures = [dic['main']['temp'] * 0.1 for dic in filtered_data]
            figure = px.line(x=dates, y=temperatures,
                             labels={'x': "Date", 'y': "Temperatures(C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            conditions = [dic['weather'][0]['main'] for dic in filtered_data]
            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            image_paths = [images[condition] for condition in conditions]
            st.image(image_paths, width=115, caption=dates)

except KeyError:
    st.info("The region does not exist.")
