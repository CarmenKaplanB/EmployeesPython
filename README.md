# Examen de Python.
 
> Python & Spring  :leaves:
 
Para poner en marcha este proyecto, siga las siguientes instrucciones:
 
* **Paso 1.** *Clonar el proyecto*.
En consola, escriba el siguiente comando.
 
~~~
git clone https://github.com/CarmenKaplanB/EmployeesPython.git
~~~
 
* **Paso 2.** *Instala los requerimientos*.
Dentro de este repositorio se encuentra un archivo nombrado requirements.txt. El cual contiene todas las librerías que fueron implementadas en este proyecto de Python. Para agregarlas a tu proyecto ejecuta el siguiente comando en terminal.
 
~~~
pip install -r requirements.txt
~~~
 
* **Paso 3.** *Ejecute el archivo nombrado requestPost.py*.
En el IDE de Visual Studio Code, abra el proyecto. Ubique la carpeta Employees, dentro de ella se encuentra un archivo nombrado "requestPost.py" ejecutelo desde el IDE.
 
* **Paso 4.** *Verifique la salida en consola*.
Cuando ejecutamos el archivo, deberá visualizarse una salida exitosa como la que se muestra en la siguiente imagen.
 
![Example](https://raw.githubusercontent.com/CarmenKaplanB/EmployeesPython/main/Screens/MuestraEjecucion.PNG "Example")
 
* **Paso 5.** *Confirme que los datos hayan sido insertados correctamente*.
En la aplicación de Postman, escriba la siguiente liga de prueba, en ella podemos visualizar los datos que fueron insertados:
~~~
http://localhost:8080/employee/listaemployee
~~~
Asegúrese que el método sea GET, como se muestra en la imagen.
 
![Example](https://raw.githubusercontent.com/CarmenKaplanB/EmployeesPython/main/Screens/MuestraEjecucionPostman.PNG "Example")
 
`Nota:`
 
Para implementar completamente el proyecto necesita al menos:
* Visual Studio Code.
* Python 3 o superior.
* Git.
* Spring 5.
* Java 8 o 11.
* Postman.

Adicionalmente, necesitará implementar el proyecto: `spring-security-jwt`. Ubica el proyecto y la guía de compilación y ejecución a continuación.

Enlace: [Repositorio spring-security-jwt.](https://github.com/CarmenKaplanB/EmployeesJava)

### ¡Listo! Hemos terminado con éxito.
