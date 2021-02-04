# Author: Adam Jeffries
# Date: 2/3/2021
# Description: Contains a class named NeighborhoodPets that has methods for adding a pet, deleting a pet,
# searching for the owner of a pet, saving data to a JSON file, loading data from a JSON file,
# and getting a set of all pet species.

import json


class NeighborhoodPets:

    def __init__(self):
        self.pets = []

    def get_pets(self):
        return self.pets

    def add_pet(self, name, species, owner):
        pet_exists = False
        for pet in self.pets:
            if pet[0].lower() == name.lower():
                pet_exists = True
        if not pet_exists:
            self.pets.append([name, species, owner])

    def delete_pet(self, name):
        for pet in self.pets:
            if pet[0] == name:
                self.pets.remove(pet)

    def get_owner(self, name):
        for pet in self.pets:
            if pet[0] == name:
                return pet[2]

    def save_as_json(self, name_of_file):
        json_file = open(name_of_file, 'w')
        json.dumps(self.pets)
        content = '{"pets":['
        for pet in self.pets:
            chunk = '"name":"{}","species":"{}","owner":"{}"'.format(pet[0], pet[1], pet[2])
            chunk = '{' + chunk + '},'
            content += chunk
        content = content[:-1]
        content += ']}'
        json_file.write(content)
        json_file.close()

    def read_json(self, name_of_file):
        with open(name_of_file, 'r') as infile:
            restored_list = json.load(infile)
        new_pets_list = []
        for pet in restored_list['pets']:
            new_pets_list.append([pet['name'], pet['species'], pet['owner']])
        self.pets = new_pets_list

    def get_all_species(self):
        species = []
        for pet in self.pets:
            species.append(pet[1])
        return species
