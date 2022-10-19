# Face to learn
Proyecto de criptografía de Alicia Benítez y Valentina Cataldo

Entrega: 4 de Noviembre -> día anterior a la defensa de la práctica
Esa semana también tenemos examen

## TO-DO LIST
- Creación, lectura y modificación de jsons asignatura-examenes y revisiones
- clases y funciones definidas abajo
- interfaz para poder ejecutar main
- cifrado de jsons + datos personales + contraseñas
-----------------------------------------------------
## Clases
- Profesores
- Aulas para cada asignatura
- Alumnos
- Archivo tipo examen
- Archivo tipo solución de examen

## Profesores
- Datos personales
- Nombre de usuario y contraseña
- Clases que imparten
- DNI
- Subir examen
- Subir solución
- Cambiar datos

## Alumnos
- Clases a las que asisten
- Datos personales
- Nombre de usuario y contraseña
- NIA
- Ver examen
- Pedir revisión
- Generador de nia

## MAIN
1. Loggearse 
2. Según el usuario que se haya metido, habrá una sección de clases y otra de revisiones
3. En cada sección habrá un botón OPERACIONES donde se podrán ejecutar los métodos de la clase de python

---------------------------------------------------------
# NOTAS
Para ver cualquier json, pedimos al alumno el nia

MEMORIA
- ANALISIS
  - Objetivos
  - funcionalidades
  - cifrado/ des...
  - hash/maac (?)
- CIFRADO/DES...
- HASH/MAAC

CÓDIGO

TRIÁNGULO CIA -> MECANISMOS
- Confidencialidad -> cifrado
- Integridad -> hash, firma (notas + exámenes usar hash, transferir y volver a hacer hash y comprobar que es igual al inicial)
- Disponibilidad
- 
- no repudio -> firma
- autenticación -> cifrado, hash, firma


hay que hacer un json con una tablita incluyendo datos personales del usuario y las cosas que queramos cifrar/no (OJO: SI GUARDAMOS ALGO QUE QUEREMOS CIFRAR, GUARDALO CIFRADO/CON FUNCIÓN RESUMEN/HASH)
Tengo que tomar decisiones acerca de qué contraseñas uso y cómo las voy a cifrar
OPCIÓN A: voy a guardar esas contraseñas en memoria, y cuando cierre sesión se borrará lo que haya puesto en memori
OPCIÓN B: como sé que es peligroso guardarlo en memoria (ojo que estamos en un navegador) pues en vez de guardar la contraseña, se la pido al usuario

EL PROFE NO QUIERE VER CONTRASEÑAS ESCRITAS EN NINGÚN SITIO
INVESTIGAR:
SALT
Derivación K
Esas dos cosas están en la libreria cryptographic.io o como se escriba xd. También hay videos en youtube

NO usar la clave, pero usar algo basado en la clave




MANDAR AL PROFE:
DOCUMENTO INCLUYENDO
- OBJETIVOS
- FUNCIONALIDADES
- CIF/dESC
- HASH /  MAAC

TRAER HECHO 
- FUNCIONALIDADES
- CIF DESC SIMETRICO (NO ASIMETRICO)
- AL MENOS PENSAR HASH MAAC
