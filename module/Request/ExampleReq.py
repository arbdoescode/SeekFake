from pydantic import BaseModel



class PushWebhook(BaseModel):

    class Pusher(BaseModel):
        name:str
        email:str

    class Repository(BaseModel):
        full_name:str
        name:str

    class Commits(BaseModel):
        message:str
        timestamp:str
        url:str
    after: str
    ref: str
    pusher: Pusher
    repository: Repository
    head_commit: Commits