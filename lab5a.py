space = {
    { 'A': "clean" },
    { 'B': "dirty" }
}

def clean(space):
    for area, status in space.get({}).items():
        if status == "dirty":
            print("suck", area)
        elif status == "clean":
            print("move to next area")
        else:
            print("No op")