from dataclasses import dataclass, field

@dataclass
class Colaborador:
    username: str
    email: str

@dataclass
class Proyecto:
    nombre: str
    lenguaje: str
    colaboradores: list[Colaborador] = field(default_factory=list)

    def agregar_colaborador(self, colaborador: Colaborador) -> None:
        for i in self.colaboradores:
            if i.username == colaborador:
                print(f"el colaborador {colaborador.username} ya existe")
        self.colaboradores.append(colaborador)

    def tiene_colaborador(self, username: str) -> bool:
        for i in self.colaboradores:
            if i.username == username:
                return True
        return False

    def __str__(self):
        return f"proyecto: {self.nombre} [{self.lenguaje}] - {len(self.colaboradores)}"

class GestorProyectos:
    def __init__(self):
        self.proyectos: list[Proyecto] = []

    def registrar_proyecto(self, proyecto: Proyecto) -> None:
        for i in self.proyectos:
            if i.nombre == proyecto:
                print(f"el proyecto {proyecto.nombre} ya existe")
            self.proyectos.append(proyecto)

    def listar_proyectos(self) -> list[Proyecto]:
        return self.proyectos

    def buscar_proyecto(self, nombre: str) -> Proyecto | None:
        for proyecto in self.proyectos:
            if proyecto.nombre == nombre:
                return proyecto
        return None

# Colaboradores
ana   = Colaborador(username="ana_dev", email="ana@mail.com")
luis  = Colaborador(username="luis99",  email="luis@mail.com")
sofia = Colaborador(username="sofiaml", email="sofia@mail.com")

# Proyectos
p1 = Proyecto(nombre="InventarioApp", lenguaje="Python")
p1.agregar_colaborador(ana)
p1.agregar_colaborador(luis)
p1.agregar_colaborador(ana)   # aviso: ya existe

p2 = Proyecto(nombre="WebStore", lenguaje="JavaScript")
p2.agregar_colaborador(sofia)

# __str__
print(p1)  # Proyecto: InventarioApp [Python] — 2 colaborador(es)
print(p2)  # Proyecto: WebStore [JavaScript] — 1 colaborador(es)

# tiene_colaborador
print(p1.tiene_colaborador("ana_dev"))  # True
print(p1.tiene_colaborador("sofiaml"))  # False

# Gestor
gestor = GestorProyectos()
gestor.registrar_proyecto(p1)
gestor.registrar_proyecto(p2)
gestor.registrar_proyecto(p1)  # aviso: ya existe

encontrado = gestor.buscar_proyecto("WebStore")
print(encontrado)  # Proyecto: WebStore [JavaScript] — 1 colaborador(es)

no_existe = gestor.buscar_proyecto("OtroProyecto")
print(no_existe)   # None

print(len(gestor.listar_proyectos()))  # 2
