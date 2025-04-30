import tkinter as tk
from tkinter import messagebox
from database import listar_clientes, consultar_cliente, agregar_cliente, modificar_cliente, borrar_cliente

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Clientes")
        
        # Widgets
        self.label_dni = tk.Label(root, text="DNI:")
        self.label_dni.grid(row=0, column=0)
        self.entry_dni = tk.Entry(root)
        self.entry_dni.grid(row=0, column=1)

        self.label_nombre = tk.Label(root, text="Nombre:")
        self.label_nombre.grid(row=1, column=0)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=1, column=1)

        self.label_apellido = tk.Label(root, text="Apellido:")
        self.label_apellido.grid(row=2, column=0)
        self.entry_apellido = tk.Entry(root)
        self.entry_apellido.grid(row=2, column=1)

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.grid(row=3, column=0, columnspan=2)

        self.button_listar = tk.Button(root, text="Listar Clientes", command=self.listar_clientes)
        self.button_listar.grid(row=4, column=0)

        self.button_agregar = tk.Button(root, text="Agregar Cliente", command=self.agregar_cliente)
        self.button_agregar.grid(row=4, column=1)

        self.button_modificar = tk.Button(root, text="Modificar Cliente", command=self.modificar_cliente)
        self.button_modificar.grid(row=5, column=0)

        self.button_borrar = tk.Button(root, text="Borrar Cliente", command=self.borrar_cliente)
        self.button_borrar.grid(row=5, column=1)

    def listar_clientes(self):
        """List all clients in the Listbox."""
        self.listbox.delete(0, tk.END)
        for cliente in listar_clientes():
            self.listbox.insert(tk.END, f"{cliente.dni} - {cliente.nombre} {cliente.apellido}")

    def agregar_cliente(self):
        """Add a new client."""
        dni = self.entry_dni.get()
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        try:
            agregar_cliente(nombre, apellido, dni)
            messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
            self.listar_clientes()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def modificar_cliente(self):
        """Modify an existing client."""
        dni = self.entry_dni.get()
        nuevo_nombre = self.entry_nombre.get()
        nuevo_apellido = self.entry_apellido.get()
        try:
            modificar_cliente(dni, nuevo_nombre, nuevo_apellido)
            messagebox.showinfo("Éxito", "Cliente modificado correctamente.")
            self.listar_clientes()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def borrar_cliente(self):
        """Delete a client."""
        dni = self.entry_dni.get()
        try:
            borrar_cliente(dni)
            messagebox.showinfo("Éxito", "Cliente borrado correctamente.")
            self.listar_clientes()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
