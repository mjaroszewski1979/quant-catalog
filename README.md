## Quant Catalog
### This is a Python application powered by Django and its Object-Relational Mapper to provide convenient access to stored data. In fact, Django's ORM is just a pythonical way to create SQL to query and manipulate your database and get results in a pythonic fashion. In this particular case users are able to view different trading strategies and related financial markets. After completing the registration subscribers can login and are now able to create their own investment strategy. To delete records from the database users need to be added to special group and granted permissions by the website administrator.

--------------------------------------------------

### Features:
* Working with template inheritance mechanism to build a base “skeleton” template that contains all the common elements and defines blocks that child templates can override
* Inserting images with dynamic path by utilizing built-in 'add' filter designed to format template variables
* Taking full advantage of Django's built-in features like cross-site request forgery protection to ensure safe data transfer in web forms to a database
* Associating multiple records in a table with multiple records in another table ( many-to-many relationship ) to achieve optimal ORM performance
* Displaying stored data with variation because of the fact that many-to-many relationships can be queried using lookups across relationships
* Using Q objects to achieve complete control over the complex queries necessary when constructing extensive search functionality
* Applying GroupRequiredMixin provided by a third-party module - django-braces - to ensure that the requesting user is in the group specified
* Breaking logic into smaller parts by adding various new Django applications to an existing project 
* Writing as much functionality as possible in models or utility files instead of views 
* Serving static files with WhiteNoise to accomplish high performance and efficiency without depending on nginx, Amazon S3 or any other external service
* Storing app’s secure credentials in environment variables
--------------------------------------------------

### Code Coverage:

<img src="https://github.com/mjaroszewski1979/quant-catalog/blob/main/cov_report.png">

### Docker info:
* Pull an image from my Docker Hub - click on the icon below
* Create and start a container 
* Pass environment variables to your container
  * with the -e flag or using .env file

```
docker run -p 8000:8000 -e SECRET_KEY="<your secret key>" <imagename>

```
```
docker run -p 8000:8000 --env-file .env <imagename>

```

--------------------------------------------------


![caption](https://github.com/mjaroszewski1979/quant-catalog/blob/main/mockup.png)
  
  Live | Code | Docker | Technologies
  ---- | ---- | ------ | ------------
  [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/heroku_g.png">](https://quantcatalog.herokuapp.com) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/quant-catalog) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_g.png">](https://hub.docker.com/r/maciej1245/quant-catalog) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/htmlup.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/js1.png"> 

