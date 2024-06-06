from dataclasses import dataclass
@dataclass
class Collegamento():
    object_id1:int
    object_id2:int

    def __hash__(self):
        return hash((self.object_id1,self.object_id2))