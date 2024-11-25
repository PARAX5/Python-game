import random

# Snake and ladder board configuration
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to update player's position
def update_position(position):
    if position in snakes:
        print(f"Oops! Bitten by a snake. Sliding down from {position} to {snakes[position]}.")
        position = snakes[position]
    elif position in ladders:
        print(f"Yay! Climbed a ladder from {position} to {ladders[position]}.")
        position = ladders[position]
    return position

# Function to play the game
def play_game():
    player_positions = [0, 0]  # Starting positions for Player 1 and Player 2
    player_names = ["Player 1", "Player 2"]
    turn = 0

    print("Welcome to Snake and Ladder!")
    print("First player to reach position 100 wins!")
    
    while True:
        current_player = turn % 2
        input(f"{player_names[current_player]}'s turn. Press Enter to roll the dice.")
        dice = roll_dice()
        print(f"{player_names[current_player]} rolled a {dice}.")
        
        # Update the player's position
        new_position = player_positions[current_player] + dice
        
        if new_position > 100:
            print(f"Roll exceeds 100. {player_names[current_player]} stays at {player_positions[current_player]}.")
        else:
            player_positions[current_player] = update_position(new_position)
            print(f"{player_names[current_player]} is now at position {player_positions[current_player]}.")
        
        # Check for a win
        if player_positions[current_player] == 100:
            print(f"Congratulations! {player_names[current_player]} wins!")
            break
        
        turn += 1

# Start the game
if __name__ == "__main__":
    play_game()
