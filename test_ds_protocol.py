import unittest
import ds_protocol
from ds_protocol import SaveFilePath

class TestClient(unittest.TestCase):
    
    def test_save(self):
       sfp =  SaveFilePath("/Users/we3kends0onlyy/Documents/TEST ING/33.dsu")
       sfp.extract_sent({"token":"user_token", "directmessage": {"entry": "Hello World!","recipient":"ohhimark", "timestamp": "1603167689.3928561"}})
if __name__ == '__main__':
    unittest.main()

