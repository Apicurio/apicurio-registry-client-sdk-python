
 
## Helper method to save api files in temporary folder
def saveApiFile(name, content):
    with open("./temp/" + name, "w+b") as file:
        try:
             print(file.name)
             file.write(content)
        except Exception as e:
            print("Error writing file: " + str(e))


