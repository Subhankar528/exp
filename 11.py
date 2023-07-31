while True : #True and False not true and false
    print("Enter here something")
    line =input("---> ")
    if line =="start" or line =="Start" :
        continue
    if line =="done" or line =="Done" :
        break
    if line[0]=="#" :
        break
    print(line)
print("Done ! ")
