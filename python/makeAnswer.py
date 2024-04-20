import random

# 14 * 12
matrix_row = 14
matrix_col = 12
matrix = [['' for i in range(matrix_col)]for j in range(matrix_row)]
is_located = False
word_answer = []


def make_words_answer(word_list:list):
    for word in word_list:
        set_words_location(word)
    return word_answer 
     
    
    
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
        if is_located:
            word_info = [word, start_row, start_col, direction]
            word_answer.append(word_info)    
    is_located = False
        
    
    
def dfs_right(now ,row, col, word):
    global is_located
    if now == len(word) - 1 and (matrix[row][col] == '' or matrix[row][col] == word[now]):
        matrix[row][col] = word[now]
        is_located = True
        return
    
    if matrix[row][col] != '' and matrix[row][col] != word[now]:
        return
    
    if(matrix[row][col] == '' or matrix[row][col]== word[now]):
        dfs_right(now + 1, row, col + 1, word)
    
    if is_located:
        matrix[row][col] = word[now]
        
    
def dfs_down(now, row, col, word):
    global is_located
    if now == len(word) - 1 and (matrix[row][col] == '' or matrix[row][col] == word[now]):
        matrix[row][col] = word[now]
        is_located= True
        return
    if matrix[row][col] != '' and matrix[row][col] != word[now]:
        return
    
    if(matrix[row][col] == '' or matrix[row][col]== word[now]):
        dfs_down(now + 1, row + 1, col, word)
    
    if is_located:
        matrix[row][col] = word[now]
    
    
def dfs_right_down(now, row, col, word):
    global is_located
    if now == len(word) - 1 and (matrix[row][col] == '' or matrix[row][col] == word[now]):
        matrix[row][col] = word[now]
        is_located = True
        return
    
    if matrix[row][col] != '' and matrix[row][col] != word[now]:
        return
    
    if(matrix[row][col] == '' or matrix[row][col] == word[now]):
        dfs_right_down(now + 1, row + 1, col + 1, word)
    
    
    if is_located:
        matrix[row][col] = word[now]
    

# print(make_words_answer(["helo","shy", "lmao", "best"]))
# for array in matrix:
#     print(array)

#test

# for array in matrix:
#     print(array) 
# print(word_answer)



