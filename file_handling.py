# | Mode   | Meaning           |
# | ------ | ----------------- |
# | `"r"`  | Read              |
# | `"w"`  | Write             |
# | `"a"`  | Append            |
# | `"x"`  | Create a new file |
# | `"r+"` | Read + Write      |
# | `"w+"` | Write + Read      |

# file = open("data.txt", "r")

# content = file.read()

# print(content)

# file.close()

f = open("data.txt","w")
f.write("good afernoon")
f = open("data.txt","a")
f.write("\nohhh good")


# f=open('handling.txt','w')
# f.write('goodmorning')
# f=open('handling.txt','a')
# f.write('\nhelloeveryone\n')
# f=open('handling.txt','a')
# f.write('\ngoodmorning\n')
f=open("data.txt","r")
# print(f.read())
content=f.readline()
content1=f.readline()
content2=f.readlines()
print(f.seek(3))

print(content)
print(content1)
print(content2)

f.close()

with open("index.txt","r") as file:
    file.seek(5)
    print(file.readline())
    print(file.readline())
    #file deleting syndax
    import os
    os.remove("index.txt")
    




