import unittest
from ds_messenger import DirectMessenger


class TestClient(unittest.TestCase):
    #'''
    def test_all(self):
        ds_mess = DirectMessenger("168.235.86.101", "jujuju", "1234")
        result = ds_mess.retrieve_all()
        print(result)
    #'''
        '''
    def test_new(self):
        ds_mess = DirectMessenger("168.235.86.101", "123", "123")
        ds_mess.send("wahwahwah", "jujuju")
        ds_mess = DirectMessenger("168.235.86.101", "julianapa", "1234")
        '''
        '''
        result = ds_mess.retrieve_new()
        print(result)
        self.assertEqual(type(result), list)

    def test_new_wrongpswd(self):
        ds_mess = DirectMessenger("168.235.86.101", "123", "123")
        ds_mess.send("AYYYYOOOOOOOOOO", "julianapa")
        ds_mess = DirectMessenger("168.235.86.101", "julianapa", "123")
        result = ds_mess.retrieve_new()
        print(result)
        self.assertEqual(result, False)

    def test_msg_send(self):
        ds_mess = DirectMessenger("168.235.86.101", "123", "123")
        result = ds_mess.send("if this works give urself a pat on the back son.", "julianapa")
        self.assertEqual(result, True)

    def test_rec_whtspc(self):
        ds_mess = DirectMessenger("168.235.86.101", "123", "123")
        result = ds_mess.send("if this works give urself a pat on the back son.", " ")
        self.assertEqual(result, False)
        #'''

if __name__ == '__main__':
    unittest.main()
