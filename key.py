import os
import sys
import argparse
import logging
import openai

def parse_args():
    parser = argparse.ArgumentParser(
        description="Simple OpenAI API client"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable DEBUG logging"
    )
    return parser.parse_args()

def main():
    # 1) Load your API key into openai.api_key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        logging.critical("Missing OPENAI_API_KEY environment variable. Exiting.")
        sys.exit(1)

    # 2) Parse CLI args & configure logging
    args = parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )

    # 3) Make an example API call
    logging.info("Sending test prompt to OpenAI…")
    resp = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Say hello!",
        max_tokens=5
    )
    print(resp.choices[0].text.strip())

if __name__ == "__main__":
    main()
