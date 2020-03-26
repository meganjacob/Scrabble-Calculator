letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]

letters_to_points = {letters: points for letters, points in zip(letters, points)}

def score_word(word):
    if word == 1:
        end == True
        return -1
    if word == 2:
        return 0

    point_total = 0
    for i in word:
        point_total += letters_to_points[i]
    return point_total

print("Welcome to the Scrabble Calculator. I keep track of scores throughout your Scrabble game so that you don't have to worry about it and can focus on the words.\n To get started enter the information requested below:")
players = int(input("Number of players: "))
print("Input the player names in the order that you are playing.")
names = []
scores = []
for i in range(players):
    names.append(input("Player " + str(i+1) + " name: "))
for i in range(len(names)):
    scores.append(0)
print("Start playing. I will prompt for the collected words, enter them in a space seperated list (ex. hope creature mine). When you are skipping a turn hit @ and when you are ending the game hit #")
end = False
while (end == False):
    for i in range(players):
        words = []
        words.append(input(names[i]  + ": ").upper())
        for word in words:
            if word.lower() == "#":
                end = True
                hs = 0
                for i in range (players):
                    if hs < scores[i]:
                        hs = scores[i]
                        index = i
                    print(names[i] + ": " + str(scores[i]))
                print("The winner is " + names[index] + "!!")
                
            elif word.lower() == "@":
                score = 0
                scores[i] += score
            else:
                score = score_word(word)
                scores[i] += score
                for i in range (players):
                    print(names[i] + ": " + str(scores[i]))
