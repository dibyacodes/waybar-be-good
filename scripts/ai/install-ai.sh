#!/bV#!/bin/bash


# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo "Starting installation of dependencies for ollama_script.py on Arch Linux..."

# Update package lists
echo "Updating package lists..."
sudo pacman -Syu --noconfirm

# Install Python 3 and pip
echo "Installing Python 3 and pip..."
sudo pacman -S --noconfirm python python-pip

# Install Python requests library
echo "Installing Python requests library..."
sudo pip3 install requests

# Install wofi
echo "Installing wofi..."
sudo pacman -S --noconfirm wofi

# Install libnotify (optional, for potential notifications)
echo "Installing libnotify (optional)..."
sudo pacman -S --noconfirm libnotify

# Install Ollama
echo "Installing Ollama..."
if ! command -v ollama &> /dev/null; then
    curl -fsSL https://ollama.com/install.sh | sudo bash
else
    echo "Ollama is already installed."
fi

# Pull the deepseek-coder model
echo "Pulling deepseek-coder model for Ollama..."
ollama pull deepseek-coder

# Verify installations
echo "Verifying installations..."
if command -v python3 &> /dev/null; then
    echo -e "${GREEN}Python 3 is installed: $(python3 --version)${NC}"
else
    echo -e "${RED}Python 3 installation failed!${NC}"
    exit 1
fi

if command -v pip3 &> /dev/null; then
    echo -e "${GREEN}pip3 is installed: $(pip3 --version)${NC}"
else
    echo -e "${RED}pip3 installation failed!${NC}"
    exit 1
fi

if python3 -c "import requests" &> /dev/null; then
    echo -e "${GREEN}Python requests library is installed.${NC}"
else
    echo -e "${RED}Python requests library installation failed!${NC}"
    exit 1
fi

if command -v wofi &> /dev/null; then
    echo -e "${GREEN}wofi is installed: $(wofi --version)${NC}"
else
    echo -e "${RED}wofi installation failed!${NC}"
    exit 1
fi

if command -v ollama &> /dev/null; then
    echo -e "${GREEN}Ollama is installed: $(ollama --version)${NC}"
else
    echo -e "${RED}Ollama installation failed!${NC}"
    exit 1
fi

if ollama list | grep -q "deepseek-coder"; then
    echo -e "${GREEN}deepseek-coder model is installed.${NC}"
else
    echo -e "${RED}deepseek-coder model installation failed!${NC}"
    exit 1
fi

echo -e "${GREEN}All dependencies installed successfully!${NC}"
echo "You can now run ollama_script.py."
echo "Ensure Ollama is running with: 'ollama serve' in a terminal."
