class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)
        if person.get("wife"):
            new_person.wife = person["wife"]
        if person.get("husband"):
            new_person.husband = person["husband"]

    return person_list
