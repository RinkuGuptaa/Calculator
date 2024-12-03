# Simple Calculator 🧮

A Python-based calculator with a beautiful and enhanced interface using the `rich` library. Perform basic arithmetic operations: addition, subtraction, multiplication, and division. The program allows you to continue or exit after each calculation.

---

## Features

- Perform **Addition**, **Subtraction**, **Multiplication**, and **Division**.
- Enhanced and colorful **User Interface** using the `rich` library.
- **Error Handling**:
  - Ensures valid numerical input.
  - Handles division by zero gracefully.
- Option to **Continue or Exit** after each calculation.

---

## Prerequisites

1. Install Python 3.x (if not already installed).
2. Install the `rich` library for enhanced output:
   ```bash
   pip install rich

##Output Interface
╭───────────────────────────────────────────╮
│ ✨ Welcome to the Mixed-Up Calculator! ✨ │
╰───────────────────────────────────────────╯
Enter the first number: 21
Enter the second number: 22
Choose an operation (+, -, *, /): +
╭─────────────────────────────────────────────────────────────────── Mixed-Up Calculator Results ───────────────────────────────────────────────────────────────────╮
│ Your choice: +                                                                                                                                                    │
│ Result of your operation: 43.0                                                                                                                                    │
│                                                                                                                                                                   │
│ Actual operation performed: *                                                                                                                                     │
│ Result of actual operation: 462.0                                                                                                                                 │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
Do you want to perform another calculation? (yes/no) [yes/no]: no
╭─────────────────────────────────────────────────────────────╮
│ 💡 Thank you for using the Mixed-Up Calculator! Goodbye! 💡 │
╰─────────────────────────────────────────────────────────────╯
