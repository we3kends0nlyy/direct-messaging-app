import unittest
import ds_client


class TestClient(unittest.TestCase):
 
    def test_true(self):
        #self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "hehe", "julianapa", "bio"), True)
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "julianapa", "1234", "new"), True)
        #self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "julianapa", "1234", "all"), True)
if __name__ == '__main__':
    unittest.main()
