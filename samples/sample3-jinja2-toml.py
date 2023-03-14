# pip install jinja2-cli[toml]

#https://quickref.me/toml

import toml
import pprint
import json

from jinja2 import Template
template = Template('Hello {{ name }}!')
output=template.render(name='John Doe')

print(f"output={output}")



# Load the TOML data into a Python dictionary
with open("sample3.toml") as f:
    data = toml.load(f),

print(f'all data=\n')
print(data)


print("***data:")
pprint.pprint(data)

template = Template('grpc={{ grpc }}')
output=template.render(grpc=data[0]['grpc'])

print("output=\n")
pprint.pprint(output)

###
template = Template('policy file name={{ policy_file }}')
iam_policy=data[0]['iam_policy']
output=template.render(policy_file=iam_policy)

print("policy=\n")
pprint.pprint(output)


with open(data[0]['iam_policy']['file_name']) as file:
    data = json.load(file)

print("iam_policy data")
pprint.pprint(data)
  
#https://sparkbyexamples.com/pyspark/pyspark-read-multiple-line-json-file/

import json
json_serial = "123"
my_json = {
    'settings': {
        "serial": json_serial,
        "status": '2',
        "ersion": '3',
    },
    'config': {
        'active': '4',
        'version': '5'
    }
}
print("my_json")
print(json.dumps(my_json))