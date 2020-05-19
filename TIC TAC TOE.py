import random
#Function for Calculation of VICTORY in Game
def get1(a,i,j,count):
    if count%2==0:
        s='X'
    else:
        s='O'
    row=0
    column=0
    diag1=0
    diag2=0
    for r in range(2):
        p=i
        if p==0:
            if r%2==0:
                p=p+1
                if a[p][j]==s:
                    row+=1
            else:
                p=p+2
                if a[p][j]==s:
                    row+=1
        p=i            
        if p==1:
            if r%2==0:
                p=p+1
                if a[p][j]==s:
                    row+=1
            else:
                 p=p-1
                 if a[p][j]==s:
                    row+=1
        p=i            
        if p==2:
            if r%2==0:
                p=p-1
                if a[p][j]==s:
                    row+=1
            else:
                p=p-2
                if a[p][j]==s:
                    row+=1
    for c in range(2):
        p=j
        if p==0:
            if c%2==0:
                p=p+1
                if a[i][p]==s:
                    column+=1
            else:
                p=p+2
                if a[i][p]==s:
                    column+=1
        p=j           
        if p==1:
            if c%2==0:
                p=p+1
                if a[i][p]==s:
                    column+=1
            else:
                p=p-1
                if a[i][p]==s:
                    column+=1
        p=j
        if p==2:
            if c%2==0:
                p=p-1
                if a[i][p]==s:
                    column+=1
            else:
                p=p-2
                if a[i][p]==s:
                    column+=1
    for d in range (2):
        p=i
        k=j
        if p==0 and k==2:
            if d%2==0:
                t=p+1
                q=k-1
                if a[t][q]==s:
                    diag1+=1
            else:
                t=t+1
                q=q-1
                if a[t][q]==s:
                    diag1+=1
        p=i
        k=j
        if p==1 and k==1:
            if d%2==0:
                p=p-1
                k=k+1
                if a[p][k]==s:
                    diag1+=1
            else:
                p,k=k,p
                p=p+1
                k=k-1
                if a[p][k]==s:
                    diag1+=1
        p=i
        k=j
        if p==2 and k==0:
            if d%2==0:
                p,k=k,p
                if a[p][k]==s:
                    diag1+=1
            else:
                p=p-1
                k=k+1
                if a[p][k]==s:
                    diag1+=1
        p=i
        k=j
    for d in range(2):
        if p==0 and k==0:
            if d%2==0:
                t=p+1
                q=k+1
                if a[t][q]==s:
                    diag2+=1
            else:
                t=t+1
                q=q+1
                if a[t][q]==s:
                    diag2+=1
        if p==1 and k==1:
            if d%2==0:
                t=p-1
                q=k-1
                if a[t][q]==s:
                    diag2+=1
            else:
                t=t+2
                q=q+2
                if a[t][q]==s:
                    diag2+=1
        if p==2 and k==2:
            if d%2==0:
                t=p-1
                q=k-1
                if a[t][q]==s:
                    diag2+=1
            else:
                t=t-1
                q=q-1
                if a[t][q]==s:
                    diag2+=1
    
    if row==2 or column==2 or diag1==2 or diag2==2:
        return 1
#Input Function In Table

def get(a,Muthu,Senthil,count):
    d={1:'00',2:'01',3:'02',4:'10',5:'11',6:'12',7:'20',8:'21',9:'22'}
    boul=0
    if Muthu=='p1':
        boul=True
    if boul:
        print("please enter the choice for the position(p1):")
    elif Senthil=='p1':
        print("please enter the choice for the position(p1):")
    l=int(input())
    for i,j in d.items():
        if i==l:
            t=int(j[0])
            s=int(j[1])
    i,j=t,s
    a[i][j]='X'
    for i in range(3):
        for j in range(3):
             print(end="___")
             print(a[i][j],end='')
             print(end="___")
             print(end="|")
        print()
    i,j=t,s
    W=get1(a,i,j,count)
    if W==1:
        return 'P1 Wins'
    count=count+1
    if count==9:
        return None
    cal=0
    if Senthil=='p2':
        cal=True
    if cal:
        print("please enter the choice for the position(p2):")
    else:
        print("please enter the choice for the position(p2):")
    f=int(input())
    for i,j in d.items():
        if i==f:
            t=int(j[0])
            s=int(j[1])
    i,j=t,s
    a[i][j]='O'
    for i in range(3):
        for j in range(3):
             print(end="___")
             print(a[i][j],end='')
             print(end="___")
             print(end="|")
        print()
    i,j=t,s
    W=get1(a,i,j,count)
    if W==1:
        return 'P2 Wins'
    count+=1
    if count<=8:
        return get(a,Muthu,Senthil,count)
#Main Function
a=[]
k=1
for _ in range(3):
    b=[]
    for _ in range(3):
        b.append(k)
        k=k+1
    a.append(b)
for i in range(3):
    for j in range(3):
        print(end="___")
        print(a[i][j],end='')
        print(end="___")
        print(end="|")
    print()
z=['head','tail']
c=random.choice(z)
print(c)
if c=='head':
    Muthu='p1'
else:
    Muthu='p2'
if Muthu=='p1':
    Senthil='p2'
else:
    Senthil='p1'
count=0
k=get(a,Muthu,Senthil,count)
if k!=None:
    print(k)
else:
    print('Draw')
    
