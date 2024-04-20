from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from python.makeAnswer import make_words_answer
from python.sql import *

class Game(BaseModel):
    title:str
    description:str
    wordList:list
    subject:str
app = FastAPI()

#create
@app.post("/game")
def create_game(game_info:Game):
    word_answers = make_words_answer(game_info.wordList)
    print(word_answers)
    insert_game_info(game_info.title, game_info.description,game_info.subject)
    for word_info in word_answers:
        insert_word_location(word_info[0], word_info[1], word_info[2], word_info[3])
    
    
    return "200"

app.mount("/",StaticFiles(directory="static", html=True),name="static")