import unittest
from functions.get_files_info import get_files_info

class TestFunctions(unittest.TestCase):
  def test_calculator_curent_dir(self):
    expected_files = ["pkg", "main.py", "tests.py"]
    test_results = {}
    print("Result from current directory:")
    lines = self.get_files_info_lines("calculator", ".")
    for l in lines:
      print(l)

  def get_files_info_lines(self, working_directory, directory="."):
    return list(get_files_info(working_directory, directory)
                .split("\n"))

if __name__ == "__main__":
  unittest.main()