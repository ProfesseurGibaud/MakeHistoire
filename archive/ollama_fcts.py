from ollama import chat
from ollama import ChatResponse


def send_prompt(prompt: str, model = 'llama2:7b') -> ChatResponse:  #'llama2:7b' # 'mixtral:8x7b'
    """
    Function to interact with the Ollama chat model.
    
    :param model: The name of the model to use for the chat.
    :param messages: A list of messages to send to the model.
    :return: The response from the chat model.
    """

    response: ChatResponse = chat(model=model, messages=[
        {
        'role': 'user',
        'content': prompt,
        },
        ])

    return response

def send_messages(messages: list, model = 'llama2:7b') -> ChatResponse:
    """
    Function to interact with the Ollama chat model using a list of messages.
    
    :param model: The name of the model to use for the chat.
    :param messages: A list of messages to send to the model.
    :return: The response from the chat model.
    """

    response: ChatResponse = chat(model=model, messages=messages)

    return response

    