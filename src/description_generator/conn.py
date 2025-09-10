import os

url = "https://hawki2.htwk-leipzig.de/api/ai-req"
headers = {
    "Authorization": f"Bearer {os.getenv("AI_API_KEY")}",
    "Content-Type": "application/json",
}

command = """
Create 100 synthetic descrptions of a device in NDJSON format, only the description field. 
Do NOT add ```json ``` or any code block. Output plain NDJSON, one JSON object per line, like:
{"description": "first description"}
{"description": "second description"}
"""

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
