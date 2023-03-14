import unittest
import ds_client


class TestClient(unittest.TestCase):
 
    #def test_message(self):
        #self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "hehe", "julianapa", "bio"), True)

    def test_new_true(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "hehe", "julianapa", "bio"), True)
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "julianapa", "1234", "new"), True)
    def test_new_false(self):
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "julianapa", "1234", "new"), False)
    
    def test_all(self):
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "julianapa", "1234", "all"), True)
    
    def test_invalid_request(self):
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "julianapa", "1234", "alll"), False)
    
    def test_invalid_user(self):
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "julia", "1234", "alll"), False)
        
    def test_bio_only(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "JLKhjkjhSKJ", "123", None, None, "1jlakjds"), True)

if __name__ == '__main__':
    unittest.main()
