
#Knn ALgo pour déterminer le revenu d'une personne en fonction 
#des similarités avec une autre personne

from math import sqrt, pow

dataset = {
			'revenue': [300000, 
				        500000,
				        1000000,
				        700000,
				        200000,
				        1500000,
				        750000,
						250000],
			'age': [ 26, 
			        30,
			        35,
			        25,
			        50,
			        45,
			        60,
					27],
			'nb_enf': [1, 
				        0,
				        4,
				        2,
				        8,
				        3,
				        4,
				0],
			'impot':[25000, 
				        30000,
				        50000,
				        5000,
				        60000,
				        48000,
				        10000,
				50000],

			}

#first = [dataset[x][0] for x in dataset]
#print(first)
def similarity(a, b):
	return sqrt(pow((a[0] - b[0]),2) + 
				pow((a[1] - b[1]),2) +
				pow((a[2] - b[2]),2))


def choice(*args):
	return str(sum(args[0])/len(args[0]))


def knn(k, dataset, to_predict):
	sim = []
	for i in range(len(dataset['revenue'])):
		compt = [dataset['revenue'][i],
				 dataset['age'][i],
				 dataset['nb_enf'][i]
				 ]
		s = similarity(to_predict, compt)
		sim.append((i,s))

	sim = sorted(sim, key=lambda x:x[1])[:k]
	print('Voici La semilarité')
	print(sim)
	impot = [dataset['impot'][v[0]] for v in sim]
	print(impot)
	return choice(impot)

revenue = float(input("Donnez le revenue: "))
age = int(input("Donnez l'age: "))
nbr_enf = int(input("Donnez le nombre d'enfant: "))

persone = [revenue, age, nbr_enf]
impot = knn(2, dataset, persone)
print(f"L'impot pour cette personne est {impot}")