import pickle

infile = open("datastore.dat","rb")

datastore = pickle.load(infile)

print(type(datastore))

print(datastore)