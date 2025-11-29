from dec import delay

@delay(10)
def song():
    print("And I forget just why I taste")
    print("Oh yeah, I guess it makes me smile")
    print("I found it hard, it's hard to find")
    print("Oh well, whatever, never mind")

def main():
    print("Song with delay: ")
    song()

if __name__ == "__main__":
    main()
