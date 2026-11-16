# 42 Exam Rank 03 Simulator 💻🎓

[English](#english) | [Türkçe](#türkçe)

---

<a id="english"></a>
## 🇬🇧 English

### About The Project
This project is a custom-built, CLI-based simulator that mimics the real **42 School's `examshell`** environment. It is specifically designed for the **Exam Rank 03 (Python)** module. The simulator provides a complete exam experience with an automated grading system (Moulinette), dynamic subject assignment, and a leveling system.

### Features
- **Authentic CLI Experience:** Replicates the real `examshell` commands (`subject`, `status`, `grademe`, `finish`).
- **Custom Moulinette:** An automated background grader (`grader.py`) that tests your code against predefined test cases.
- **Leveling System:** 6 levels in total, structured with a 100-point scoring system (16-16-16-16-16-20).
- **JSON Based Question Pool:** Easily customizable question database (`pool.json`).

### Prerequisites
- Python 3.6 or higher.
- No external libraries required (Built entirely with Python standard libraries).

### Installation
1. Clone the repository or download the files.
2. Ensure you have the following files in the same directory:
   - `examshell.py`
   - `grader.py`
   - `pool.json`

### Usage
1. Open your terminal and navigate to the project directory.
2. Start the simulator by running:
   ```bash
   python examshell.py
3. Type `subject` to get your first assignment.
4. Go to the automatically created ./rendu/ folder and create your Python file (e.g. py_bracket_validator.py).
5. Write your solution inside this file.
6. Return to the terminal and type grademe to let Moulinette test your code.

### Available Commands