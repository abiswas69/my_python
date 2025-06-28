path="semple\\text\\text.txt"
with open(path,'w+')as fds:
    fds.write("hi this is new line")
    # fds.seek(0)# Move cursor back to start before reading
    print(fds.read())