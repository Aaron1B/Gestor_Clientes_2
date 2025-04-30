class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def modificar(self, nuevo_nombre, nuevo_apellido):
        self.nombre = nuevo_nombre
        self.apellido = nuevo_apellido

    def __repr__(self):
        return f"Cliente(dni='{self.dni}', nombre='{self.nombre}', apellido='{self.apellido}')"

clientes = [
    Cliente("12345678A", "Juan", "Pérez"),
    Cliente("87654321B", "Ana", "García"),
    Cliente("11223344C", "Luis", "Martínez")
]

def listar_clientes():
    """List all clients."""
    return clientes

def consultar_cliente(dni):
    """Retrieve a client by their DNI."""
    for cliente in clientes:
        if cliente.dni == dni:
            return cliente
    return None

def agregar_cliente(nombre, apellido, dni):
    """Add a new client if the DNI is unique."""
    if consultar_cliente(dni) is not None:
        raise ValueError("El cliente con este DNI ya existe.")
    clientes.append(Cliente(dni, nombre, apellido))

def modificar_cliente(dni, nuevo_nombre, nuevo_apellido):
    """Modify the name and surname of a client by their DNI."""
    cliente = consultar_cliente(dni)
    if cliente is None:
        raise ValueError("El cliente con este DNI no existe.")
    cliente.modificar(nuevo_nombre, nuevo_apellido)

def borrar_cliente(dni):
    """Delete a client by their DNI."""
    global clientes
    clientes = [cliente for cliente in clientes if cliente.dni != dni]
