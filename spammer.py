import time

# ANSI escape code for red text
RED = "\033[91m"
RESET = "\033[0m"

def spam_text(message: str, delay: float = 0.1):
    count = 1
    while True:
        print(f"{RED}{count}: {message}{RESET}")
        count += 1
        time.sleep(delay)

if __name__ == "__main__":
    spam_text("YOU BROKE THE RULES! ", delay=0.01)
