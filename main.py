import display
import fetcher

def main():
    username = "apathydevil"
    data = fetcher.fetch(username)
    display.display(data)

if __name__ == "__main__":
    main()