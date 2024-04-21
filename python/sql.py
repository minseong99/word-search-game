import sqlite3 

#db처리를 하다가 여러 처리가 오면 lock이 걸려서 timeout을 설정 
con = sqlite3.connect("word-search.db", check_same_thread=False,timeout=10)
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


def insert_game_info(game_id, title, description, subject):
    
    cur = con.cursor()
    #id는 나중에 실제 사용자 id로 바꿀것임 
    cur.execute(f"""
                INSERT INTO games(game_id, title, description, subject)
                VALUES ('{game_id}','{title}', '{description}', '{subject}')
                """)
    
    con.commit()
    print("games_success")
    return

def read_game_info():
    con.row_factory = sqlite3.Row
    
    cur = con.cursor()
    
    rows = cur.execute(f"""
                       SELECT * FROM games 
                       JOIN words ON games.game_id=words.game_id
                       """).fetchall()
    
    
    return [dict(row) for row in rows]




