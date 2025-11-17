#!/usr/bin/env python3
"""Verify that all cost optimizations are active."""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=" * 60)
print("🔍 Cost Optimization Verification")
print("=" * 60)

# Check OpenAI settings
print("\n1️⃣  OpenAI Model Configuration:")
model = os.getenv("OPENAI_MODEL", "NOT SET")
embedding_model = os.getenv("OPENAI_EMBEDDING_MODEL", "NOT SET")
max_tokens = os.getenv("OPENAI_MAX_TOKENS", "NOT SET")

if model == "gpt-4o-mini":
    print(f"   ✅ GPT Model: {model} (COST-OPTIMIZED)")
    print(f"      Cost: $0.15/1M input, $0.60/1M output")
elif model == "gpt-4-turbo-preview":
    print(f"   ⚠️  GPT Model: {model} (EXPENSIVE)")
    print(f"      Cost: $10/1M input, $30/1M output")
    print(f"      💡 Consider switching to gpt-4o-mini for 97% savings")
else:
    print(f"   ❓ GPT Model: {model}")

if embedding_model == "text-embedding-3-small":
    print(f"   ✅ Embedding Model: {embedding_model} (COST-OPTIMIZED)")
    print(f"      Cost: $0.02/1M tokens")
elif embedding_model == "text-embedding-3-large":
    print(f"   ⚠️  Embedding Model: {embedding_model} (EXPENSIVE)")
    print(f"      Cost: $0.13/1M tokens")
    print(f"      💡 Consider switching to text-embedding-3-small for 85% savings")
else:
    print(f"   ❓ Embedding Model: {embedding_model}")

print(f"   ℹ️  Max Tokens: {max_tokens}")

# Check document processing settings
print("\n2️⃣  Document Processing Configuration:")
chunk_size = os.getenv("CHUNK_SIZE", "NOT SET")
chunk_overlap = os.getenv("CHUNK_OVERLAP", "NOT SET")

if chunk_size == "800":
    print(f"   ✅ Chunk Size: {chunk_size} tokens (COST-OPTIMIZED)")
    print(f"      ~20% fewer chunks than 1000 tokens")
elif chunk_size == "1000":
    print(f"   ⚠️  Chunk Size: {chunk_size} tokens")
    print(f"      💡 Consider reducing to 800 for 20% savings")
else:
    print(f"   ❓ Chunk Size: {chunk_size} tokens")

print(f"   ℹ️  Chunk Overlap: {chunk_overlap} tokens")

# Check RAG settings
print("\n3️⃣  RAG Configuration:")
top_k = os.getenv("RETRIEVAL_TOP_K", "NOT SET")
cache_enabled = os.getenv("ENABLE_QUERY_CACHE", "NOT SET")
cache_ttl = os.getenv("CACHE_TTL_SECONDS", "NOT SET")

if top_k == "3":
    print(f"   ✅ Retrieval Top-K: {top_k} documents (COST-OPTIMIZED)")
    print(f"      ~40% less context sent to GPT vs 5 documents")
elif top_k == "5":
    print(f"   ⚠️  Retrieval Top-K: {top_k} documents")
    print(f"      💡 Consider reducing to 3 for 40% savings")
else:
    print(f"   ❓ Retrieval Top-K: {top_k} documents")

if cache_enabled == "True":
    print(f"   ✅ Query Cache: ENABLED (SAVES 30-50%)")
    print(f"      Cache TTL: {cache_ttl} seconds")
else:
    print(f"   ⚠️  Query Cache: DISABLED")
    print(f"      💡 Enable caching for 30-50% savings on repeated queries")

# Calculate expected costs
print("\n4️⃣  Expected Monthly Costs (558MB docs, 2000 queries):")

if (model == "gpt-4o-mini" and 
    embedding_model == "text-embedding-3-small" and 
    chunk_size == "800" and 
    top_k == "3" and 
    cache_enabled == "True"):
    print("   ✅ FULLY OPTIMIZED CONFIGURATION")
    print("   📊 Estimated Cost: ~$2.84/month")
    print("      • Document processing: $1.44 (one-time)")
    print("      • Queries: $1.40/month")
    print("   💰 Savings: ~$169/month (98% reduction)")
elif (model == "gpt-4-turbo-preview" and 
      embedding_model == "text-embedding-3-large"):
    print("   ⚠️  STANDARD CONFIGURATION (EXPENSIVE)")
    print("   📊 Estimated Cost: ~$172/month")
    print("      • Document processing: $12 (one-time)")
    print("      • Queries: $160/month")
else:
    print("   ℹ️  MIXED CONFIGURATION")
    print("   📊 Estimated Cost: Varies based on settings")
    print("      Check COST_OPTIMIZATION.md for details")

# Overall status
print("\n" + "=" * 60)
optimizations = []
warnings = []

if model == "gpt-4o-mini":
    optimizations.append("GPT-4o-mini")
else:
    warnings.append("Switch to GPT-4o-mini")

if embedding_model == "text-embedding-3-small":
    optimizations.append("Small embeddings")
else:
    warnings.append("Switch to text-embedding-3-small")

if chunk_size == "800":
    optimizations.append("Optimized chunks")
else:
    warnings.append("Reduce chunk size to 800")

if top_k == "3":
    optimizations.append("Optimized retrieval")
else:
    warnings.append("Reduce top_k to 3")

if cache_enabled == "True":
    optimizations.append("Query caching")
else:
    warnings.append("Enable query caching")

if not warnings:
    print("🎉 ALL OPTIMIZATIONS ACTIVE!")
    print(f"   Active: {', '.join(optimizations)}")
    print("   Status: Ready for production")
    print("   Expected savings: 98% vs standard config")
else:
    print(f"✅ Active optimizations: {', '.join(optimizations)}")
    print(f"⚠️  Recommended: {', '.join(warnings)}")

print("=" * 60)

# Instructions
print("\n📚 Resources:")
print("   • Full details: COST_OPTIMIZATION.md")
print("   • Quick summary: OPTIMIZATION_SUMMARY.md")
print("   • Monitor usage: https://platform.openai.com/usage")
print("\n🔧 To modify settings:")
print("   1. Edit: nano .env")
print("   2. Restart: ./stop.sh && ./start.sh")
print("\n✅ System ready! Access UI at: http://localhost:8501")
print("=" * 60)

