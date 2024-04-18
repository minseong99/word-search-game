import random

# 14 * 12
matrix_row = 6
matrix_col = 6
matrix = [['' for i in range(matrix_col)]for j in range(matrix_row)]
is_located = False
word_answer = {}


def make_words_answer(word_list:list):
    for word in word_list:
        word_answer[word] = ""
        set_words_location(word)
        
     
    
    
def set_words_location(word):
    max_length = len(word)
    start_max_row = matrix_row - max_length
    start_max_col = matrix_col - max_length
    
    global is_located
    while (not is_located):
        start_row = random.randint(0, start_max_row)
        start_col = random.randint(0, start_max_col)
        direction = random.choice(["right", "down", "right-down"])
        if direction == "right":
            dfs_right(0, start_row, start_col, word)
        elif direction == "down":
            dfs_down(0, start_row, start_col, word)
        elif direction == "right-down":
            dfs_right_down(0, start_row, start_col, word)    
    is_located = False
        
    
    
def dfs_right(now ,row, col, word):
    global is_located
    if now == len(word) - 1 and (matrix[row][col] == '' or matrix[row][col] == word[now]):
        matrix[row][col] = word[now]
        word_answer[word] = str(col) + word_answer[word]
        word_answer[word] = str(row) + word_answer[word]
        is_located = True
        return
    
    if matrix[row][col] != '' and matrix[row][col] != word[now]:
        return
    
    if(matrix[row][col] == '' or matrix[row][col]== word[now]):
        dfs_right(now + 1, row, col + 1, word)
    
    if is_located:
        matrix[row][col] = word[now]
        word_answer[word] = str(col) + word_answer[word]
        word_answer[word] = str(row) + word_answer[word]
        
    
def dfs_down(now, row, col, word):
    global is_located
    if now == len(word) - 1 and (matrix[row][col] == '' or matrix[row][col] == word[now]):
        matrix[row][col] = word[now]
        word_answer[word] = str(col) + word_answer[word]
        word_answer[word] = str(row) + word_answer[word]
        is_located= True
        return
    if matrix[row][col] != '' and matrix[row][col] != word[now]:
        return
    
    if(matrix[row][col] == '' or matrix[row][col]== word[now]):
        dfs_down(now + 1, row + 1, col, word)
    
    if is_located:
        matrix[row][col] = word[now]
        word_answer[word] = str(col) + word_answer[word]
        word_answer[word] = str(row) + word_answer[word]
    
    
def dfs_right_down(now, row, col, word):
    global is_located
    if now == len(word) - 1 and (matrix[row][col] == '' or matrix[row][col] == word[now]):
        matrix[row][col] = word[now]
        word_answer[word] = str(col) + word_answer[word]
        word_answer[word] = str(row) + word_answer[word]
        is_located = True
        return
    
    if matrix[row][col] != '' and matrix[row][col] != word[now]:
        return
    
    if(matrix[row][col] == '' or matrix[row][col] == word[now]):
        dfs_right_down(now + 1, row + 1, col + 1, word)
    
    
    if is_located:
        matrix[row][col] = word[now]
        word_answer[word] = str(col) + word_answer[word]
        word_answer[word] = str(row) + word_answer[word]
    

get_Answer(["helo","shy", "lmao", "best"])


#test

# for array in matrix:
#     print(array) 
# print(word_answer)

# dict = {"word":""}

# dict["word"] = dict["word"] + "1"

# print(dict["word"])
# dict["word"] = dict["word"] + "2"
# print(dict["word"])

# reverse = ""
# for char in dict["word"]:
#     reverse = char + reverse
# print(reverse)

    
# for word in ["helo","shy", "lmao", "best"]:
    
#     print(word_answer)

