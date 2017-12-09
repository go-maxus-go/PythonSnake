import unittest

from src.field import *

class TestField(unittest.TestCase):

    def setUp(self):
        self.field = Field(10, 20)
        self.customField = Field(4, 3,
                                 [1, 1, 1, 1,
                                  1, 0, 0, 1,
                                  1, 1, 1, 1])

    def test_width(self):
        self.assertEqual(self.field.width(), 10)

    def test_height(self):
        self.assertEqual(self.field.height(), 20)

    def test_data(self):
        for x in range(self.field.width() - 1):
            for y in range(self.field.height() - 1):
                self.assertEqual(self.field.cell(x, y), CellType.Empty)

    def test_customData(self):
        self.assertEqual(self.customField.cell(0, 0), CellType.Wall)
        self.assertEqual(self.customField.cell(1, 0), CellType.Wall)
        self.assertEqual(self.customField.cell(2, 0), CellType.Wall)
        self.assertEqual(self.customField.cell(3, 0), CellType.Wall)

        self.assertEqual(self.customField.cell(0, 1), CellType.Wall)
        self.assertEqual(self.customField.cell(1, 1), CellType.Empty)
        self.assertEqual(self.customField.cell(2, 1), CellType.Empty)
        self.assertEqual(self.customField.cell(3, 1), CellType.Wall)

        self.assertEqual(self.customField.cell(0, 2), CellType.Wall)
        self.assertEqual(self.customField.cell(1, 2), CellType.Wall)
        self.assertEqual(self.customField.cell(2, 2), CellType.Wall)
        self.assertEqual(self.customField.cell(3, 2), CellType.Wall)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestField))
    return suite

if __name__ == '__main__':
    unittest.main()
