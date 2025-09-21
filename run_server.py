#!/usr/bin/env python3
"""
Single server startup script for 404 Found Stress Management App
Connects all HTML pages, model.py, and app.py on one server
"""

import os
import sys
from app import app

def main():
    print("🚀 Starting 404 Found Stress Management Server...")
    print("📁 All HTML pages connected")
    print("🤖 ML model loaded and ready")
    print("🌐 Server running on: http://localhost:5000")
    print("\n📋 Available pages:")
    print("   • Home: http://localhost:5000/")
    print("   • Stress Test: http://localhost:5000/stress")
    print("   • Meditation: http://localhost:5000/meditation_guides")
    print("   • Music: http://localhost:5000/relaxingmusic")
    print("   • Exercises: http://localhost:5000/stress_exercises")
    print("   • Login: http://localhost:5000/login")
    print("   • Signup: http://localhost:5000/signup")
    print("\n🔧 Press Ctrl+C to stop the server")
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    main()