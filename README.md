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
OPCIÓN A: voy a guardar esas contraseñas en memoria, y cuando cierre sesión se borrará lo que haya puesto en memoria
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

REUTILIZACIÓN DE HASH PARA CONTRASEÑAS

- en la tabla de contraseñas tendremos


CONTRASEÑA | SALT
-------------------
Carmen.1*  | salt

lo que haré será calcular el hash de la contraseña + salt

antes de calcular el hash le daré un slat
EJEMPLO:
- Contraseña de Carmen1.* = H3?_1fM3* -> H(SALT || contraseña) -> lo guardo en la base de datos
- CON SALT -> 19/--3/JC: --------------> H(SALT || contraseña) ->  no es el mismo! no coincide con el salt que le di!!!! -> tengo que guardar el salt-> lo cifro?
		pensado para q los hashes sean distintos: guardo el salt tal cual en mi base de datos (guardo cada salt asociado a cada usuario)
yo asigno un salt aleatorio distino a cada una de las personas

- el salt no puede ser corto, porque si no sería demasiado fácil
- el usuario va a tener siempre el mismo salt
- NO ES NECESARIO RENOVAR LOS SALT (aunque debería hacerse -> si lo haces, mejor)
- hay que comprobar que el salt es aleatorio -> NO ES UN NÚMERO: ES UN VALOR -> ASCII, etc
--------------------------------------------------------------------------------------------------------------------------------------------------------
NONCE (= UN VALOR PSEUDO-ALEATORIO) (necesito que mi salt sea un valor pseudo-aleatorio, así que utilizaré los nons para ello)
- Autenticación
- IV
- Hash

semilla -> ALGORITMO -> valor pseudo-aleatorio
---------------------------------------------------------------------------------------------------------------------------------------------------------
SEGURIDAD:
- CONFIDENCIALIDAD -> CIFRADO/DESCIFRADO
- INTEGRIDAD -> HASH
- AUTENTICACIÓN -> COMBINAR DE ALGUNA MANERA LAS DOS COSAS ANTERIORES => CIFRADO AUTENTICADO
--------------------------------MUY RECOMENDABLE USAR HASH CIFRADO ----------------------------------
# CIFRADO AUTENTICADO:
Distintos modelos, pero nosotros veremos dos
Pretendo cifrar, verificar integridad y además autenticar.
busco que el cifrado esté autenticado
-- MODELO 1
Texto en claro
|<- klave
Cifrado

Texto en claro || H(TeC)

remix: voy a usar la clave del cifrado para hacer un resumen

HASH AUTENTICADO != HASH NORMAL
Texto en claro --------
|<----Klave---------->|
Cifrado               |
|                     |
----------|---------Hx(TeC)
          |
	C||Hx(TeC)

-- MODELO 2
M
|
|<----K
|	|down
C----------->Hx(C)
|		  |
---------------
	C Hx(C)


en la librería cryptography, HMAC ES ESTO -> INVESTIGARLO
