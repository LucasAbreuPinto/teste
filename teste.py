from autogen import ConversableAgent
import os
from pathlib import Path

# Supondo que a chave API esteja definida como uma variável de ambiente para segurança
os.environ["OPENAI_API_KEY"] = "KEYYYYYY"

# Configuração do LLM com a chave API obtida do ambiente
llm_config = {
    "config_list": [{"model": "gpt-4", "api_key": os.environ.get("OPENAI_API_KEY")}],
}

# Criação do agente conversável
assistant = ConversableAgent(
    "assistant",
    llm_config=llm_config,
    code_execution_config=False,  # Desativa a execução de código
    function_map=None,  # Sem funções registradas
    human_input_mode="NEVER",  # Nunca solicita entrada humana
)

# Exemplo de como pedir ao agente para gerar uma resposta
# Nota: Este passo é simplificado e não executa a tarefa específica mencionada
reply = assistant.generate_reply(messages=[{"content": "Tell me a joke.", "role": "user"}])
print(reply)
