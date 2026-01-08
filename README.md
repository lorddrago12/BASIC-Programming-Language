# 🧠 BASIC — Mini Programming Language

A tiny custom-built programming language written in Python.  
Includes a lexer, parser, interpreter, variables, evaluation, and an interactive REPL.

---

## 📂 Project Files
```
basic.py               → Core language (lexer + parser + interpreter)
shell.py               → REPL (run + test code)
strings_with_arrows.py → Library for showing errors with arrows
Grammer.txt            → Syntax rules for the language
```

---

## ✨ Features
- 🔤 Lexical analysis (numbers, identifiers, operators, keywords)
- 🧩 Parser creates an AST from tokens
- 🧠 Interpreter executes expressions
- 📝 Variables using `VAR name = value`
- 🧮 Supports `+ - * / ^` and parentheses
- ➕ Unary ops (`-5`, `+3`)
- 🚨 Three error types:
  - Illegal Character
  - Invalid Syntax
  - Runtime Error
- 🎯 Arrow-based error highlighting
- 💬 Full REPL shell (`Basic >`)

---

## 🧠 Supported Examples
```
5 + 3
VAR x = 10
x * 2
-(3 + 5)
2^3^2
```

---

## ▶️ Running the Program
```
python shell.py
```
Type expressions and press Enter.
Use Ctrl + C to exit.

---

## 🧩 Grammar Summary (from Grammer.txt)
```
expr   → VAR assignment | math expression
term   → multiplication/division
factor → unary + or -
power  → exponent operator ^
atom   → number | identifier | (expr)
```

---

## 🎯 Why This Project?
To learn how real languages work:
- Tokenizing code
- Building grammar rules
- Parsing into structure
- Evaluating logic step by step
- Handling runtime errors



## 📝 Note
This project is **for learning and experimentation** 
