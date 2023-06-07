import unittest
import pathlib as pl

class TestCase(unittest.TestCase):
    def test_fileexist(self):
        # ...
        path = pl.Path("C:\\Users\\Alimu\\Desktop\\de_proj\\2023-amse-23150759-\\project\\data\\Munich_VR_&_BS.sqlite")
        self.assertTrue(path.is_file())
        self.assertTrue(path.parent.is_dir())

if __name__ == "__main__":
    unittest.main(verbosity=2)

    