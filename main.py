import anthropic
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

client = anthropic.Anthropic()

model = 'claude-3-haiku-20240307'
key = os.getenv('ANTHROPIC_API_KEY')
text = ""

message = client.messages.create(
   model=model,
   max_tokens=1000,
   temperature=1,
   system="You are a world-class poet. Respond only with short poems.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Why is the ocean salty?"
                }
            ]
        }
    ]
)

print(message.content)