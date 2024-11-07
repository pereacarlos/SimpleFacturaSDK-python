from enum import Enum

class IndicadorExentoEnum(Enum):
    NotSet = (0, "")
    Exento = (1, "No afecto o exento de IVA")
    NoFacturable = (2, "No facturable")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
