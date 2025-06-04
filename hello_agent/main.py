from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

agent = Agent(name = "Assistant", instructions = "You are a helpful assistant.")

result = Runner.run_sync(agent, "What is PIAIC ?")

print(result.final_output)

