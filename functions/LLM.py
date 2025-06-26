import os
from mistralai import Mistral
from dotenv import load_dotenv

from ollama import chat as chat_ollama
from ollama import ChatResponse as ChatResponse_ollama

 

def send_prompt(prompt: str,model = 'llama2:7b'):  #'llama2:7b' # 'mixtral:8x7b'
    """
    Function to interact with the Ollama chat model.
    
    :param model: The name of the model to use for the chat.
    :param messages: A list of messages to send to the model.
    :return: The response from the chat model.
    """
    if model.lower() == "mistral":
        load_dotenv()
        api = os.getenv("MISTRAL")

        client = Mistral(api_key=api)
        response = client.chat.complete(model="mistral-large-latest", messages=[
            {
            'role': 'user',
            'content': prompt,
            },
            ])
        return response.choices[0].message.content
    else:
        response = chat_ollama(model=model, messages=[
        {
        'role': 'user',
        'content': prompt,
        },
        ])
        return response.message.content

def send_messages(messages: list, model = 'llama2:7b'):
    """
    Function to interact with the Ollama chat model using a list of messages.
    
    :param model: The name of the model to use for the chat.
    :param messages: A list of messages to send to the model.
    :return: The response from the chat model.
    :return: The response from the chat model.
    """
    if model.lower() == "mistral":
        load_dotenv()
        api = os.getenv("MISTRAL")

        client = Mistral(api_key=api)
        response = client.chat.complete(model="mistral-large-latest", messages=messages)
        return response.choices[0].message.content
    else:
        response = chat_ollama(model=model, messages=messages)
        return response.message.content



    load_dotenv()
    api = os.getenv("MISTRAL")

    client = Mistral(api_key=api)
    response = client.chat.complete(model="mistral-large-latest", messages=messages)

    return response