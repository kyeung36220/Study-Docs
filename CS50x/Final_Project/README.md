# Weather Finder
#### Video Demo:  https://youtu.be/xuyhgRV_SEI

Weather Finder is a web application that provides users with detailed weather forecasts, including current conditions, hourly forecasts, and 7-day forecasts for any location. Designed with a clean and user-friendly interface, this application allows users to check the weather for their city or any specific location using latitude and longitude coordinates.

## Features:
- **City-based Weather Search:** Users can search for weather information by entering a city name.
- **Seven-Day Forecast:** Displays a seven-day weather forecast, showing high and low temperatures, weather conditions, and icons representing each day's weather.
- **Hourly Weather Details:** Provides hourly weather information, including temperature and condition icons.
- **Dark Mode:** Offers a sleek dark theme for comfortable viewing.
- **Error Handling:** Displays user-friendly error messages if the city is not found or if the input is invalid.
- **Responsive Design:** Ensures a seamless user experience on both desktop and mobile devices.

## How it Works:
1. **User Input:** The user enters a city name into the search bar on the homepage.
2. **Geocoding API:** The application fetches the city’s coordinates and country information using the OpenCage Geocoder API.
3. **Weather API:** The application fetches weather data from the Open-Meteo API using the retrieved coordinates.
4. **Data Display:** Weather information, including current conditions, daily forecast, and hourly details, is dynamically displayed on the results page.
5. **Error Handling:** If a city is not entered, a default city is shown. For invalid cities, the user is notified via an error message.

## Requirements:
To run the Weather Finder application, you need to have the following Python libraries installed:

**Flask** - A lightweight web framework for building the application.
**Requests** - A library for sending HTTP requests to the APIs.

## Files in Project:
1. Icons Folder
    - Contains images used to visually represent various weather conditions, such as sunny, rainy, snowy, etc.
    - Enhances the user experience by making weather information more intuitive and visually appealing.
2. style.css
    - Defines the styling of the web application, including:
        - Dark mode settings.
        - Layout and spacing for a clean, user-friendly design.
        - Custom styles for cards, icons, and nackgrounds.
    - Ensures the application is responsive and visually cohesive.
3. index.html
    - Serves as the homepage of the application.
    - Contains the input field where users can search for weather information by entering a city name.
    - Includes a button to submit the user's query and navigate to the results page and a button to find user's location using latitude and longitude.
4. error.html
    - Displays user-friendly error messages in case of invalid input or issues retrieving weather data.
    - Styled to match the dark theme of the application.
5. result.html
    - Displays the weather forecast results based on the user's search.
    - Includes:
        - Current weather conditions with temperature and an appropriate weather icon.
        - A 7-day weather forecast with high and low temperatures for each day.
        - Dropdown menus for viewing detailed hourly weather information.
        - Implements dynamic content rendering using Flask and Jinja templates.
6. app.py
    - The main Python file containing the backend logic for the application.
    - Functions include:
        - Handling user input from the homepage.
        - Fetching geolocation data using the OpenCage Geocoder API.
        - Retrieving weather data from the Open-Meteo API.
        - Processing and formatting the data for display in HTML templates.
    - Implements error handling to provide fallback data or user notifications in case of issues.

## Design Choices:
One of the design choices that I made was to make the whole website dark mode. I think that it gives a more professional and sleek look while make the displays and icons easier to see. I decided against adding too much information below the Max and Min temperatures (e.g. wind speed and precipitation) because I felt that it clogged the result page and I wanted a sleeker look. Instead I opted to make an hour report drop down which makes the result page seem more informative even with it's clean design. I finally opted into making a detect location button just in case the user did not know where they were or (more realistically) was too lazy to type in their city name. Using APIs, I was able to just get the latitude and longitude of the user's PC which can enhance the effciency of people using my website, insteado f needing to type their city name everytime. I also made all the units of temperature into farenheit because that's what I use.

## About me:
I'm just a recent graduate in Marketing trying to make strides into the computer science world. I really enjoy learning new things and trying out new projects. I really hope that I can one day be part of bigger projects and bigger teams in the computer science/ programming world.
