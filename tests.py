import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


class TestAiAgent(unittest.TestCase):
    # def setUp(self):
    #     self.calculator = Calculator()

    def test_get_files_info(self):
        # Folder checking tests
        #----------------------

        # result = get_files_info("calculator", ".")
        # print("Result for current directory")
        # print(result)
        
        # result = get_files_info("calculator", "pkg")
        # print("Result for 'pkg'' directory")
        # print(result)

        # result = get_files_info("calculator", "/bin")
        # print("Result for '/bin' directory")
        # print(result)

        # result = get_files_info("calculator", "../")
        # print("Result for '../' directory")
        # print(result)

        # Read file tests
        #----------------

        # result = get_file_content("calculator", "lorem.txt")
        # print("Result for 'lorem.txt' 20000 chars text")
        # print(result)
        # print(f'Length of result: {len(result)}')

        # result = get_file_content("calculator", "main.py")
        # print("Result for 'main.py' file")
        # print(result)
        # print(f'Length of result: {len(result)}')

        # result = get_file_content("calculator", "pkg/calculator.py")
        # print("Result for 'pkg/calculator.py' file")
        # print(result)
        # print(f'Length of result: {len(result)}')
        
        # result = get_file_content("calculator", "/bin/cat")
        # print("Result for '/bin/cat' file")
        # print(result)
        # print(f'Length of result: {len(result)}')
        
        # result = get_file_content("calculator", "pkg/does_not_exist.py")
        # print("Result for not existing file")
        # print(result)
        # print(f'Length of result: {len(result)}')

        # Write tests
        #------------

        # result = write_file("calculator", "ole/ale/text.txt", "directory path was created")
        # print("Result for writing to 'ole/ale/text.txt' file")
        # print(result)

        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print("Result for writing to 'lorem.txt' file")
        print(result)
        
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print("Result for writing to 'pkg/morelorem.tx' file")
        print(result)
        
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print("Result for writing to not existing file")
        print(result)
        

if __name__ == "__main__":
    unittest.main()