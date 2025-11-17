#!/bin/bash
# Speed optimization configuration

# Backup current .env
cp .env .env.backup_$(date +%s)

# Update vision settings for MAXIMUM SPEED
sed -i 's/VISION_MAX_PARALLEL=3/VISION_MAX_PARALLEL=5/' .env
sed -i 's/OPENAI_VISION_MODEL=gpt-4o/OPENAI_VISION_MODEL=gpt-4o-mini/' .env
sed -i 's/OPENAI_VISION_MAX_TOKENS=2000/OPENAI_VISION_MAX_TOKENS=1000/' .env
sed -i 's/VISION_INITIAL_SCAN_DETAIL=low/VISION_INITIAL_SCAN_DETAIL=auto/' .env
sed -i 's/VISION_MIN_IMAGE_SIZE_KB=20/VISION_MIN_IMAGE_SIZE_KB=50/' .env
sed -i 's/VISION_EARLY_STOPPING=False/VISION_EARLY_STOPPING=True/' .env

echo "✅ Speed optimizations applied!"
