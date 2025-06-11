#!/usr/bin/env python3
"""
Enhanced Agent with dedicated weather API using smolagents framework
This agent has tools to add numbers, perform web searches, and get real-time weather data.
"""

import requests
import os
from datetime import datetime
from smolagents import Tool, ToolCallingAgent, LiteLLMModel


class AddNumbersTool(Tool):
    """A simple tool to add two numbers."""
    
    name = "add_numbers"
    description = "Adds two numbers together. Takes two numeric inputs and returns their sum."
    inputs = {
        "a": {
            "type": "number",
            "description": "The first number to add"
        },
        "b": {
            "type": "number", 
            "description": "The second number to add"
        }
    }
    output_type = "number"
    
    def forward(self, a: float, b: float) -> float:
        """Add two numbers together."""
        return a + b


class WeatherTool(Tool):
    """A tool to get real-time weather information for any city."""
    
    name = "get_weather"
    description = "Gets current weather information for a specific city. Use this when someone asks about weather conditions, temperature, or weather forecasts for any location."
    inputs = {
        "city": {
            "type": "string",
            "description": "The name of the city to get weather for (e.g., 'London', 'New York', 'Tokyo')"
        }
    }
    output_type = "string"
    
    def forward(self, city: str) -> str:
        """Get current weather information for a city."""
        try:
            # Using OpenWeatherMap API (free tier)
            # You can get a free API key from: https://openweathermap.org/api
            api_key = os.getenv('OPENWEATHER_API_KEY', 'demo_key_for_testing')
            
            # If using demo key, provide sample data
            if api_key == 'demo_key_for_testing':
                return self._get_demo_weather(city)
            
            # Make API call to OpenWeatherMap
            url = "http://api.openweathermap.org/data/2.5/weather"
            params = {
                'q': city,
                'appid': api_key,
                'units': 'metric'  # Use Celsius
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract weather information
            weather_info = self._parse_weather_data(data, city)
            return weather_info
            
        except requests.RequestException as e:
            return f"Error getting weather for {city}: {str(e)}"
        except Exception as e:
            return f"Unexpected error getting weather for {city}: {str(e)}"
    
    def _parse_weather_data(self, data, city):
        """Parse weather data from OpenWeatherMap API response."""
        try:
            # Extract basic information
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            description = data['weather'][0]['description']
            wind_speed = data['wind']['speed']
            
            # Get current time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Format the response
            weather_info = f"""🌤️ Current Weather in {city} ({current_time})

🌡️ Temperature: {temp}°C (feels like {feels_like}°C)
☁️ Conditions: {description.title()}
💧 Humidity: {humidity}%
🌪️ Wind Speed: {wind_speed} m/s
📊 Pressure: {pressure} hPa"""
            
            return weather_info
            
        except KeyError as e:
            return f"Error parsing weather data for {city}: Missing field {e}"
    
    def _get_demo_weather(self, city):
        """Provide demo weather data when no API key is available."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Demo data for common cities
        demo_data = {
            'london': {'temp': 15, 'feels_like': 13, 'description': 'partly cloudy', 'humidity': 75, 'wind': 3.2},
            'new york': {'temp': 22, 'feels_like': 24, 'description': 'sunny', 'humidity': 60, 'wind': 2.1},
            'tokyo': {'temp': 18, 'feels_like': 19, 'description': 'clear sky', 'humidity': 65, 'wind': 1.8},
            'paris': {'temp': 16, 'feels_like': 15, 'description': 'light rain', 'humidity': 80, 'wind': 4.5},
            'sydney': {'temp': 25, 'feels_like': 27, 'description': 'sunny', 'humidity': 55, 'wind': 2.8}
        }
        
        city_lower = city.lower()
        if city_lower in demo_data:
            data = demo_data[city_lower]
            return f"""🌤️ Current Weather in {city.title()} ({current_time}) [DEMO DATA]

🌡️ Temperature: {data['temp']}°C (feels like {data['feels_like']}°C)
☁️ Conditions: {data['description'].title()}
💧 Humidity: {data['humidity']}%
🌪️ Wind Speed: {data['wind']} m/s
📊 Pressure: 1013 hPa

💡 Note: This is demo data. Get real-time weather by setting OPENWEATHER_API_KEY environment variable."""
        else:
            return f"""🌤️ Weather for {city} ({current_time}) [DEMO DATA]

🌡️ Temperature: 20°C (feels like 21°C)
☁️ Conditions: Partly Cloudy
💧 Humidity: 70%
🌪️ Wind Speed: 2.5 m/s
📊 Pressure: 1013 hPa

💡 Note: This is demo data. Get real-time weather by setting OPENWEATHER_API_KEY environment variable."""


class WebSearchTool(Tool):
    """A tool to perform web searches and get information."""
    
    name = "web_search"
    description = "Performs a web search to find information about a topic. Use this when you need to find current information, facts, or details about something that's not weather-related."
    inputs = {
        "query": {
            "type": "string",
            "description": "The search query to look up on the web"
        }
    }
    output_type = "string"
    
    def forward(self, query: str) -> str:
        """Perform a web search and return relevant information."""
        try:
            # Using DuckDuckGo Instant Answer API (no API key required)
            url = "https://api.duckduckgo.com/"
            params = {
                'q': query,
                'format': 'json',
                'no_html': '1',
                'skip_disambig': '1'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract relevant information
            result_parts = []
            
            # Add abstract if available
            if data.get('Abstract'):
                result_parts.append(f"Summary: {data['Abstract']}")
            
            # Add answer if available
            if data.get('Answer'):
                result_parts.append(f"Answer: {data['Answer']}")
            
            # Add related topics if available
            if data.get('RelatedTopics') and len(data['RelatedTopics']) > 0:
                topics = data['RelatedTopics'][:3]  # Limit to first 3
                topic_texts = []
                for topic in topics:
                    if isinstance(topic, dict) and topic.get('Text'):
                        topic_texts.append(topic['Text'])
                if topic_texts:
                    result_parts.append(f"Related: {'; '.join(topic_texts)}")
            
            # If no specific results, provide a general response
            if not result_parts:
                result_parts.append(f"I searched for '{query}' but couldn't find specific information. You might want to try a more specific search term.")
            
            return "\n".join(result_parts)
            
        except requests.RequestException as e:
            return f"Error performing web search: {str(e)}"
        except Exception as e:
            return f"Unexpected error during web search: {str(e)}"


def create_weather_enhanced_agent():
    """Create and return an enhanced agent with math, web search, and weather tools."""
    
    # Create the tools
    add_tool = AddNumbersTool()
    search_tool = WebSearchTool()
    weather_tool = WeatherTool()
    
    # Create a model (using LiteLLM to connect to Ollama)
    model = LiteLLMModel(
        model_id="ollama/qwen2:7b",  # Specify ollama provider
        api_base="http://localhost:11434"  # Ollama default endpoint
    )
    
    # Create the agent with all tools
    agent = ToolCallingAgent(
        tools=[add_tool, search_tool, weather_tool],
        model=model,
        max_steps=5,  # Limit steps for simple tasks
        verbosity_level=1  # Show some output
    )
    
    return agent


def main():
    """Main function to run the weather enhanced agent."""
    
    print("🤖 Creating Weather Enhanced Agent...")
    agent = create_weather_enhanced_agent()
    
    print("✅ Agent created successfully!")
    print("🔧 Available tools:")
    print("   • add_numbers (adds two numbers)")
    print("   • web_search (searches the web for information)")
    print("   • get_weather (gets real-time weather for any city)")
    print("\n" + "="*70)
    
    # Check for API key
    if os.getenv('OPENWEATHER_API_KEY') is None:
        print("💡 Tip: Set OPENWEATHER_API_KEY environment variable for real-time weather data")
        print("   Get a free API key from: https://openweathermap.org/api")
        print("   Example: export OPENWEATHER_API_KEY='your_api_key_here'")
        print("-" * 70)
    
    # Example usage
    while True:
        try:
            user_input = input("\n💬 Ask me anything - math, weather, or web search (or type 'quit' to exit): ")
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not user_input.strip():
                continue
                
            print(f"\n🤔 Processing: {user_input}")
            print("-" * 50)
            
            # Run the agent
            result = agent.run(user_input)
            
            print("-" * 50)
            print(f"✅ Result: {result}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main() 