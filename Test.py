import unittest
from decimal import Decimal
from Cash_Machine_Prj import CashMachine

class CashMachineTestCase(unittest.TestCase):
    def test_load_coins(self):
        cash_machine = CashMachine()

        cash_machine.load_coins(10, Decimal("0.2"))
        self.assertEqual(cash_machine.coins[Decimal("0.2")], 10)
        cash_machine.load_coins(5, Decimal("0.5"))
        self.assertEqual(cash_machine.coins[Decimal("0.5")], 5)
        cash_machine.load_coins(3, 1)
        self.assertEqual(cash_machine.coins[1], 3)
        cash_machine.load_coins(2, 2)
        self.assertEqual(cash_machine.coins[2], 2)

    def test_exchange(self):
        cash_machine = CashMachine()

        cash_machine.coins[Decimal("0.2")] = 5
        cash_machine.coins[Decimal("0.5")] = 10
        cash_machine.coins[1] = 3
        cash_machine.coins[2] = 2

        result = cash_machine.exchange(Decimal("1"))

        self.assertEqual(result, [Decimal("0.2"), Decimal("0.2"), Decimal("0.2"), Decimal("0.2"), Decimal("0.2")])
        self.assertEqual(cash_machine.coins[Decimal("0.2")], 0)
        self.assertEqual(cash_machine.coins[Decimal("0.5")], 10)
        self.assertEqual(cash_machine.coins[1], 3)
        self.assertEqual(cash_machine.coins[2], 2)
        
    def test_print_machine_status(self):
        cash_machine = CashMachine()

        cash_machine.coins[Decimal("0.2")] = 5
        cash_machine.coins[Decimal("0.5")] = 10
        cash_machine.coins[1] = 3
        cash_machine.coins[2] = 2
        notes = {5: 2, 10: 3, 20: 1}

        result = cash_machine.print_machine_status(notes)
        expected_result = "5 0.2£, 10 0.5£, 3 1£, 2 2£, 2 5£, 3 10£, 1 20£"
        self.assertEqual(result, expected_result)
        

if __name__ == "__main__":
    unittest.main()


