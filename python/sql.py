import sqlite3 

#db처리를 하다가 여러 처리가 오면 lock이 걸려서 timeout을 설정 
con = sqlite3.connect("word-search.db", check_same_thread=False,timeout=20)
cur = con.cursor()



def insert_word_location(game_id, word, start_row, start_col, direction):
    
    #id는 나중에 실제 사용자 id로 바꿀것임 
    cur.execute(f"""
                INSERT INTO words(game_id, word, start_row, start_col, direction)
                VALUES ('{game_id}', '{word}',{start_row}, {start_col}, '{direction}')
                """)
    con.commit()
    print("success")
    return 


def insert_game_info(game_id, title, description, subject, url):
    
    cur = con.cursor()
    #id는 나중에 실제 사용자 id로 바꿀것임 
    cur.execute(f"""
                INSERT INTO games(game_id, title, description, subject, url)
                VALUES ('{game_id}','{title}', '{description}', '{subject}', '{url}')
                """)
    
    con.commit()
   
    return

def read_game_info(title):
    con.row_factory = sqlite3.Row
    
    cur = con.cursor()
    
    rows = cur.execute(f"""
                       SELECT * FROM games 
                       JOIN words ON games.game_id=words.game_id
                       WHERE title='{title}'
                       """).fetchall()
    
    
    return [dict(row) for row in rows]


def check_answer_db(word):
    
    cur = con.cursor()
    
    
    row = cur.execute(f"""
                    SELECT * FROM words 
                    WHERE word='{word}'
                    """).fetchone()
    if(row == None):
        return False   
    
    return True

    

def update_score_in_db(user_score):
    name = user_score.name
    score = user_score.score
    complete_time = user_score.time 
    title = user_score.title 
    
    cur = con.cursor()
    
    cur.execute(f"""
                INSERT OR REPLACE INTO user_score(title, name, score, complete_time)
                VALUES ('{title}', '{name}', {score}, {complete_time})
                """)
    con.commit()
    
    
def get_score_in_db(title):
    con.row_factory = sqlite3.Row
    
    cur = con.cursor()
    
    scores = cur.execute(f"""
                        SELECT * FROM user_score
                        WHERE title='{title}'
                        ORDER BY complete_time ASC
                        """).fetchall()
    
    return [dict(row) for row in scores] 


def create_user_in_db(id, password, name):
    cur = con.cursor()
    
    cur.execute(f"""
                INSERT INTO user(id, password, name)
                VALUES ('{id}', '{password}', '{name}')
                """)
    con.commit()
 
 
def find_user(where_statement):
    con.row_factory = sqlite3.Row
    cur = con.cursor()  
    user = cur.execute(f"""
                       SELECT * FROM user
                       WHERE {where_statement}
                       """).fetchone()
    return user

def update_refresh_token_db(id, refresh_token):
    
    cur = con.cursor()
    cur.execute(f"""
                INSERT OR REPLACE into tokens(id, refresh_token)
                VALUES ('{id}', '{refresh_token}')
                """)
    con.commit()
    
def find_id_by_token(refresh_token):
    con.row_factory = sqlite3.Row;
    cur = con.cursor()
    
    row = cur.execute(f"""
                      SELECT id FROM tokens 
                      WHERE refresh_token='{refresh_token}'
                      """).fetchone()
    return dict(row)["id"]
    