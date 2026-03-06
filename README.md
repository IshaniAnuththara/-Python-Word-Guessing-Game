# 🐍 Python Word Guessing Game
A lightweight, terminal-based Hangman-style game built with Python.Test your vocabulary and save your attempts before they hit zero! 🎮
✨ Features
Dynamic Word Selection: Randomly picks words from a curated bank 🎲

Real-time Feedback: Tracks your progress and remaining attempts 📉

Input Validation: Handles case sensitivity and prevents invalid entries 🛠️

Custom Themes: Easily swappable word lists (Space, Tech, Tropical, and more!) 🌴

🚀 Quick Start

1. Clone the repository:
git clone https://github.com/your-username/python-word-guess.git

2. Navigate to the folder:
cd python-word-guess

3. Run the game:
python word_game.py

🕹️ How to Play

The game selects a secret word and shows you blank underscores _ _ _.

Type a single letter and press Enter.

If the letter is in the word, it fills the blanks! ✅

If the letter is wrong, you lose 1 attempt. ❌

Win by completing the word before your attempts run out! 🏆


🛠️ Customization

Want to change the words? Just edit the word_bank list in word_game.py:

# Change this to whatever you like!
word_bank = ['galaxy', 'nebula', 'planet', 'starlight']
