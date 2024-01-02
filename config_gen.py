# Jinja Configurator Example with CSV input
import csv
from jinja2 import Environment, FileSystemLoader



with open('config_variables.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    routers = [row for row in csv_reader]


# Open CSV for reading 
#file = open('config_variables.csv')
#csvreader = csv.DictReader(file)



# Extract CSV header
# header = []
# header = next(csvreader) 

# Extract Router Records 
# routers = []
# for router in csvreader:
#     routers.append(router) 


# Close CSV
# file.close()


print(routers)

max_score = 100
test_name = "Python Challenge"
students = [
	{"name": "Sandrine", "score": 100},
	{"name": "Gergeley", "score": 87},
	{"name": "Frieda", "score": 92},
]

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("config")

for router in routers:
    filename = f"configs/config_{router['Hostname'].lower()}.txt"
    content = template.render(
        router,
        Hostname=router['Hostname'].lower(),
        IP=router['IP']
    )
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")
