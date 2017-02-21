#encoding=UTF-8
import Biaoge
import unittest
class BiaogeTest(unittest.TestCase):
    def setUp(self):
        self.bg = Biaoge.Biaoge()

    def tearDown(self):
        pass

    def testAdd(self):
        self.bg.set("表1", "exp1", "@10", 0.2)
        result ="""## 表1

|    |@10|
|--- |---|
|exp1|0.2|
"""
        self.assertEqual(self.bg.getMarkdown(), result)

    def testMulti(self):
        self.bg.setDesc("我的表1", "This is my first experiment.")
        self.bg.set("我的表1", "row0", "col0", "%.2f"%7.7)
        self.bg.set("我的表1", "row0", "col2", "interest")
        self.bg.set("我的表1", "row1", "col3", 6.00)
        self.bg.setDesc("表2", "This is my second experiment.")
        self.bg.set("表2", "r0", 'c0', 0.89746)
        self.bg.set("表2", "r2", 'c1', None)
        self.bg.set("表2", "r9", 'c7', 'a')
        self.bg.set("表2", "r0", 'c0', 0.777)
        result = """## 我的表1
This is my first experiment.
|    |col0|  col2  |col3|
|--- |--- |  ---   |--- |
|row0|7.70|interest| -  |
|row1| -  |   -    |6.0 |
## 表2
This is my second experiment.
|   | c0  | c1 |c7 |
|---| --- |--- |---|
|r0 |0.777| -  | - |
|r2 |  -  |None| - |
|r9 |  -  | -  | a |
"""
        self.assertEqual(self.bg.getMarkdown(), result)


if __name__ == '__main__':
    unittest.main()

