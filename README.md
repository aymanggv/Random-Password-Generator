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

---

## Code Structure

- Collects user preferences for password generation
- Validates minimum length requirement
- Builds a character set based on user selections
- Ensures at least one character from each selected type
- Randomly selects remaining characters to reach desired length
- Shuffles the final password for additional randomness

---

## Example Output
```text
What length would you like your password to be?: 12
Should there be an uppercase letter? (y/n): y
Should there be digits? (y/n): y
Should there be a punctuation? (y/n): y
Your randomly generated password is: xD3!k9Lp@2#v
```

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.
