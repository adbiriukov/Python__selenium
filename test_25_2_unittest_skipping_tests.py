import unittest


class Apptesting(unittest.TestCase):
    # sKIP TEST
    @unittest.SkipTest  # Decorator
    def test_1(self):
        print("This is test 1")
    # SKIP TEST WITH REASON
    # it show that run in total but specif that skipped

    @unittest.skip("I am skipping this test method because this is not ready")
    def test_2(self):
        print("This is test 2")

    # sKIP TEST WITH BASED ON CONDITION
    @unittest.skipIf(1 == 1, "1==1, IF NOT TRUE THEN NOT SKIPPED")
    def test_3(self):
        print("This is test 3")

    def test_4(self):
        print("This is test 4")

    def test_5(self):
        print("This is test 5")

    def test_6(self):
        print("This is test 6")


if __name__ == '__main__':
    unittest.main
