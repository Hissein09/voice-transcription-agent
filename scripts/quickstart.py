#!/usr/bin/env python3
"""
Quick start script for the application
"""

import os
import sys
from pathlib import Path

def main():
    print("\n" + "="*70)
    print("🎤 Voice Transcription Agent - Quick Start")
    print("="*70 + "\n")
    
    # Check .env
    if not Path(".env").exists():
        print("⚠️  .env file not found")
        print("Creating from .env.example...\n")
        os.system("cp .env.example .env")
        print("✅ Created .env")
        print("   Edit .env to add your API keys (optional)\n")
    
    # Check dependencies
    print("Checking dependencies...\n")
    try:
        import pyaudio
        import numpy
        import fastapi
        print("✅ All dependencies installed\n")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Install with: pip install -r requirements.txt\n")
        sys.exit(1)
    
    # Menu
    print("="*70)
    print("Select mode:")
    print("="*70)
    print("1. Interactive (Free/Freemium with voice recording)")
    print("2. Server (API mode)")
    print("3. Run tests")
    print("4. Budget management")
    print("5. Batch transcription")
    print("0. Exit\n")
    
    choice = input("Enter your choice (0-5): ").strip()
    
    if choice == "1":
        print("\n🎤 Starting Interactive Mode...\n")
        budget = input("Monthly budget ($10): ") or "10.0"
        provider = input("Provider (auto/vosk/openai) [auto]: ") or "auto"
        
        cmd = f"python main.py --mode interactive --provider {provider} --budget {float(budget)}"
        os.system(cmd)
    
    elif choice == "2":
        print("\n🌐 Starting Server Mode...\n")
        budget = input("Monthly budget ($10): ") or "10.0"
        port = input("Port (8000): ") or "8000"
        
        cmd = f"python main.py --mode server --budget {float(budget)} --port {int(port)}"
        print(f"Server starting on http://localhost:{port}")
        print(f"API docs: http://localhost:{port}/docs\n")
        os.system(cmd)
    
    elif choice == "3":
        print("\n🧪 Running Tests...\n")
        os.system("python scripts/test_installation.py")
    
    elif choice == "4":
        print("\n💰 Budget Management\n")
        print("1. Show status")
        print("2. Show summary")
        print("3. Show history")
        print("4. Export CSV")
        print("5. Reset budget\n")
        
        sub_choice = input("Enter choice (1-5): ").strip()
        
        if sub_choice == "1":
            os.system("python scripts/manage_budget.py status")
        elif sub_choice == "2":
            os.system("python scripts/manage_budget.py summary")
        elif sub_choice == "3":
            os.system("python scripts/manage_budget.py history")
        elif sub_choice == "4":
            os.system("python scripts/manage_budget.py export")
        elif sub_choice == "5":
            os.system("python scripts/manage_budget.py reset")
    
    elif choice == "5":
        print("\n📁 Batch Transcription\n")
        input_dir = input("Input directory: ").strip()
        output_dir = input("Output directory (transcriptions): ") or "transcriptions"
        budget = input("Monthly budget ($10): ") or "10.0"
        provider = input("Provider (auto/vosk/openai) [auto]: ") or "auto"
        
        cmd = f"python scripts/batch_transcribe.py '{input_dir}' --output '{output_dir}' --provider {provider} --budget {float(budget)}"
        os.system(cmd)
    
    elif choice == "0":
        print("Goodbye! 👋\n")
        sys.exit(0)
    
    else:
        print("Invalid choice!")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye! 👋\n")
        sys.exit(0)
