from inputimeout import inputimeout, TimeoutOccurred
import os

class ConversableAgent:
    def __init__(self, name, llm_config):
        self.name = name
        self.llm_config = llm_config

class CustomAgent:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.llm_config = {
            "config_list": [{"model": "gpt-4", "api_key": os.environ.get("KEYYYYYY")}],
        }
        self.agent = ConversableAgent(name, llm_config=self.llm_config)
        self.tasks_completed = []

    def perform_task(self, task_description):
        print(f"{self.name} performing task: {task_description} with skills {self.skills}")
        response = f"{self.name} completed task: {task_description}"
        self.tasks_completed.append(response)

    def share_results(self):
        for result in self.tasks_completed:
            print(f"{self.name} shares result: {result}")

def conduct_meeting(agents):
    print("\n--- Meeting Start ---\n")
    for agent in agents:
        try:
            response = inputimeout(prompt=f"Do you authorize {agent.name} to share results? (y/n): ", timeout=10)
            if response.lower() == 'y':
                agent.share_results()
            else:
                print(f"{agent.name}'s results will not be shared.")
        except TimeoutOccurred:
            print("Timeout occurred. Proceeding without explicit authorization.")
            agent.share_results()
    print("\n--- Meeting End ---\n")

if __name__ == "__main__":
    researcher = CustomAgent("Researcher", ["data analysis", "literature review"])
    developer = CustomAgent("Developer", ["coding", "software design"])
    writer = CustomAgent("Writer", ["content creation", "blogging"])

    task = input("Please enter the task for the agents: ")

    researcher.perform_task(task)
    developer.perform_task(task)
    writer.perform_task(task)

    conduct_meeting([researcher, developer, writer])
