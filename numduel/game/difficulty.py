def choose_difficulty(difficulty):

    

    score = 0
    if difficulty == "easy":
        upper_limit = 50
        max_attempts = 20
        score=50
    elif difficulty == "medium":
        upper_limit = 100
        max_attempts = 10
        score=100
    elif difficulty == "hard":
        upper_limit = 500
        max_attempts = 7
        score=200
    else:
        return None,None,None
        
    return upper_limit,max_attempts,score
