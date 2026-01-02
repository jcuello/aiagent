import unittest
from functions.write_file import write_file
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file

class TestFunctions(unittest.TestCase):
  def test_get_files_info_in_pkg(self):
    print(get_files_info("calculator", "pkg"))
    
  def test_get_file_content(self):
    print(get_file_content("calculator", "lorem.txt"))

  def test_write_file(self):
    print(write_file("calculator", "test.txt", "Succesfully wrote to file!"))

  def test_run_python_calculator_main(self):
    print(run_python_file("calculator", "main.py"))

  def test_run_python_calculator_main_with_args(self):
    print(run_python_file("calculator", "main.py",["3 + 5"]))

  def test_run_python_calculator_test_file(self):
    print(run_python_file("calculator", "tests.py"))

  # Should return errors
  def test_run_python_calculator_with_forbidden_path(self):
    print(run_python_file("calculator", "../main.py"))

  def test_run_python_calculator_with_nonexistent_file(self):
    print(run_python_file("calculator", "nonexistent.py"))

  def test_run_python_calculator_with_invalid_text_file(self):
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
  unittest.main()