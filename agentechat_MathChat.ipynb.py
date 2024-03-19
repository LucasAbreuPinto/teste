import autogen
from autogen.agentchat.contrib.math_user_proxy_agent import MathUserProxyAgent

# Configuração já definida no código, como mostrado anteriormente
config_list = [
    {
        'model': 'gpt-4',
        'api_key': "API KEY",
    },
    # Adicione mais configurações conforme necessário...
]

# Cria uma instância de AssistantAgent
assistant = autogen.AssistantAgent(
    name="assistant",
    system_message="You are a helpful assistant.",
    llm_config={
        "timeout": 600,
        "seed": 42,
        "config_list": config_list,
    },
)

# Cria uma instância de MathUserProxyAgent
mathproxyagent = MathUserProxyAgent(
    name="mathproxyagent",
    human_input_mode="NEVER",
    code_execution_config={"use_docker": False},
)

# Definindo o problema matemático
math_problem = (
    "Quanto é 2 elevador a 457 potencia?."
)

# Iniciando a conversa
# Observação: Este código presume que o MathUserProxyAgent tem um método para iniciar o chat diretamente.
# Se o método correto para iniciar o chat diferir, você precisará ajustar esta parte conforme a API da biblioteca.
mathproxyagent.initiate_chat(assistant, problem=math_problem)
