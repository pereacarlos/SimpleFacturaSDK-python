from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
from SimpleFacturaSDK.models.ActividadesEconomicaApiEnt import ActividadesEconomicaEnt

@dataclass
class EmisorAapiEnt:
    rut: str
    razonSocial: str
    giro: str
    correoFact: str
    comuna: str
    nroResol: int
    fechaResol: datetime
    ambiente: int
    telefono: float
    rutRepresentanteLegal: str
    actividadesEconomicas: List[ActividadesEconomicaEnt]
    dirPart: Optional[str] = None
    dirFact: Optional[str] = None
    correoPar: Optional[str] = None
    ciudad: Optional[str] = None
    unidadSII: Optional[str] = None

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            Rut=d.get("rut"),
            RazonSocial=d.get("razonSocial"),
            Giro=d.get("giro"),
            CorreoFact=d.get("correoFact"),
            Comuna=d.get("comuna"),
            NroResol=d.get("nroResol"),
            FechaResol=datetime.strptime(d.get("fechaResol"), "%Y-%m-%d"),
            Ambiente=d.get("ambiente"),
            Telefono=d.get("telefono"),
            RutRepresentanteLegal=d.get("rutRepresentanteLegal"),
            ActividadesEconomicas=[ActividadesEconomicaEnt.from_dict(item) for item in d.get("actividadesEconomicas")],
            DirPart=d.get("dirPart"),
            DirFact=d.get("dirFact"),
            CorreoPart=d.get("correoPar"),
            Ciudad=d.get("ciudad"),
            UnidadSII=d.get("unidadSII")
        )