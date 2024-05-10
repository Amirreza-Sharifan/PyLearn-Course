# Spaceship Game

## Introduction

Spaceship Game is an engaging arcade-style game implemented in Python using the `arcade` library. In this game, players navigate a spaceship through a field of incoming enemies, dodging and shooting to survive as long as possible. The game showcases simple yet captivating mechanics with continuous challenges.

## Features

- **Dynamic Enemy Encounters:** Enemies spawn at random locations at the top of the screen and move downwards, creating a varied and unpredictable challenge for players.
- **Spaceship Controls:** Players have full control over the spaceship, capable of moving in four directions to dodge enemies and navigate the play area.
- **Fire Mechanism:** The spaceship is equipped with a bullet firing capability, allowing players to destroy incoming enemies.
- **Health and Score Tracking:** The game tracks the player's health and score, displaying them on the screen, providing a continuous update on performance and survival.

## How to Run

To play the Spaceship Game, you must have Python installed along with the `arcade` library. Here are the steps to get started:

1. **Install the Arcade Library:** If not already installed, you can install the `arcade` library using pip:
   ```pyrhon
   pip install arcade
   ```
2. **Download the Game Files:** Clone the repository or download the game files to your local machine.
3. **Run the Game:** Navigate to the game directory and run the ***Game.py*** file:

## Game Controls
Control your spaceship using the following keys:
- Move Right: → or D
- Move Left: ← or A
- Move Up: ↑ or W
- Move Down: ↓ or S
- Fire Bullets: Spacebar
## Game Files
- **Game.py:** Main game file containing the game loop and event handlers.
- **spaceship.py:** Defines the spaceship's behavior, including movement and firing bullets.
- **enemy.py:** Describes the enemy's characteristics and movement behavior.
- **bullet.py:** Contains the bullet's properties and movement logic.