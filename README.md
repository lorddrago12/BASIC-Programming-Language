# 🧠 Mini BASIC Interpreter 

A small but serious **BASIC-like language prototype** written in Python. This project now implements a **full front-end pipeline** for a language: **lexing**, **parsing**, **AST generation**, and **developer‑friendly error reporting**,
and this is a project I'm working on to understand how programming language works and wanted to know how exactly it is made by making it my self.

---

## 🚀 What This Project Is

This project is the foundation of a programming language. It currently supports:

* 🔤 **Lexing** — converting raw text into tokens
* 🌳 **Parsing** — converting tokens into an AST (Abstract Syntax Tree)
* ➕ **Operator precedence** (`+ - * /`)
* ➖ **Unary operators** (`+5`, `-3`)
* 📍 **Precise syntax & character errors** with arrows
* 💻 **Interactive REPL shell** for testing

The output is an **AST**, not an evaluated result (evaluation comes later 👀).

---

## 🧩 Project Structure

```
project/
├── basic.py              # Lexer, parser, AST nodes, core logic
├── shell.py              # Interactive REPL
├── Grammer.txt           # Grammar reference (BNF-style)
├── strings_with_arrows.py# Pretty error highlighting
```

Each file has a single, clear responsibility — just like real interpreter projects.

---

## 📦 basic.py — Core Language Engine

This file contains everything related to **understanding program structure**.

---

### 🔢 Tokens & Constants

Defines token types like:

* `INT`, `FLOAT`
* `PLUS`, `MINUS`, `MUL`, `DIV`
* `LPAREN`, `RPAREN`
* `EOF`

Tokens are the **building blocks** of the language.

---

### 🧾 Token Class

Represents a single token with:

* `type` → what kind of token it is
* `value` → optional (numbers)
* `pos_start` / `pos_end` → source location

Readable `__repr__` makes debugging easy.

---

### 🚨 Error System

Custom error classes:

* `IllegalCharError` → unknown characters
* `InvalidSyntaxError` → grammar violations

Errors carry **position info**, enabling precise diagnostics.

---

### 📍 Position Tracking

The `Position` class tracks:

* Index in text
* Line number
* Column number

This allows accurate error messages and arrow highlighting.

---

### 🔤 Lexer (Tokenizer)

The lexer reads input **character by character** and produces tokens.

Responsibilities:

* Skip whitespace
* Build integers & floats
* Recognize operators and parentheses
* Detect illegal characters

Key methods:

* `advance()` — moves through the text
* `make_tokens()` — main token loop
* `make_number()` — parses numeric literals

---

### 🌳 AST Nodes

* `NumberNode` → numeric literals
* `UnaryOpNode` → unary operations (`+x`, `-x`)
* `BinOpNode` → binary operations (`x + y`, `x * y`)

The AST represents **structure**, not execution.

---

### 🧠 Parser (Recursive Descent)

The parser converts tokens into an AST using **recursive descent parsing**.

Grammar (from `Grammer.txt`):

```
expr   : term ((+|-) term)*
term   : factor ((*|/) factor)*
factor : INT | FLOAT
       | (PLUS|MINUS) factor
       | LPAREN expr RPAREN
```

This naturally enforces **operator precedence** and supports unary operators.

---

### 🏁 run() — Public Interface

```python
run(filename, text)
```

Pipeline:

```
Text → Lexer → Tokens → Parser → AST / Error
```

This clean interface is used by the shell and future interpreter stages.

---

## 💻 shell.py — Interactive REPL

A simple **Read–Eval–Print Loop**:

1. Prompt user (`Basic >`)
2. Send input to `basic.run()`
3. Print AST or error
4. Repeat forever

Perfect for quick testing while developing the language.

---

## 🎯 strings_with_arrows.py — Error Highlighting

This utility displays **exact error locations** using arrows:

```
1 + * 3
    ^
```

It makes syntax errors much easier to understand and debug — a feature real languages rely on.

---

## 🔁 Execution Flow

```
User Input
   ↓
Lexer → Tokens
   ↓
Parser → AST
   ↓
Shell Output
```

No evaluation yet — this stage focuses purely on **language structure**.

---

## 🧠 Why This Architecture Works

* Mirrors real compiler/interpreter pipelines
* Clear separation of concerns
* Easy to extend (evaluation comes next)
* Beginner-friendly but industry-aligned

This is exactly how real languages start.

---

### Parser & Errors

* Better syntax recovery
* More descriptive error messages
* Unexpected-token handling

---
