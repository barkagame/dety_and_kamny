countc1=10
countc2=44
temp=44
result=44
isProccessing=True
while(isProccessing):
    for i in range(0,2):
        temp = countc2
        for j in range(0,2):
            if i==0:
                if temp %2 !=0:
                    temp=temp-1
                temp=temp//2

            if i==1:

                temp=temp-1
            if j==0:
                if temp %2 !=0:
                    temp=temp-1
                temp= temp//2
            if j==1:
                temp=temp-1
            if temp+countc1<=20:
                result=countc2
                isProccessing=False
                break
            else:
                temp=countc2
        if isProccessing==False:
            break
    countc2-=1
print(result)
