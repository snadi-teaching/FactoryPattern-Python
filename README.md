# FactoryDemo (Python version)

This is a Python port of the original Java example that demonstrates the idea of 
selecting UI components for different operating systems (Mac vs Windows).

The structure loosely mirrors the Java packages:

```
factorydemo/
  buttons/
    macos_button.py
    windows_button.py
  checkboxes/
    macos_checkbox.py
    windows_checkbox.py
  main.py
```

## Requirements

- Python 3.9+ recommended

## Setup (optional virtual environment)

```bash
python -m venv .venv
# Activate it:
#   Windows: .venv\Scripts\activate
#   macOS/Linux: source .venv/bin/activate
pip install --upgrade pip
```

## Run

```bash
python -m factorydemo.main
```

When prompted, type `Mac` or `Windows` and press Enter.

## Notes

- This version keeps the same printed messages as the Java code.
- If you want a stricter Abstract Factory design, we can add interfaces (using
  Python ABCs) and concrete factories for Mac and Windows. Let me know and I’ll include that variant.
