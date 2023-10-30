import json

# Cargar el diccionario desde el archivo
def cargar_diccionario():
    try:
        with open('reservas.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Guardar el diccionario en el archivo
def guardar_diccionario(diccionario):
    with open('reservas.json', 'w') as f:
        json.dump(diccionario, f)

# Agregar una reserva al diccionario
def agregar_reserva(fecha, hora, num_asistentes, nombre_cliente, telefono):
    diccionario = cargar_diccionario()
    if fecha in diccionario:
        print(f'Error: ya existe una reserva para la fecha {fecha}')
    else:
        diccionario[fecha] = {'hora': hora, 'num_asistentes': num_asistentes, 'nombre_cliente': nombre_cliente, 'telefono': telefono}
        guardar_diccionario(diccionario)
        print(f'Reserva agregada para la fecha {fecha}')
        
# Eliminar una reserva del diccionario
def eliminar_reserva(fecha):
    diccionario = cargar_diccionario()
    if fecha in diccionario:
        del diccionario[fecha]
        guardar_diccionario(diccionario)
        print(f'Reserva eliminada para la fecha {fecha}')
    else:
        print(f'Error: no existe una reserva para la fecha {fecha}')

# Listar todas las reservas
def listar_reservas():
    diccionario = cargar_diccionario()
    if not diccionario:
        print('No hay reservas')
    else:
        for fecha, reserva in diccionario.items():
            print(f'Fecha: {fecha}, Hora: {reserva["hora"]}, Número de asistentes: {reserva["num_asistentes"]}, Nombre del cliente: {reserva["nombre_cliente"]}, Teléfono: {reserva["telefono"]}')

# Ejemplo de uso
agregar_reserva('2022-01-01', '20:00', 4, 'Juan Pérez', '123456789')
agregar_reserva('2022-01-02', '21:00', 2, 'María Gómez', '987654321')
listar_reservas()