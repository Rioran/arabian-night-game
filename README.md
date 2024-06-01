# arabian-night-game

Do you like BlackJack and writing python tests? Here is a project for ya! It is like a usual BJ but Ace is always 11 points and in most cases Dealer is a preferred winner!

HTML coverage report: https://rioran.github.io/arabian-night-game/htmlcov

### run game

Make sure that terminal faces the root directory.

```bash
python source/main.py
```

### deploy venv

```bash
python -m venv venv
```

### activate venv on WIN

```bash
venv/Scripts/activate
```

### install requirements

```bash
pip install -r requirements.txt
```

### run tests

```bash
pytest -v
```

### get coverage report

```bash
coverage run -m pytest
```
```bash
coverage html
```
```bash
git add -f htmlcov/*
```
