# Program Header
# Purpose         : This Python program interacts with a web service to obtain weather data.
# Author          : Arulsree Mozhi Thangaraj Santhakumar
# Date Created    : 02/24/2024

from urllib.parse import quote
import requests
from colorama import Fore, Style
from uszipcode import SearchEngine
import re


# Fetching the Geo API response based on user input
def get_geo_data(api_key, location, zip_code):
    try:
        country = "US"

        # if the user choice is Zip code
        if zip_code is True:
            geo_url = (f"https://api.openweathermap.org/geo/1.0/zip?"
                       f"zip={location},{country}&limit=5"
                       f"&appid={api_key}")

        # if the user choice is City and State
        else:
            city, state = map(quote, location.split(','))
            geo_url = (f"https://api.openweathermap.org/geo/1.0/direct?"
                       f"q={city},{state},{country}&limit=5"
                       f"&appid={api_key}")

        geo_response = requests.get(geo_url, timeout=5)
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data:
            raise ValueError("Unable to retrieve coordinates "
                             "from the location. \nGeo data is empty.")

        if isinstance(geo_data, list):
            geo_data = geo_data[0]

        print(f"{Fore.GREEN}\nConnection to the geo API successful."
              f"{Style.RESET_ALL}")
        return geo_data

    # error handling for Geo API call
    except requests.exceptions.HTTPError:
        print(f"{Fore.RED}HTTP Error while connecting to the geo API."
              f"{Style.RESET_ALL}")

    except requests.exceptions.ConnectionError:
        print(f"{Fore.RED}Connection Error while connecting to the geo API."
              f"{Style.RESET_ALL}")

    except requests.exceptions.Timeout:
        print(f"{Fore.RED}Timeout while connecting to the geo API."
              f"{Style.RESET_ALL}")

    except ValueError as ve:
        print(f"{Fore.RED}Error: {ve}"
              f"{Style.RESET_ALL}")

    except requests.exceptions.RequestException:
        print(f"{Fore.RED}Request Error while connecting to the geo API."
              f"{Style.RESET_ALL}")


# Fetching the Weather API response based on Latitude and Longitude
def get_weather_data(api_key, location, unit, zip_code):
    try:
        # Check if API key is not hardcoded in the main function
        if not api_key:
            raise ValueError("API key is missing. "
                             "Please provide a valid API key.")

        # fetching the lat and lon coordinates
        geo_data = get_geo_data(api_key, location, zip_code)

        if geo_data is None:
            return None

        lat, lon = geo_data['lat'], geo_data['lon']

        # Weather API call
        weather_url = (f"https://api.openweathermap.org/data/2.5/"
                       f"weather?lat={lat}&lon={lon}&units={unit}"
                       f"&appid={api_key}")

        weather_response = requests.get(weather_url, timeout=5)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        print(f"{Fore.GREEN}Connection to the weather API successful."
              f"{Style.RESET_ALL}")
        return weather_data

    # error handling for Weather API call
    except requests.exceptions.HTTPError:
        print(f"{Fore.RED}HTTP Error while connecting to the weather API."
              f"{Style.RESET_ALL}")

    except requests.exceptions.ConnectionError:
        print(f"{Fore.RED}Connection Error while connecting to "
              f"the weather API."
              f"{Style.RESET_ALL}")

    except requests.exceptions.Timeout:
        print(f"{Fore.RED}Timeout while connecting to the weather API."
              f"{Style.RESET_ALL}")

    except ValueError as ve:
        print(f"{Fore.RED}Error: {ve}"
              f"{Style.RESET_ALL}")

    except requests.exceptions.RequestException:
        print(f"{Fore.RED}Request Error while connecting to the weather API."
              f"{Style.RESET_ALL}")


# displaying the weather output
def display_weather(weather_data, unit):
    if weather_data:
        try:
            # Check for key existence before accessing them
            if ('name' in weather_data and 'sys' in weather_data
                    and 'country' in weather_data['sys']):

                print(f"\n{Fore.CYAN}\033[4m\033[1mWeather Information\033[0m"
                      f"{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Location            : "
                      f"{get_symbol('Location')} "
                      f"{weather_data['name']}, "
                      f"{weather_data['sys']['country']}"
                      f"{Style.RESET_ALL}")

                # Assigning the weather details to the variables
                current_temp = weather_data['main']['temp']
                feels_like = weather_data['main']['feels_like']
                low_temp = weather_data['main']['temp_min']
                high_temp = weather_data['main']['temp_max']

                # function call to get the temperature symbol
                unit_symbol = get_temperature_unit_symbol(unit)

                if unit_symbol is None:
                    return

                # Printing the weather information with generic symbols
                print(f"{Fore.CYAN}Current Temperature : "
                      f"{get_symbol('Current Temperature')} "
                      f"{current_temp} {unit_symbol}"
                      f"{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Feels Like          : "
                      f"{get_symbol('Feels Like')} "
                      f"{feels_like} {unit_symbol}"
                      f"{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Low Temperature     : "
                      f"{get_symbol('Low Temperature')} "
                      f"{low_temp} {unit_symbol}"
                      f"{Style.RESET_ALL}")
                print(f"{Fore.CYAN}High Temperature    : "
                      f"{get_symbol('High Temperature')} "
                      f"{high_temp} {unit_symbol}"
                      f"{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Pressure            : "
                      f"{get_symbol('Pressure')} "
                      f"{weather_data['main']['pressure']} hPa"
                      f"{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Humidity            : "
                      f"{get_symbol('Humidity')} "
                      f"{weather_data['main']['humidity']}%"
                      f"{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Cloud Cover         : "
                      f"{get_symbol('Cloud Cover')} "
                      f"{weather_data['clouds']['all']}%"
                      f"{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Wind Speed          : "
                      f"{get_symbol('Wind Speed')} "
                      f"{weather_data['wind']['speed']} m/s"
                      f"{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Visibility          : "
                      f"{get_symbol('Visibility')} "
                      f"{weather_data['visibility']} meters"
                      f"{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Description         : "
                      f"{get_symbol('Description')} "
                      f"{weather_data['weather'][0]['description']}"
                      f"{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Location information is not available."
                      f"{Style.RESET_ALL}")

        except (KeyError, TypeError) as e:
            print(f"{Fore.RED}Error while displaying the weather information."
                  f"\n{e}"
                  f"{Style.RESET_ALL}")

    else:
        print(f"{Fore.RED}Weather data is not available."
              f"{Style.RESET_ALL}")


# adding symbols for weather details
def get_symbol(info_type):
    symbols = {
        'Location': '📍',
        'Current Temperature': '🌡️',
        'Feels Like': '😊',
        'Low Temperature': '🔽',
        'High Temperature': '🔼',
        'Pressure': '⚙️',
        'Humidity': '💧',
        'Cloud Cover': '☁️',
        'Wind Speed': '🌬️',
        'Visibility': '👀',
        'Description': '🌈',
    }

    return symbols.get(info_type, '')


# Fetching the temperature unit symbol based on user input
def get_temperature_unit_symbol(unit):
    try:
        if unit == 'C':
            return '°C'
        elif unit == 'F':
            return '°F'
        elif unit == 'K':
            return 'K'
        else:
            raise ValueError("Invalid temperature unit.")
    except ValueError as ve:
        print(
            f"{Fore.RED}\nError: {ve}{Style.RESET_ALL}")
        return None


# Validate ZIP code
def validate_zipcode(zipcode):
    try:
        search = SearchEngine()
        zipcode_info = search.by_zipcode(zipcode)
        if not zipcode_info:
            raise ValueError("Invalid ZIP code. "
                             "Provided ZIP code does not exist "
                             "in the United States.")
        return True
    except ValueError as ve:
        return str(ve)


# Validate state code
def validate_state_code(state):
    valid_state_codes = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE',
                         'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS',
                         'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS',
                         'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY',
                         'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                         'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV',
                         'WI', 'WY']
    if state.upper() not in valid_state_codes:
        return ("Invalid state code. Provided state code does not "
                "exist in the United States.")
    return True


# Main function to run the weather application
def main():
    # Hard coding the API key
    api_key = "46419ecb88ab356d591a2cd3f8cfae61"
    unit = ""

    while True:
        try:
            print(f"\n{Fore.MAGENTA}\033[4m"
                  f"{Style.BRIGHT}Weather Application\033[0m"
                  f"{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}1. City/State Lookup"
                  f"{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}2. Zip Code Lookup"
                  f"{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}3. Exit"
                  f"{Style.RESET_ALL}")

            # Getting user input
            user_choice = input(f"{Fore.BLUE}\nEnter your choice (1/2/3): "
                                f"{Style.RESET_ALL}")

            if user_choice not in {'1', '2', '3'}:
                raise ValueError("Invalid choice. Please enter 1, 2, or 3.")

            if user_choice == '1':
                city_name = input(
                    f"{Fore.BLUE}Enter city name: {Style.RESET_ALL}")

                # City name should not contain numbers/special characters
                if (any(char.isdigit() for char in city_name)
                        or not all(char.isalpha() or char in (' ', '-', "'")
                                   for char in city_name)):
                    raise ValueError("Invalid city name. "
                                     "\nCity name should not contain a number "
                                     "or special characters other than a "
                                     "space, hyphen, or apostrophe.")

                state_name = input(
                    f"{Fore.BLUE}Enter state code (2 letters, "
                    f"e.g., CA for California): "
                    f"{Style.RESET_ALL}")

                # Validate the state code format
                if not (state_name.isalpha() and len(state_name) == 2):
                    raise ValueError(
                        "Invalid state code. Please enter 2 letters.")

                # Validate that entered state code exists
                result = validate_state_code(state_name)
                if result is not True:
                    raise ValueError(result)

                location = f"{city_name},{state_name.upper()}"
                zip_code = False

            elif user_choice == '2':
                zip_code_input = input(
                    f"{Fore.BLUE}Enter ZIP code: {Style.RESET_ALL}")

                # Validate ZIP code
                if not re.match(r'^\d{5}(-\d{4})?$', zip_code_input):
                    raise ValueError(
                        "Invalid ZIP code. \nPlease enter a numeric standard "
                        "ZIP code or ZIP+4 format.")

                # Strip the standard ZIP code if in ZIP+4 format
                zip_code_input = zip_code_input.split('-')[0] \
                    if '-' in zip_code_input else zip_code_input

                # Validate the entered ZIP code exists
                result = validate_zipcode(zip_code_input)
                if result is not True:
                    raise ValueError(result)

                location = zip_code_input
                zip_code = True

            else:
                print(f"{Fore.GREEN}\nExiting Weather Application. Goodbye!"
                      f"{Style.RESET_ALL}")
                break

            # Getting user choice of temperature unit
            temperature_unit = input(f"{Fore.BLUE}Choose temperature unit "
                                     f"(C - Celsius"
                                     f" or F - Fahrenheit"
                                     f" or K - Kelvin) : "
                                     f"{Style.RESET_ALL}").upper()

            if temperature_unit not in {'C', 'F', 'K'}:
                raise ValueError("Invalid temperature unit. "
                                 "Please enter C, F, or K.")

            # Assigning the temperature unit based on open weather data
            elif temperature_unit == 'C':
                unit = 'metric'

            elif temperature_unit == 'F':
                unit = 'Imperial'

            elif temperature_unit == 'K':
                unit = 'standard'

            # Get weather data and display the output
            weather_data_result = get_weather_data(api_key,
                                                   location,
                                                   unit,
                                                   zip_code)
            display_weather(weather_data_result,
                            temperature_unit)

        # exception handling for value and index error
        except ValueError as ve:
            # Handle value errors
            print(f"{Fore.RED}Error: {ve}"
                  f"{Style.RESET_ALL}")
        except IndexError as ve:
            # Handle index errors
            print(f"{Fore.RED}Error: {ve}"
                  f"{Style.RESET_ALL}")
        except Exception as e:
            # Handle unexpected errors
            print(f"{Fore.RED}Unexpected error: {e}"
                  f"{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
