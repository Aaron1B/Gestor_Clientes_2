from database import listar_clientes

class DNIHelper:
    @staticmethod
    def es_dni_valido(dni):
        """Verifica si el DNI tiene 8 dígitos y solo contiene números."""
        return len(dni) == 8 and dni.isdigit()

    @staticmethod
    def es_dni_unico(dni):
        """Verifica si el DNI no está duplicado en la base de datos."""
        clientes = listar_clientes()
        for cliente in clientes:
            if cliente.dni == dni:
                return False
        return True
