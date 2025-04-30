from google import generativeai as genai
from config import environment

genai.configure(api_key=environment.exampleapikey)

gemionimodel = genai.GenerativeModel('gemini-2.0-flash')