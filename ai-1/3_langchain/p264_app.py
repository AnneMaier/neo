import os
from langchain.agents import initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory


# wolfram_alpha_appid = os.environ.get("WOLFRAM_ALPHA_APPID")


# 도구 준비
tools = load_tools(
    ['wolfram-alpha']
)

# 메모리 생성
memeory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)


# 에이전트 생성
agent = initialize_agent(
    agent="zero-shot-react-description",
    llm=ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    ),
    tools=tools,
    verbose=True,
    memory=memeory
)



# query = "How many kilometers is the distance between Seoul and Busan?"
query = "How many kilometers is the distance between San Francisco and Grand Canyon?"
print("-" * 50)
print(query)
print("-" * 50)
print(agent.run(query))