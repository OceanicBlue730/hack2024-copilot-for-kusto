import json
import requests
import time
from openai import AzureOpenAI
client = AzureOpenAI(
  azure_endpoint = "https://oaiauseasts0.openai.azure.com/",
  api_key= "2343856f2bea4689892a56f5883bf3d1",
  api_version="2024-05-01-preview"
)

assistant = client.beta.assistants.create(
  model="test-gpt-4o", # model deployment name.
  instructions="You are an intelligent Copilot that will help Microsoft internal employees - particularly support engineers and developer teams write KQL queries based on English prompts sent by the user. Ask them follow up questions to refine the prompt further, wherever necessary. If any files are added, share insights from only the shared files.",
  tools=[{"type":"code_interpreter"},{"type":"file_search"}],
  tool_resources={"file_search":{"vector_store_ids":[]},"code_interpreter":{"file_ids":[]}},
  temperature=0.74,
  top_p=0.6
)
