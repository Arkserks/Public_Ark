class ClassCat:
    def __init__(self, name="", gender="", age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

    def init_from_dict(self, cat_catalog):
        self.name = cat_catalog.get("name")
        self.gender = cat_catalog.get("gender")
        self.age = cat_catalog.get("age")
