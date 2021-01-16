import unittest


class Test(unittest.TestCase):
    def testName(self):
        list = {"python", "selenium", "java"}
        self.assertIn("python", list)  # passed
        # self.assertIn("ruby", list)    # failed

        # assert not in
        self.assertNotIn('ruby', list)  # passed
        # self.assertNotIn('python', list)  # failed


if __name__ == '__main__':
    unittest.main
