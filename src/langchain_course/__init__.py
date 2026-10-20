from dotenv import load_dotenv
import os

load_dotenv()

def main() -> None:
    print("Loading environment variables...")
    print(os.getenv("GOOGLE_API_KEY"))

if __name__ == "__main__":
    main()
