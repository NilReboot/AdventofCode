with open("solve.txt","r") as myfile:
    lines = myfile.read().splitlines()
    for line in lines:
        print(line)
        vlen = 14
        for i in range(vlen,len(line)):
            s = line[i-vlen:i]
            if len(set(s)) == vlen:
                print(i)
                break
        
