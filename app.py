import pyautogen as autogen

assistant = autogen.Assistant(
    "assistant"
)

user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    code_execution_config={
        "work_dir": "coding"
    }
)

user_proxy.initiate_chat(assistant, message="Create a snake game and same in a file")
