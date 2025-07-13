# Random Password Generator

A simple Python script that generates secure random passwords based on user preferences.

---

## Features

- Generates passwords with customizable length
- Allows user to specify inclusion of:
  - Uppercase letters
  - Digits
  - Special characters
- Always includes lowercase letters by default
- Ensures at least one character from each selected character type
- Validates minimum password length (minimum 4 characters)

---

## Usage

1. Run the script:
   ```bash
   python password_generator.py
   ```

2. Follow the prompts:
- Enter desired password length
- Specify whether to include uppercase letters (y/n)
- Specify whether to include digits (y/n)
- Specify whether to include special characters (y/n)

3. Your generated password will be displayed

---

## Requirements
- Python 3.x
- No external dependencies (uses built-in random and string modules)
