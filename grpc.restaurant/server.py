#!/usr/bin/python3


from concurrent import futures 
import json
import grpc
import restaurant_pb2
import restaurant_pb2_grpc

class Restaurant(restaurant_pb2_grpc.RestaurantServicer):
     
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
    def reservar(self, request, context):
        print("Client sent: '{}'".format(request.message))
        reserva=request.reservation
        date=reserva.date
        time=reserva.time
        number_of_diners=reserva.number_of_diners
        client_name=reserva.client_name
        phone=reserva.phone

        diccionario = self.cargar_diccionario()
        if date in diccionario:
            print(f'Error: ya existe una reserva para la fecha {date}')
            order_reply = restaurant_pb2.Response()
            order_reply.message = f'Error: ya existe una reserva para la fecha {date}' 
        else:
            diccionario[date] = {'time': time, 'number_of_diners': number_of_diners, 'client_name': client_name, 'phone': phone}
            self.guardar_diccionario(diccionario)
            print(f'Reserva agregada para la fecha {date}')
            order_reply = restaurant_pb2.Response()
            order_reply.message = f'Reserva agregada para la fecha {date}'

        return order_reply
    
    def cancelar(self,request,context):
        print("Client sent: '{}'".format(request.message))
        date=request.date
        diccionario = self.cargar_diccionario()
        if date in diccionario:
            del diccionario[date]
            self.guardar_diccionario(diccionario)
            print(f'Reserva eliminada para la fecha {date}')
            order_reply = restaurant_pb2.Response()
            order_reply.message = f'Reserva eliminada para la fecha {date}'
        else:
            print(f'Error: no existe una reserva para la fecha {date}')
            order_reply = restaurant_pb2.Response()
            order_reply.message = f'Error: no existe una reserva para la fecha {date}'
        return order_reply

    def listar(self,request,context):
        print("Client sent: '{}'".format(request.message))
        diccionario = self.cargar_diccionario()
        if not diccionario:
            print('No hay reservas')
            order_reply = restaurant_pb2.Response()
            order_reply.message = f'No hay reservas'
        else:
            for date, reserva in diccionario.items():
                print(f'Fecha: {date}, Hora: {reserva["time"]}, Número de asistentes: {reserva["number_of_diners"]}, Nombre del cliente: {reserva["client_name"]}, Teléfono: {reserva["phone"]}')
                order_reply = restaurant_pb2.Response()
                order_reply.message = f'Fecha: {date}, Hora: {reserva["time"]}, Número de asistentes: {reserva["number_of_diners"]}, Nombre del cliente: {reserva["client_name"]}, Teléfono: {reserva["phone"]}'
        return order_reply