class Pedido:
    def __init__(self, numero_pedido, nombre_cliente, producto, cantidad, tipo_pedido, tiempo_preparacion):
        self.numero_pedido = numero_pedido
        self.nombre_cliente = nombre_cliente
        self.producto = producto
        self.cantidad = cantidad
        self.tipo_pedido = tipo_pedido.lower()  # 'normal' o 'prioritario'
        self.tiempo_preparacion = tiempo_preparacion

    def __str__(self):
        return (f"ID: {self.numero_pedido} | Cliente: {self.nombre_cliente} | "
                f"Producto: {self.producto} (x{self.cantidad}) | "
                f"Tipo: {self.tipo_pedido.upper()} | Tiempo: {self.tiempo_preparacion} min")