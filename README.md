# flaskswaggerapi

This is a simple app that utilizes Flask and flasgger to show basic API use. Flasgger has the 
Swagger UI embedded in it. 

To begin 

docker build yourname/dockerfile . 

The dockerfile has 5000 exposed, and has flask set to run on 0.0.0.0 by default. 

When you are ready to begin 

docker run -p 5000:5000 -it yourname/dockerfile /bin/ash 

(Bash is also installed in this container - feel free to substitute) 


In addition, you can also pull kenlavoie/flaskapi, and use that with the above command vs building yourself 

 
