from langchain.prompts import FewShotPromptTemplate
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

examples = [{"input": "明るい", "output": "暗い"},
    {"input": "おもしろい", "output": "つまらない"},]

example_prompt = PromptTemplate(
    input_variables = ["input", "output"],
    template = "入力: {input}\n出力: {output}"
)

prompt_from_string_examples = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="주어진 입력 단어의 반의어를 출력하시오.",
    suffix="입력: {adjective}",
    input_variables=["adjective"],
    example_separator="\n\n"
)

prompt = prompt_from_string_examples.format(adjective="악마")
print("생성된 프롬프트:\n")
print(prompt)

chat_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
result = chat_llm([HumanMessage(content=prompt)])
print(f'출력: {result.content}')