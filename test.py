import os

file = open("crash.txt", mode="w")
file.write("Hello, world!")
file.flush()  # Flush the buffer to ensure data is written to the file
os._exit(1)
