agent = ToolCallingAgent(
    tools=[WebSearchTool()],
    model=InferenceClientModel(model_id="Qwen/Qwen3-8B", tool_choice="auto"),
)

agent.run(
    "Search for the best music recommendations for a party at the Wayne's mansion."
)
