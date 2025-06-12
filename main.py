"""main"""

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import get_files_info


def main():
    """main"""

    res = get_files_info("calculator", "pkg")
    print(f"res: {res}")

    inputs = sys.argv
    if len(inputs) < 2:
        sys.exit(1)

    # verbose = "--verbose" in inputs
    # messages = [types.Content(role="user", parts=[types.Part(text=inputs[1])])]
    #
    # load_dotenv()
    # api_key = os.environ.get("GEMINI_API_KEY")
    # client = genai.Client(api_key=api_key)
    #
    # response = client.models.generate_content(
    #     model="gemini-2.0-flash-001",
    #     contents=messages,
    # )
    #
    # metadata = response.usage_metadata
    #
    # if verbose:
    #     print(f"User prompt: {inputs[1]}")
    #     print(f"Prompt tokens: {metadata.prompt_token_count}")
    #     print(f"Response tokens: {metadata.candidates_token_count}")
    #
    # print("Response:")
    # print(response.text)


if __name__ == "__main__":
    main()
