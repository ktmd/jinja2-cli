# pip install jinja2-cli[toml]

import toml
import pprint

from jinja2 import Template
template = Template('Hello {{ name }}!')
output=template.render(name='John Doe')

print(f"output={output}")



# Load the TOML data into a Python dictionary
with open("sample3.toml") as f:
    data = toml.load(f),

print(f'all data=\n')
print(data)

# data='''{'debug': True,
#   'grpc': {'address': ['tcp://0.0.0.0:1234'],
#            'debugAddress': '0.0.0.0:6060',
#            'gid': 0,
#            'tls': {'ca': '/etc/buildkit/tlsca.crt',
#                    'cert': '/etc/buildkit/tls.crt',
#                    'key': '/etc/buildkit/tls.key'},
#            'uid': 0},
#   'history': {'maxAge': 172800, 'maxEntries': 50}
#   }
# '''
print("***data:")
pprint.pprint(data)

template = Template('grpc={{ grpc }}')
output=template.render(grpc=data[0]['grpc'])

print("output=\n")
pprint.pprint(output)
