path="semple\\text\\text.txt"
with open(path,"a+") as paths:
    paths.write("\nthis just now new line")
    paths.seek(0)
    print(paths.read())