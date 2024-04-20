import sqlite3 


con = sqlite3.connect("word-search.db", check_same_thread=False)
cur = con.cursor()



def insert_word_location(word, start_row, start_col, direction):
    
    cur.execute(f"""
                INSERT INTO words(word, start_row, start_col, direction)
                VALUES ('{word}',{start_row}, {start_col}, '{direction}')
                """)
    con.commit()
    print("success")
    return 



