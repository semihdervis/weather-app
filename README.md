# Weather App

This simple Python script fetches current weather information for a specified city using the OpenWeatherMap API. The script retrieves the temperature and weather description in Celsius and prints the information to the console.

## Setup

1. Clone the repository to your local machine.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your OpenWeatherMap API key:

   ```env
   API_KEY=your_openweathermap_api_key
   ```

   Replace `your_openweathermap_api_key` with your actual API key.

## Usage

1. Open the `main.py` file.
2. Replace the `city` variable with the name of the city you want to get the weather for.

   ```python
   city = 'YourCityName'
   ```

3. Run the script:

   ```bash
   python main.py
   ```

## Important Note

Make sure to keep your API key confidential and do not share it publicly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.