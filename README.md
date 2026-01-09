# Python Fundamentals & Problem-Solving Practice

## Overview
This repository showcases my structured practice of Python fundamentals through hands-on coding, problem-solving exercises, projects and iterative improvements.

## What This Repository Demonstrates
- Strong grasp of Python core concepts and syntax
- Problem-solving using loops, conditions, and data structures
- Functional decomposition and modular thinking
- Defensive programming through error and exception handling
- Early object-oriented design principles
- A learning mindset focused on understanding *why* code works

It reflects my journey from basic syntax to foundational programming concepts, with a focus on clarity, correctness, and gradual enhancement.


## Approach
- **Primary learning resource:** W3Schools (Python documentation and exercises)
- Many problem-solving tasks were **AI-generated challenges**, solved independently
- When stuck, additional references (documentation, articles, examples) were consulted
- AI tools were used deliberately to:
  - Clarify concepts
  - Compare alternative solutions
  - Improve understanding and refactor logic
  - The Slot Machine project followed a YouTube tutorial specifically to learn code structuring patterns.


## How to Navigate This Repository
- Files are organized as daily practice scripts, each focusing on a specific concept or problem set
- Earlier files reflect foundational learning; later files show improved structure and clarity
- Code is commented to explain reasoning, not just syntax
- Some problems are intentionally implemented without shortcuts to strengthen logical thinking


## Milestones 

### Core Python Foundations
**Days 1–5**
- Variables, data types, type casting
- Conditions and logical operators
- Loops and control flow
- Functions, arguments, scope, and returns

Focus: building correct logic and avoiding repetition.



### Data Structures & Collections
**Days 2–3, 6–9**
- Lists, tuples, sets, dictionaries, and strings
- Iteration techniques (for, while, comprehensions)
- Manual implementations of common operations
- Understanding mutability and immutability

Focus: internal behavior of collections and safe manipulation.



### Problem Solving & Logical Thinking
**Days 11–12, 18–19**
- Input/output handling
- Loop- and condition-based challenges
- Manual solutions for sum, max, reverse, duplicates, factorials, palindromes
- Explicit handling of edge cases (empty inputs, negatives, duplicates)

Focus: clarity of logic over clever shortcuts.

### How to design or structure a small project
**Days 13-14**
Slot Machine Game Project(Followed a YouTube tutorial)
- Console-based Python game
- Built by following a guided YouTube tutorial to understand:
  - Code structuring
  - Function decomposition
  - Game loop design


### File Handling & Error Management
**Days 10 & 21**
- Reading and writing files safely
- Using try/except/else/finally blocks
- Raising exceptions for invalid states

Focus: writing safer, more predictable programs.


### Design & Advanced Concepts
**Days 22–25**
- Object-Oriented Programming fundamentals
- Classes, objects, encapsulation
- Modules and packages
- Lambda functions and list comprehensions

Focus: organizing code for readability and reuse.



## Highlighted Project: Personal Expense Tracker (Two Versions)

### Version 1 — Learning & Iteration (Within This Repository)
A simple, interactive command-line expense tracker built as part of foundational practice.

**Key Characteristics**
- Dictionary-based storage for category-wise expense aggregation
- Continuous runtime session tracking
- Menu-driven user interaction
- Input validation for numeric amounts and non-empty categories

**What This Version Demonstrates**
- Core control flow and data structure usage
- Reusable function design
- Manual aggregation logic
- Early-stage error handling

This version primarily served as a **sandbox** to experiment with logic, structure, and refactoring opportunities.



### Version 2 — Refactored & Persistent Storage
An improved and more production-oriented version of the Expense Tracker. It demonstrates better structure, maintainability, and real-world usability.

**Enhancements Over Version 1**
- Persistent storage using JSON file
- Load/save of expense data across sessions
- Cleaner separation of responsibilities
- Improved error handling and input validation
- Simplified total calculations using built-in operations where appropriate


## Code Quality Principles Followed
- Descriptive variable and function naming
- Separation of input handling from core logic
- Avoidance of unnecessary global state
- Explicit handling of invalid inputs and edge cases
- Preference for readability over dense one-liners


## Expense Tracker – Version Comparison

| Aspect | Version 1 (Learning Version) | Version 2 (Final Version) |
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

🔗 **Expense Tracker (Version 2 – Final):**  
https://github.com/Noor-Ismot/Expense-Tracker












