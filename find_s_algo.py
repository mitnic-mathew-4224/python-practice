data = [
    ['green', 'hard', 'no', 'wrinkles', 'yes'],
    ['green', 'hard', 'yes', 'smooth', 'no'],
    ['brown', 'soft', 'no', 'wrinkled', 'no'],
    ['orange', 'hard', 'no', 'wrinkled', 'yes'],
    ['green', 'soft', 'yes', 'smooth', 'no'],
    ['green', 'hard', 'no', 'wrinkled', 'yes'],
    ['orange', 'hard', 'no', 'wrinkled', 'yes']
]


hypothesis=['^']*(len(data[0])-1)
for d in data:
    if d[-1]=='yes':
        hypothesis=d[:-1]
        break
for d in data:
    if d[-1]=='yes':
        for i in range(len(hypothesis)):
            if hypothesis[i]!=d[i]:
                hypothesis[i]='?'

print("Final Hypothesis:",hypothesis)


title=['color','toughness','fungus','apperance']
result=[]
val=True
for i in range(len(title)):
    str=input(f"{title[i]}: ").strip().lower()
    result.append(str)
for i in range(len(result)):
    if hypothesis[i]!='?':
        if(result[i]!=hypothesis[i]):
            val=False

if val:
    print("poisonous")
else:
    print("Not poisonous")