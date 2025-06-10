# Simple Math Agent with smolagents

This is a simple LLM agent built using the smolagents framework that can add two numbers together.

## Features

- 🤖 Simple LLM agent using smolagents framework
- 🔧 Custom tool to add two numbers
- 💬 Interactive chat interface
- 📝 Example usage demonstrations

## Prerequisites

1. **Python 3.8+** installed
2. **Ollama** installed and running locally
3. **A model** pulled in Ollama (e.g., qwen2:7b)

## Setup

### 1. Install Dependencies

Make sure you have the required packages installed:

```bash
pip install smolagents litellm
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

## Usage

### Option 1: Run the Main Agent

```bash
cd agents_course
python simple_math_agent.py
```

This will start an interactive session where you can ask the agent to add numbers.

### Option 2: Run Examples

```bash
cd agents_course
python example_usage.py
```

This will run several example queries to demonstrate the agent's capabilities.

### Option 3: Interactive Mode

```bash
cd agents_course
python example_usage.py interactive
```

This starts an interactive session with the agent.

## Example Queries

You can ask the agent questions like:

- "What is 5 + 3?"
- "Can you add 10.5 and 7.3?"
- "Calculate the sum of 100 and 200"
- "Add these numbers: 42 and 58"
- "What's 15.7 plus 8.9?"

## How It Works

### 1. The Tool

The `AddNumbersTool` class defines a simple tool that:
- Takes two numeric inputs (`a` and `b`)
- Returns their sum
- Has proper type hints and descriptions for the LLM

### 2. The Agent

The `ToolCallingAgent`:
- Uses the `LiteLLMModel` to connect to Ollama
- Has access to the addition tool
- Can understand natural language requests and call the appropriate tool

### 3. The Model

The agent uses `LiteLLMModel` to connect to Ollama, which allows it to:
- Use any model you have in Ollama
- Make API calls to your local Ollama instance
- Handle tool calling and function calling

## Customization

### Change the Model

To use a different model, modify the `model_id` in `simple_math_agent.py`:

```python
model = LiteLLMModel(
    model_id="llama3.1:8b",  # Change to your preferred model
    api_base="http://localhost:11434"
)
```

### Add More Tools

You can easily add more mathematical tools by creating additional `Tool` classes:

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
    tools=[add_tool, multiply_tool],  # Add both tools
    model=model,
    max_steps=5
)
```

## Troubleshooting

### Common Issues

1. **Connection Error**: Make sure Ollama is running and accessible at `http://localhost:11434`
2. **Model Not Found**: Make sure you have pulled the model in Ollama (`ollama pull qwen2:7b`)
3. **Import Error**: Make sure you have installed smolagents and litellm

### Debug Mode

To see more detailed output, you can increase the verbosity level:

```python
agent = ToolCallingAgent(
    tools=[add_tool],
    model=model,
    max_steps=5,
    verbosity_level=2  # Increase for more detailed output
)
```

## Files

- `simple_math_agent.py` - Main agent implementation
- `example_usage.py` - Example usage and interactive mode
- `README.md` - This documentation

## Next Steps

This is a basic example. You can extend it by:

1. Adding more mathematical operations (subtract, multiply, divide)
2. Adding more complex tools (calculator, unit conversion)
3. Implementing memory or conversation history
4. Adding web interface using Gradio
5. Deploying to Hugging Face Spaces

Happy coding! 🚀 