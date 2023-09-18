## Ejercicio básico de sockets
Implementar un script servidor y un script cliente que hagan lo siguiente (con sockets UDP):

1. El servidor debe ponerse a la escucha en un puerto accesible.
2. El cliente debe enviar un mensaje al servidor.
3. El servidor debe decodificar el mensaje y mostrarlo por pantalla.

A tener en cuenta:

- El mensaje del cliente debe ir codificado en utf-8.
- El servidor debe decodificar el mensaje en ascii.
- Por la diferencia de encodings, el servidor debe manejar de alguna forma los errores de decodificación.

Prueba a 1) enviar desde el cliente la cadena "ñandú" para ver los errores de decodificación y a 2) ejecutar el ejercicio con otra persona (cada uno ejecutáis un script, el cliente o el servidor).
