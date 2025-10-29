import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

class TestFunctions(unittest.TestCase):
  def test_calculator_main_file(self):
    print("\nResult from main file:")
    contents = get_file_content("calculator", "main.py")
    print(contents)

  def test_calculator_pkg_calculator_file(self):
    print("\nResult from pkg/calculator file:")
    contents = get_file_content("calculator", "pkg/calculator.py")
    print(contents)

  def test_bin_cat_file(self):
    print("\nResult from /bin/cat file:")
    contents = get_file_content("calculator", "/bin/cat")
    print(contents)

  def test_calculator_pkg_does_not_exist_file(self):
    print("\nResult from pkg/does_not_exist.py file:")
    contents = get_file_content("calculator", "pkg/does_not_exist.py")
    print(contents)

if __name__ == "__main__":
  unittest.main()