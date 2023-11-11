import unittest
from math_quiz import Generate_Random_Integer, Generate_Random_Operator, Make_Problem_Answer


class TestMathGame(unittest. TestCase):
    def test_Generate_Random_Integer (self):
        #Test if random numbers generated are within the specified range
        min_value = 1
        max_value = 10
        for _ in range(1000): # Test a large number of random values
            random_number = Generate_Random_Integer(min_value, max_value)
            self.assertTrue(min_value <=random_number <=max_value)

    def test_Generate_Random_Operator (self):
        for _ in range(1000):
            random_operator = Generate_Random_Operator ()
            Operators_List = ['+','-','*']
            self.assertTrue(random_operator in Operators_List)
        pass


    def test_Make_Problem_Answer(self):
        test_cases = [
            (5, 2, '+','5 + 2', 7),
            (60, 9, '+','60 + 9', 69),
            (210, 2,'*','210 * 2', 420),
            (9, 10,'-','9 - 10', -1),
            (52, 80,'-',52-80, - 28)]
        for number1, number2, operator, expected_problem, expected_answer in test_cases:
            Problem, Answer = Make_Problem_Answer(number1, number2, operator)
            self.assertTrue(Problem , expected_problem)
            self.assertTrue(Answer, expected_answer)
        pass

if __name__ == "__main__":
    unittest.main()
