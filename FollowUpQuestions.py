# Add a new follow-up question to the thread
# The question is hard-coded for now
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Use TraceCallResult table instead of AzureDiagnostics"
)
if run.status == 'completed':
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )
  print(messages)
elif run.status == 'requires_action':
  # the assistant requires calling some functions
  # and submit the tool outputs back to the run
  pass
else:
  print(run.status)
