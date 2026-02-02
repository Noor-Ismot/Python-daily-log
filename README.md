# Overview

This repository showcases my regular structured practice of Python fundamentals through hands-on coding, problem-solving exercises, projects and iterative improvements.

## Resources & Approach

- **Primary learning resource:** W3Schools (Python documentation and exercises)
- Many problem-solving tasks were **AI-generated challenges**, solved independently
- When stuck, additional references (documentation, articles, examples) were consulted
- AI tools were used deliberately to:
  - Clarify concepts
  - Compare alternative solutions
  - Improve understanding and refactor logic
  - The Slot Machine project followed a YouTube tutorial specifically to learn code structuring patterns.

## Milestones

### Core Python Foundations

**Days 1–5**

- Variables, data types, type casting
- Conditions and logical operators
- Loops and control flow
- Functions, arguments, scope, and returns

Focus: building correct logic and avoiding repetition.<br><br><br>

### Data Structures & Collections

**Days 2–3, 6–9**

- Lists, tuples, sets, dictionaries, and strings
- Iteration techniques (for, while, comprehensions)
- Manual implementations of common operations
- Understanding mutability and immutability

Focus: internal behavior of collections and safe manipulation.<br><br><br>

### Problem Solving & Logical Thinking

**Days 11–12, 18–19**

- Input/output handling
- Loop- and condition-based challenges
- Manual solutions for sum, max, reverse, duplicates, factorials, palindromes
- Explicit handling of edge cases (empty inputs, negatives, duplicates)

Focus: clarity of logic over clever shortcuts.<br><br><br>

### How to design or structure a small project

**Days 13-14**
Slot Machine Game Project(Followed a YouTube tutorial)

- Console-based Python game
- Built by following a guided YouTube tutorial to understand:
  - Code structuring
  - Function decomposition
  - Game loop design
Focus: learning project design patterns and structuring code effectively.<br><br><br>

### File Handling & Error Management

**Days 10 & 21**

- Reading and writing files safely
- Using try/except/else/finally blocks
- Raising exceptions for invalid states

Focus: writing safer, more predictable programs. <br><br><br>

### Design & Advanced Concepts

**Days 22–25**

- Object-Oriented Programming fundamentals
- Classes, objects, encapsulation
- Modules and packages
- Lambda functions and list comprehensions

Focus: organizing code for readability and reuse.<br><br>

### Datacamp Course : Introduction to Python for Developers

**Days 25-30**

- Certificate <br><br>
![IntroToPythonForDevelopers.png](https://github.com/Noor-Ismot/Python-daily-log/blob/main/IntroToPythonForDevelopers.png)
<br><br><br>

## Project : Word Frequency Analyzer

A simple **Python command-line tool** that analyzes a text passage and calculates the frequency of each word. It also identifies the **most frequently used word**, helping demonstrate text preprocessing, dictionary usage, and basic algorithmic thinking.

## Features

- Converts text to lowercase for consistent analysis  
- Removes common punctuation marks  
- Splits text into individual words  
- Calculates word frequency  
- Identifies the most frequent word in the passage  
- Handles empty input gracefully  

## Code Highlights

- **Text normalization:** Ensures accurate word comparison
- **Dictionary-based counting:** Uses Python dictionaries for frequency tracking
- **Clear function separation:** Improves readability and maintainability
- **Edge case handling:** Detects and handles empty input

## How It Works

1. User inputs a paragraph of text.
2. The program:
   - Normalizes the text
   - Removes punctuation
   - Splits the passage into words
3. Each word’s frequency is calculated and displayed.
4. The most frequently occurring word is displayed.
<br><br>

## Project: Personal Expense Tracker

A console-based personal expense tracker implemented in two versions to demonstrate learning progression.

### Version 1 – Learning & Iteration

**Focus:** Core Python logic, dictionary-based aggregation, reusable functions.

### Version 2 – Refactored & Persistent

**Focus:** Data persistence, cleaner structure, improved error handling.

## Expense Tracker – Evolution Overview

| Aspect | ([Version 1](https://github.com/Noor-Ismot/Python-daily-log/blob/main/ExpenseTracker_v1.py))  | ([Version 2](https://github.com/Noor-Ismot/Python-daily-log/blob/main/ExpenseTracker_v2.py)) |
|------|-----------------------------|---------------------------|
| Purpose | Practice core Python logic and problem-solving | Refactored, more production-ready implementation |
| Storage | In-memory (runtime only) | Persistent storage using JSON file |
| Data Structure | Dictionary-based aggregation by category | Dictionary + JSON serialization/deserialization |
| Session Handling | Data lost after program exit | Data automatically saved and loaded across sessions |
| Input Validation | Basic validation for numeric amount and non-empty category | Improved validation using `try/except` and safer parsing |
| Code Structure | Procedural with reusable functions | More modular, cleaner separation of responsibilities |
| Error Handling | Basic conditional checks | Explicit exception handling (`try/except`) |
| Scalability | Limited to single runtime session | Easily extensible for reports, dates, or budgets |
| Learning Outcome | Understanding logic, loops, and functions | Applying persistence, refactoring, and maintainability |

---

## Final Version Repository

The refactored and persistent version of the Expense Tracker is maintained here:

🔗 **Expense Tracker (Final version):**  
<https://github.com/Noor-Ismot/Expense-Tracker>
