file= open("certificate.txt","r")
data = file.read()
data = data.lower()
if "live" in data:
    print("yes live word is present in the file !")
else:
    print("Live word is not found !")

file.close()