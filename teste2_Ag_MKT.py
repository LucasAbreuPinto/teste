from autogen import ConversableAgent
import os

# Configuração do LLM com a chave API diretamente inserida
llm_config = {
    "config_list": [{"model": "gpt-4", "api_key": os.environ.get("KEYYYYYY")}],
}

# Criação dos agentes
user_proxy = ConversableAgent(
    "user_proxy",
    llm_config=llm_config,
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER",
)

pesquisador = ConversableAgent(
    "pesquisador",
    llm_config=llm_config,
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER",
)

escritor_blog = ConversableAgent(
    "escritor_blog",
    llm_config=llm_config,
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER",
)

# Simulação de uma conversa
# O User Proxy faz uma pergunta ao Pesquisador
reply_pesquisador = pesquisador.generate_reply(messages=[{"content": "Qual é o tema da pesquisa mais recente em IA?", "role": "user"}])
print("Pesquisador:", reply_pesquisador)

# O Pesquisador 'responde', e então o User Proxy 'pergunta' ao Escritor de Blog
reply_escritor_blog = escritor_blog.generate_reply(messages=[{"content": "Como posso escrever um blog sobre o tema da pesquisa mais recente em IA?", "role": "user"}])
print("Escritor de Blog:", reply_escritor_blog)

# Nota: Este código assume que o método generate_reply retorna diretamente a resposta desejada.
