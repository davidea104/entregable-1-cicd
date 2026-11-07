# Entregable 1: CI/CD

Primer entregable del curso de CI/CD. En este repositorio se presenta el trabajo realizado por:

- David Gustavo Moreno Morán | Angélica María Martínez Carmona 

- GitHub: [@davidea104](https://github.com/davidea104)
— GitHub: [@amcangelica](https://github.com/amcangelica)

Qué eventos configuraste para disparar tu workflow y por qué?
- Configuramos los eventos de push y de workflow_dispatch para que el workflow se ejecute cada que se haga un push a main o cuando se desee hacer una ejecución manual desde el panel de github 

¿Qué sistema operativo utiliza el runner ubuntu-latest y por qué puede ejecutar tu workflow aunque tu computadora sea Windows o macOS? ¿Qué relación tiene el runner con el shell de los pasos run?
-El runner ubuntu-latest utiliza una máquina virtual con Ubuntu Linux, mantenida por GitHub.El workflow no se ejecuta en la computadora personal, sino en la infraestructura de GitHub, crea temporalmente este entorno en sus propios servidores, ejecuta las tareas definidas y luego lo elimina, por eso da igual si es Windows o macOS. 
- El runner es el entorno donde se ejecuta el workflow, mientras que el shell es el intérprete de comandos que ejecuta cada instrucción definida en un paso run.

Menciona al menos 3 acciones pre-construidas del Marketplace de GitHub Actions no mencionadas en este material. Excluye actions/checkout, actions/setup-python, actions/upload-artifact y aws-actions/configure-aws-credentials, aunque alguna solo aparezca como ejemplo conceptual. Describe qué hacen y para qué sirven.
- actions/cache.
Hace: Permite almacenar y reutilizar dependencias, bibliotecas o archivos generados entre ejecuciones del workflow.
Sirve: Reduce significativamente los tiempos de ejecución porque evita descargar o instalar nuevamente las mismas dependencias en cada ejecución.
- github/codeql-action/analyze
Hace: Ejecuta análisis de seguridad estático sobre el código fuente utilizando CodeQL.
Sirve: Detecta vulnerabilidades, errores de programación y posibles problemas de seguridad antes de desplegar una aplicación.
- docker/build-push-action
Hace: Construye imágenes Docker y puede publicarlas automáticamente en un registro como Docker Hub o Amazon ECR.
Sirve: Facilita la automatización de procesos de contenerización y despliegue.

¿Qué es un secreto en GitHub Actions y para qué se usa? ¿Cómo lo usarías en tu workflow?
-Un secreto es una variable protegida que almacena información sensible, como contraseñas, tokens de acceso, claves API, credenciales de servicios en la nube y evita que estos datos aparezcan expuestos en el repositorio o en los archivos del workflow. Lo usaríamos para los valores que no se deben cambiar o modificar.

Reflexiona sobre el uso de GitHub Actions en tu flujo de trabajo diario. ¿Qué tareas automatizarías? ¿Por qué?
-David:
-Angelica: En mi trabajo diario lo utilizaría principalmente para ejecutar pruebas, validar la calidad del código, construir imágenes Docker y desplegar aplicaciones en AWS, porque son tareas frecuentes, repetitivas y propensas a errores cuando se realizan manualmente.