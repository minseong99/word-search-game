from fastapi import FastAPI, WebSocket, Form, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from python.makeAnswer import make_words_answer
from python.sql import *
from python.html import *
from fastapi.responses import HTMLResponse
from typing import Annotated
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from datetime import timedelta 

SECRET = "super"
manager = LoginManager(SECRET, "/login")
class Game(BaseModel):
    title:str
    description:str
    wordList:list
    subject:str

class User_score(BaseModel):
    name:str
    score:int
    time:int
    title:str
    

app = FastAPI()

@manager.user_loader()
def query_user(data):
    
    WHERE_STATEMENT = f'id="{data}"'
    if type(data) == dict:
        WHERE_STATEMENT = f'id="{data["id"]}"'
      
      
    return find_user(WHERE_STATEMENT)
         
@app.post("/login")
def login(id:Annotated[str, Form()],
               password:Annotated[str, Form()]):
    
    user = query_user(id)
    
    if not user:
        raise InvalidCredentialsException
    elif user["password"] != password:
        raise InvalidCredentialsException
    
    access_token = manager.create_access_token(data={
        "sub":{
            "id":user["id"],
            "name":user["name"]
        }
    },expires=timedelta(seconds=10))
    
    refresh_token = manager.create_access_token(data={
        "sub":{
            "message":"this is refresh token!"
        }
    },expires=timedelta(minutes=2))
    
    update_refresh_token_db(user["id"], refresh_token)
    
    return {"access_token":access_token, "refresh_token":refresh_token}



#create
@app.post("/game")
def create_game(game_info:Game, user=Depends(manager)):
    word_answers = make_words_answer(game_info.wordList)
    
    url = f"""http://127.0.0.1:8000/play/{game_info.title}"""
    insert_game_info(game_info.title, game_info.title, game_info.description,game_info.subject, url)
    for word_info in word_answers:
        insert_word_location(game_info.title, word_info[0], word_info[1], word_info[2], word_info[3])
    
    
    return url;

@app.get("/game/play/{title}")
def get_game_info(title):
    
    
    game_info_obj = read_game_info(title)
    
    
    return JSONResponse(jsonable_encoder(game_info_obj))
    
               

@app.get("/answer{word}")
def check_answer(word):
    if(check_answer_db(word)):
        return "exist"
    return "noexist"   


@app.get("/play/{title}")
def get_page():
    return HTMLResponse(html);

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        
        
        await websocket.send_text(data)
        
@app.post("/score")
def update_score(user_score:User_score):
    print(user_score) 
    #update in db 
    update_score_in_db(user_score)   
    
@app.get("/score{title}")
def read_score(title):
    
    user_score_obj = get_score_in_db(title)
    return JSONResponse(jsonable_encoder(user_score_obj))


@app.post("/signup")
def create_user(id:Annotated[str, Form()],
                password:Annotated[str, Form()],
                name: Annotated[str, Form()]):
    
    create_user_in_db(id, password, name)


def get_access_token(user):
    access_token = manager.create_access_token(data={
        "sub":{
            "id":user["id"],
            "name":user["name"]
        }
    }, expires=timedelta(seconds=10))
    return access_token

@app.get("/token/{token}")
def create_access_token(token):
    try:
        payload = manager._get_payload(token)
        id = find_id_by_token(token)
        user = query_user(id)
        access_token = get_access_token(user)
    except:
        #refresh토큰 유효하지 않으면 db에서 삭제 
        delete_refresh_token(token)
        
        raise InvalidCredentialsException
    
    return {"access_token":access_token}
    
    
        
        
    
    

app.mount("/",StaticFiles(directory="static", html=True),name="static")