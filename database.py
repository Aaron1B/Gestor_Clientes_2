import json

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

DATABASE_FILE = "clientes.json"

clientes = []

def guardar_clientes():
    """Save the clients to a JSON file."""
    with open(DATABASE_FILE, "w") as file:
        json.dump([cliente.__dict__ for cliente in clientes], file)

def cargar_clientes():
    """Load the clients from a JSON file."""
    global clientes
    try:
        with open(DATABASE_FILE, "r") as file:
            clientes = [Cliente(**data) for data in json.load(file)]
    except FileNotFoundError:
        clientes = []

# Cargar los clientes al iniciar el programa
cargar_clientes()

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
    guardar_clientes()

def modificar_cliente(dni, nuevo_nombre, nuevo_apellido):
    """Modify the name and surname of a client by their DNI."""
    cliente = consultar_cliente(dni)
    if cliente is None:
        raise ValueError("El cliente con este DNI no existe.")
    cliente.modificar(nuevo_nombre, nuevo_apellido)
    guardar_clientes()

def borrar_cliente(dni):
    """Delete a client by their DNI."""
    global clientes
    clientes = [cliente for cliente in clientes if cliente.dni != dni]
    guardar_clientes()
