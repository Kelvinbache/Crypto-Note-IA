import os
from ollama import Client

ollama_host = os.getenv('OLLAMA_URL', 'http://localhost:11434')

class Ollama_consult():
    def __init__(self, model="llama3.2:latest"):
       self.client = Client(host=ollama_host, timeout=300)
       self.model_IA = model

    def prepare_promt(self, prompt:str):
        return f"Actúa como un experto en criptomonedas. Analiza: {prompt}"     
    
    def consult(self, prompt:str):
        prompt_user = self.prepare_promt(prompt)

        try:

           response = self.client.chat(
                model=self.model_IA,
                messages=[
                    {
                        "role": "user",
                        "content": prompt_user
                    }
                ]
            )
           
           return response["message"]["content"]
         
        except Exception as err:
            return f"Error conectando con la IA: {str(err)}"

ollama_consult = Ollama_consult()