"""Create the TaskFlow triage agent in Azure AI Foundry.

Run once, then save the printed agent ID to your .env as AZURE_AGENT_ID.

Usage:
    az login
    python scripts/create_agent.py
"""
from azure.ai.projects import AIProjectClient
from azure.ai.agents.models import CodeInterpreterTool
from azure.identity import DefaultAzureCredential

PROJECT_ENDPOINT = "https://myfndryq.services.ai.azure.com/api/projects/proj-default"

client = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)

# Create agent using the 1.1.0 API (.agents.create instead of .agents.create_agent)
agent = client.agents.create(
    model="gpt-4o",
    name="taskflow-triage-agent",
    instructions="""You are a task planning and triage assistant for TaskFlow.
Help users:
- Break down vague requests into concrete tasks with clear titles and descriptions
- Suggest priority (todo / in_progress / done) and effort estimates
- Identify blockers and dependencies between tasks
- Summarise the current task list and flag overdue or stalled items
Always return structured suggestions the app can act on.""",
    tools=[CodeInterpreterTool()],
)

print(f"\nAgent created successfully!")
print(f"Agent ID : {agent.id}")
print(f"Agent name: {agent.name}")
print(f"\nAdd to your .env:")
print(f"AZURE_FOUNDRY_ENDPOINT={PROJECT_ENDPOINT}")
print(f"AZURE_AGENT_ID={agent.id}")
