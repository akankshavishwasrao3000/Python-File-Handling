with open("py2.py","r") as f:
    content = f.read()
    print(content)
print("Reading Done.....")


with open("filewrite.text" ,"w") as f:
    f.write(content)   #this include new file but old data erase
    # f.write("\nThis is new content")  //it will include in new file
    # f.write("\nwrite mode use to store the data")
print("write mode is done.......")    
