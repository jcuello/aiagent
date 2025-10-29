import unittest
from functions.write_file import write_file

class TestFunctions(unittest.TestCase):
  def test_write_lorem_txt(self):
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

  def test_write_more_lorem_txt(self):
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
  
  def test_write_to_tmp_dir_failure(self):
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

if __name__ == "__main__":
  unittest.main()