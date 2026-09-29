from huggingface_hub import login

login(skip_if_logged_in=False)


from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()], model=InferenceClientModel(model_id="Qwen/Qwen3-8B")
)

agent.run("Search for the best music recommendation for a party at Wayne's mansion.")
