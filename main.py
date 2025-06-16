import argparse
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

parser = argparse.ArgumentParser(description="Lithid's Py Agent")
parser.add_argument("user_prompt", help="Name of the input file")
parser.add_argument(
    "-v", "--verbose", action="store_true", help="Enable verbose output"
)
args = parser.parse_args()
user_prompt = args.user_prompt
verbose = args.verbose

if len(user_prompt) < 1:
    print("Must add prompt text as argument!")
    sys.exit(1)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001", contents=messages
)

if verbose:
    print("User prompt:", user_prompt)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count, "\n")

print(response.text)
