def wants_replay():
     
    replay = input("\nDo you want to play agian?").lower()

    if replay == "yes":
        return True
    
    return False