print("---Binary permission checker---")
read=1
write=2
execute=4
permission=0
while True:
    print("Would you like to read or write?")
    choice=input()
    if choice=="read":
        permission|=read
    if choice=="write":
        permission|=write
    print("permission value is ",permission)

    if permission & read:
     print("You have read permission")
    elif permission&write:
         print("You have write permission")
    elif permission &execute:
         print("You have execute permission")
    else:
         print("execute access denied")
