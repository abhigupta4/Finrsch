import nltk

the_list = []

data = open("Caterpillar.txt","r")

sentences = nltk.sent_tokenize(data.read())

out = []

def find_sentences(the_list):
	for sent in sentences:
		for ele in the_list:
			if ele in sent:
				out.append(sent)

	return out