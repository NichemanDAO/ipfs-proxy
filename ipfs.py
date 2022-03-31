import ipfshttpclient
import requests
import os

# connect to local node
# api = ipfshttpclient.connect(os.getenv('IPFS_API_ENDPOINT', '/ip4/127.0.0.1/tcp/5001'));
api = ipfshttpclient.connect(os.getenv('IPFS_API_ENDPOINT', '127.0.0.1:5001'));

def add_file(file_path, pin=True, wrap_with_directory=True):
    res = api.add(file_path, wrap_with_directory=wrap_with_directory, pin=pin)
    return res

def add_directory(directory_path, pin=True, recursive=True):
    res = api.add(directory_path, pin=pin, recursive=recursive)
    return res

# gateway_endpoint = os.getenv('IPFS_GATEWAY_ENDPOINT','/ip4/127.0.0.1/tcp/8080');
gateway_endpoint = os.getenv('IPFS_GATEWAY_ENDPOINT','127.0.0.1:8080');

gateway_timeout = os.getenv('IPFS_GATEWAY_TIMEOUT', 30);

def cat_file(file_path):
    res = requests.get('%s/ipfs/%s' % (gateway_endpoint, file_path), timeout=gateway_timeout)
    return res
