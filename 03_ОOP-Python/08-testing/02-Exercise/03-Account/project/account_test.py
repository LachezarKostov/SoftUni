from project.account import Account

import unittest


class AccountTest(unittest.TestCase):
    def setUp(self) -> None:
        self.acc1 = Account("Name1", 100)
        self.acc2 = Account("Name2")

    def test_if_acc_get_initializations(self):
        self.assertEqual((self.acc1.owner, self.acc1.amount), ("Name1", 100))

    def test_if_acc_get_initializations_when_by_deff(self):
        self.assertEqual((self.acc2.owner, self.acc2.amount), ("Name2", 0))

    def test_if_repr_returning_correct_string(self):
        self.assertEqual(repr(self.acc1), "Account(Name1, 100)")

    def test_if_str_returning_correct_string(self):
        self.assertEqual(str(self.acc1), 'Account of Name1 with starting amount: 100')

    def test_can_add_positive_transactions(self):
        self.acc1.add_transaction(100)
        self.assertEqual(self.acc1.balance, 200)

    def test_can_add_negative_transactions_result_grater_then_zero(self):
        self.acc1.add_transaction(-50)
        self.assertEqual(self.acc1.balance, 50)

    def test_can_add_negative_transactions_negative_result(self):
        self.acc1.add_transaction(-150)
        self.assertEqual(self.acc1.balance, -50)

    def test_count_len_be_zero_by_deff(self):
        self.assertEqual(len(self.acc1), 0)

    def test_transaction_increase_after_adding(self):
        self.acc1.add_transaction(10)
        self.acc1.add_transaction(10)
        self.assertEqual(len(self.acc1), 2)

    def test_adding_accepts_only_int(self):
        with self.assertRaises(ValueError) as context:
            self.acc1.add_transaction(1.1)

        self.assertIn("int", str(context.exception))

    def test_validate_transactions_return_new_amount(self):
        res = Account.validate_transaction(self.acc1, 10)
        self.assertEqual(self.acc1.balance, 110)

    def test_validate_negative_transactions_return_new_amount(self):
        with self.assertRaises(ValueError) as context:
            self.acc1.validate_transaction(self.acc1, -110)
        self.assertEqual("sorry cannot go in debt!", str(context.exception))
        self.assertEqual(self.acc1.balance, 100)

    def test_if_validate_transactions_return_str_when_positive_and_positive_trans(self):
        new_balance = Account.validate_transaction(self.acc1, 10)
        self.assertEqual(new_balance, "New balance: 110")

    def test_if_validate_transactions_return_str_when_positive_and_negative_trans(self):
        new_balance = Account.validate_transaction(self.acc1, -10)
        self.assertIn(new_balance, "New balance: 90")

    def test_can_we_add_two_accounts(self):
        added_acc = self.acc1 + self.acc2
        self.assertEqual(added_acc.balance, 100)
        self.assertEqual(added_acc.owner, "Name1&Name2")
        self.assertEqual(len(added_acc), 0)

    def test_grater_or_equal_on_acc(self):
        temp_bool = self.acc1 >= self.acc2
        self.assertEqual(temp_bool, True)

    def test_grater_on_acc(self):
        temp_bool = self.acc1 >= self.acc2
        self.assertEqual(temp_bool, True)

    def test_less_or_equal_on_acc(self):
        temp_bool = self.acc1 <= self.acc2
        self.assertEqual(temp_bool, False)

    def test_less_on_acc(self):
        temp_bool = self.acc1 < self.acc2
        self.assertEqual(temp_bool, False)

    def test_equal_on_acc(self):
        temp_bool = self.acc1 == self.acc2
        self.assertEqual(temp_bool, False)

    def test_do_transactions_reversed(self):
        self.acc2.add_transaction(1)
        self.acc2.add_transaction(2)
        self.acc2.add_transaction(3)

        new_acc = reversed(self.acc2)

        self.assertEqual(new_acc, [3, 2, 1])

    def test_do_getitem_from_transaction(self):
        self.acc2.add_transaction(1)
        self.acc2.add_transaction(2)
        self.acc2.add_transaction(3)

        item = self.acc2[1]

        self.assertEqual(item, 2)



if __name__ == "__main__":
    unittest.main()
