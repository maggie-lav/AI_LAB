room = ["Dirty"] * 6

print("Initial Room Status:")
for i in range(6):
    print(f"Tile {i+1}: {room[i]}")

print("\nRobot Started Cleaning...\n")

for tile in range(6):
    print(f"Robot is cleaning Tile {tile+1}")
    room[tile] = "Clean"

print("\nCleaning Completed!\n")

print("Final Room Status:")
for i in range(6):
    print(f"Tile {i+1}: {room[i]}")

room = ["C", "D", "D", "D", "D", "C"]

print("Initial Room Status:")
print(room)

for i in range(6):
    print("\nRobot is at Tile", i + 1)

    if room[i] == "D":
        print("Tile is Dirty.")
        print("Cleaning Tile...")
        room[i] = "C"
        print("Tile Cleaned.")
    else:
        print("Tile is already Clean.")
        print("Moving to the next Tile.")

print("\nFinal Room Status:")
print(room)
print("\nAll tiles have been checked.") 
