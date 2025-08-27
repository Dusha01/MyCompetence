#!/bin/bash

echo "🚀 Starting deployment..."

# Pull latest changes
echo "📥 Pulling latest changes..."
cd /var/www/myapp/MyCompetence
git pull origin main

# Backend deployment
echo "🔧 Deploying backend..."
cd backend
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart myapp-backend

# Frontend deployment
echo "🎨 Deploying frontend..."
cd ../frontend
npm install
npm run build

echo "✅ Deployment completed!"
