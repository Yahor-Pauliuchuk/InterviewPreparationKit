import sys
sys.path.append("D:\\Education\\Python\\InterviewPreparationKit\\WarmUpChallenges")
# hate this garbage ridiculous hard code, but relative paths aren't working...
import SalesByMatch
import unittest

class SalesByMatchTests(unittest.TestCase):
    def test_WhenArgsAreProvided_ThenResultIsAsExpected(self):
        # Arrange
        testCases = [
            ([1], 0),
            ([1, 1], 1),
            ([1, 2], 0),
            ([10, 20, 10], 1),
            ([30, 30, 30, 30], 2),
            ([10, 20, 30, 40], 0),
            ([10, 20, 20, 10, 10, 30, 50, 10, 20], 3)
        ]
        instance = SalesByMatch.SalesByMatch()

        for testCase in testCases:
            expectedResult = testCase[1]
            # Act
            actualResult = instance.sockMerchant(testCase[0])

            # Assert
            self.assertEqual(expectedResult, actualResult)

if __name__ == '__main__':
    unittest.main()