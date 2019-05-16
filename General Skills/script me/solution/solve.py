

proble= '((())()) + (()()()) + (()) + () + (()()()(())()()) + (()) + (((()())()())()) + ()() + (()) + (()()()()()()()())'
proble=proble.split(" + ")

num=[]

for one in proble:
    count=0
    max_c=0

    for i in range(len(one)):
        if one[i]=='(':
            count+=1
        elif one[i]==')':
            count-=1
        max_c=max(max_c,count)
    num=num+[max_c]


def combine(str1,str2,num1,num2):

    if num1<num2:
        return '('+str1+str2[1:]
    elif num1>num2:
        return str1[0:-1]+str2+')'
    elif num1==num2:
        return str1+str2


ans=proble[0]
num_total=num[0]
for i in range(1,len(proble),1):
    ans=combine(ans,proble[i],num_total,num[i])
    #print(ans)
    num_total=max(num_total,num[i])


print("answer:",ans)

#flag: picoCTF{5cr1pt1nG_l1k3_4_pRo_0466cdd7}




