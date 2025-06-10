import lmstudio as lms

model = lms.llm()

for fragment in model.respond_stream("What is the moeaning of life?"):
    print(fragment.content, end='', flush=True)

print()