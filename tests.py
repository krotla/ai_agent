import unittest
from functions.get_files_info import get_files_info


class TestAiAgent(unittest.TestCase):
    # def setUp(self):
    #     self.calculator = Calculator()

    def test_get_files_info(self):
        result = get_files_info("calculator", ".")
        print("Result for current directory")
        print(result)
        
        result = get_files_info("calculator", "pkg")
        print("Result for 'pkg'' directory")
        print(result)

        result = get_files_info("calculator", "/bin")
        print("Result for '/bin' directory")
        print(result)

        result = get_files_info("calculator", "../")
        print("Result for '../' directory")
        print(result)

if __name__ == "__main__":
    unittest.main()