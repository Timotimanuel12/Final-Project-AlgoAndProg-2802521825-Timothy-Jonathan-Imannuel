
#Blitz Battle
A straightforward, beginner-friendly fighting game created using Pygame.
This project showcases basic mechanics like character movement, attacks, health bars, and animations.

#Features:
🎮 Two-player gameplay.
🕹️ Smooth character movements and jumping.
💥 Attack mechanics with real-time health updates.
🎨 Animated sprites for Player 1.
📊 Health bars for both players.
🌆 A bamboo village background for the game area


#How to Play
#Controls:
    #Player 1:
    Move Left: A
    Move Right: D
    Jump: W
    Attack: G or T

    #Player 2:
    Move Left: Left Arrow
    Move Right: Right Arrow
    Jump: Up Arrow
    Attack: L or P

#Objective:
    Deplete your opponent's health to zero and claim victory!


#Getting Started
1. Install Python and Pygame
Ensure Python is installed on your system. Then, install Pygame by running the following in the terminal:
    bash
    Copy code
    pip install pygame

2. Clone This Repository
#Clone the project to your local machine:

    bash
    Copy code
    git clone <repository_url>
    cd Simple-Fighting-Game

3. Run the Game
#Launch the game using:

    bash
    Copy code
    python blitzbattle.py

#File Structure
    blitzbattle.py: Main game logic and window setup.
    Charactersbackup.py: Defines character movement, attack mechanics, and sprite animations.
    Assets/: Contains all images and sprites used in the game.
    Neon Background.png: The game arena background.
    Character.png and Character 2.png: Static images for characters.
    Martial Hero 2/Sprites/{action}/: Animated sprites for Player 1.

#How It Works
Character Class:
    Handles character properties like movement, attacking, and animations.

Health Bars:
    Visual representation of player health, updating dynamically based on attacks.

Animations:
    Player 1 and PLayer 2 uses a sprite animation loop for added visual appeal.

#Customizing the Game
Change Background: Replace Assets/bamboo forest (2).jpg with a new image.

Add New Animations: Add sprites to the Martial Hero 2/Sprites folder and modify the Player class.

Adjust Attack Damage: Modify the attack method in Characters.py to tweak damage values.

#Credits
Game Framework: Pygame
Sprites: Martial Hero 1 and Martial Hero 2 from luizmelo
Background: Free assets from Google and ChatGPT (AI generated image)


#License
This project is for educational purposes and is open-source. Feel free to use and modify it as you like.
