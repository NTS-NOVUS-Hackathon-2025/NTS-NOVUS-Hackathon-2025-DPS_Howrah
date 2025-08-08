import google.generativeai as gemini
import os
from dotenv import load_dotenv
load_dotenv()
gemini.configure(api_key=os.getenv("GEMINI_API_KEY"))

prompt_file= open("prompt.txt")
MODEL= gemini.GenerativeModel("gemini-1.5-flash",system_instruction=prompt_file.read())
prompt_file.close()

#Code goes here

if __name__=="__main__":    
    response= MODEL.generate_content("I feel so sad")
    print(response.text)