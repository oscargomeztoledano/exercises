## Ejercicio con el módulo struct
Implementar un script servidor y un script cliente que hagan lo siguiente (con sockets UDP):

- Cliente: enviar un mensaje al servidor compuesto por un entero de 16 bits y un string aleatorio. El entero indica la longitud del string.
- Servidor: recibir el mensaje del cliente, decodificarlo y mostrarlo por pantalla.

Ten en cuenta que la longitud del string es variable, por lo que el servidor debe decodificar el mensaje de forma dinámica.
