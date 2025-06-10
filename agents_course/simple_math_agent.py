#!/usr/bin/env python3
"""
Simple Math Agent using smolagents framework
This agent has a tool to add two numbers provided by the user.
"""

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


def create_math_agent():
    """Create and return a simple math agent with addition tool."""
    
    # Create the addition tool
    add_tool = AddNumbersTool()
    
    # Create a model (using LiteLLM to connect to Ollama)
    # You can change the model_id to any model you have in Ollama
    model = LiteLLMModel(
        model_id="ollama/qwen2:7b",  # Specify ollama provider
        api_base="http://localhost:11434"  # Ollama default endpoint
    )
    
    # Create the agent with the tool
    agent = ToolCallingAgent(
        tools=[add_tool],
        model=model,
        max_steps=5,  # Limit steps for simple tasks
        verbosity_level=1  # Show some output
    )
    
    return agent


def main():
    """Main function to run the math agent."""
    
    print("🤖 Creating Simple Math Agent...")
    agent = create_math_agent()
    
    print("✅ Agent created successfully!")
    print("🔧 Available tool: add_numbers (adds two numbers)")
    print("\n" + "="*50)
    
    # Example usage
    while True:
        try:
            user_input = input("\n💬 Ask me to add numbers (or type 'quit' to exit): ")
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not user_input.strip():
                continue
                
            print(f"\n🤔 Processing: {user_input}")
            print("-" * 30)
            
            # Run the agent
            result = agent.run(user_input)
            
            print("-" * 30)
            print(f"✅ Result: {result}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main() 