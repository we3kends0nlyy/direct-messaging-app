import unittest
import ds_client


class TestClient(unittest.TestCase):
 
    def test_true(self):
        #self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "YEAH EEE YEEEAAHHH", "julianapa", "bio"), True)
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "julianapa", "1234", "new"), True)
if __name__ == '__main__':
    unittest.main()
