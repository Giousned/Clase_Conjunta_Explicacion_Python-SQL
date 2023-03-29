id = 0


products_table = []

insert_into = lambda item, table: table.append(item)



class Product:
    def __init__(self, name, description, category, brand):
        global id
        id += 1
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.brand = brand

    def create(self):
        insert_into(self, products_table)

    # # DESPUES DE DEFINIR __INIT__ PODEMOS DEFINIR MAS METODOS
    # # Y DESPUES PUEDO USAR ESOS METODOS CON .READ
    # def read(self):
    #     return select(table=PRODUCTS_LIST, where=[("id", self.id)])


fregona = Product(
    brand= "Mileda",
    name= "Fregona de microfibra",
    description= "Fregona.....",
    category= "Productos de limpieza"
    )

print(fregona.name)

print("First: ", products_table)

fregona.create()

print("Second: ", products_table)

