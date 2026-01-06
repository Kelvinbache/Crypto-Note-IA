from google import genai

from config.config import geminis 

class Geminis():
    def __init__(self, model="gemini-1.5-flash"):
       self.client = genai.Client(api_key="AIzaSyCcputHWqujnhAhwaOkN2ra75T9YX48Quo")
       self.model_IA = model 

    def prepare_promt(self, prompt:str):
        return f"Actúa como un experto en criptomonedas. Analiza: {prompt}"     
    
    def consult(self, prompt:str):
        prompt_user = self.prepare_promt(prompt)

        try:

           response = self.client.models.generate_content(
                model=self.model_IA,
                contents=prompt_user
            )
           
           return response.text
         
        except Exception as err:
            return f"Error conectando con la IA: {str(err)}"

geminis = Geminis()            