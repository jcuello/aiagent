import unittest
from functions.write_file import write_file
from functions.run_python_file import run_python_file

class TestFunctions(unittest.TestCase):
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