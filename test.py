from dotenv import load_dotenv
import os
import anthropic

# Load your API key from the .env file
load_dotenv()

# Connect to Claude
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

# Send a test message
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Say hello in exactly 10 words."}
    ]
)

# Print the response
print(message.content[0].text)
