#!/usr/bin/env python3
"""
Simple test script for the math agent
"""

from simple_math_agent import create_math_agent


def test_addition():
    """Test the agent with addition requests."""
    
    print("🧪 Testing Simple Math Agent")
    print("=" * 40)
    
    # Create the agent
    agent = create_math_agent()
    
    # Test cases
    test_cases = [
        "add 2 and 3",
        "What is 2 + 3?",
        "Calculate the sum of 2 and 3",
        "Add these numbers: 2 and 3"
    ]
    
    for i, query in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {query}")
        print("-" * 30)
        
        try:
            result = agent.run(query)
            print(f"✅ Result: {result}")
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
        
        print("-" * 30)
    
    print("\n🎉 Testing completed!")


if __name__ == "__main__":
    test_addition() 