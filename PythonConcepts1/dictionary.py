# dictionary = a changeable(mutable), unordered collection of unique key:value pairs
#              fast beacuase they use hashoing and allows us to access a value quickly

capitals ={'USA': 'Washington',
           'India': 'New Delhi',
           'China': 'Beijing',
           'Russia': 'Moscow'}

capitals.update({'Germany,': 'Berlin'})
capitals.update({'USA': 'Las Vegas',})
capitals.pop('China')
capitals.clear()
#print(capitals['Russia'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
#for key, value in capitals.items():
#    print(key, value)