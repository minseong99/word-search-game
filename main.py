from fastapi import FastAPI, WebSocket, Form
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

#create
@app.post("/game")
def create_game(game_info:Game):
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


@manager.user_loader()
def query_user(data):
    
    WHERE_STATEMENT = f'id="{data}"'
    if type(data) == dict:
        WHERE_STATEMENT = f'id="{data["id"]}"'
    print(WHERE_STATEMENT)   
      
    return find_user(WHERE_STATEMENT)
         
@app.post("/login")
def login(id:Annotated[str, Form()],
               password:Annotated[str, Form()]):
    
    user = query_user(id)
    print(user)
    
    if not user:
        raise InvalidCredentialsException
    elif user["password"] != password:
        raise InvalidCredentialsException
    
    
    
    
        
        
    
    

app.mount("/",StaticFiles(directory="static", html=True),name="static")