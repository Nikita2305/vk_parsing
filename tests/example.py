from vk_parsing.exceptions import *
from vk_parsing.parser import Parser 

token = "c6d010bf99b7da90f3d9e236b13043f41e02b1623e8055656a95c49e3137b00231782e8d9c72d23e8633c"

parser = Parser(["Important description like login"], [token])

def p(response):
    print(response["count"])
    raise RuntimeError("abcd")

try:
    parser.direct_call("friends.get", {"user_id": 704560495}, callback=p)
except StopParsingError as ex:
    print("status1 " + str(ex))
    quit()
except Exception as ex:
    print("status2 " + str(ex))

for i in range(2 * 25): # two buckets
    try:
        parser.add_task("friends.get", {"user_id": 704560495}, callback=p)
    except StopParsingError as ex:
        print("status1 " + str(ex))
        quit()
    except Exception as ex:
        print("status2 " + str(ex))
