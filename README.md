# Gabriel Herrera y Neliad Abarca
¿que problema resualve el codigo? 
este codigo resuelve un sistema de adopcion para una veterinaria, mas especificamente el centro de adopcion de esta misma. 
¿a que tipo de usuarios esta dirigido? 
este etaria dirigido a usuarios los cuales quieran adoptar animalitos uwu 
En el codigo decidimos realizar un centro de adopcion, en el cua primcipalmente muestra un menu por pantalla para el  usuario-adoptante, lo hace escoger una de las opciones de animales "disponibles" en adopcion, despues de escoger uno y  ver por el sistema si esta "dispobile" muestra por consola al usuario otro mini menu en el cual le pide sus datos para poder confirmar la adopcion de el animal adoptado
en el codigo como tal se dejaron registrados los cometarios, donde se puede ver el uso de clases,objetos, herencia, en encapculamineto, polimorfismo y para realiazr este codigo nos estuvimos guiando con guias anteriormente realizadas en clase e IA (la del Visual)
conceptos utilizados
Para empezar, usamos la Abstracción al crear Mascota como un molde general al final, nadie adopta una mascota sino un animal concreto.
En la Herencia, donde Perro y Gato heredan al tiro los datos básicos (nombre, edad y peso) de ese molde para no andar repitiendo código, y solo les agregamos lo suyo, como la raza o el color.
El Polimorfismo hace toda la magia en el centro de adopción asi el sistema solo le pide a la mascota hacer_sonido() sin importarle qué animal sea, y el código hara lo suyo si es un perro para tirar un Guau o un gato para un Miau y al final, todo se mantiene seguro gracias al Encapsulamiento con esos guiones bajos en los atributos como _adoptado, que son como un escudo para que nadie cambie los datos a la fuerza desde fuera, sino a través de funciones ordenadas y seguras.
