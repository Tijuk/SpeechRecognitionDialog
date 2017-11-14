from __future__ import print_function

import os
import sys
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            os.pardir
        )
    )

    import apiai


# demo agent acess token: e5dc21cab6df451c866bf5efacb40178

#CLIENT_ACCESS_TOKEN = '65877e113a5b429395d4c4cb4543f867'
CLIENT_ACCESS_TOKEN = '4b693ee4418848028d47eb9290d175e4'


def query(input):
    print('quering')
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    user_message = input
    if input == '-=-':
        return
    request = ai.text_request()
    request.query = user_message

    response = json.loads(request.getresponse().read())

    result = response['result']
    action = result.get('action')
    actionIncomplete = result.get('actionIncomplete', False)

    if action is not None:
        print(result.get('fulfillment').get('speech'))

    return action
