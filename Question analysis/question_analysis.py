import nltk
from clean_extract import find_sentences

ques = ["What is the company business", "What are the company business segments","What are the recent acquisitions?"]

# for ele in ques:
ele = ques[2]
lis = []
temp = nltk.pos_tag(nltk.word_tokenize(ele)) 
pos = 0
for i in range(len(temp)):
	if 'VB' in temp[i][1]:
		pos = i
		break

for i in range(pos+1,len(temp)):
	if 'NN' in temp[i][1]:
		if i != len(temp)-1 and 'NN' in temp[i+1][1]:
			lis.append(temp[i+1][0])
		else:
			lis.append(temp[i][0])
		break

ans = find_sentences(lis)
print("The question taken is")
print(ele)
print()
print("The_list is: " + str(lis))
print("Sentences found are") 
for se in ans:
	print(se)		
