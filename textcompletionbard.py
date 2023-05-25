import requests

def get_bard_completion(text):
    """Gets text completion from Bard API."""

    url = "https://bard.ai/v2/completion"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
    }

    response = requests.post(url, headers=headers, data={"text": text})

    if response.status_code == 200:
        completions = response.json()["completions"]
        return completions
    else:
        raise Exception("Error getting text completion from Bard API")


if __name__ == "__main__":
    text = "This is a sentence."
    completions = get_bard_completion(text)

    for completion in completions:
        print(completion["text"])
