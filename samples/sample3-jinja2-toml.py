from jinja2 import Template
template = Template('Hello {{ name }}!')
output=template.render(name='John Doe')

print(f"output={output}")


# pip install jinja2-cli[toml]

import toml

# Load the TOML data into a Python dictionary
with open("sample2.toml") as f:
    data = toml.load(f),

print(f'all data={data}\n')

data={'title': 'My Configuration', 'items': ['foo', 'bar', 'baz'], 'database': {'host': 'localhost', 'port': 5432, 'username': 'user', 'password': 'secret'}, 'section2': {'items': ['foo', 'bar', 'baz']}}
section2_items=data['title']

template = Template('items={{ section2_items }}')
output=template.render(sections2_items=data['title'])

print(output)
