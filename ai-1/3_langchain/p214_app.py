from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

chat_llm = ChatOpenAI(
    model = 'gpt-3.5-turbo',
    temperature = 0.9
)

message = [
    HumanMessage(content = "고양이 울음 소리는?"),
]

print("-" * 50)
result = chat_llm(message)
print(result)

prompts =["고양이 울음소리는?", "까마귀 울음 소리는?"]

for i, pormpt in enumerate(prompts):
    message = [
        HumanMessage(content = pormpt),
    ]

    print("-" * 50)
    result = chat_llm(message)
    print(f"result {i} : {result.content}")