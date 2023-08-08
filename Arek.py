for i in range(1,20):
    dziel = 0
    for j in range(1,20):
        if i%j == 0:
            dziel+=1
    if dziel==2:
        print(i)