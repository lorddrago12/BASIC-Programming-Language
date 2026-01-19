# 🧠 BASIC — My Own Mini Programming Language

This is a small programming language I built using python
It now supports variables, math, conditions, loops, functions, strings and you can run everything inside a REPL.  
I made this to learn how real languages work under the hood.

---

## 📂 Project Files
```
basic.py               → The main brain (lexer, parser, interpreter)
shell.py               → REPL where you type and run BASIC code
strings_with_arrows.py → Makes errors readable with arrows
Grammer.txt            → All the language rules written out
```

---

## ✨ What BASIC Can Do
- 🔤 Handle numbers, names, keywords and strings `"hello"`
- ➕ Math operations `+ - * / ^`
- 🔗 Comparison and logic (`==`, `<`, `>`, `AND`, `OR`, `NOT`)
- 📦 Variables using `VAR`
- 🚦 If/elif/else
- 🔁 While loops and for loops
- 🧪 Create and call your own functions like:
  ```
  FUNC add(x, y) -> x + y
  ```
- 🎯 Return values properly
- 💬 Run everything in an interactive shell

Pretty much everything you’d expect in a tiny language.

---

## 🧠 Code Examples
```
5 + 3 * 2

VAR x = 10
x = x + 1

IF x > 5 THEN "bigger" ELSE "smaller"

FOR i = 1 TO 5 THEN i

WHILE x < 20 THEN x = x + 2

FUNC square(n) -> n * n
square(6)
```

---

## ▶️ How To Run It
```
python shell.py
```
Start typing code and hit ENTER.  
Use Ctrl + C to quit.

---

## 📌 Grammar (from Grammer.txt)
```
expr   → VAR assignment or logic
comp   → comparisons
arith  → + and -
term   → * and /
factor → unary + or -
power  → ^
call   → function calls
atom   → number | string | identifier | (expr)
if     → IF / ELIF / ELSE
for    → FOR ... TO ...
while  → WHILE ...
func   → FUNC name(params) -> expression
```

---

## 💡 Why I Built This
I wanted to understand:
- how code gets read
- how tokens and syntax rules work
- how to build an AST
- how to execute expressions step by step
- and how real languages handle errors

The best way to learn it was to just build one myself.

---

## 🚀 Things I Want To Add Later
- Better `return` statements
- Lists, booleans, maybe strings with functions
- Standard library functions
- Run `.bas` files directly
- Scoping (global/local)
- Loops with break/continue
- More built-ins

---
