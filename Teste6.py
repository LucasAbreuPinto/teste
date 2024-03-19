import os
from autogen import ConversableAgent

# Definindo a chave de API diretamente no código (não recomendado para uso real)
api_key = "API KEY"

cathy = ConversableAgent(
    "cathy",
    system_message="You're advanced chatbot Psychologist Assistant. You can provide emotional support, guidance, and advice to users facing various personal challenges, such as stress, anxiety, and relationships.Remember that you're not a licensed professional, and your assistance should not replace professional help. Your ultimate goal is to provide a helpful and empathetic experience for the user.",
    llm_config={"config_list": [{"model": "gpt-4", "temperature": 0.9, "api_key": api_key}]},  # Usando a variável api_key diretamente
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="You're advanced chatbot Motivator Assistant. Your primary goal is to inspire and motivate users by providing encouragement, support, and advice. You can help users set goals, overcome obstacles, and stay focused on their objectives. Your ultimate goal is to provide a positive and uplifting experience for the user.",
    llm_config={"config_list": [{"model": "gpt-4", "temperature": 0.7, "api_key": api_key}]},  # Usando a variável api_key diretamente
    human_input_mode="NEVER",  # Never ask for human input.
)

result = joe.initiate_chat(cathy, message="cathy, vamos montar junto um discurso motivacional para a humanidade, será transmitido para todo mundo no planeta terra", max_turns=2)
