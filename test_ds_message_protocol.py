# Julian Aparicio
# japaric4@uci.edu
# 74237345
import unittest
import ds_client
from ds_messenger import DirectMessage

class TestClient(unittest.TestCase):
    
    def test_new_message(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "JAJAJAJAJAJA", "Jandhiiiitest1", "bio"), True)

    def test_all(self):
        result = ds_client.send_2("168.235.86.101", 3021, "julianapa", "1234", "all")
        directmessage = DirectMessage()

    def test_invalid_request(self):
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "julianapa", "1234asa", "alll"), False)

    def test_invalid_user(self):
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "juli a", "1234", "alll"), False)
        
    
    def test_password_space(self):
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "sdfasdasd", "34 2", "asd"), False)
    
    def test_username_space(self):
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "kjh kjh", "34123", "asd"), False)
    
    def test_username_integer(self):
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, 1, "34123", "asd"), False)

    def test_bio_integer(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", None, 123), False)

    def test_user_lenzero(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "", None, 123), False)

    def test_new_true(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "hehe", "julianapa", "bio"), True)
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "julianapa", "1234", ""), False)

    def test_new_false(self):
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "12 3", "123", "new"), False)

    def test_rec_white_only(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "hehe", "  ", "bio"), False)

    def test_msg_white_only(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "  ", "julianapa", "bio"), False)
    
    def test_req_integer(self):
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "julianapa", "1234", 123), None)


    def test_mess_empty(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "  ", None, None), False)

    def test_notoken(self):
            self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "12312", "hehe", "julianapa", "bio"), False)

    def test_connect_error(self):
            self.assertEqual(ds_client.send("168.235.86.1", 3021, "123", "12312", "hehe", "julianapa", "bio"), False)

if __name__ == '__main__':
    unittest.main()
