import os
from google import generativeai as genai
from dotenv import load_dotenv
from config.aimodel import gemionimodel
from module.Request.ExampleReq import SimpleReq

def aibasicresponse(msg:SimpleReq):
    response = gemionimodel.generate_content(msg.msg)
    return response.text