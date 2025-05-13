
class Pet:
    """Represents a pet with a name, type, and optional owner."""
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Stores all instances of Pet

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {self.PET_TYPES}.")
        
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Invalid owner. Must be an instance of the Owner class.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)

    pass

class Owner:
    """Represents a pet owner."""
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Returns a list of all pets owned by this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assigns an owner to a pet if the pet is a valid Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet. Must be an instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        """Returns a sorted list of pets owned by this owner, sorted by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)


    pass