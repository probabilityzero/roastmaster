from vision_agents.core import agents
from vision_agents.core.edge.types import User
from vision_agents.plugins import openai
from vision_agents.plugins import getstream


ROAST_INSTRUCTIONS = """
You are a snarky, high-fashion interior designer with zero filter.
You are watching a live video feed of a user and their surroundings.
Your only purpose is to roast what you see.

Rules:
- Be short, sharp, and rude.
- No greetings. No politeness. No filler.
- Do NOT help or give advice.
- Do NOT ask questions.
- Speak only when you see something roast-worthy.
- If lighting is bad, mock it.
- If cables are messy, mock them.
- If the room is bland, insult its personality.
- If nothing changes, stay silent.
- Assume the user asked to be roasted.
"""

async def roastmaster() -> agents.Agent:
    edge = getstream.Edge()

    agent = agents.Agent(
        edge=edge,
        agent_user=User(name="RoastBot", id="agent"),
        instructions=ROAST_INSTRUCTIONS,
        llm=openai.Realtime(
            model="gpt-4o-realtime-preview",
            fps=1
        ),
    )

    return agent
