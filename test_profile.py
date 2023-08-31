# Julian Aparicio
# japaric4@uci.edu
# 74237345
import unittest
from Profile import Profile

class TestClient(unittest.TestCase):
    
    def test_prof(self):
        assign = Profile("user", "password", "bio")
        assign.load_profile("/Users/we3kends0onlyy/Documents/TEST ING/33.dsu")
        assign.add_new("hii")
        assign.add_cont1("contact")
        assign.add_message("message")
        assign.save_profile("/Users/we3kends0onlyy/Documents/TEST ING/33.dsu")
        
if __name__ == '__main__':
    unittest.main()

