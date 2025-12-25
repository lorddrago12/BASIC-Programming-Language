# 🧠 Mini BASIC Interpreter 

A growing **BASIC-like programming language** written in Python. This project now goes beyond parsing — it includes a **working interpreter** that can actually **evaluate expressions**, complete with **runtime errors** and **clean error messages**.
and this is a project I'm working on to understand how programming language works and wanted to know how exactly it is made by making it my self.


---

## 🚀 What This Project Is

This project implements a **full mini language pipeline**:

* 🔤 **Lexer** — turns text into tokens
* 🌳 **Parser** — turns tokens into an AST
* 🧮 **Interpreter** — evaluates the AST
* 🚨 **Error system** — syntax + runtime errors
* 💻 **REPL shell** — interactive playground

You can now type math expressions and get **real results**, not just ASTs 👀

---

## 🧩 Project Structure

```
project/
├── basic.py               # Lexer, parser, AST, interpreter, runtime
├── shell.py               # Interactive REPL
├── Grammer.txt            # Language grammar reference
├── strings_with_arrows.py # Pretty error highlighting
```

Each file has a single responsibility, just like real language projects.

---

## 📦 basic.py — The Language Engine

This file contains **everything that makes the language work**.

---

### 🔢 Tokens & Constants

Defines all token types:

* Numbers: `INT`, `FLOAT`
* Operators: `+ - * /`
* Parentheses
* `EOF` (end of file)

Tokens are the smallest meaningful units of the language.

---

### 🧾 Token & Position Tracking

Every token stores:

* its type & value
* where it started and ended in the source code

The `Position` system tracks:

* index, line, column

This enables **pinpoint-accurate error messages**.

---

### 🚨 Error System (Compiler‑style)

Custom error classes:

* `IllegalCharError` — unknown characters
* `InvalidSyntaxError` — grammar mistakes
* `RTError` — runtime errors (like division by zero)

Errors use `strings_with_arrows.py` to visually highlight mistakes:

```
1 + * 3
    ^
```

---

### 🔤 Lexer

Reads input **character by character** and produces tokens.

Handles:

* integers & floats
* operators & parentheses
* whitespace skipping
* illegal character detection

---

### 🌳 AST Nodes

The AST represents **structure**, not text:

* `NumberNode` → numbers
* `UnaryOpNode` → `+x`, `-x`
* `BinOpNode` → `x + y`, `x * y`

---

### 🧠 Parser (Recursive Descent)

Uses recursive descent parsing based on this grammar (`Grammer.txt`):

```
expr   : term ((+|-) term)*
term   : factor ((*|/) factor)*
factor : INT | FLOAT
       | (PLUS|MINUS) factor
       | LPAREN expr RPAREN
```

This automatically enforces **operator precedence**.

---

### 🧮 Runtime Values & Context

* `Number` represents runtime numeric values
* Supports arithmetic with error checking
* `Context` tracks where execution happens

This is groundwork for future variables & scopes.

---

### ⚙️ Interpreter

The interpreter **walks the AST** using the visitor pattern:

* `visit_NumberNode`
* `visit_BinOpNode`
* `visit_UnaryOpNode`

Each visit returns an `RTResult` containing:

* a value **or**
* a runtime error

This separation keeps execution clean and safe.

---

### 🏁 run() — The Public API

```python
run(filename, text)
```

Execution pipeline:

```
Text → Lexer → Tokens → Parser → AST → Interpreter → Result / Error
```

Used by the REPL and future integrations.

---

## 💻 shell.py — Interactive REPL

A simple loop that lets you test the language:

```
Basic > 1 + 2 * 3
7
```


---

## 🎯 strings_with_arrows.py — A library which helps in error handling

Utility that prints **exact error locations** with arrows.

This dramatically improves debugging and mirrors real compilers.

---
