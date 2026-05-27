def wants_replay():
     
    replay = input("\nDo you want to play again?").lower()

    if replay == "yes":
        return True
    
    return False