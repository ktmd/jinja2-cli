# $ jinja2
A CLI interface to Jinja2 with toml sample
```
$ jinja2 helloworld.tmpl data.json --format=json
$ cat data.json | jinja2 helloworld.tmpl
$ curl -s http://httpbin.org/ip | jinja2 helloip.tmpl
$ curl -s http://httpbin.org/ip | jinja2 helloip.tmpl > helloip.html
```

## Install
`$ pip install jinja2-cli`

## Usage
```
Usage: jinja2 [options] <input template> <input data>

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  --format=FORMAT       format of input variables: auto, ini, json,
                        querystring, yaml, yml
  -e EXTENSIONS, --extension=EXTENSIONS
                        extra jinja2 extensions to load
  -D key=value          Define template variable in the form of key=value
  -s SECTION, --section=SECTION
                        Use only this section from the configuration
  --strict              Disallow undefined variables to be used within the
                        template
```

## Optional YAML support
If `PyYAML` is present, you can use YAML as an input data source.

`$ pip install jinja2-cli[yaml]`

## Optional TOML support
If `toml` is present, you can use TOML as an input data source.

`$ pip install jinja2-cli[toml]`

## Optional XML support
If `xmltodict` is present, you can use XML as an input data source.

`$ pip install jinja2-cli[xml]`

## Optional HJSON support
If `hjson` is present, you can use HJSON as an input data source.

`$ pip install jinja2-cli[hjson]`

## Optional JSON5 support
If `json5` is present, you can use JSON5 as an input data source.

`$ pip install jinja2-cli[json5]`

## TODO
 * Variable inheritance and overrides
  * Tests!
