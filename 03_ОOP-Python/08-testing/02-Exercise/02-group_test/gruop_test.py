from group import Group, Person

import unittest


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.person1 = Person("Elon", "Musk")
        self.person2 = Person("John", "Wick")

    def test_person_have_name_surname(self):
        self.assertEqual((self.person1.name, self.person1.surname), ("Elon", "Musk"))

    def test_if_person_can_add_person(self):
        person3 = self.person1 + self.person2
        self.assertEqual((person3.name, person3.surname), ("Elon", "Wick"))



class TestGroup(unittest.TestCase):
    def setUp(self) -> None:
        self.person1 = Person("Elon", "Musk")
        self.person2 = Person("John", "Wick")
        self.person3 = Person("Ivan", "Petrov")
        self.person4 = Person("Aleksii", "Ivanovich")

        self.group1 = Group("Epic", [self.person1, self.person2])
        self.group2 = Group("Mega", [self.person3, self.person4])

    def test_groups_have_list_of_people(self):
        self.assertEqual((self.group1.name, self.group1.people), ("Epic", [self.person1, self.person2]))

    def test_can_two_groups_add_their_people_in_one_list(self):
        group3 = self.group1 + self.group2
        self.assertEqual(len(group3), 4)
        self.assertEqual((group3.name, group3.people),
                         (self.group1.name, [self.person1, self.person2, self.person3, self.person4]))


    def test_group_len_is_working(self):
        self.assertEqual(len(self.group1), 2)

    def test_str_returned_correctly(self):
        self.assertEqual(str(self.group1), "Group Epic with members Elon Musk, John Wick")

    def test_group_returning_details_when_indexed(self):
        self.assertEqual(self.group1[0], "Person 0: Elon Musk")
        self.assertEqual(self.group1[1], "Person 1: John Wick")

    def test_interpretation_should_return_info_for_people(self):
        self.assertEqual(list(self.group1), ["Person 0: Elon Musk", "Person 1: John Wick"])


if __name__ == "__main__":
    unittest.main()
