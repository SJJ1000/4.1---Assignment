# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.


'''
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

'''




datastore = { "medical":[
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }

      ]
}


outfile = open('retail_space.csv', 'w')
outfile.write('room-number,use,sq-ft,price\n')

list_of_office = datastore['medical']

#for office in list_of_office:
 #   roomno = office['room-number']
  #  use = office['use']
   # sqft = office['sq-ft']
    #price = office['price']

    #outfile.write(str(roomno)+','+ use + ',' + str(sqft) + ',' + str(price) + '\n')


for office in datastore['medical']:
    outfile.write(str(office['room-number'])+','+ office['use'] + ',' + str(office['sq-ft']) + ',' + str(office['price']) + '\n')

outfile.close()

import pickle

pickle_file = open("datastore.dat","wb")
pickle.dump(datastore,pickle_file)




    
    #print(type(office))
    #print(office)
