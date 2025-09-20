### Waybar but Way Better (with optional AI integration)
This is a my waybar configuration to make my Arch Experience Better

<img width="1921" height="35" alt="screenshot-2025-09-19-153204" src="https://github.com/user-attachments/assets/46926852-c5bb-4190-8726-0a3648fb752a" />

To use it 

1. Make sure you have `hyprlock` installed to make use of the Lock Screen
2. Also make sure to have waybar installed

`sudo pacman -S hyprlock`
`sudo pacman -S waybar`

### Installation

Step 1 : Backup your existing waybar configuration probably located in `~/.config/waybar`

`mv ~/.config/waybar ~/.config/waybar-backup`

Step 2 : **(witout AI)** 

Clone this repo to `~/.config/waybar`

`git clone https://github.com/dibyacodes/waybar-be-good.git ~/.config/waybar`

**(with AI)**

Clone this repo to `~/.config/waybar`

`git clone https://github.com/dibyacodes/waybar-be-good.git ~/.config/waybar`

`git checkout origin/waybar/ai -- ~/.config/waybar/config`

Step 3 : Tweak the elements, in the `config` file if you want to, the designs are in the `style.css` file (obviously)

Kill existing waybar session using `pkill waybar` in your terminal & reviving it with `waybar &` to see the changes happen


### To change the AI model (tweak things in the AI version)

#### Changing the model (default is deepseek-coder)

-> Ensure you have `Ollama` installed, if not open your terminal and run

`curl -fsSL https://ollama.com/install.sh | sh`

-> After installing run

`ollama pull <your_model_name>`

For eg : ollama pull deepseek-coder

-> Now headover to the `~/.config/waybar/scripts/ai/waybar-ai.py` file (waybar-ai.py file)

You'll see a `MODEL` VARIABLE there, change it to your preferred model.

**And have fun.**

**Pro tip : Uninstall the previous model if you wanna save some space** 


If you want my Arch + Hyprland setup, [you can find it here :)](https://github.com/dibyacodes/arch-hyprland.git)

***If you happen to like this setup, consider giving this repo a start***

[Let have a chat on twitter](https://x.com/dibyacodes)
