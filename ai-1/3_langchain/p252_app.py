from langchain.agents import initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory


# 도구 준비
tools = load_tools(
    tool_names=["serpapi", "llm-math"],
    llm=ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )
)

# 메모리 생성
memeory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)


# 에이전트 생성
agent = initialize_agent(
    agent="conversational-react-description",
    llm=ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    ),
    tools=tools,
    verbose=True,
    memory=memeory
)

print(agent.run("좋은 아침입니다."))
print("-" * 50)

print(agent.run("우리집 반려견 이름은 보리입니다."))
print("-" * 50)

print(agent.run("우리집 반려견 이름을 불러주세요."))

print("-" * 50)



