import os
from autogen import ConversableAgent

# Definindo a chave de API diretamente no código (não recomendado para uso real)
api_key = "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"

agent_mkt = ConversableAgent(
    "agent_mkt",
    system_message="You are usefull assistante "
    "your expertise is on the commercial area ",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": api_key}]},
    is_termination_msg=lambda msg: "exit" in msg["content"],  # terminate if the number is guessed by the other agent
    human_input_mode="NEVER",  # never ask for human input
)

agent_comercial = ConversableAgent(
    "agent_comercial",
    system_message="You are usefull assistante "
    "your expertise is on the marketing area ",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": api_key}]},
    human_input_mode="NEVER",
)

human_proxy = ConversableAgent(
    "human_proxy",
    llm_config=False,  # no LLM used for human proxy
    human_input_mode="ALWAYS",  # always ask for human input
)

# Start a chat with the agent with number with an initial guess.
result = human_proxy.initiate_chat(
    agent_mkt, agent_comercial, # this is the same agent with the number as before
    message="Como eu posso te ajudar?",
)