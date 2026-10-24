class Persona:
    # Entidad de dominio que encapsula las reglas de negocio de una Persona
    def __init__(self, nombre: str):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self.nombre = nombre.strip()

    def obtener_nombre(self) -> str:
        return self.nombre

    def saludar(self) -> str:
        return f"Hola, {self.nombre}"
