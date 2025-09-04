class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    pass


def create_person_list(people: list[Person]) -> list:
    result = []
    couples = {}

    for pep in people:
        person = Person(name=pep["name"], age=pep["age"])
        result.append(person)
        couples[person.name] = person

    for pep in people:
        if "wife" in pep and pep["wife"]:
            couples[pep["name"]].wife = couples.get(pep["wife"])
        if "husband" in pep and pep["husband"]:
            couples[pep["name"]].husband = couples.get(pep["husband"])

    return result
