#!/usr/bin/env python3
"""
Enhanced Agent using smolagents framework
This agent has tools to add numbers and perform web searches.
"""

import requests
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


class WebSearchTool(Tool):
    """A tool to perform web searches and get information."""
    
    name = "web_search"
    description = "Performs a web search to find information about a topic. Use this when you need to find current information, facts, or details about something."
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


def create_enhanced_agent():
    """Create and return an enhanced agent with math and web search tools."""
    
    # Create the tools
    add_tool = AddNumbersTool()
    search_tool = WebSearchTool()
    
    # Create a model (using LiteLLM to connect to Ollama)
    model = LiteLLMModel(
        model_id="ollama/qwen2:7b",  # Specify ollama provider
        api_base="http://localhost:11434"  # Ollama default endpoint
    )
    
    # Create the agent with both tools
    agent = ToolCallingAgent(
        tools=[add_tool, search_tool],
        model=model,
        max_steps=5,  # Limit steps for simple tasks
        verbosity_level=1  # Show some output
    )
    
    return agent


def main():
    """Main function to run the enhanced agent."""
    
    print("🤖 Creating Enhanced Agent...")
    agent = create_enhanced_agent()
    
    print("✅ Agent created successfully!")
    print("🔧 Available tools:")
    print("   • add_numbers (adds two numbers)")
    print("   • web_search (searches the web for information)")
    print("\n" + "="*60)
    
    # Example usage
    while True:
        try:
            user_input = input("\n💬 Ask me anything - math or web search (or type 'quit' to exit): ")
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not user_input.strip():
                continue
                
            print(f"\n🤔 Processing: {user_input}")
            print("-" * 40)
            
            # Run the agent
            result = agent.run(user_input)
            
            print("-" * 40)
            print(f"✅ Result: {result}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main() 