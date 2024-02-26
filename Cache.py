class Cache:
    def __init__(self):
        self.cache_data = {}

    def buscar_cache(self, busqueda):
        if busqueda in self.cache_data:
            return True, self.cache_data[busqueda]
        else:
            return False, None

    def añadir_cache(self, busqueda, result):
        self.cache_data[busqueda] = result


cache = Cache()

def buscar_precio(articulo):
    inventario = {
        "agua": 100,
        "pan": 50,
        "leche": 80,
        "manzana": 20,
        "banana": 15
    }

    if articulo in inventario:
        print("Buscando en el inventario...")
        print("Cargando inventario...")
        return inventario[articulo]
    else:
        print("Este articulo no esta a la venta")
        return 



def buscar_en_cache_o_ejecutar(parametro):
    encontrado, resultado = cache.buscar_cache(parametro)
    if encontrado:
        print("Obteniendo resultado del caché para la busqueda de:", parametro, "este precio es:", resultado)
        
    else:
        resultado = buscar_precio(parametro)
        cache.añadir_cache(parametro, resultado)
        print("El resultado de la consulta para '" + parametro + "' es:", resultado)
    return resultado


buscar_en_cache_o_ejecutar("agua")
buscar_en_cache_o_ejecutar("pan")
buscar_en_cache_o_ejecutar("agua")
