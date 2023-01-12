import json

with open('friends_json.txt', 'r') as file:  # used context manager ie with
    file_contents = json.load(file)  # read file and turns it into a dictionary


print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

with open('cars_json.txt', 'w') as file:
    json.dump(cars, file)


json_list = []
csv_file = open('csv_file.txt', 'r')

for line in csv_file.readlines():
    club,city,country = line.strip().split(',')
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)

csv_file.close()
json_file = open('json_file.txt', 'w')
json.dump(json_list, json_file)
json_file.close()







