# gemini_test.py — simple snippet for Gemini text chat to read from GitHub
# https://github.com/SireGrindalot/python_learning

def greet(name: str) -> str:
    return f"Hello {name} from python_learning!"

if __name__ == "__main__":
    for target in ["Gemini", "SireGrindalot", "world"]:
        print(greet(target))
