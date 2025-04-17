from openai import OpenAI
client = OpenAI(api_key="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")

response = client.responses.create(
    model="gpt-4.1",
    input="who is lionel messi ?"
)

print(response.output_text)
