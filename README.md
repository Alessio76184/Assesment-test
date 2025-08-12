# Assessment Task – Algorithm + Tests

This small project contains:
- **`main_functions.py`** – the core algorithm.
- **`test_main_functions.py`** – a simple test runner with multiple cases, including edge cases (spaces, empty input).
- **`Task_Questions.txt`** – written answers for the assessment questions (unit/integration/system tests, design pattern, multi-thread vs multi-process, Dockerfile).

---

## 1) Project Structure

```
Assessment-Tests/
├── main_functions.py            # algorithm: return characters that appear at least twice
├── test_main_functions.py       # prints test outcomes (PASS/FAIL)
└── Task_Questions.txt           # written answers
```

---

## 2) How to Run (Windows, macOS, Linux)

### Prerequisites
- Python 3.10+ installed (`python --version` or `python3 --version`)

### Option A – Run from VS Code Terminal
1. Open the folder in **VS Code**.
2. Open the terminal (**View → Terminal**).
3. Run the tests:
   ```bash
   python test_main_functions.py
   # or on some systems:
   python3 test_main_functions.py
   ```

You should see lines like:
```
Running sample tests...

Test 1: Input=['c', 'a', 'i', 'o', 'p', 'a'] → Output=['a'] Expected=['a'] → PASS ✅
...
```

### Option B – Run from Git Bash / Command Prompt
```bash
cd "C:/..."
python test_main_functions.py
```

> Note: Use quotes around the path because of spaces in the folder name.

---

## 3) The Algorithm

**Function:** `return_characters_appearing_twice(chars: list[str]) -> list[str]`

**Goal:** Given a list of characters (e.g., `['c','a','i','o','p','a']`), return the characters that appear **at least twice**, preserving the order of first appearance. For the example above, the output is `['a']`.

**Approach:**
1. Count occurrences with a frequency dictionary.
2. Walk the input again and collect each character whose count is ≥ 2, without duplicates (tracked via a `seen` set).

**Time / Space Complexity:**
- Let `n = len(chars)`, `k = distinct characters`.
- **Time:** `O(n)` to count + `O(n)` to build result → overall **O(n)**.
- **Space:** `O(k)` for the frequency map (and up to `O(k)` for `seen`).

**Edge Cases Covered by Tests:**
- No duplicates → returns `[]`.
- Triple repeats → returns the character once.
- Empty input → returns `[]`.
- Whitespace as a character → included if it repeats (e.g., `['a', ' ', 'b', ' ', 'c']` → `[' ']`).

---

## 4) How the Tests Work

In **`test_main_functions.py`**, the test runner defines a list of `(input, expected_output)` pairs, calls the function, and prints `PASS`/`FAIL` for each case. This keeps the tests simple and easy to read in the terminal.

If you want to switch to the `unittest` framework later, you can wrap the same cases in `unittest.TestCase` methods without changing the algorithm.

---

## 5) Summary of Written Answers (`Task_Questions.txt`)

- **Unit vs Integration vs System Tests:**  
  - *Unit* → a small piece (function/class) in isolation, often with mocks.  
  - *Integration* → components working together (e.g., service + DB).  
  - *System* → end-to-end as a user/external system would use it.

- **Design Pattern (Strategy) & SRP Connection:**  
  Strategy organises interchangeable algorithms into separate classes. In this task, the algorithm and tests are split into separate files, which follows the **Single Responsibility Principle** and keeps code reusable and maintainable.

- **Multi-Process vs Multi-Thread:**  
  Threads share memory (lightweight, great for I/O/waiting work, but can interfere if not synchronised).  
  Processes are isolated (more memory/overhead, but safer and allow true parallel CPU work).

- **Dockerfile Comments:**  
  Starts from a small Debian image, generates a random token at build time, creates and runs a script to delete it, then prints `done` on container start.  
  Caveats: avoid `latest` (pin versions), and don’t generate secrets during image build (they persist in image layers). Prefer runtime secrets or BuildKit secrets; combine steps to avoid leaving helper files behind.

---

## 6) Quick Demo Snippets

Run a quick call to the function from a Python shell:
```python
from main_functions import return_characters_appearing_twice
return_characters_appearing_twice(['c','a','i','o','p','a'])
# ['a']
```

Try a case with spaces:
```python
return_characters_appearing_twice(['a',' ','b',' ','c'])
# [' ']
```

---

## 7) Notes for Reviewers 
- The algorithm is linear-time with predictable memory usage.
- Tests include common paths and edge cases (empty, no duplicates, whitespace).  
- Answers in `Task_Questions.txt`, and happy to elaborate later if needed
