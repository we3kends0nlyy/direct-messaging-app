# Julian Aparicio
# japaric4@uci.edu
# 74237345
import unittest
import user

class TestClient(unittest.TestCase):
    
    def test_user(self):
        self.assertEqual(user.user_asker("/Users/we3kends0onlyy/Documents/TEST ING/33.dsu", "john", "password", "123123"), True)
        
if __name__ == '__main__':
    unittest.main()

