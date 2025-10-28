import unittest
from functions.get_files_info import get_files_info

class TestFunctions(unittest.TestCase):
  def test_calculator_curent_dir(self):
    print("\nResult from current directory:")
    lines = self.get_files_info_lines("calculator", ".")
    for l in lines:
      print(l)

  def test_pkg_dir(self):
    print("\nResult for 'pkg' directory:")
    lines = self.get_files_info_lines("calculator", "pkg")
    for l in lines:
      print(l)

  def test_bin_dir(self):
    print("\nResult for '/bin' directory:")
    lines = self.get_files_info_lines("calculator", "/bin")
    for l in lines:
      print(l) 

  def test_previous_dir(self):
    print("\nResult for '../' directory:")
    lines = self.get_files_info_lines("calculator", "../")
    for l in lines:
      print(l) 

  def get_files_info_lines(self, working_directory, directory="."):
    lines = get_files_info(working_directory, directory).split("\n")
    return list(filter(lambda x: not x.startswith("- __pycache__"), lines))

if __name__ == "__main__":
  unittest.main()