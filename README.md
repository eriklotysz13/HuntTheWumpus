# Hunt The Wumpus Game

This is a simple Python version of the classic text-based game Hunt the Wumpus built as a final project for a DevOps class. The game runs in the terminal and includes basic DevOps features such as unit tests, GitHub Actions for CI and linting, a Dockerfile, and documentation.

---

## File Structure

```
HuntTheWumpus/
├── main.py                # Game logic
├── tests/
│   └── test_game.py       # Unit tests
├── Dockerfile             # For containerization
├── .flake8                # Linter config
└── .github/workflows/
    ├── tests.yml          # CI for testing
    └── lint.yml           # CI for linting
```

---

## How to Play

You are placed in a network of 20 rooms. Each room is connected to 3 others. Hazards lurk in the darkness:
- Pits (you fall to your doom)
- Bats (they carry you to a random room)
- The Wumpus (it eats you if you enter its room)

You can:
- Move to adjacent rooms
- Shoot an arrow through up to 3 connected rooms to try and kill the Wumpus

You win by killing the Wumpus. You lose if you fall into a pit, get eaten, or waste your arrow.

---

## Running the Game

### Locally with Python

```bash
python main.py
```

---

### With Docker

Build the image:

```bash
docker build -t wumpus-game .
```

Run the game:

```bash
docker run -it wumpus-game
```

---

## Features

- Terminal-based interactive gameplay
- Unit tests with `unittest`
- GitHub Actions CI for:
  - Unit testing
  - Linting with `flake8`
- Dockerized for cross-platform running
