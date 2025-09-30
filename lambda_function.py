import json
import urllib.request
import os

def lambda_handler(event, context):
    """
    Lambda function to retrieve current temperature for mumbai city
    """
    try:
        # Use OpenWeatherMap API (free tier)
        api_key = os.environ.get('WEATHER_API_KEY', '9f215bd2e12d6e9e91993580b686774c')
        city = "Mumbai"
        country_code = "IN"
        
        # API endpoint
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}&units=metric"
        
        # Make API request
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
        
        # Extract temperature data
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        
        response_data = {
            "city": city,
            "country": country_code,
            "temperature_celsius": temperature,
            "feels_like_celsius": feels_like,
            "humidity_percent": humidity,
            "weather_description": description,
            "timestamp": data['dt']
        }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(response_data)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e),
                'message': 'Failed to retrieve temperature data'
            })
        }

