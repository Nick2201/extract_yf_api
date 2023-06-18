from pathlib import Path


import json
# "C:\Users\nickl\nick_\companies\ACLX.json
parameters_Descriptive=(
    'symbol','longName',
    'sector','industry','country',
    'longBusinessSummary','fullTimeEmployees',
    'website','logo_url','exchange')






def transform (_path, _mapping_parameters:iter):
    '''
        get json file from yf : _path
        return: list
    '''
    with open(_path, 'r') as _file:
        dict_from_json = json.load(_file)

        _dict = {_key:
            dict_from_json.get(_key,None)
            for _key
            in (parameters_Descriptive)
        }
        return _dict


descriptive = transform(
    _path=r"C:\Users\nickl\nick_\companies\ACLX.json",
    _mapping_parameters=parameters_Descriptive
)