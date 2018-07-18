from mirageframework.codable.encodable import Encodable, EncodableFormats

class EncodeJSONTest(Encodable):

    user_name = "shotastage"
    email = "hornet.live.mf@gmail.com"
    age = 20
    birth_year = 1997


instance = EncodeJSONTest()
print(instance.encode(EncodableFormats.json))
