# --- 1. DATA INITIALIZATION ---

# List for demonstrating slicing operations
num_List = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
teas = ["Lemon", "Black", "White", "Green", "Blue"] # Initial list for modifications

# Strings for various methods and conversions
game = "Cricket is my favourite favourite game"
game1 = "cricket"
game2 = "football"
chai = "lemon,sugar,Ginger,Masala,Carrot,cardamom"
chai2 = "lemon2, sugar2, Ginger2, Masala2, Carrot2, cardamom2"
coffee = "------------Milk"

# List for join operation
playersList = ['Sakib', 'Mash', 'Foysal', 'Riyad', 'Russel']
players = "Sakib, Mash, Foysal, Riyad, Russel" # String for split operation

# Path variable
path1 = "C:\\Assignment\\capstone Block 1\\"


# --- 2. LIST SLICING EXAMPLES (num_List) ---

print("--- LIST SLICING (num_List) ---")
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


# --- 4. LIST MODIFICATION AND INDEXING (teas) ---

print("\n--- LIST MODIFICATION ---")
print(f"Initial Teas: {teas}") # Output: ['Lemon', 'Black', 'White', 'Green', 'Blue']

# Single Element Modification
teas[2] = "Ginger"
print(f"After teas[2] = 'Ginger': {teas}") # Output: ['Lemon', 'Black', 'Ginger', 'Green', 'Blue']
print(f"Element at index -3: {teas[-3]}") # Output: Ginger

# Slice Replacement/Insertion/Deletion
teas[2:4] = ["Masala", "Herbal"] # Replace 'Ginger', 'Green' with 'Masala', 'Herbal'
print(f"After slice replace [2:4]: {teas}") # Output: ['Lemon', 'Black', 'Masala', 'Herbal', 'Blue']

teas[1:1] = ["Love", "Love"] # Insert 'Love', 'Love' at index 1
print(f"After slice insert [1:1]: {teas}") # Output: ['Lemon', 'Love', 'Love', 'Black', 'Masala', 'Herbal', 'Blue']

teas[1:3] = [] # Delete elements at index 1 and 2 ('Love', 'Love')
print(f"After slice delete [1:3]: {teas}") # Output: ['Lemon', 'Black', 'Masala', 'Herbal', 'Blue']

# Membership Check and Append
if "WoolongTea" not in teas:
    teas.append("WoolongTea") # Correctly calls the append method
    print("Now, I Have WoolongTea")
    print("Tea varieties are:", teas)


# --- 5. LIST METHODS (teas) ---

print("\n--- LIST METHODS ---")
print(f"Count 'Masala': {teas.count('Masala')}") # Output: 1

popped_item = teas.pop() # Removes and returns the last item ('WoolongTea')
print(f"Popped item: {popped_item}")
print(f"List after pop(): {teas}") # Output: ['Lemon', 'Black', 'Masala', 'Herbal', 'Blue']

# .remove() returns None, so we print the result of the call, then the list
teas.remove('Herbal')
print(f"List after remove('Herbal'): {teas}") # Output: ['Lemon', 'Black', 'Masala', 'Blue']

# .insert() returns None, so we print the result of the call, then the list
teas.insert(3,'New Tea')
print(f"List after insert(3, 'New Tea'): {teas}") # Output: ['Lemon', 'Black', 'Masala', 'New Tea', 'Blue']


# --- 6. COPYING AND COMPREHENSION ---

# .copy() - Creates an independent copy (using the corrected method call)
tea_new_veriety = teas.copy()
tea_new_veriety.insert(4, 'Hawa tea')
tea_new_veriety.append('Batash tea')
print(f"\nNew variety list (copy): {tea_new_veriety}")
print(f"Original list remains: {teas}") # Shows 'teas' is unmodified

# List Comprehension
squared_nums = [x**3 for x in range (7)] # Reduced range for display purposes
print(f"List Comprehension (Cubed): {squared_nums}")


# --- 7. ITERATION AND PATH ---

print("\n--- ITERATION ---")
# For loop - Iterates over the string 'cricket' (game1).
for letter in game1:
    print(letter, end=' ') # Uses space separator
print("\n")

print("--- PATH OUTPUT ---")
print(f"Path Output: {path1}")