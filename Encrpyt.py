alpha ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str = print("enter message")
n = len(str)
out =""




for i in range(n):
        c = str[i]
        loc = alpha.find(c)
        print(i,c,loc)
        newloc = loc + 3
        out += alpha[newloc]
        print(newloc,out)

print("encryp string",out)        
