from reportlab.platypus import SimpleDocTemplate, Table, Spacer


class Informe():
    def __init__(self, datos):
        self.elementosDoc = []
        for dato in datos:
            self.fichaCliente(dato)
        documento = SimpleDocTemplate("informeClientes.pdf")
        documento.build(self.elementosDoc)
        print("Informe Creado")

    def fichaCliente(self, dato):
        elemento = [
            [dato[0], "Nome Cliente", dato[1]]
        ]
        estilo = [
            # estilo , (inicio columna, inicio fila), (fin columna, fin fila),
            ("INNERGRID", (0, 0), (-1, -1), 1, "BLACK"),
            ("BACKGROUND", (1, 0), (1, 0), "LIGHTGREY"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
        ]

        tabla1 = Table(data=elemento, style=estilo, colWidths=[65, 100, 80], rowHeights=20)

        elemento = [
            [dato[5], "Provincia", dato[6]]
        ]
        tabla2 = Table(data=elemento, style=estilo, colWidths=[65, 100, 80], rowHeights=20)

        elemento = [
            [dato[7], "Teléfono", dato[3]]
        ]
        tabla3 = Table(data=elemento, style=estilo, colWidths=[65, 100, 80], rowHeights=20)

        elemento = [
            [dato[8], "Axente Comercial", dato[9]]
        ]
        tabla4 = Table(data=elemento, style=estilo, colWidths=[65, 100, 80], rowHeights=20)

        elementos = [
            ["Ficha Cliente"],
            ["Número Cliente", tabla1],
            ["Apelidos", dato[2]],
            ["Direccion", dato[4]],
            ["Cidade", tabla2],
            ["Código postal", tabla3],
            ["País", tabla4]
        ]

        estilo = [
            # estilo , (inicio columna, inicio fila), (fin columna, fin fila),
            ("GRID", (0, 1), (-1, -1), 1, "BLACK"),
            ("BACKGROUND", (0, 1), (0, -1), "LIGHTGREY"),
            ("BOTTOMPADDING", (1, 1), (1, 1), 0),
            ("BOTTOMPADDING", (1, 4), (1, -1), 0),
            ("LEFTPADDING", (1, 1), (1, 1), 0),
            ("LEFTPADDING", (1, 4), (1, -1), 0)
        ]

        tabla = Table(data=elementos, style=estilo, colWidths=[100, 300], rowHeights=20)
        self.elementosDoc.append(tabla)
        self.elementosDoc.append(Spacer(0, 30))


if __name__ == "__main__":
    Informe([[1, "Ana", "Perez Diz", 986456780, "Garcia Barbon 38, 6ºA", "Vigo", "Pontevedra", 36201, "España", 1],
             [1, "Ana", "Perez Diz", 986456780, "Garcia Barbon 38, 6ºA", "Vigo", "Pontevedra", 36201, "España", 1]])
