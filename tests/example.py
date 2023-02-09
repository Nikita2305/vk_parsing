from vk_parsing.exceptions import *
from vk_parsing.parser import Parser 

token = "PASTE_VK_TOKEN"
which_id = 1

parser = Parser(["Important description like login"], [token])

def p(response):
    print(response["count"])
    raise RuntimeError("abcd")

try:
    parser.direct_call("friends.get", {"user_id": which_id}, callback=p)
except StopParsingError as ex:
    print("status1 " + str(ex))
    quit()
except Exception as ex:
    print("status2 " + str(ex))

for i in range(2 * 25): # two buckets
    try:
        parser.add_task("friends.get", {"user_id": which_id}, callback=p)
    except StopParsingError as ex:
        print("status1 " + str(ex))
        quit()
    except Exception as ex:
        print("status2 " + str(ex))
