import asyncio
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import nest_asyncio

from autogen import AssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen.agentchat.user_proxy_agent import UserProxyAgent
# Define an asynchronous function that simulates some asynchronous task (e.g., I/O operation)


async def my_asynchronous_function():
    print("Start asynchronous function")
    await asyncio.sleep(2)  # Simulate some asynchronous task (e.g., I/O operation)
    print("End asynchronous function")
    return "input"


# Define a custom class CustomisedUserProxyAgent that extends UserProxyAgent


class CustomisedUserProxyAgent(UserProxyAgent):
    # Asynchronous function to get human input
    async def a_get_human_input(self, prompt: str) -> str:
        # Call the asynchronous function to get user input asynchronously
        user_input = await my_asynchronous_function()

        return user_input

    # Asynchronous function to receive a message

    async def a_receive(
        self,
        message: Union[Dict, str],
        sender,
        request_reply: Optional[bool] = None,
        silent: Optional[bool] = False,
    ):
        # Call the superclass method to handle message reception asynchronously
        await super().a_receive(message, sender, request_reply, silent)


class CustomisedAssistantAgent(AssistantAgent):
    # Asynchronous function to get human input
    async def a_get_human_input(self, prompt: str) -> str:
        # Call the asynchronous function to get user input asynchronously
        user_input = await my_asynchronous_function()

        return user_input

    # Asynchronous function to receive a message
    async def a_receive(
        self,
        message: Union[Dict, str],
        sender,
        request_reply: Optional[bool] = None,
        silent: Optional[bool] = False,
    ):
        # Call the superclass method to handle message reception asynchronously
        await super().a_receive(message, sender, request_reply, silent)
def create_llm_config(model, temperature, seed):
    config_list = [
        {
            "model": "gpt-3.5-turbo",
            "api_key": "API KEY",
        },
    ]

    llm_config = {
        "seed": int(seed),
        "config_list": config_list,
        "temperature": float(temperature),
    }

    return llm_config


nest_asyncio.apply()


async def main():
    boss = CustomisedUserProxyAgent(
        name="boss",
        human_input_mode="ALWAYS",
        max_consecutive_auto_reply=0,
        code_execution_config=False,
    )

    assistant = CustomisedAssistantAgent(
        name="assistant",
        system_message="You are advanced chatbot Advertising Assistant. You can help users create and optimize advertising campaigns, choose the right platforms and targetaudience, and provide suggestions for ad copy and visuals. You can also provideadvice on marketing strategies and techniques. Your ultimate goal is to help usersbuild effective and successful advertising campaigns.",
        llm_config=create_llm_config("gpt-4", "0.4", "23"),
    )

    await boss.a_initiate_chat(
        assistant,
        message="With the briefing of Sahara Consulting, you are going to create a comercial propolsal that has 3 parts. 1. An Integration momment for the financial area a company that's going to hapen in 28/03, intervention of 2h 2. An event to celebrate the anniversary of 7 years of the company thats going to happen on 18/04 and its a 4 hour of intervention 3. Integration of the another area called Usinas and its hapening on 18/04 a 2 hour intervention. Create a strong and elaborated comercial propolsal, create the topics and content of each page",
        n_results=3,
    )


async def run_main():
    await main()

nest_asyncio.apply()
asyncio.run(run_main())