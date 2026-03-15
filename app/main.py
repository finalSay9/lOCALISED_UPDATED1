from fastapi import FastAPI

from app.routes import users



app = FastAPI()


@app.get('/')
def evan():
    return {'name': 'welcome evan chimwaza'}

    
app.include_router(users.router)