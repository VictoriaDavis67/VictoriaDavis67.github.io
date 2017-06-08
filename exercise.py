#greeting = input("Hello, possible pirate! What's the password? ")
#if greeting in ["Arrr!"]:
	#print("Go away, pirate.")
#else:
    #print("Greetings, hater of pirates!")

#authors = {
    #"Charles Dickens": "1870",
    #"William Thackeray": "1863",
    #"Anthony Trollope": "1882",
    #"Gerard Manley Hopkins": "1889"
#}
#for author, date in authors.items():
    #print(author + " died in " + date)

#year = int(input("Greetings! What is your year of origin? "))

#if year <= 1900:
    #print('Woah, that is the past!')
#elif year > 1900 and year < 2020:
    #print("That is totally the present!")
#else:
    #print("Far out, that's the future!!")

#sentence = "The quick brown fox jumped over the lazy dogs"
#longest = ""

#words = sentence.split()

#for word in words:
    #if len(word) > len(longest):
        #longest = word

#print("The word '" + longest + "' is ", len(longest), " characters long.")

years = (100)
population = [0,10]
for i in range(years):
    population.append(population[-1] + population[-2])
print(population)
