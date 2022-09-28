from articulo import Articulo

class Tienda:

    def __init__(self, id, nombre, articulos):
        self.id = id
        self.nombre = nombre
        self.articulos = articulos
    
    def imprimir(self):
        print("\n\n--------------------------------------------------------------------------------------------")
        print("Id Tienda: ", self.id, "\tNombre Tienda: ", self.nombre)
        print("--------------------------------------------------------------------------------------------")
        for articulo in self.articulos:
            print("\n\tCodigo: ", articulo.codigo, "\tArticulo: ", articulo.nombre, "\tPrecio: ", articulo.precio, "\tCantidad disponible: ", articulo.cantidad)
        print("--------------------------------------------------------------------------------------------\n")

articulos = list()
articulos.append(Articulo(1, "Televisor", 2200000, 10))
articulos.append(Articulo(2, "Lavadora", 1200000, 6))
articulos.append(Articulo(3, "Nevera", 2430000, 9))
articulos.append(Articulo(4, "Computadora", 1800000, 6))
articulos.append(Articulo(5, "Tostadora", 315000, 12))
articulos.append(Articulo(6, "Licuadora", 895000, 5))
articulos.append(Articulo(7, "Estufa", 745000, 4))
articulos.append(Articulo(8, "Silla", 130000, 32))
articulos.append(Articulo(9, "Celular", 900000, 15))
articulos.append(Articulo(10, "Moto", 7610000, 3))

tienda = Tienda(123456, "Electronics SA", articulos)    
# tienda.imprimir()