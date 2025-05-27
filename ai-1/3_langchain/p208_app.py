import os
from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI

serpapi_api_key = os.environ.get("SERPAPI_API_KEY")

tools = load_tools(["serpapi", "llm-math"], 
    llm=OpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
        )
    ,serpapi_api_key=serpapi_api_key
)

agent = initialize_agent(
    agent="zero-shot-react-description",
    tools =tools,
    llm = OpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",),
    verbose=True,
)

print("-" * 50)

input_agent = "123 * 4를 계산기로 계산하세요."

agent.run(input_agent)

print("-" * 50)

input_agent = "오늘 한국 서울의 날씨를 웹 검색으로 확인하세요."
agent.run(input_agent)