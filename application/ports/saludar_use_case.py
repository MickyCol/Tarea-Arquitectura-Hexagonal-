from abc import ABC, abstractmethod

class SaludarUseCase(ABC):
    # Puerto de entrada que define el contrato del caso de uso
    @abstractmethod
    def ejecutar(self, nombre: str) -> str:
        pass
