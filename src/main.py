from hufffunc import compress_text
from hufffunc import decompress_text

def compressing_mode():
    print("Compressing mode chosen.")
    print("Please place text to be compressed inside ./files/decompressed.txt")
    input("Press enter when ready... ")
    fileText: str = ""
    try:
        with open("./files/decompressed.txt", "r") as f:
            fileText = f.read()
    except Exception as e:
        print("Some error ocurred while handling the file:")
        print(e)
        return
    if fileText == "":
        print("File is empty.")
        input("Press enter to close... ")
        return
    print("Processing...")
    try:
        compress_text(fileText)
    except Exception as e:
        print("Some error ocurred while handling the file:")
        print(e)
        return
    print("Done!")
    print("File ./files/compressed.txt contains compressed text.")
    input("Press enter to close... ")

def decompressing_mode():
    print("Deompressing mode chosen.")
    print("Please place text to be decompressed inside ./files/compressed.txt")
    input("Press enter when ready... ")
    print("Processing...")
    try:
        decompress_text()
    except Exception as e:
        print("Some error ocurred while handling the file:")
        print(e)
        return
    print("Done!")
    print("File ./files/decompressed.txt contains decompressed text.")
    input("Press enter to close... ")

if __name__ == "__main__":
    # Place text to be compressed in ./files/decompressed.txt
    # Place text to be decompressed in ./files/compressed.txt
    while True:
        print("Choose action:\n0. Compress text\n1. Decompress text")
        choice: str = input()
        if choice == '0' or choice == '1':
            break
        print("Please type a valid option.")
    
    if choice == '0':
        compressing_mode()
    else:
        decompressing_mode()