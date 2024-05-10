from openai import AzureOpenAI
from typing import Optional
from lib.config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT_NAME,
    AZURE_OPENAI_ENDPOINT,
)

client = AzureOpenAI(
    api_version="2023-07-01-preview",
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
)


def call(text: str, image: Optional[str] = None):

    if image is None:

        completion = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT_NAME,
            temperature=1,
            top_p=1,
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": text,
                        },
                    ],
                },
            ],
        )

        return completion.choices[0].message.content
    else:
        completion = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT_NAME,
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": text,
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image,
                            },
                        },
                    ],
                },
            ],
        )
        return completion.choices[0].message.content
