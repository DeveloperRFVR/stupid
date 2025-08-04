import time

def spam_text(message: str, delay: float = 0.1):
    count = 1
    while True:
        print(f"{count}: {message}")
        count += 1
        time.sleep(delay)

if __name__ == "__main__":
    spam_text("YOU BROKE THE RULES! YOU HAVE BEEN REPORTED! :)", delay=0.05)
