import openai

def response_from_ChatAI(user_content, r_num=1):
    messages = [
        {"role" : "user", "content" : user_content },
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
        temperature=0.8,
        n=r_num
    )

    assistant_replies = []

    for c in response['choices']:
        assistant_replies.append(c['message']['content'])

    return assistant_replies

res = response_from_ChatAI("대한민국 헌법의 1조 1항은?")
print(res)

