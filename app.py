from autogen import AssistantAgent, UserProxyAgent
from autogen.coding import LocalCommandLineCodeExecutor
import os
from pathlib import Path

# Configuração do LLM com a chave API diretamente inserida
llm_config = {
    "config_list": [{"model": "gpt-4", "api_key": "KEYYYYYY"}],
}

# Diretório de trabalho para a execução do código
work_dir = Path("coding")
work_dir.mkdir(exist_ok=True)

# Instanciação do AssistantAgent
assistant = AssistantAgent("assistant", llm_config=llm_config)

# Executor de código para o UserProxyAgent
code_executor = LocalCommandLineCodeExecutor(work_dir=work_dir)

# Instanciação do UserProxyAgent com a configuração do executor de código
user_proxy = UserProxyAgent(
    "user_proxy", code_execution_config={"executor": code_executor}
)

# Iniciar a conversa
user_proxy.initiate_chat(
    assistant,
    message="Create a snake game and save it in a file"
)
