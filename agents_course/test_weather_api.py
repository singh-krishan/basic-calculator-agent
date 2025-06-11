#!/usr/bin/env python3
"""
Test script to demonstrate the weather API functionality
"""

from weather_enhanced_agent import create_weather_enhanced_agent


def test_weather_queries():
    """Test the agent with various weather queries."""
    
    print("🌤️ Testing Weather API with Enhanced Agent")
    print("=" * 60)
    
    # Create the agent
    agent = create_weather_enhanced_agent()
    
    # Test various queries
    test_queries = [
        "What is the weather in London today?",
        "How's the weather in New York?",
        "Tell me about the weather in Tokyo",
        "What's 15 + 25?",  # Test math functionality
        "Who is Albert Einstein?"  # Test web search
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n📝 Test {i}: {query}")
        print("-" * 50)
        
        try:
            result = agent.run(query)
            print(f"✅ Result: {result}")
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
        
        print("-" * 50)
    
    print("\n🎉 All tests completed!")


if __name__ == "__main__":
    test_weather_queries() 