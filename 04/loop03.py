test1 = [90,92,76,86,67]
test2 = [x for x in test1 if x >= 80]
print(test2)

test2=[]
for score in test1:
    if score >= 80:
        test2.append(score)

print(test2)