import asyncio
from playground_agent import roastmaster

async def main():
    agent = await roastmaster()

    print("Roast playground")
    print("Press ENTER to start")
    input()

    print("Watching. Press Ctrl+C to stop.")
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
