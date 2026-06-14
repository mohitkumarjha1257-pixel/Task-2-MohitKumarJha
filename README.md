readme_content = """# Project 2: Expense Tracker

**A State-Preserving Backend Engine for Continuous Financial Data Accumulation**

*Developed by Mohit Kumar Jha | DecodeLabs (Batch: 2026)*

---

## 📌 Project Overview

This project is the second milestone in the DecodeLabs Python Programming Industrial Training Kit. It serves as a bridge to professional backend development by focusing on data accumulation, state preservation, and defensive coding. 

Instead of simple arithmetic, this script acts as a continuous "Audit Loop" that processes numerical data in real-time, handling continuous data entry through pure mathematical and programmatic logic.

## ⚙️ The Architecture (IPO Model)

This project strictly follows the **Input-Process-Output (IPO)** blueprint:
1. **Input (The Gate):** Receives raw material (user input) as strings.
2. **Process (The Engine):** Validates the data, transforms strings to floats/integers, and accumulates the total state.
3. **Output (The Display):** Presents the refined, actionable reality (the final financial total).

## 🚀 Key Features

* **Continuous Audit Loop:** Utilizes a `while True:` execution cycle to allow users to enter multiple expenses continuously without the program terminating after a single entry.
* **The Accumulator Pattern (Stateful Ledger):** Maintains a running total outside the loop (`total += new_expense`) to ensure the financial state is preserved across multiple iterations.
* **Defensive Coding (Digital Poka-Yoke):** Implements a `try...except ValueError` shield interface. If non-numerical data (like text) is entered, the engine catches the error and rejects it safely, preventing a system crash.
* **The Kill Switch (Sentinel Value):** Features a graceful shutdown mechanism. Entering a sentinel value (e.g., `quit`) breaks the loop and triggers the final financial output.

## 💻 Code Structure & Quality Standards

* **Stability:** Handles infinite continuous transactions.
* **State Management:** Variable state (`total`) is correctly initialized *outside* the loop memory space to prevent loop-induced amnesia.
* **Defense:** Implements robust type-safety mechanisms.
* **Control:** Sentinel routing guarantees safe termination and output delivery.

## 🛠️ How to Run

1. Ensure you have Python installed on your machine.
2. Clone this repository or download the script.
3. Run the script via your terminal:
