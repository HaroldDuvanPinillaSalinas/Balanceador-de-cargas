from articulo import articulos as items

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
articulos.append(items[0])
articulos.append(items[1])
articulos.append(items[3])
articulos.append(items[4])
articulos.append(items[7])

tienda = Tienda(123456, "Electronics SA", articulos)    
# tienda.imprimir()