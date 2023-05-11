# HOPR daemon API

This repository contains a Python native wrapper around the HOPR daemon.

The goal of this wrapper is to simplify the interaction with the daemon using Python as well as offer native Python types for advanced interaction in a fully `async` manner.

### Example Usage

The folder called "example" contains an example of how to use the HOPR daemon API. To execute the script called "hoprd_api_example.py" you need:  

1. Python >=3.7
2. Install dependencies:  
```bash
pip install -r requirements.txt 
```
3. Set up a run.sh file:
```bash 
#!/bin/sh

export API_URL='http://INSERT_YOUR_IP_ADDRESS:3001'
export API_TOKEN='INSERT_YOUR_API_TOKEN'

python hoprd_api_example.py 
 
```

### Configuration of Environment Variables
This program requires two environment variables to be set. If either of these environment variables is not set, the program will exit with an error.

1. `API_URL`: the URL of the API endpoint to be used. Here you must insert your IP address.
2. `API_TOKEN`: the authentication token to be used with the API endpoint.

 
### Execute the Program 

To execute the program, run the following command:

```bash
./run.sh
```

The program will fetch the 'hopr_address' (i.e. the peerId) of your HOPR node and check whether your node is available.

### Logging
This program logs to the file hoprd_api.log. The log level is set to DEBUG by default.

## Contact

- [Twitter](https://twitter.com/hoprnet)
- [Telegram](https://t.me/hoprnet)
- [Medium](https://medium.com/hoprnet)
- [Reddit](https://www.reddit.com/r/HOPR/)
- [Email](mailto:contact@hoprnet.org)
- [Discord](https://discord.gg/5FWSfq7)
- [Youtube](https://www.youtube.com/channel/UC2DzUtC90LXdW7TfT3igasA)

## License

[GPL v3](LICENSE) © HOPR Association
