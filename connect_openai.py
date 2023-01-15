import openai
import time

openai.api_key = "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"

def chatgpt_response(prompt):
    try:
        response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"You: {prompt}\nFriend:",
                temperature=0.5,
                max_tokens=60,
                top_p=1.0,
                frequency_penalty=0.5,
                presence_penalty=0.0,
                stop=["You:"]
                )
        return response['choices'][0]['text']
        
    except openai.exceptions.OpenAIError as e:
        return

