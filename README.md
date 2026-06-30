# topTrumpsFyProject

A command-line implementation of the classic Top Trumps card game, built in Python as a foundation-year project. Players compete against a bot, comparing dinosaur stats to win cards until one side has them all.

## Features

- **Player accounts** — sign up / log in with username validation (rejects blank or numbers-only usernames) and persistent storage via a local text file database
- **Custom data structures** — a `card` class to represent each dinosaur and its stats, and a stack-based `stackOfCards` class (push, pop, peek, isEmpty, size) used to shuffle and deal the deck
- **Turn-based gameplay** — players pick a card and an attribute to battle; the round winner takes both cards; ties trigger a re-draw
- **Input validation throughout** — invalid menu choices, invalid card numbers, and invalid attribute numbers are all caught and re-prompted

## How it works

1. Ten dinosaur cards are created, each with six stats: Height, Weight, Length, Age, Killer Rating, and Intelligence
2. The deck is shuffled and pushed into a stack, then dealt alternately into the player's and bot's hands
3. Each round, the player picks a card and an attribute to compare; the bot picks a random card from its hand
4. Whoever has the higher value for that attribute wins both cards; a tie means both sides draw again
5. The game ends when one side runs out of cards

## Running it

```bash
python main.py
```

No external dependencies — just the Python standard library (`random`).

## Tech used

- Python
- Object-oriented programming (classes, encapsulation)
- Custom stack data structure
- File I/O for persistent player data

## Possible future improvements

- Smarter bot logic (currently picks a random card rather than the strongest one)
- Difficulty/level progression as players win games
- Prevent the player database file from needing to exist beforehand

