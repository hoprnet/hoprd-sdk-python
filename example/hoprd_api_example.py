import sys
import logging
import os
import asyncio
from hoprd import wrapper

# set logging level
logging.basicConfig(filename='hoprd_api.log',
                    level=logging.DEBUG,
                    format='%(levelname)s:%(asctime)s:%(message)s')


def _getenvvar(name: str) -> str:
    """
    Returns the string contained in environment variable `name` or None.
    """
    ret_value = None
    if os.getenv(name) is None:
        print("Environment variable", name, "not found")
        sys.exit(1)
    else:
        ret_value = os.getenv(name)
    return ret_value


async def get_peerId():
    """
    Fetches information about the host of the API Url and checks whether the host is available.
    Returns the 'hopr_address' (i.e. the peerId) of the host. 
    """
    node = wrapper.HoprdAPI(api_url, api_token)
    address_response = await node.get_address()

    my_pid = None
    if address_response.status_code == 200:
        my_pid = address_response.json()['hoprAddress']
        logging.info("Host available (PID: {})".format(my_pid))
    else:
        logging.error("Host is NOT available. Status code: {}".format(address_response.status_code))
        sys.exit(1)
    return my_pid


if __name__ == "__main__":

    api_url = _getenvvar('API_URL')
    api_token  = _getenvvar('API_TOKEN')

    asyncio.run(get_peerId())