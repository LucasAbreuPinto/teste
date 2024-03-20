from autogen import ConversableAgent
from autogen import GroupChat
from autogen import GroupChatManager

# Definindo a chave de API diretamente no código (não recomendado para uso real)
api_key = "API_KEY"

# O Agente de Tendências analisa as tendências do mercado
trends_agent = ConversableAgent(
    name="Trends_Agent",
    system_message="Analyze and report back the current market trends.",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": api_key}]},
    human_input_mode="NEVER",
)

# O Agente de Satisfação do Cliente avalia a satisfação do cliente
customer_satisfaction_agent = ConversableAgent(
    name="Customer_Satisfaction_Agent",
    system_message="Evaluate customer satisfaction based on the latest surveys.",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": api_key}]},
    human_input_mode="NEVER",
)

# O Agente de Análise Competitiva estuda os concorrentes
competitive_analysis_agent = ConversableAgent(
    name="Competitive_Analysis_Agent",
    system_message="Study our competitors and summarize their strengths and weaknesses.",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": api_key}]},
    human_input_mode="NEVER",
)

# O Agente de Inovação sugere novas ideias de produtos
innovation_agent = ConversableAgent(
    name="Innovation_Agent",
    system_message="Suggest new product ideas based on the latest market trends and customer feedback.",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": api_key}]},
    human_input_mode="NEVER",
)

# O Agente de Feedback do Produto coleta feedbacks sobre os produtos
product_feedback_agent = ConversableAgent(
    name="Product_Feedback_Agent",
    system_message="Collect and summarize product feedback from various channels.",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": api_key}]},
    human_input_mode="NEVER",
)

# Descrições dos agentes
trends_agent.description = "Analyze current market trends."
customer_satisfaction_agent.description = "Evaluate customer satisfaction."
competitive_analysis_agent.description = "Analyze competitors."
innovation_agent.description = "Suggest new product ideas."
product_feedback_agent.description = "Collect product feedback."

group_chat_with_introductions = GroupChat(
    agents=[trends_agent, customer_satisfaction_agent, competitive_analysis_agent, innovation_agent, product_feedback_agent],
    messages=[],
    max_round=6,
    send_introductions=True,
)

# Let's use the group chat with introduction messages created above.
group_chat_manager_with_intros = GroupChatManager(
    groupchat=group_chat_with_introductions,
    llm_config={"config_list": [{"model": "gpt-4", "api_key": api_key}]},
)

# Iniciando um chat para uma discussão de equipe sobre um novo produto
chat_result = trends_agent.initiate_chat(
    group_chat_manager_with_intros,
    message="Identify opportunities in the industry of AI agency.",
    summary_method="reflection_with_llm",
)

print(chat_result.summary)
