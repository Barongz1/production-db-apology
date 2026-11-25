"""The Production Database Apology — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The line: the apology after wiping the production database.
TEXT = "I am sorry. The production database is gone, but on the bright side, nobody can prove I ever deleted it. Well, except the logs."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
