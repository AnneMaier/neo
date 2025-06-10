import lmstudio as lms

model = lms.llm()
result = model.respond("What is the moeaning of life?")
print(result)