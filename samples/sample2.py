# pip install jinja2-cli[toml]

import toml

# Load the TOML data into a Python dictionary
with open("sample2.toml") as f:
    data = toml.load(f)

print(f'all data={data}\n')

# Access the data in the dictionary
print(f'title={data["title"]}\n')

print(f'items={data["items"]}\n')