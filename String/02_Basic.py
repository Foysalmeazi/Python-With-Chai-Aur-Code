# --- 1. DATA INITIALIZATION ---

# List for demonstrating slicing operations
num_List = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Strings for various methods and conversions
game = "Cricket is my favourite favourite game"
game1 = "cricket"
game2 = "football"
chai = "lemon,sugar,Ginger,Masala,Carrot,cardamom"
chai2 = "lemon2, sugar2, Ginger2, Masala2, Carrot2, cardamom2"
coffee = "------------Milk"

# List for join operation
playersList = ['Sakib', 'Mash', 'Foysal', 'Riyad', 'Russel']

# Path variable (using a regular string for Windows path)
path1 = "C:\\Assignment\\capstone Block 1\\"

# --- 2. LIST SLICING EXAMPLES ---

print("\n--- LIST SLICING ---")
# [:] - Prints a shallow copy of the entire list.
print(f"Full List ([:]): {num_List[:]}")
# [2:5] - Elements from index 2 up to (but not including) index 5.
print(f"Slice [2:5]: {num_List[2:5]}")
# [3:] - Elements from index 3 to the end.
print(f"Slice [3:]: {num_List[3:]}")
# [:6] - Elements from the start up to (but not including) index 6.
print(f"Slice [:6]: {num_List[:6]}")
# [0:7:2] - Elements from 0 to 7 (exclusive), step of 2.
print(f"Slice [0:7:2] (Step 2): {num_List[0:7:2]}")
# [0:7:3] - Elements from 0 to 7 (exclusive), step of 3.
print(f"Slice [0:7:3] (Step 3): {num_List[0:7:3]}")

# --- 3. STRING MANIPULATION & FORMATTING ---

print("\n--- STRING METHODS ---")
# .lower() and .upper() - Case conversion.
print(f"Chai Lowercase: {chai.lower()}")
print(f"Chai Uppercase: {chai.upper()}")

# .strip(chars) - Removes specified characters from the START and END.
print(f"Coffee Stripped: {coffee.strip('-')}")

# .replace(old, new) - Swaps substrings.
print(f"Chai Replace: {chai.replace('Masala', 'Honey')}")

# .find(substring) - Finds the index of the first occurrence.
print(f"'favourite' find index: {game.find('favourite')}")

# .count(substring) - Counts the occurrences of the substring.
print(f"'favourite' count: {game.count('favourite')}")

# .format() - Inserts variables into a string template.
todayGame = "I played {} and {}"
print(f"Formatted Game: {todayGame.format(game1, game2)}")


# --- 4. CONVERSIONS (SPLIT & JOIN) ---

# String to List (.split()) - Splits string by the delimiter.
players = "Sakib, Mash, Foysal, Riyad, Russel"
print(f"\nPlayers List (Split): {players.split(', ')}")

# List to String (.join()) - Joins list elements using the separator.
print(f"Players String (Join): {' '.join(playersList)}")


# --- 5. ITERATION AND PATH EXAMPLE ---

print("\n--- ITERATION ---")
# For loop - Iterates over the string 'cricket' (game1).
for letter in game1:
    # This prints the message multiple times, once for each letter
    print(f'Total Letter in game1 is: {letter}') 
    
print("\n--- PATH OUTPUT ---")
# Path variable printing - Backslashes are displayed literally.
print(f"Path Output: {path1}")