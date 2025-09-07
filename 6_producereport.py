'''
We have a dictionary of produce with their per unit cost, the number of units sold and the total. We want to verify that the total is accurate
since it was manually entered. Print out the details of any produce that has in inaccurate total. Print both the stated total from the dictionary
as well as the calculated total that shows the discrepancy.
'''

ProduceDictionary={ 
    'Potatoes': {
        'cost': 0.86,
        'amt_sold': 39.8,
        'total': 34.23
    },
    'Okra': {
        'cost': 2.26,
        'amt_sold': 6.4,
        'total': 14.46
    },
    'Fava beans': {
        'cost': 2.69,
        'amt_sold': 5.2,
        'total': 13.99
    },
    'Watermelon': {
        'cost': 0.66,
        'amt_sold': 39.5,
        'total': 26.07
    },
    'Garlic': {
        'cost': 1.19,
        'amt_sold': 25.8,
        'total': 30.7
    },
    'Parsnips': {
        'cost': 2.27,
        'amt_sold': 28.1,
        'total': 63.79
    },
    'Asparagus': {
        'cost': 2.49,
        'amt_sold': 23.2,
        'total': 57.77
    },
    'Avocados': {
        'cost': 3.23,
        'amt_sold': 2.0,
        'total': 6.46
    },
    'Celery': {
        'cost': 3.07,
        'amt_sold': 18.5,
        'total': 56.79
    },
    'Spinach': {
        'cost': 4.12,
        'amt_sold': 4.9,
        'total': 20.19
    },
    'Cucumber': {
        'cost': 1.07,
        'amt_sold': 4.5,
        'total': 6.75
    },
    'Apricots': {
        'cost': 3.71,
        'amt_sold': 17.6,
        'total': 65.3
    },
    'Ginger': {
        'cost': 5.13,
        'amt_sold': 20.2,
        'total': 103.63
    },
    'Corn': {
        'cost': 1.07,
        'amt_sold': 38.1,
        'total': 40.77
    },
    'Grapefruit': {
        'cost': 0.76,
        'amt_sold': 13.5,
        'total': 10.26
    },
    'Eggplant': {
        'cost': 2.32,
        'amt_sold': 15.0,
        'total': 34.8
    },
    'Green cabbage': {
        'cost': 0.8,
        'amt_sold': 31.8,
        'total': 25.49
    },
    'Yellow peppers': {
        'cost': 2.87,
        'amt_sold': 26.9,
        'total': 77.2
    },
    'Grapes': {
        'cost': 2.63,
        'amt_sold': 36.2,
        'total': 95.21
    },
    'Cherries': {
        'cost': 9.5,
        'amt_sold': 28.6,
        'total': 271.7
    },
    'Apples': {
        'cost': 1.88,
        'amt_sold': 1.2,
        'total': 2.26
    },
    'Green beans': {
        'cost': 2.52,
        'amt_sold': 34.0,
        'total': 85.68
    },
    'Tomatoes': {
        'cost': 3.16,
        'amt_sold': 9.7,
        'total': 30.65
    },
    'Red onion': {
        'cost': 0.78,
        'amt_sold': 39.3,
        'total': 31.25
    },
    'Strawberries': {
        'cost': 4.4,
        'amt_sold': 1.1,
        'total': 4.84
    },
    'Papaya': {
        'cost': 1.34,
        'amt_sold': 23.3,
        'total': 31.22
    },
    'Butternut squash': {
        'cost': 1.28,
        'amt_sold': 36.6,
        'total': 46.85
    },
    'Bananas': {
        'cost': 0.86,
        'amt_sold': 26.1,
        'total': 17.65
    },
    'Lettuce': {
        'cost': 1.88,
        'amt_sold': 25.0,
        'total': 47.0
    },
    'Carrots': {
        'cost': 1.26,
        'amt_sold': 37.1,
        'total': 46.75
    },
    'Daikon': {
        'cost': 1.4,
        'amt_sold': 1.8,
        'total': 2.52
    },
    'Lime': {
        'cost': 1.06,
        'amt_sold': 5.2,
        'total': 5.51
    },
    'Green peppers': {
        'cost': 1.89,
        'amt_sold': 5.3,
        'total': 10.02
    },
    'Beets': {
        'cost': 1.51,
        'amt_sold': 5.7,
        'total': 8.61
    },
    'Coconuts': {
        'cost': 1.18,
        'amt_sold': 4.2,
        'total': 4.96
    },
    'Orange': {
        'cost': 1.09,
        'amt_sold': 28.6,
        'total': 31.17
    },
    'Lemon': {
        'cost': 1.29,
        'amt_sold': 5.5,
        'total': 7.1
    },
    'Brussels sprouts': {
        'cost': 1.65,
        'amt_sold': 22.9,
        'total': 37.78
    },
    'Kale': {
        'cost': 5.02,
        'amt_sold': 16.8,
        'total': 84.34
    },
    'Bok choy': {
        'cost': 1.42,
        'amt_sold': 15.4,
        'total': 21.87
    }
    
}


#method 1
for produce in ProduceDictionary:
    cost = ProduceDictionary[produce]['cost']
    amt_sold = ProduceDictionary[produce]['amt_sold']
    stated_total = ProduceDictionary[produce]['total']

    calc_total = round((cost * amt_sold), 2)

    if stated_total != calc_total:
        print(f"Produce NAme: {produce}")
        print(f"Calc total: ${calc_total:.2f}")
        print(f"Stated total: ${stated_total:.2f}")
        print()
        print()
#method 2

for produce, details in ProduceDictionary.items():
    cost = details['cost']
    amt_sold = details['amt_sold']
    stated_total = details['total']

    calc_total = round((cost * amt_sold), 2)

    if stated_total != calc_total:
        print(f"Produce NAme: {produce}")
        print(f"Calc total: ${calc_total:.2f}")
        print(f"Stated total: ${stated_total:.2f}")
        print()
        print()