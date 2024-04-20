import sqlite3 


con = sqlite3.connect("word-search.db", check_same_thread=False)
cur = con.cursor()



def insert_word_location(word, start_row, start_col, direction):
    
    #id는 나중에 실제 사용자 id로 바꿀것임 
    cur.execute(f"""
                INSERT INTO words(word, start_row, start_col, direction)
                VALUES ('{word}',{start_row}, {start_col}, '{direction}')
                """)
    con.commit()
    print("success")
    return 


def insert_game_info(title, description, subject):
    
    cur = con.cursor()
    #id는 나중에 실제 사용자 id로 바꿀것임 
    cur.execute(f"""
                INSERT INTO games(title, description, subject)
                VALUES ('{title}', '{description}', '{subject}')
                """)
    
    con.commit()
    print("games_success")
    return



