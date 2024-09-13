file = open("youtube.txt", "w")

try:
    file.write("Making the youtube manager app")
finally:
    file.close()

with open("youtube.txt", "w") as file:
    file.write("I am happy !")