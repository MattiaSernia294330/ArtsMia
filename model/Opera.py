from dataclasses import dataclass
@dataclass
class Opera():
    object_id:int
    classification:str
    object_name:str

    def __hash__(self):
        return hash(self.object_id)