import unittest
import ds_client
from ds_messenger import DirectMessage

class TestClient(unittest.TestCase):
    
    def test_new_message(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "JAJAJAJAJAJA", "Jandhiiiitest1", "bio"), True)
        #self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "julianapa", "1234", "new"), True)

    def test_all(self):
        #self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "julianapa", "1234", "all"), True)
        result = ds_client.send_2("168.235.86.101", 3021, "julianapa", "1234", "all")
        directmessage = DirectMessage()
        
        print(result)

    def test_invalid_request(self):
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "julianapa", "1234asa", "alll"), False)

    def test_invalid_user(self):
        self.assertEqual(ds_client.send_2("168.235.86.101", 3021, "juli a", "1234", "alll"), False)
        
    def test_bio_only(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "JLKhjkjhSKJ", "123", None, None, "1jlakjds"), True)
    
    def test_post(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "hehe", None, "bio"), True)

    def test_empty_bio(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "JLK", "123", "sdf", None, "   "), False)
    
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

    def test_bio_int(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", None, None, 123), False)

    def test_msg_int(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", 123, None, "bio"), False)

    def test_post_bio_none(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "post", None, None), True)

    def test_all_none(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", None, None, None), False)

    def test_mess_empty(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "  ", None, None), False)

    def test_notoken(self):
            self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "12312", "hehe", "julianapa", "bio"), False)
    '''
    def test_connect_error(self):
            self.assertEqual(ds_client.send("168.235.86.1", 3021, "123", "12312", "hehe", "julianapa", "bio"), False)
    '''
    def test_bio_empty_andmess(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", None, None, "  "), False)

    def test_bio_int2(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "post", None, 123), False)

    def test_bio_userspace(self):
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "12 3", "1  23", None, None, "bio"), False)

if __name__ == '__main__':
    unittest.main()
