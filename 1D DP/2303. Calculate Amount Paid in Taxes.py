from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        s = 0
        last_amount = 0
        for amount, per in brackets:
            go = True
            if income < amount:
                podstawa_opodatkowania = income - last_amount
                go = False
            else:
                podstawa_opodatkowania = amount - last_amount
            s += ( podstawa_opodatkowania * per ) / 100
            if not go:
                break
            last_amount = amount
        return s