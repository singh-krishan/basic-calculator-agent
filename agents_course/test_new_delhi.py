#!/usr/bin/env python3
"""
Test script for New Delhi weather query
"""

from weather_enhanced_agent import create_weather_enhanced_agent


def test_new_delhi_weather():
    """Test the agent with New Delhi weather query."""
    
    print("🌤️ Testing New Delhi Weather with Enhanced Agent")
    print("=" * 60)
    
    # Create the agent
    agent = create_weather_enhanced_agent()
    
    # Test the New Delhi query
    query = "What's the weather in New Delhi today?"
    
    print(f"📝 Query: {query}")
    print("-" * 50)
    
    try:
        result = agent.run(query)
        print(f"✅ Result: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    print("-" * 50)
    print("🎉 Test completed!")


if __name__ == "__main__":
    test_new_delhi_weather() 