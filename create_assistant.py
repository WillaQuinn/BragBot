from openai import OpenAI
client = OpenAI()

my_assistant = client.beta.assistants.create(
    instructions="You are BragBot, a helpful assistant for the company Hello Sci Com.",
    name="BragBot",
    tools=[{"type": "retrieval"}],
    model="gpt-4",
    file_ids=["bragging-doc"],
)
print(my_assistant)