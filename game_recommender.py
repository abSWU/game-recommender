import openai
from gamekey import key #api key from different file

client = openai.OpenAI(api_key=key)

print("A program meant to recommend games based on you budget and personal tastes.\n")

while (True):
    #User's parameters
    console = input("What platform do you use? (PC/Mobile/Xbox/PlayStation)\n")
    budget = input("What is your budget (in USD)?\n")
    genres = input("What genres of games do you like?\n")
    favorite_games = input("What are some games that you enjoy?\n")

    #Prompt - sets up the above parameters and outlines the response for the AI
    prompt = (
        "Recommend 3 games to a person with the following parameters:"
        f"Platform {console}\n"
        f"Budget: {budget}\n"
        f"favorite genres: {genres}\n"
        f"favorite game: {favorite_games}\n"
        "Say the game name and cost. Then, provide a description about the game and why it would be a good fit for the user (max 50 words)."
    )


    #setting up our message
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo", #api model
        messages=[
            {"role":"user","content": prompt}
        ]
    )

    #Print out the response
    print(response.choices[0].message.content)

    restart = input("Would you like to try again? (yes/no)\n").lower().strip()
    if (restart!="yes"):
        break
