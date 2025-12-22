# 🧠 Mini BASIC Interpreter (Lexer + Shell)

this is a mini BASic Interperter which i made because I'm trying to make my own language using python and i wll also add more features.


---

## 🚀 What This Project Is

This project is **not a full programming language yet**.

Right now, it is:

* A **lexer** that converts raw text into tokens
* A **REPL-style shell** to test expressions interactively
* The foundation for a future interpreter or language

If someone types:

```
1 + 2 * (3 - 4)
```

The program **does not evaluate it** — instead, it **breaks it into tokens** like:

```
[INT:1, PLUS, INT:2, MUL, LPAREN, INT:3, MINUS, INT:4, RPAREN]
```

That’s the first and most important step of building a language.

---

## 🧩 Project Structure

```
project/
├── basic.py   # Core language logic (lexer, tokens, errors)
└── shell.py   # Interactive shell (REPL)
```

Each file has a **single, clear responsibility**.

---

## 📦 basic.py — The Language Core

This file contains everything related to **turning text into tokens**.

### 1️⃣ Constants

```python
DIGITS = "0123456789"
```

Defines valid characters for number parsing.

---

### 2️⃣ Token Types

```python
TT_INT, TT_FLOAT, TT_PLUS, TT_MINUS, ...
```

Each token type represents a **meaningful unit** of the language:

* Numbers (`INT`, `FLOAT`)
* Operators (`+ - * /`)
* Parentheses (`(` and `)`)

Tokens are the *vocabulary* of the language.

---

### 3️⃣ Token Class

The `Token` class stores:

* The token type
* An optional value (for numbers)

```python
INT:5
FLOAT:3.14
PLUS
```

This makes debugging and printing tokens extremely clear.

---

### 4️⃣ Error System

Custom error classes allow **clean, readable error messages**.

* `Error` → base class
* `IllegalCharError` → triggered when an unknown character is found

Errors include:

* File name
* Line number
* Error description

This is real interpreter-style error handling.

---

### 5️⃣ Position Tracking

The `Position` class tracks:

* Index in the text
* Line number
* Column number

This allows precise error reporting later when the language grows.

---

### 6️⃣ Lexer (Tokenizer)

The **Lexer** is the heart of the project.

Its job:

* Read input **character by character**
* Group characters into numbers
* Recognize operators and parentheses
* Ignore whitespace
* Raise errors for illegal characters

Important methods:

* `advance()` → moves through the input
* `make_tokens()` → main tokenization loop
* `make_number()` → builds INT or FLOAT tokens

This follows how real languages tokenize source code.

---

### 7️⃣ run() Function

```python
def run(fn, text):
    lexer = Lexer(fn, text)
    return lexer.make_tokens()
```

This acts as a **clean public interface**:

* Input → raw text
* Output → tokens or an error

`shell.py` depends on this function.

---

## 💻 shell.py — Interactive REPL

This file creates a simple **Read–Eval–Print Loop** (REPL).

What it does:

1. Prompts the user with `Basic >`
2. Sends input to `basic.run()`
3. Prints tokens or errors
4. Repeats forever

This allows instant testing without restarting the program.

---

## 🔁 Execution Flow (Big Picture)

1. User types an expression
2. Shell sends input to the lexer
3. Lexer converts text → tokens
4. Tokens are printed OR an error is shown

No parsing. No evaluation. Just **pure lexical analysis**.

---
