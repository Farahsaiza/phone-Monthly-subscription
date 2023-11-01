def totalcost(D):
    tab=[]
    if D>120:
         A1=(D-120)*0.5
         tab.append(A1)

    else:
         tab.append(100)
    if D>60:
         A2=(D-60)
         tab.append(A2)
    else:
         tab.append(50)
    if D>30:     
         A3=(D-30)*1.5
         tab.append(A3)
    else:
         tab.append(20)
              
    A4=D*2
    tab.append(A4)
    
    return tab


D=int(input("enter your duration communication of the month in minutes: "))

print("if you had the 200 dh subscription the calls are unlimited all month")

print("if you don't,here are the costs total to pay at the end of the month if you pay the subscription  of100 DH,50 DH,20 DH and 0 DH")

print(totalcost(D))

tab1=totalcost(D)
u=0

for  i in range (4):
     for j in range(i+1,4):
          if tab1[j]<tab1[i]:
               min=tab1[j]
               u=i

tab2=[100,50,20,0]



print("the most interesting subscription and the lowest cost for you based on your communication duration in a month is: ",tab2[u],"DH")
