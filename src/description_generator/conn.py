import os

url = "https://hawki2.htwk-leipzig.de/api/ai-req"
headers = {
    "Authorization": f"Bearer {os.getenv("AI_API_KEY")}",
    "Content-Type": "application/json",
}

command = """Create 10 synthetic descriptions of a device in NDJSON format, only the description field. 
Do NOT add ```json ``` or any code block. Output plain NDJSON, one JSON object per line, like:
{"description": "A compact smartphone with a 5.8-inch display, 128GB storage, and dual rear cameras."}
{"description": "Wireless noise-cancelling headphones with up to 30 hours of battery life and touch control."} """

my_data = {
    "payload": {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": {
                    "text": command
                }
            }
        ]
    }
}
