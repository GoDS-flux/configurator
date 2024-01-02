# Jinja Configurator Example with CSV input
import csv
from jinja2 import Environment, FileSystemLoader

# Open CSV and read the contents into routers
with open('config_variables.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    routers = [row for row in csv_reader]

# Test the contents of routers
print(routers)

# Template replacement 
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("config")

for router in routers:
    filename = f"configs/{router['Hostname'].lower()}.config"
    content = template.render(
        router,
        Hostname=router['Hostname'].lower(),
        IP=router['IP']
    )
    with open(filename, mode="w", encoding="utf-8") as config:
        config.write(content)
        print(f"wrote config for " + router['Hostname'])
