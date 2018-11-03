import unittest
from miragecore.codable import Codable
from miragecore.codable.json_encorder_decoder import encode


class EncodeJSONTest(Codable):

    user_name = "shotastage"
    email = "hornet.live.mf@gmail.com"
    age = 20
    birth_year = 1997


instance = EncodeJSONTest()

if __name__ == "__main__":
    print(encode(instance))
