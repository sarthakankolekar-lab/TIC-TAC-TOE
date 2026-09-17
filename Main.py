list = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

for i in range(0, 3):
  if (i == 0):
    print("    0   1   2")
  print(f"{i} | ", end="")
  for j in range(0, 3):
    print(f"{list[i][j]} | ", end="")
  print()


while True:
  p1 = input("\nPlayer 1 Choose X or O: ").upper()
  if (p1 == "X" or p1 == "O"):
    print(f"Player 1 will play as {p1}")
    if (p1 == "X"):
      p2 = "O"
    else:
      p2 = "X"
    print(f"Player 2 will play as {p2}")
    break
  else:
    print("Error: Invalid Input!")

print("\nEnter Coordinates to fill the Boxes")
print("Take help of the box provided for indexes")

for a in range(0,9):
  if (a % 2 == 0):
    while True:
      print("\n===== Player 1 Turn =====")
      px = int(input("Player 1 X-axis index: "))
      py = int(input("Player 1 Y-axis index: "))
      
      if px in [0,1,2] and py in [0,1,2]:
        list[px][py] = p1
        for i in range(0, 3):
          if (i == 0):
            print("\n    0   1   2")
          print(f"{i} | ", end="")
          for j in range(0, 3):
            print(f"{list[i][j]} | ", end="")
          print()
        break
      else:
        print("Error: Invalid Input!")
  else:
    while True:
      print("\n===== Player 2 Turn =====")
      px = int(input("Player 2 X-axis index: "))
      py = int(input("Player 2 Y-axis index: "))
      
      if px in [0,1,2] and py in [0,1,2]:
        list[px][py] = p2
        for i in range(0, 3):
          if (i == 0):
            print("\n    0   1   2")
          print(f"{i} | ", end="")
          for j in range(0, 3):
            print(f"{list[i][j]} | ", end="")
          print()
        break
      else:
        print("Error: Invalid Input!")
        
  if (a > 2):
    lines = [
      [list[0][0], list[0][1], list[0][2]],
      [list[1][0], list[1][1], list[1][2]],
      [list[2][0], list[2][1], list[2][2]],
      [list[0][0], list[1][0], list[2][0]],
      [list[0][1], list[1][1], list[2][1]],
      [list[0][2], list[1][2], list[2][2]],
      [list[0][0], list[1][1], list[2][2]],
      [list[0][2], list[1][1], list[2][0]]
    ]
    for li in lines:
      if li[0] == li[1] == li[2] == "X" or li[0] == li[1] == li[2] == "O":
        if li[0] == p1:
          print("Player 1 Wins")
          break;
        else:
          print("Player 2 Wins")
          break;
  
