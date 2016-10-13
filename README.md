Proyecto TEST_LAMBDA

Este proyecto incluye el src y varios test unitario de lo que sería una lambda con su parte de testeo unitario. Este proyecto está basado en el enlace inferior, para probarlo en AWS ver el texto completo (además sirve para información adicional):
http://www.giantflyingsaucer.com/blog/?p=5730

--------------------------

Testeo de lambdas

Para testear lambda hay diversas posibilidades dependiendo del alcance y del lenguaje de programación usado.

Lenguajes de programación

Para Java:
-Con el AWS SDK for Java, AWS SDK Lambda de runtine y el plugin de Eclipse de AWS se puede crear rápidamente una función Java con sus test con el esqueleto que proporciona de base.

Los test unitarios se hacen fácilmente usando JUnit llamando al método de la función Lambda dentro del test. Se puede hacer Assert con la salida de la llamada y para la entrada se puede probar mappeando la entrada mediante un JSON que puede ser el JSON de un servicio de AWS o JSON para  una clase POJO.

En el siguiente enlace hay un ejemplo: 
https://java.awsblog.com/post/TxWZES6J1RSQ2Z/Testing-Lambda-functions-using-the-AWS-Toolkit-for-Eclipse

Para los test de integración no se ha encontrado nada en Java. 

Para python:
Para python existe este blog donde dice que para hacer testing con placebo y boto3.
Según dice puedes hacer registrar llamadas al SDK con una sesión real, guardar la respuesta y después testear la lambda-funcional en un entorno de testeo usando la respuesta guardada. Mejor explicado:
https://serverless.zone/unit-and-integration-testing-for-lambda-fc9510963003#.rujnqhsyr

También existe un framework para desarrollar, crear y testear todas las lambdas en python del proyecto:
https://github.com/sportarchive/aws-lambda-python-local

Para NodeJS:
Hay un blueprint de lambda llamado "unit and load test harness Lambda" (y que llamaremos aquí como lambda-test o lambda-integración) disponible en AWS que consiste en una lambda que llama a la lambda-funcional que queremos probar y posteriormente guarda el resultado de la operación en una tabla de DynamoDB.
Hay una explicación completa al final del siguiente enlace de blog en “unit and load testing” donde se explica mejor: https://aws.amazon.com/blogs/compute/microservices-without-the-servers/

En este enlace explica cómo es el esquema de JSON para llamar a lambda-test:
https://aws.amazon.com/blogs/compute/serverless-testing-with-aws-lambda/

Finalmente se tiene este tutorial donde explica como diseñar unas lambdas de forma óptima para testearlas:
https://claudiajs.com/tutorials/designing-testable-lambdas.html

Y si quieres ver una guía completa sobre lambdas, en este blog lo explican perfectamente:
https://www.npmjs.com/package/learn-aws-lambda

Integración Continua

Existen varios proyectos relacionados con Lambda e integración continua que simplemente lo que hacen es sustituir a las herramientas de integración continua que ya existen (Jenkins, por ej) usando las lambdas como orquestadores del proceso de build y deploy. Son:
Lambci: https://github.com/lambci/lambci
Serverless: https://github.com/serverless/serverless

Para Jenkins se ha encontrado lo siguiente:
Implantación usando Jenkins de Lambda después de commit https://aws.amazon.com/blogs/compute/building-testing-and-deploying-java-applications-on-aws-lambda-using-maven-and-jenkins/
Plugin de AWS Lambda para levantar y ejecutar lambdas https://github.com/jenkinsci/aws-lambda-plugin
Otra implantación usando Jenkins y Grunt https://aws.amazon.com/blogs/compute/continuous-integration-deployment-for-aws-lambda-functions-with-jenkins-and-grunt-part-1/


Conclusión:
La conclusión es que no hay ningún framework para test de integración de lambda. Como son proyectos con una funcionalidad atómica (autosuficientes con su entrada y su salida) con los JUnit y probando una vez en un entorno local es más que suficiente para probar su correcto funcionamiento.

Una de las formas que creemos que se podría tener un entorno de integración es la de crear una pequeña librería “lambda-integración” con la lambda de nodejs (o una ad-hoc). De esta forma hay dos posibilidades:

1. Si miramos los enlaces de Jenkins se podría realizar unos pasos para que fuese integración continúa con los test (a)). Por ejemplo:  
La librería de test de integración se introduciría como dependencia en el proyecto de la lambda-funcional y se crea una llamada a esta lambda.
Se hace un commit de la lambda-funcional
Jenkins lo detecta y lanza los test unitarios de la funcionalidad y el test de integración con su JSON (finalmente un test unitario del proyecto que levanta una lambda-integración con los datos del JSON necesarios del evento de la lambda-funcional).
Sube la nueva versión a AWS en caso correcto de todo.

2. Con el plugin de Jenkins (b)) y la lambda-integración subida en AWS, en cada build se podría ejecutar TODOS los lambdas nuevos y antiguos haciendo X llamadas de lambda-integración, tantas como lambdas-funcionales haya con el JSON del evento correspondiente a la lambda-funcionalidad que se ejecuta en este momento.
