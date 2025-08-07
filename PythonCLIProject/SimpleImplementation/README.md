
# 🛠️ Python CLI Package Installer

A simple **CLI (Command-Line Interface)** tool that simulates a package manager like `apt-get`, `pip`, or `mvn install`.

---

## 🧾 What is CLI?

**CLI (Command-Line Interface)** is a way to interact with programs by typing commands in a terminal.

In Python, CLIs are built using:
- `sys.argv` – basic argument handling
- `argparse` – structured argument parsing
- `click` – rich CLI creation (optional for later)

---

### 📦 Installing a package:

```bash
$ py mypkg.py install seaborn 

```

**Output:**

```text
Akanksha@DESKTOP-JKK54DJ MINGW64 ~/Git/Python/PythonCLIProject/SimpleImplementation (main)
$ py mypkg.py install seaborn
 Installing numpy...
numpy installed successfully!
 Installing matplotlib...
matplotlib installed successfully!
 Installing numpy...
numpy installed successfully!
 Installing pandas...
pandas installed successfully!
 Installing seaborn...
```
