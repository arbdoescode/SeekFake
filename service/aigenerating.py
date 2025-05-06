from config.aimodel import gemionimodel
from module.Request.ExampleReq import SimpleReq
import asyncio

async def aibasicresponse(msg:SimpleReq):
    response = await asyncio.to_thread(gemionimodel.generate_content, msg.msg)
    return response.text