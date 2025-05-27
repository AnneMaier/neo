from langchain.chains import ConversationChain
from langchain.llms import OpenAI


chain = ConversationChain(
    llm = OpenAI(
        model = 'gpt-3.5-turbo-instruct',
        temperature = 0.9
    ),
    verbose = True
)
print("-" * 50)
chain.run("우리집 반려견 이름은 달래와 랑이입니다.")
print("-" * 50)
chain.predict(input="우리집 반려견 이름을 불러주세요.")