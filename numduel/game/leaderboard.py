import json
def save_score(attempts):

    score_data = {
        "attempts":attempts
        }
    with open("../data/leaderboard.json","r") as file:

        data = json.load(file)

    data.append(score_data)

    with open("../data/leaderboard.json","w") as file:

        json.dump(data,file)
        
def show_leaderboard():

    with open("../data/leaderboard.json","r") as file:

        data = json.load(file)

    print("\nLeaderboard: ")

    for score in data:

        print(score)