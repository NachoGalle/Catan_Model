RUTA_COMERCIAL = 5
EJERCITO_MAS_GRANDE = 3

class estado():
    def __init__(self,poblados: int=2,caminos: int=2,ciudades: int =0,caballeros: int = 0, ruta_larga:int = 0,ejercito:int = 0, ptos_victoria: int=0):
        self.poblados = poblados
        self.caminos = set_caminos(caminos,poblados,ruta_larga)
        self.ciudades=ciudades
        self.caballeros= set_caballeros(caballeros,ejercito)
        self.ruta_larga= ruta_larga
        self.ejercito= ejercito
        self.ptos_victoria= ptos_victoria
        self.ptos_totales= poblados + 2*ciudades + 2*ruta_larga+2*ejercito+ptos_victoria
        self.propiedades = {"poblados":poblados,"caminos":caminos,"ciudades":ciudades,
                            "caballeros":caballeros,"ruta_larga":ruta_larga,
                            "ejercito":ejercito,"p_victoria":ptos_victoria,"puntos_totales":self.ptos_totales}


    def get_name(self) -> str:
        return f"P{self.poblados}-R{self.caminos}-C{self.ciudades}-K{self.caballeros}-RL{int(self.ruta_larga)}-EJ{int(self.ejercito)}-V{self.ptos_victoria}"

    def __eq__(self, other):
        if not isinstance(other, estado):
            return False
        return (self.poblados == other.poblados and
                self.ciudades == other.ciudades and
                self.caballeros == other.caballeros and
                self.ruta_larga == other.ruta_larga and
                self.ejercito == other.ejercito and
                self.ptos_victoria == other.ptos_victoria)
    
    def __hash__(self):
        return hash((self.poblados, self.caminos ,self.ciudades, self.caballeros,
                     self.ruta_larga, self.ejercito, self.ptos_victoria))

def set_caminos(caminos,poblados,ruta_larga) -> int:
    if caminos < min_caminos(poblados):
        caminos = min_caminos(poblados)
    if ruta_larga == 1 and caminos < RUTA_COMERCIAL:
        caminos = RUTA_COMERCIAL
    return caminos

def set_caballeros(caballeros,ejercito) -> int:
    if ejercito == 1 and caballeros < EJERCITO_MAS_GRANDE:
        caballeros = EJERCITO_MAS_GRANDE
    return caballeros

def diferencia(estado1: estado,estado2: estado,ruta_mas_larga :int = RUTA_COMERCIAL) -> estado:

    caminos = min_caminos((estado2.poblados+estado2.ciudades))-estado1.caminos
    if estado2.ruta_larga > estado1.ruta_larga:
        caminos = max(ruta_mas_larga - caminos,caminos)

    estado_dif=estado(estado2.poblados-estado1.poblados,caminos,estado2.ciudades-estado1.ciudades,
                      estado2.caballeros-estado1.caballeros,estado2.ruta_larga-estado1.ruta_larga,
                      estado2.ejercito-estado1.ejercito,estado2.ptos_victoria-estado1.ptos_victoria)
    return estado_dif

def costo_estado(estado: estado) -> dict:
    #arcilla , madera, trigo, piedra, oveja
    poblados = estado.poblados
    ciudades = estado.ciudades
    caminos = estado.caminos
    caballeros = estado.caballeros
    victorias = estado.ptos_victoria

    costo = {"arcilla":poblados+caminos+ciudades,"madera":poblados+caminos+ciudades,"trigo":poblados+3*ciudades+caballeros+victorias,
             "piedra":3*ciudades+caballeros+victorias,"oveja":poblados+ciudades+caballeros+victorias}

    return costo

def min_caminos(p:int) -> int:
    if p < 7:
        return p
    return p + (p-1)//3


def costo(estado1: estado,estado2: estado) -> dict:
    est_dif = diferencia(estado1,estado2)
    costo = costo_estado(est_dif)
    return costo

def estado_valido(estado: estado) -> bool:
    if estado.poblados + estado.ciudades < 2 or estado.poblados > 5 or estado.ciudades > 4:
        return False
    if estado.caminos < min_caminos(estado.poblados) or estado.caminos > 15:
        return False
    if (estado.ruta_larga == 1 and estado.caminos < RUTA_COMERCIAL) or estado.ruta_larga > 1:
        return False
    if (estado.ejercito == 1 and estado.caballeros < EJERCITO_MAS_GRANDE) or estado.ejercito > 1:
        return False
    if estado.ptos_victoria > 5 or estado.poblados < 0:
        return False
    if estado.ptos_totales > 11 or estado.ptos_totales < 2 or (estado.ptos_totales == 11 and estado.ruta_larga + estado.ejercito == 0):
        return False
    return True

def max_poblados(c:int) -> int:
    if c < 7: return c
    elif c > 10: return 9
    else: return ((c-6)*2)//3 + 6

e1 = estado(poblados= 0,ciudades= 2)
e2 = estado(poblados= 5, ruta_larga= 1, ejercito= 1, ptos_victoria= 2)

print(costo(e1,e2))
print(costo(e2,e1))