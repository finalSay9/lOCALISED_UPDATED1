from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def evan():
    return {'name': 'welcome evan chimwaza'}
