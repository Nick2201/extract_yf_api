from pathlib import Path
from main import transform, parameters_Descriptive
from data_base import descriptive_info,engine,metadata
import json

_main_path = Path(r"C:\Users\nickl\nick_\companies")




# descriptive = transform(
#     _path=r"C:\Users\nickl\nick_\companies\ACLX.json",
#     _mapping_parameters=parameters_Descriptive
# )

def load_to_db(data:dict):
    conn = engine.connect()
    ins = descriptive_info.insert().values(**data)
    # logging.info(str({_row['cik']:[
    #     _row['date_added']
    #     ]})+"data inserted into database")
    conn.execute(ins)
    conn.commit()

for _comp_file in _main_path.iterdir():

    _dict = transform(
        _path=_comp_file,
        _mapping_parameters=parameters_Descriptive)
    load_to_db(_dict)

metadata.create_all(engine)