#!/usr/bin/env python3
"""
Test script to demonstrate the enhanced agent's web search capability
"""

from enhanced_agent import create_enhanced_agent


def test_weather_query():
    """Test the agent with a weather query."""
    
    print("🌤️ Testing Weather Search with Enhanced Agent")
    print("=" * 50)
    
    # Create the agent
    agent = create_enhanced_agent()
    
    # Test the weather query
    query = "What is the weather in London today?"
    
    print(f"📝 Query: {query}")
    print("-" * 40)
    
    try:
        result = agent.run(query)
        print(f"✅ Result: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    print("-" * 40)
    print("🎉 Test completed!")


if __name__ == "__main__":
    test_weather_query() 