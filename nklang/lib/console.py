def log(*text):
    print(text)
    def info(*text):
        print(f"INFO {text}")
    def debug(*text):
        print(f"DEBUG {text}")
    def warning(*text):
        print(f"WARNING {text}")
    def error(*text):
        print(f"ERROR {text}")