# Weather Forecast App

This is a simple web application that provides weather forecast information for the next few days. It allows users to enter a location and view the temperature and sky conditions for the specified number of forecast days.

## Features

- User-friendly interface: The app has an intuitive and user-friendly interface that makes it easy to input the desired location and forecast preferences.
- Temperature visualization: Users can view the temperature trends over the forecasted days through interactive line charts.
- Sky conditions: Users can also check the sky conditions (e.g., clear, cloudy, rainy, snowy) through corresponding icons and captions.
- Dynamic data retrieval: The app retrieves weather forecast data from the OpenWeatherMap API based on the user's location input.
- Customizable forecast length: Users can adjust the number of forecasted days from 1 to 5 to suit their needs.

## Technologies Used

- Python: The backend of the app is built using Python programming language.
- Streamlit: The web application is developed using the Streamlit framework, providing an interactive and responsive user interface.
- Plotly: The app utilizes Plotly Express library to create interactive line charts for temperature visualization.
- OpenWeatherMap API: Weather forecast data is fetched from the OpenWeatherMap API to provide up-to-date and accurate information.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/weather-forecast-app.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Obtain an API key from the OpenWeatherMap website: [https://openweathermap.org/](https://openweathermap.org/)
4. Replace the placeholder API key in `backend.py` file with your own API key.
5. Run the application: `streamlit run main.py`

## Acknowledgements

This project is inspired by the Streamlit documentation and the OpenWeatherMap API.

## License

This project is licensed under the [MIT License](LICENSE).
Please make sure to replace `your-username` in the installation instructions with your actual GitHub username. Feel free to modify the description to include any additional information or customization specific to your project.