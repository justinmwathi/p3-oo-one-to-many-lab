class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    def __init__(self,name,pet_type,owner=None):
        self.name=name
        self.pet_type=pet_type
        self.owner=owner
        Pet.append_pets(self)

        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of: {', '.join(self.PET_TYPES)}")
    @classmethod
    def append_pets(cls,pet):
        cls.all.append(pet)

class Owner:
    def __init__(self,name):
        self.name=name
        self.pets_list=[]
        
    def pets(self):
        return[owner for owner in Pet.all]
    
    def add_pet(self,pet):
        if not isinstance(pet,Pet):
            raise TypeError("Pet must be an instance of Pet")
        self.pets_list.append(pet)
        pet.owner=self


    def get_sorted_pets(self):

        return sorted([owner for owner in Pet.all], key=lambda pet: pet.name)
    