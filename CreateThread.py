# Create a thread
# This generates KQL query to retrieve backend logs from English prompts and continues the conversation
thread = client.beta.threads.create()

# Add a user question to the thread
# As of now, I have hard-coded the prompt, as part of the sample code, and used my own Azure AI Speech resource. 
# Attached at the end is also a sample list of prompts that the Copilot can suggest and respond to.
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="Generate a KQL query for me that will help me fetch backend logs for the past 7 days for this resource: /subscriptions/c1eacc76-3311-4114-bee8-a2e6129bbaa0/resourceGroups/CognitiveResources/providers/Microsoft.CognitiveServices/accounts/speechwesteus0"
  # This is our prompt
)

"""
Sample prompts - 1. Generate a KQL query that filters the calls which had 200 response codes in the past 2 hours.
2. Write a KQL query to summarize the number of different response codes received for calls made to this resource in the past week: /subscriptions/c1eacc76-3311-4114-bee8-a2e6129bbaa0/resourceGroups/CognitiveResources/providers/Microsoft.CognitiveServices/accounts/speechwesteus0
3. Write a KQL query to generate a bar chart comparing the number of 200 response codes and 429 response codes for this resource in the last month: /subscriptions/c1eacc76-3311-4114-bee8-a2e6129bbaa0/resourceGroups/CognitiveResources/providers/Microsoft.CognitiveServices/accounts/speechwesteus0
"""
