# Julian Aparicio
# japaric4@uci.edu
# 74237345
import unittest
from ds_messenger import DirectMessenger
import ds_messenger

class TestClient(unittest.TestCase):
    
    def test_save(self):
        ds_messenger.save_p("/User/we3kends0nlyy/Documents/TEST ING/1.dsu")
        ds_mess = DirectMessenger("168.235.86.101", "jujuju", "1234")
        result = ds_mess.retrieve_new()
        self.assertEqual(result, None)

    def test_new_response(self):
        ds_mess = DirectMessenger("168.235.86.101", "jujuju", "1234")
        result = ds_mess.retrieve_new()
        self.assertEqual(type(result), list)

    def test_all(self):
        ds_mess = DirectMessenger("168.235.86.101", "jujuju", "1234")
        result = ds_mess.retrieve_all()
        self.assertEqual(type(result), list)

    def test_msg_send(self):
        ds_mess = DirectMessenger("168.235.86.101", "123", "123")
        result = ds_mess.send("if this works give urself a pat on the back son.", "jujuju")
        self.assertEqual(result, True)

    def test_new_wrongpswd(self):
        ds_mess = DirectMessenger("168.235.86.101", "123", "123")
        ds_mess.send("AYYYYOOOOOOOOOO", "julianapa")
        ds_mess = DirectMessenger("168.235.86.101", "julianapa", "123qwqw")
        result = ds_mess.retrieve_new()
        self.assertEqual(result, None)

    def test_msg_send(self):
        ds_mess = DirectMessenger("168.235.86.101", "jel", "12345")
        result = ds_mess.send("let me rizz u up zaddy", "patrickroll")
        self.assertEqual(result, True)

    def test_new(self):
        ds_mess = DirectMessenger("168.235.86.101", "julianapaa2", "123")
        ds_mess.send("wahwahwah", "jujuju")
        ds_mess = DirectMessenger("168.235.86.101", "julianapa", "1234")
        result = ds_mess.retrieve_new()
        self.assertEqual(type(result), list)

    def test_rec_whtspc(self):
        ds_mess = DirectMessenger("168.235.86.101", "123", "123")
        result = ds_mess.send("if this works give urself a pat on the back son.", " ")
        self.assertEqual(result, False)

    def test_conn(self):
        ds_mess = DirectMessenger("a2312", "123", "123")
        result = ds_mess.send("if this works give urself a pat on the back son.", " ")
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
