class Articulo:

    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

articulos = list()

articulo1 = Articulo(1, "Televisor", 2200000)
articulo2 = Articulo(2, "Lavadora", 1200000)
articulo3 = Articulo(3, "Nevera", 2430000)
articulo4 = Articulo(4, "Computadora", 1800000)
articulo5 = Articulo(5, "Tostadora", 315000)       
articulo6 = Articulo(6, "Equipo de sonido", 895000)
articulo7 = Articulo(7, "Estufa", 745000)
articulo8 = Articulo(8, "Silla", 130000)
articulo9 = Articulo(9, "Celular", 900000)
articulo10 = Articulo(10, "Moto", 7610000)  

articulos.append(articulo1)
articulos.append(articulo2)
articulos.append(articulo3)
articulos.append(articulo4)
articulos.append(articulo5)
articulos.append(articulo6)
articulos.append(articulo7)
articulos.append(articulo8)
articulos.append(articulo9)
articulos.append(articulo10)