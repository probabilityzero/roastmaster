from playground_agent import roastmaster

def main():
    agent = roastmaster()

    print("Roast playground")
    print("Press ENTER to start")
    input()

    print("Watching. Press Ctrl+C to stop.")
    agent.run()

if __name__ == "__main__":
    main()
