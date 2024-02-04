from langchain.llms import OpenAI
import os

os.environ['OPENAI_API_KEY'] = "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"
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)

text = "Suggest a personalized workout routine for someone looking to improve cardiovascular endurance and prefers outdoor activities."
print(llm(text))