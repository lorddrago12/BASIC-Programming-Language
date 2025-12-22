# 🧠 Mini BASIC Interpreter 

A small but serious **BASIC-like language prototype** written in Python. This project now includes **lexing**, **parsing**, and **AST generation**, making it a real interpreter foundation — not just a tokenizer anymore.

---

## 🚀 What This Project Is

This is a project that I'm building to understand how a programming language works and how exactly we build it.

* 🔤 **Lexer** → converts raw text into tokens
* 🌳 **Parser** → converts tokens into an AST (Abstract Syntax Tree)
* 💻 **REPL shell** → lets you test expressions interactively

It currently supports **mathematical expressions with precedence**:

```
1 + 2 * (3 - 4)
```

The output is an **AST**, not a computed result.

---

## 🧩 Project Structure

```
project/
├── basic.py     # Lexer, Parser, AST, core language logic
├── shell.py     # Interactive REPL
├── Grammer.txt  # Grammar reference
```

Each file has a clear responsibility and mirrors how real interpreters are organized.

---

## 📦 basic.py — Core Language Engine

This file contains **everything required to understand source code structure**.

---

### 🔢 Tokens & Constants

Defines:

* Valid digits
* Token types (`INT`, `FLOAT`, `PLUS`, `MUL`, etc.)

Tokens are the **atomic units** of the language.

---

### 🧾 Token Class

Represents a single token:

* `type` → what the token is
* `value` → optional (numbers)

Readable `__repr__` makes debugging painless.

---

### 🚨 Error System

Custom error classes handle invalid input:

* `IllegalCharError` triggers when unknown characters appear

This mimics real compiler-style error handling.

---

### 📍 Position Tracking

Tracks:

* Index
* Line
* Column

Used for accurate error reporting and future diagnostics.

---

### 🔤 Lexer (Tokenizer)

Reads input **character by character** and produces tokens.

Main responsibilities:

* Ignore whitespace
* Build integers and floats
* Recognize operators and parentheses
* Detect illegal characters

Key methods:

* `advance()` — moves through the text
* `make_tokens()` — main token loop
* `make_number()` — builds numeric tokens

---

### 🌳 AST Nodes

* `NumberNode` → represents numeric values
* `BinOpNode` → represents binary operations (`+ - * /`)

The AST describes **structure**, not execution.

---

### 🧠 Parser

The parser converts tokens into an AST using **recursive descent parsing**.

Grammar (from `Grammer.txt`):

```
expr   → term ((+|-) term)*
term   → factor ((*|/) factor)*
factor → INT | FLOAT | "(" expr ")"
```

This structure automatically enforces **operator precedence**.

---

### 🏁 run() Interface

```python
run(filename, text)
```

Pipeline:

1. Lex input
2. Parse tokens
3. Return AST or error

This clean interface is used by the shell and future stages.

---

## 💻 shell.py — Interactive REPL

Provides a **Read–Eval–Print Loop**:

1. Prompt user (`Basic >`)
2. Send input to `run()`
3. Print AST or error
4. Repeat

Perfect for rapid testing.

---

## 🔁 Execution Flow

```
User Input → Lexer → Tokens → Parser → AST → Output
```

No evaluation yet — this project focuses purely on **language structure**.

---

### Language Features

* 🧮 AST evaluation (interpreter)
* 🔢 Variables & assignments
* 🧾 Statements & blocks
* 🔁 Control flow (if / while)
