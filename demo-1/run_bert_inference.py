from transformers import pipeline

qa_pipeline = pipeline("question-answering")

context = "Intel Gaudi2 is an AI accelerator designed for deep learning and inference tasks."
question = "What is Gaudi2 used for?"

result = qa_pipeline(question=question, context=context)
print(result)
