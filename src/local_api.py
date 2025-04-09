"""Local API call"""

from openai import OpenAI


def generate(base_url: str, api_key: str, model: str, query: str) -> None:
    """Generates a response from a local model.

    Parameters
    ----------
    base_url : str
        The base URL of the API endpoint.
    api_key : str
        The API key used for authentication.
    model : str
        The name or ID of the model to use for generation.
    query : str
        The input prompt or message to send to the model.
    """
    client = OpenAI(
        base_url=base_url,
        api_key=api_key,
    )

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": query},
        ],
        temperature=0.7,
        n=1,
        # seed=1,
        stream=True,
    )

    for token in completion:
        print(token.choices[0].delta.content, end="", flush=True)
