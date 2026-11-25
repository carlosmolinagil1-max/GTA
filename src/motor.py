"""
Motor base de simulación y lógica para el proyecto GTA.
Incluye entidades de Jugador, Vehículo y Sistema de Misiones.
"""
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Entidad:
    nombre: str = "Entidad"
    x: float = 0.0
    y: float = 0.0
    velocidad: float = 0.0
    angulo: float = 0.0  # en grados (0 - 360)

    def mover(self, dx: float, dy: float):
        self.x += dx
        self.y += dy


@dataclass
class Vehiculo(Entidad):
    nombre: str = "Vehículo"
    modelo: str = "Banshee"
    color: str = "Rojo"
    salud: float = 100.0
    combustible: float = 100.0
    ocupado_por: Optional[str] = None

    def acelerar(self, incremento: float = 5.0, vel_max: float = 120.0):
        self.velocidad = min(vel_max, self.velocidad + incremento)
        return self.velocidad

    def frenar(self, decremento: float = 8.0):
        self.velocidad = max(0.0, self.velocidad - decremento)
        return self.velocidad


@dataclass
class Jugador(Entidad):
    nombre: str = "Jugador"
    vida: int = 100
    blindaje: int = 50
    dinero: int = 500
    estrellas_busqueda: int = 0
    vehiculo_actual: Optional[Vehiculo] = None
    inventario: List[str] = field(default_factory=lambda: ["Móvil iFruit", "Llaves"])

    def entrar_vehiculo(self, vehiculo: Vehiculo):
        self.vehiculo_actual = vehiculo
        vehiculo.ocupado_por = self.nombre
        self.x = vehiculo.x
        self.y = vehiculo.y
        return f"{self.nombre} se ha subido a {vehiculo.modelo}."

    def salir_vehiculo(self):
        if self.vehiculo_actual:
            nombre_vehiculo = self.vehiculo_actual.modelo
            self.vehiculo_actual.ocupado_por = None
            self.vehiculo_actual = None
            return f"{self.nombre} se bajó de {nombre_vehiculo}."
        return f"{self.nombre} no está en ningún vehículo."

    def ganar_dinero(self, cantidad: int):
        self.dinero += cantidad
        return self.dinero


@dataclass
class Mision:
    id_mision: str = "MIS-000"
    titulo: str = "Misión Base"
    descripcion: str = "Descripción de misión"
    recompensa_dinero: int = 1000
    completada: bool = False

    def completar(self, jugador: Jugador):
        if not self.completada:
            self.completada = True
            jugador.ganar_dinero(self.recompensa_dinero)
            return f"¡Misión '{self.titulo}' completada! Recompensa: ${self.recompensa_dinero}."
        return f"La misión '{self.titulo}' ya estaba completada."
