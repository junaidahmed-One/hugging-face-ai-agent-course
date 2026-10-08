import os

from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, VisitWebpageTool
from tool_cargo_plane_tt import calculate_cargo_travel_time

model = LiteLLMModel(
    model_id=os.environ.get("OPENROUTER_MODEL", "openrouter/auto"),
    api_key=os.environ.get("OPENROUTER_API_KEY"),
)

task = """Find all Batman filming locations in the world, calculate the time to transfer via cargo plane to here (we're in Gotham, 40.7128° N, 74.0060° W), and return them to me as a pandas dataframe.
Also give me some supercar factories with the same cargo plane transfer time."""

agent = CodeAgent(
    model=model,
    tools=[DuckDuckGoSearchTool(), VisitWebpageTool(), calculate_cargo_travel_time],
    additional_authorized_imports=["pandas"],
    max_steps=20,
)

result = agent.run(task)

print(result)
