import display
import fetcher

def main():
    print("Welcome to my github activity CLI!")
    username = input("Please enter a github username to see their recent activity: ").strip().lower()
    data = fetcher.fetch(username)
    display.display(data)

if __name__ == "__main__":
    main()