import os
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

def main():
    arg_len = len(sys.argv)
    if arg_len == 1:
        print("Prompt argument required.")
        exit(1)

    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )
    
    if "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    print(response.text)

if __name__ == "__main__":
    main()
