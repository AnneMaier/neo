import lmstudio as lms

image_path = 'C:\Users\kibwa\Documents\카카오톡 받은 파일\iish.png'
image_handle = lms.prepare_images(image_path)

model = lms.llm('google/gemma-3-4b-it')
chat = lms.Chat()

chat.add_user_message("Describe this image please.",
                      image=image_handle)

prediction = model.respond(chat)

print(prediction)