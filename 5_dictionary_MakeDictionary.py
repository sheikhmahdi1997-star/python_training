#3
symbol=",.;:!?"
text= input("Enter a sentence:")
for i in symbol:
    text=text.replace(i ," ")

text=text.lower().split()


dic_count={}

for t in text:
    count=text.count(t)
    dic_count[t]=count
    

print(dic_count)