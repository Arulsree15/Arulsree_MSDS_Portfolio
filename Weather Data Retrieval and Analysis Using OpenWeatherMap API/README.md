# Python Weather Application

## Overview
The Python Weather Application allows users to fetch real-time weather information for locations in the United States. Users can input either a city/state combination or a ZIP code, and choose the temperature unit (Celsius, Fahrenheit, Kelvin). Weather information is displayed with symbols and formatted output for enhanced readability.

## Features
- City/State Lookup
- ZIP Code Lookup
- Temperature in Celsius, Fahrenheit, or Kelvin
- Detailed weather info: temperature, feels like, high/low, pressure, humidity, wind, visibility, cloud cover, and description
- Symbols and colors for better UX
- Input validation and error handling

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project folder:
cd weather-application

3. Install dependencies:
pip install -r requirements.txt

## Usage

Run the program:
python weather_app.py

Select the lookup method:
	1 for City/State
	2 for ZIP Code
	3 to Exit

Enter the required input and temperature unit.

Weather information will be displayed in the console.

## Dependencies

requests – HTTP requests

colorama – Colored console output

uszipcode – ZIP code validation

urllib.parse – URL encoding

re – Regular expressions

## Notes

Requires a valid OpenWeatherMap API key.

Only supports U.S. locations.

Validates inputs for city, state, and ZIP code to ensure proper API requests.

## Author

Arulsree Mozhi Thangaraj Santhakumar
Date Created: February 24, 2024