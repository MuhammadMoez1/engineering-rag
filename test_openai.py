#!/usr/bin/env python3
"""
Test OpenAI API connection and check credits/usage.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
import sys

# Load environment variables
load_dotenv()

def test_openai_connection():
    """Test OpenAI API connection and get usage info."""
    
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in .env file")
        return False
    
    print("🔑 OpenAI API Key found")
    print(f"   Key starts with: {api_key[:20]}...")
    print()
    
    try:
        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)
        print("✅ OpenAI client initialized successfully")
        print()
        
        # Test 1: List available models
        print("📋 Testing API connection - Fetching available models...")
        try:
            models = client.models.list()
            model_names = [model.id for model in models.data[:5]]
            print(f"✅ API is working! Found {len(models.data)} models")
            print(f"   First few models: {', '.join(model_names)}")
            print()
        except Exception as e:
            print(f"❌ Error fetching models: {e}")
            return False
        
        # Test 2: Simple API call (minimal cost)
        print("🧪 Testing GPT API with a simple query (costs ~$0.001)...")
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Using cheaper model for testing
                messages=[
                    {"role": "user", "content": "Say 'API test successful' in exactly 3 words."}
                ],
                max_tokens=10
            )
            
            answer = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            
            print(f"✅ GPT API test successful!")
            print(f"   Response: {answer}")
            print(f"   Tokens used: {tokens_used}")
            print()
            
            # Estimate cost
            # GPT-3.5-turbo pricing: ~$0.0015 per 1K tokens (input) + $0.002 per 1K tokens (output)
            estimated_cost = (tokens_used / 1000) * 0.002
            print(f"💰 Estimated cost of this test: ${estimated_cost:.6f}")
            print()
            
        except Exception as e:
            print(f"❌ Error with GPT API: {e}")
            return False
        
        # Test 3: Embeddings API (used in your RAG system)
        print("🔢 Testing Embeddings API (used for document search)...")
        try:
            embedding_response = client.embeddings.create(
                model="text-embedding-3-small",  # Smaller model for testing
                input="Test embedding"
            )
            
            embedding_dim = len(embedding_response.data[0].embedding)
            tokens_used = embedding_response.usage.total_tokens
            
            print(f"✅ Embeddings API test successful!")
            print(f"   Embedding dimension: {embedding_dim}")
            print(f"   Tokens used: {tokens_used}")
            print()
            
            # Embeddings pricing: ~$0.00002 per 1K tokens for text-embedding-3-small
            estimated_cost = (tokens_used / 1000) * 0.00002
            print(f"💰 Estimated cost of this test: ${estimated_cost:.6f}")
            print()
            
        except Exception as e:
            print(f"❌ Error with Embeddings API: {e}")
            return False
        
        print("="*60)
        print("✅ ALL TESTS PASSED!")
        print("="*60)
        print()
        print("📊 Summary:")
        print("   ✓ API key is valid")
        print("   ✓ Can access OpenAI models")
        print("   ✓ GPT API is working")
        print("   ✓ Embeddings API is working")
        print()
        print("💡 Your OpenAI API is ready for the Engineering AI Assistant!")
        print()
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def check_usage_info():
    """Provide information about checking usage and credits."""
    
    print("="*60)
    print("📈 How to Check Your OpenAI Credits & Usage")
    print("="*60)
    print()
    print("1️⃣  Check Usage on OpenAI Dashboard:")
    print("   🌐 https://platform.openai.com/usage")
    print("   - View daily usage")
    print("   - See cost breakdown by model")
    print("   - Monitor spending limits")
    print()
    
    print("2️⃣  Check Billing & Credits:")
    print("   🌐 https://platform.openai.com/settings/organization/billing/overview")
    print("   - Current balance")
    print("   - Payment methods")
    print("   - Set spending limits")
    print()
    
    print("3️⃣  Estimated Costs for Your Project:")
    print()
    print("   📄 Document Processing (one-time per document):")
    print("      • 1 MB document ≈ 1,500 chunks")
    print("      • Embedding cost: ~$0.03 per 1 MB")
    print("      • 100 MB of documents: ~$3")
    print()
    print("   💬 Query Costs (per question):")
    print("      • Simple query: $0.01 - $0.02")
    print("      • Complex query: $0.02 - $0.05")
    print("      • 100 queries/day: ~$1.50 - $3.00/day")
    print()
    print("   📊 Monthly Estimate (typical usage):")
    print("      • 200 MB documents: $6")
    print("      • 2,000 queries: $40-60")
    print("      • Total: ~$50-70/month")
    print()
    
    print("4️⃣  Tips to Reduce Costs:")
    print("   ✓ Process documents once, query many times")
    print("   ✓ Use smaller chunk sizes if appropriate")
    print("   ✓ Cache frequently asked questions")
    print("   ✓ Set spending limits in OpenAI dashboard")
    print()


if __name__ == "__main__":
    print("="*60)
    print("🧪 OpenAI API Test & Credit Check")
    print("="*60)
    print()
    
    # Run connection test
    success = test_openai_connection()
    
    # Show usage info
    check_usage_info()
    
    if success:
        print("✅ Your OpenAI API is configured correctly!")
        print()
        print("🚀 You can now use the Engineering AI Assistant")
        print("   http://localhost:8501")
        sys.exit(0)
    else:
        print("❌ There were issues with your OpenAI API")
        print()
        print("💡 Troubleshooting:")
        print("   1. Check your API key in .env file")
        print("   2. Verify you have credits: https://platform.openai.com/usage")
        print("   3. Check billing: https://platform.openai.com/settings/organization/billing")
        sys.exit(1)

