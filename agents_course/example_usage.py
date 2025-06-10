#!/usr/bin/env python3
"""
Example usage of the Simple Math Agent
This script demonstrates how to use the agent with various types of requests.
"""

from simple_math_agent import create_math_agent


def run_examples():
    """Run example queries with the math agent."""
    
    print("🚀 Starting Simple Math Agent Examples")
    print("=" * 50)
    
    # Create the agent
    agent = create_math_agent()
    
    # Example queries
    examples = [
        "What is 5 + 3?",
        "Can you add 10.5 and 7.3?",
        "Calculate the sum of 100 and 200",
        "Add these numbers: 42 and 58",
        "What's 15.7 plus 8.9?",
        "I need to add 1234 and 5678"
    ]
    
    for i, query in enumerate(examples, 1):
        print(f"\n📝 Example {i}: {query}")
        print("-" * 40)
        
        try:
            result = agent.run(query)
            print(f"✅ Answer: {result}")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print("-" * 40)
    
    print("\n🎉 All examples completed!")


def interactive_mode():
    """Run the agent in interactive mode."""
    
    print("\n🎮 Interactive Mode")
    print("=" * 30)
    print("You can now ask the agent to add any two numbers!")
    print("Examples:")
    print("- 'What is 5 + 3?'")
    print("- 'Add 10.5 and 7.3'")
    print("- 'Calculate the sum of 100 and 200'")
    print("- Type 'quit' to exit")
    
    agent = create_math_agent()
    
    while True:
        try:
            user_input = input("\n💬 Your question: ")
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not user_input.strip():
                continue
            
            print(f"🤔 Processing: {user_input}")
            result = agent.run(user_input)
            print(f"✅ Answer: {result}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        interactive_mode()
    else:
        run_examples()
        print("\n💡 To run in interactive mode, use: python example_usage.py interactive") 