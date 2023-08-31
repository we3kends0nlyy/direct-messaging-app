# Julian Aparicio
# japaric4@uci.edu
# 74237345
import unittest
import ds_client

class TestClient(unittest.TestCase):
    
    def test_client(self):
        ds_client.save_path("/Users/we3kends0onlyy/Documents/TEST ING/33.dsu")
        self.assertEqual(ds_client.send("168.235.86.101", 3021, "123", "123", "JAJAJAJAJAJA", "Jandhiiiitest1", "bio"), True)
        
if __name__ == '__main__':
    unittest.main()
