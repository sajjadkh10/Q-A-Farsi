from llama_cpp import Llama
from app.config import MODEL_PATH

class AnswerGenerator:
    def __init__(self):
        try:
            self.llm = Llama(
                model_path=MODEL_PATH,
                n_gpu_layers=-1,
                n_ctx=2048,
                verbose=False
            )
            print("Generator initialized successfully!")
        except Exception as e:
            raise RuntimeError(f"Failed to initialize generator: {str(e)}")

    def generate(self, question, context):
        try:
            prompt = f"""
            شما یک دستیار پاسخگو به پرسش هستید. بر اساس اطلاعات زیر به سوال پاسخ دهید:

            اطلاعات:
            {context}

            سوال:
            {question}

            پاسخ:
            """
            output = self.llm(
                prompt=prompt,
                max_tokens=256,
                stop=["\n"],
                temperature=0.7
            )
            return output["choices"][0]["text"].strip()
        except Exception as e:
            print(f"Error in generation: {str(e)}")
            return "متاسفانه در تولید پاسخ مشکلی پیش آمد."