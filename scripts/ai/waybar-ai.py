#!/usr/bin/env python3
import os
import subprocess
import sys
import json
import requests
import textwrap  # Added for text wrapping

# Ollama local API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "deepseek-coder"  # Change to any model you have installed (e.g., "llama3", "deepseek-chat")

# Simple session file for context
SESSION_FILE = "/tmp/ollama_session.json"

def load_session():
    """Load conversation history from session file."""
    if os.path.exists(SESSION_FILE):
        try:
            with open(SESSION_FILE, 'r') as f:
                return json.load(f).get('messages', [])
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading session: {e}", file=sys.stderr)
            return []
    return []

def save_session(messages):
    """Save conversation history to session file."""
    try:
        with open(SESSION_FILE, 'w') as f:
            json.dump({'messages': messages}, f)
    except IOError as e:
        print(f"Error saving session: {e}", file=sys.stderr)

def get_user_input():
    """Get user input using wofi dmenu, centered on the screen."""
    try:
        result = subprocess.run(
            ['wofi', '--prompt', 'Ask AI:', '--dmenu', '-l', '1', '-L', 'center', '-W', '800', '-H', '100'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error getting input from wofi: {e}", file=sys.stderr)
        return ""

def show_response(response):
    """Display the AI response in a wofi popup, centered on the screen with wrapped text."""
    # Wrap the response text to fit within the wofi box (approx. 80 characters)
    wrapped_response = textwrap.fill(response, width=80)
    try:
        subprocess.run(
            ['wofi', '--prompt', 'AI Response:', '--dmenu', '-l', '10', '-L', 'center', '-W', '800', '-H', '400'],
            input=wrapped_response,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error showing response in wofi: {e}", file=sys.stderr)

def send_to_ollama(prompt, messages):
    """Send prompt to Ollama API and return response."""
    data = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result.get('response', 'No response content')
    except requests.exceptions.RequestException as e:
        return f"Connection error: {str(e)}"

def main():
    """Main function to handle user input and AI response in a chat-like loop."""
    messages = load_session()
    
    while True:
        prompt = get_user_input()
        if not prompt:
            break  # Exit if no input or user cancels

        reply = send_to_ollama(prompt, messages)

        # Update session (keep last 10 messages)
        messages.append({"role": "user", "content": prompt})
        messages.append({"role": "assistant", "content": reply})
        messages = messages[-10:]  # Keep last 10 messages
        save_session(messages)

        # Show the AI response in a wofi popup with wrapped text
        show_response(reply)

if __name__ == "__main__":
    main()
