# Enhanced Math Agent with Weather API using smolagents

This is an enhanced LLM agent built using the smolagents framework that can add numbers, perform web searches, and get real-time weather data for any city.

## Features

- 🤖 Enhanced LLM agent using smolagents framework
- 🔢 Custom tool to add two numbers
- 🌤️ Dedicated weather API tool for real-time weather data
- 🌐 Web search tool for general information lookup
- 💬 Interactive chat interface
- 📝 Example usage demonstrations
- 🧪 Comprehensive test scripts

## Prerequisites

1. **Python 3.8+** installed
2. **Ollama** installed and running locally
3. **A model** pulled in Ollama (e.g., qwen2:7b)

## Setup

### 1. Install Dependencies

Make sure you have the required packages installed:

```bash
pip install -r requirements.txt
```

### 2. Start Ollama

Make sure Ollama is running and you have a model available:

```bash
# Start Ollama (if not already running)
ollama serve

# Pull a model (if you haven't already)
ollama pull qwen2:7b
```

### 3. Verify Ollama is Running

You can test if Ollama is accessible at `http://localhost:11434`

### 4. (Optional) Get Weather API Key

For real-time weather data, get a free API key from [OpenWeatherMap](https://openweathermap.org/api):

```bash
export OPENWEATHER_API_KEY='your_api_key_here'
```

## Usage

### Option 1: Run the Enhanced Weather Agent

```bash
cd agents_course
python weather_enhanced_agent.py
```

This will start an interactive session where you can ask the agent to:
- Add numbers
- Get weather information for any city
- Search the web for information

### Option 2: Run the Basic Enhanced Agent

```bash
cd agents_course
python enhanced_agent.py
```

This version includes math and web search tools.

### Option 3: Run the Original Math Agent

```bash
cd agents_course
python simple_math_agent.py
```

This is the original version with only math functionality.

### Option 4: Run Examples

```bash
cd agents_course
python example_usage.py
```

This will run several example queries to demonstrate the agent's capabilities.

### Option 5: Interactive Mode

```bash
cd agents_course
python example_usage.py interactive
```

This starts an interactive session with the agent.

## Example Queries

### Math Queries
- "What is 5 + 3?"
- "Can you add 10.5 and 7.3?"
- "Calculate the sum of 100 and 200"

### Weather Queries
- "What is the weather in London today?"
- "How's the weather in New York?"
- "Tell me about the weather in Tokyo"
- "What's the weather like in New Delhi?"

### Web Search Queries
- "Who is Albert Einstein?"
- "Tell me about artificial intelligence"
- "What is machine learning?"

## How It Works

### 1. The Tools

#### AddNumbersTool
- Takes two numeric inputs (`a` and `b`)
- Returns their sum
- Has proper type hints and descriptions for the LLM

#### WeatherTool
- Gets real-time weather information for any city
- Uses OpenWeatherMap API (with demo fallback)
- Returns comprehensive weather data: temperature, humidity, wind, pressure, conditions
- Supports both real-time data (with API key) and demo data

#### WebSearchTool
- Performs web searches using DuckDuckGo Instant Answer API
- Returns summaries, direct answers, and related topics
- No API key required

### 2. The Agent

The `ToolCallingAgent`:
- Uses the `LiteLLMModel` to connect to Ollama
- Has access to all three tools
- Can understand natural language requests and call the appropriate tool
- Intelligently selects the right tool based on the query

### 3. The Model

The agent uses `LiteLLMModel` to connect to Ollama, which allows it to:
- Use any model you have in Ollama
- Make API calls to your local Ollama instance
- Handle tool calling and function calling

## Customization

### Change the Model

To use a different model, modify the `model_id` in the agent files:

```python
model = LiteLLMModel(
    model_id="llama3.1:8b",  # Change to your preferred model
    api_base="http://localhost:11434"
)
```

### Add More Tools

You can easily add more tools by creating additional `Tool` classes:

```python
class MultiplyNumbersTool(Tool):
    name = "multiply_numbers"
    description = "Multiplies two numbers together"
    inputs = {
        "a": {"type": "number", "description": "The first number"},
        "b": {"type": "number", "description": "The second number"}
    }
    output_type = "number"
    
    def forward(self, a: float, b: float) -> float:
        return a * b
```

Then add it to the agent:

```python
agent = ToolCallingAgent(
    tools=[add_tool, search_tool, weather_tool, multiply_tool],  # Add all tools
    model=model,
    max_steps=5
)
```

## Testing

### Run All Tests

```bash
# Test weather functionality
python test_weather_api.py

# Test specific city
python test_new_delhi.py

# Test basic functionality
python test_agent.py
```

## Troubleshooting

### Common Issues

1. **Connection Error**: Make sure Ollama is running and accessible at `http://localhost:11434`
2. **Model Not Found**: Make sure you have pulled the model in Ollama (`ollama pull qwen2:7b`)
3. **Import Error**: Make sure you have installed all dependencies (`pip install -r requirements.txt`)
4. **Weather API Error**: If you get weather errors, the agent will fall back to demo data

### Debug Mode

To see more detailed output, you can increase the verbosity level:

```python
agent = ToolCallingAgent(
    tools=[add_tool, search_tool, weather_tool],
    model=model,
    max_steps=5,
    verbosity_level=2  # Increase for more detailed output
)
```

## Files

- `weather_enhanced_agent.py` - Main enhanced agent with weather API
- `enhanced_agent.py` - Enhanced agent with math and web search
- `simple_math_agent.py` - Original math agent
- `example_usage.py` - Example usage and interactive mode
- `test_weather_api.py` - Test weather functionality
- `test_new_delhi.py` - Test specific city weather
- `test_agent.py` - Test basic functionality
- `requirements.txt` - Python dependencies
- `README.md` - This documentation

## Next Steps

This is an enhanced example. You can extend it by:

1. Adding more mathematical operations (subtract, multiply, divide)
2. Adding more specialized tools (unit conversion, currency exchange)
3. Implementing memory or conversation history
4. Adding web interface using Gradio
5. Deploying to Hugging Face Spaces
6. Adding more weather features (forecasts, historical data)

## API Keys

### OpenWeatherMap API
- **Free tier**: 1,000 API calls per day
- **Get key**: [https://openweathermap.org/api](https://openweathermap.org/api)
- **Usage**: `export OPENWEATHER_API_KEY='your_api_key_here'`

### DuckDuckGo API
- **No API key required** for web search functionality
- **Rate limits**: Generous limits for personal use

Happy coding! 🚀 