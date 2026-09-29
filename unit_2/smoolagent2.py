from huggingface_hub import login
from smolagents import CodeAgent, tool, InferenceClientModel

login(skip_if_logged_in=False)


@tool
def suggent_menu(occasion: str) -> str:
    """
        Suggests a menu based on the occasion.
    Args:
        occasion (str): The type of occasion for the party. Allowed values are:
                        - "casual": Menu for casual party.
                        - "formal": Menu for formal party.
                        - "superhero": Menu for superhero party.
                        - "custom": Custom menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks"
    elif occasion == "formal":
        return "3-course dinner with wine and desert"
    else:
        return "Custom menu for butler"


agent = CodeAgent(
    tools=[suggent_menu], model=InferenceClientModel(model_id="Qwen/Qwen3-8B")
)

agent.run("Prepare a formal menu for the party.")
