from articulo import Articulo

class Tienda:

    def __init__(self, id, nombre, articulos):
        self.id = id
        self.nombre = nombre
        self.articulos = articulos
    
    def imprimir(self):
        print("\n\n-------------------------------------------------------------------------")
        print("Id Tienda: ", self.id, "\tNombre Tienda: ", self.nombre)
        print("-------------------------------------------------------------------------")
        for articulo in self.articulos:
            print("\n\tCodigo: ", articulo.codigo, "\tArticulo: ", articulo.nombre, "\tPrecio: ", articulo.precio)
        print("-------------------------------------------------------------------------\n")

articulos = list()
articulos.append(Articulo(1, "Televisor", 2200000))
articulos.append(Articulo(2, "Lavadora", 1200000))
articulos.append(Articulo(3, "Nevera", 2430000))
articulos.append(Articulo(4, "Computadora", 1800000))
articulos.append(Articulo(5, "Tostadora", 315000))
articulos.append(Articulo(6, "Equipo de sonido", 895000))
articulos.append(Articulo(7, "Estufa", 745000))
articulos.append(Articulo(8, "Silla", 130000))
articulos.append(Articulo(9, "Celular", 900000))
articulos.append(Articulo(10, "Moto", 7610000))

tienda = Tienda(123456, "Electronics SA", articulos)    
# tienda.imprimir()