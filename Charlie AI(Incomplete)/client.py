from openai import OpenAI
client = OpenAI(
    api_key="sk-None-Y3rG7hJObwB9Pr2AZWnGT3BlbkFJKyVyoxeOj0x28DQLw6aR"
)
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message.content)



