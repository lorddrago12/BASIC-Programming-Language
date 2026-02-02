# 🚀 BASIC Programming Language

A dynamically-typed, interpreted programming language built from scratch in Python. Features a complete lexer, parser, and interpreter with support for variables, functions, control flow, and more.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Status](https://img.shields.io/badge/status-educational-orange.svg)

---

## ✨ Features

### Core Language Features
- 🔢 **Data Types**: Integers, floats, strings, lists, and functions
- 📝 **Variables**: Dynamic typing with `VAR` keyword
- 🧮 **Operators**: Arithmetic (`+`, `-`, `*`, `/`, `^`), comparison (`==`, `!=`, `<`, `>`, `<=`, `>=`), logical (`AND`, `OR`, `NOT`)
- 🔁 **Control Flow**: `IF`/`ELIF`/`ELSE`, `FOR`, `WHILE` loops
- 🎯 **Functions**: First-class functions with arrow syntax support
- 📋 **Lists**: Dynamic arrays with built-in methods
- 🔄 **Loop Control**: `BREAK` and `CONTINUE` statements
- ↩️ **Return Statements**: Early returns from functions

### Built-in Functions
- **I/O**: `PRINT()`, `PRINT_RET()`, `INPUT()`, `INPUT_INT()`
- **Type Checking**: `IS_NUMBER()`, `IS_STRING()`, `IS_LIST()`, `IS_FUNCTION()`
- **List Operations**: `APPEND()`, `POP()`, `EXTEND()`, `LEN()`
- **Utilities**: `CLEAR()` (clear console)

### Developer Experience
- 🎯 Detailed error messages with arrow-based highlighting
- 💬 Interactive REPL shell
- 📍 Full position tracking for debugging
- 🔍 Traceback support for runtime errors

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/lorddrago12/BASIC-Programming-Language.git
cd BASIC-Programming-Language

# Run the REPL
python shell.py
```

### Your First Program

```
Basic > PRINT("Hello, World!")
Hello, World!
0

Basic > VAR x = 10
10

Basic > VAR y = x * 2 + 5
25

Basic > PRINT(y)
25
0
```

### Run Example Programs

Check out `example.basic` for comprehensive examples:

```bash
python shell.py < example.basic
```

---

## 📖 Language Guide

### Variables

```python
VAR name = "Alice"
VAR age = 25
VAR pi = 3.14159
```

### Arithmetic

```python
5 + 3          # 8
10 - 4         # 6
3 * 7          # 21
15 / 3         # 5
2 ^ 8          # 256 (exponentiation)
-(5 + 3)       # -8 (unary minus)
```

### Comparison & Logic

```python
5 == 5         # 1 (true)
10 != 5        # 1 (true)
3 < 7          # 1 (true)
10 >= 10       # 1 (true)

1 AND 1        # 1 (true)
1 OR 0         # 1 (true)
NOT 0          # 1 (true)
```

### Strings

```python
VAR greeting = "Hello"
VAR name = "World"
PRINT(greeting + " " + name)  # Hello World

VAR message = "Basic" * 3     # BasicBasicBasic
```

### Lists

```python
VAR numbers = [1, 2, 3, 4, 5]
VAR mixed = [1, "hello", 3.14, [1, 2]]

# List operations
APPEND(numbers, 6)         # [1, 2, 3, 4, 5, 6]
POP(numbers, 0)            # Removes first element
EXTEND(numbers, [7, 8])    # [2, 3, 4, 5, 6, 7, 8]

# Access elements
numbers/0                  # 2 (first element after pop)
LEN(numbers)               # Get list length
```

### Conditionals

#### Single-line if

```python
IF 5 > 3 THEN PRINT("5 is greater")
```

#### Multi-line if-elif-else

```python
VAR score = 85

IF score >= 90 THEN
    PRINT("Grade: A")
ELIF score >= 80 THEN
    PRINT("Grade: B")
ELIF score >= 70 THEN
    PRINT("Grade: C")
ELSE
    PRINT("Grade: F")
END
```

### Loops

#### For Loop

```python
# Basic for loop
FOR i = 0 TO 5 THEN
    PRINT(i)
END

# With step
FOR i = 0 TO 10 STEP 2 THEN
    PRINT(i)
END

# Countdown
FOR i = 10 TO 0 STEP -1 THEN
    PRINT(i)
END
```

#### While Loop

```python
VAR count = 0
WHILE count < 5 THEN
    PRINT(count)
    VAR count = count + 1
END
```

#### Loop Control

```python
FOR i = 0 TO 10 THEN
    IF i == 3 THEN CONTINUE    # Skip 3
    IF i == 7 THEN BREAK        # Stop at 7
    PRINT(i)
END
```

### Functions

#### Basic Function

```python
FUNC greet(name) -> PRINT("Hello, " + name)
greet("Alice")  # Hello, Alice
```

#### Multi-line Function

```python
FUNC factorial(n)
    IF n <= 1 THEN RETURN 1
    RETURN n * factorial(n - 1)
END

PRINT(factorial(5))  # 120
```

#### Anonymous Functions

```python
VAR square = FUNC(x) -> x * x
PRINT(square(5))  # 25

VAR add = FUNC(a, b) -> a + b
PRINT(add(3, 7))  # 10
```

---

## 🏗️ Architecture

### Project Structure

```
basic-lang/
├── basic.py                    # Core language implementation
│   ├── Lexer                   # Tokenization
│   ├── Parser                  # AST generation
│   ├── Interpreter             # Execution engine
│   └── Built-in Functions      # Standard library
├── shell.py                    # REPL interface
├── strings_with_arrows.py      # Error visualization
├── Grammar.txt                 # Language grammar specification
└── example.basic               # Example programs
```

### Implementation Details

#### Lexer
Converts source code into tokens:
```
"VAR x = 5 + 3" → [KEYWORD:VAR, IDENTIFIER:x, EQ, INT:5, PLUS, INT:3]
```

#### Parser
Builds an Abstract Syntax Tree (AST) from tokens using recursive descent parsing:
```
BinOpNode(+)
├── NumberNode(5)
└── NumberNode(3)
```

#### Interpreter
Traverses the AST and executes operations using the visitor pattern.

---

## 🎯 Example Programs

### FizzBuzz

```python
FOR i = 1 TO 100 THEN
    IF i % 15 == 0 THEN
        PRINT("FizzBuzz")
    ELIF i % 3 == 0 THEN
        PRINT("Fizz")
    ELIF i % 5 == 0 THEN
        PRINT("Buzz")
    ELSE
        PRINT(i)
    END
END
```

### Fibonacci Sequence

```python
FUNC fib(n)
    IF n <= 1 THEN RETURN n
    RETURN fib(n - 1) + fib(n - 2)
END

FOR i = 0 TO 10 THEN
    PRINT(fib(i))
END
```

### Prime Number Checker

```python
FUNC is_prime(n)
    IF n < 2 THEN RETURN 0
    IF n == 2 THEN RETURN 1
    
    FOR i = 2 TO n - 1 THEN
        IF n % i == 0 THEN RETURN 0
    END
    
    RETURN 1
END

PRINT(is_prime(17))  # 1 (true)
PRINT(is_prime(18))  # 0 (false)
```

### Interactive Calculator

```python
FUNC calculator()
    PRINT("Simple Calculator")
    PRINT("Enter 'q' to quit")
    
    WHILE TRUE THEN
        VAR num1 = INPUT_INT("Enter first number: ")
        VAR op = INPUT("Enter operator (+, -, *, /): ")
        VAR num2 = INPUT_INT("Enter second number: ")
        
        IF op == "+" THEN PRINT(num1 + num2)
        ELIF op == "-" THEN PRINT(num1 - num2)
        ELIF op == "*" THEN PRINT(num1 * num2)
        ELIF op == "/" THEN PRINT(num1 / num2)
        ELSE PRINT("Invalid operator")
        END
    END
END
```

---

## 🔧 Error Handling

BASIC provides detailed error messages with source code highlighting:

### Illegal Character Error
```
Basic > VAR x = 5 @ 3
Illegal Character: '@'
File <stdin>, line 1

VAR x = 5 @ 3
          ^
```

### Invalid Syntax Error
```
Basic > VAR = 5
Invalid Syntax: Expected identifier
File <stdin>, line 1

VAR = 5
    ^
```

### Runtime Error
```
Basic > VAR x = y
Runtime Error: 'y' is not defined
File <stdin>, line 1

VAR x = y
        ^
```

### Division by Zero
```
Basic > 10 / 0
Runtime Error: Division by zero
File <stdin>, line 1

10 / 0
   ^
```

---

## 📚 Grammar Reference

```
statements  : NEWLINE* statement (NEWLINE+ statement)* NEWLINE*

statement   : KEYWORD:RETURN expr?
            : KEYWORD:CONTINUE
            : KEYWORD:BREAK
            : expr

expr        : KEYWORD:VAR IDENTIFIER EQ expr
            : comp-expr ((KEYWORD:AND | KEYWORD:OR) comp-expr)*

comp-expr   : NOT comp-expr
            : arith-expr ((EE | LT | GT | LTE | GTE) arith-expr)*

arith-expr  : term ((PLUS | MINUS) term)*

term        : factor ((MUL | DIV) factor)*

factor      : (PLUS | MINUS) factor
            : power

power       : call (POW factor)*

call        : atom (LPAREN (expr (COMMA expr)*)? RPAREN)?

atom        : INT | FLOAT | STRING | IDENTIFIER
            : LPAREN expr RPAREN
            : list-expr
            : if-expr
            : for-expr
            : while-expr
            : func-def

func-def    : KEYWORD:FUNC IDENTIFIER?
              LPAREN (IDENTIFIER (COMMA IDENTIFIER)*)? RPAREN
              (ARROW expr | NEWLINE statements KEYWORD:END)
```

---

## 🧪 Running Tests

```bash
# Interactive REPL
python shell.py

# Run example file
python shell.py < example.basic

# Run your own programs
python shell.py < your_program.basic
```

---

## 🛠️ Built-in Constants

```python
NULL    # Null value
TRUE    # Boolean true (1)
FALSE   # Boolean false (0)
```

---

## 🤝 Contributing

This is a personal learning project, but suggestions and improvements are welcome! Here are some ideas for enhancements:

- [ ] Add file I/O operations
- [ ] Implement dictionaries/hash maps
- [ ] Add more built-in functions
- [ ] Implement import/module system
- [ ] Add string methods (split, join, etc.)
- [ ] Implement try/catch error handling
- [ ] Add lambda expressions
- [ ] Create standard library
- [ ] Add debugging features
- [ ] Implement comments
- [ ] Add multi-line string support
- [ ] Implement class/object system

---

## 📝 License

This project is free to use for **educational and learning purposes**. Feel free to study the code, learn from it, and build upon it for your own education!

**Please note:** This is a personal learning project and is not intended for commercial use.

---

## 🎓 Learning Resources

This project demonstrates fundamental concepts in programming language design:

- **Lexical Analysis**: Tokenizing source code into meaningful symbols
- **Parsing**: Building Abstract Syntax Trees using recursive descent
- **Interpreting**: Executing code via tree traversal and the visitor pattern
- **Symbol Tables**: Managing variable scope and context
- **Error Handling**: Comprehensive error reporting with position tracking
- **Type Systems**: Implementing dynamic typing
- **Memory Management**: Reference counting and garbage collection
- **Control Flow**: Implementing conditionals, loops, and function calls

### Recommended Reading
- *Crafting Interpreters* by Robert Nystrom
- *Writing An Interpreter In Go* by Thorsten Ball
- *Dragon Book* (Compilers: Principles, Techniques, and Tools)

---

## 🌟 Acknowledgments

Built as an educational project to understand interpreter design and language implementation from first principles. This project explores how real programming languages work under the hood, from tokenization to execution.

---

## 💡 Why BASIC?

This language is called BASIC as a tribute to the original BASIC (Beginner's All-purpose Symbolic Instruction Code) that helped millions learn programming. While this implementation differs significantly from the original, it shares the same spirit: making programming concepts accessible and understandable.

---

<div align="center">
Made with ❤️ for learning • Built with Python
</div>
