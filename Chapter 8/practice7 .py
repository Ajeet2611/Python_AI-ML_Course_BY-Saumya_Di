#open a file named story .txt and print the full content
with open("story.txt","r") as f:
    fullcontent=f.readlines()
    print(fullcontent)