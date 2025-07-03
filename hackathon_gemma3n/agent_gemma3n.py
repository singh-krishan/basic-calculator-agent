from smolagents import CodeAgent, tool, DuckDuckGoSearchTool, LiteLLMModel, WikipediaSearchTool
# Configure LiteLLMModel (adjust model and api_base as needed)
model = LiteLLMModel(
    model="ollama/gemma3n:latest",  # Using gemma3n model
    api_base="http://localhost:11434",  # or your API endpoint
    model_id="ollama/gemma3n:latest"  # Explicitly set model_id
)


# Define custom tools
@tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together.
    
    Args:
        a: The first number to add
        b: The second number to add
        
    Returns:
        The sum of a and b
    """
    return a + b

@tool
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together.
    
    Args:
        a: The first number to multiply
        b: The second number to multiply
        
    Returns:
        The product of a and b
    """
    return a * b

# Create the agent with the model and tools
agent = CodeAgent(
    model=model,
    tools=[
        add_numbers,
        multiply_numbers,
        DuckDuckGoSearchTool(),
        WikipediaSearchTool()
    ],
    
)

# Example usage
if __name__ == "__main__":
    # Test the agent
    response = agent.run("What is 15 + 27?")
    print("Agent response:", response)
    
    # Test with a more complex query
    response2 = agent.run("What is the current weather in New York?")
    print("Weather query response:", response2)
