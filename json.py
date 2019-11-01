import json
import random
import string

def randomString(stringLength=6):
    """Generate a random string of letters and digits """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

val1=randomString()
val2=randomString()
my_json_string = json.dumps({'key1': val1, 'key2': val2})
print (my_json_string)
