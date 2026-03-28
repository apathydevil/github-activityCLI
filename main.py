import display
import fetcher

def main():
    print("Welcome to my GitHub activity CLI!")
    username = input("Please enter a GitHub username to see their recent activity: ").strip().lower()
    if username is None or username == "":
        print("Invalid username. Please try again.")
        return
    data = fetcher.fetch(username)
    display.display(data)

if __name__ == "__main__":
    main()