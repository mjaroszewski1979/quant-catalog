## Quant Catalog
### This is a Python-based application designed for quantitative finance enthusiasts and professionals. This repository includes a collection of trading algorithms and data analysis tools, built using the Django framework and various financial data sources. The project aims to provide users with robust tools for backtesting and analyzing trading strategies.

--------------------------------------------------

### Features
* Working with template inheritance mechanism to build a base “skeleton” template that contains all the common elements and defines blocks that child templates can override
* Inserting images with dynamic path by utilizing built-in 'add' filter designed to format template variables
* Taking full advantage of Django's built-in features like cross-site request forgery protection to ensure safe data transfer in web forms to a database
* Associating multiple records in a table with multiple records in another table ( many-to-many relationship ) to achieve optimal ORM performance
* Displaying stored data with variation because of the fact that many-to-many relationships can be queried using lookups across relationships
* Using Q objects to achieve complete control over the complex queries necessary when constructing extensive search functionality
* Applying GroupRequiredMixin provided by a third-party module - django-braces - to ensure that the requesting user is in the group specified
* Breaking logic into smaller parts by adding various new Django applications to an existing project 
* Writing as much functionality as possible in models or utility files instead of views 
* Storing app’s secure credentials in environment variables

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/mjaroszewski1979/quant-catalog.git
    cd quant-catalog
    ```
2. Create a Virtual Environment:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply Migrations and Start the Server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

### Usage
* Access the Application: Open your browser and navigate to http://127.0.0.1:8000/.
* Explore Features: Use the web interface to interact with the trading algorithms and data analysis tools.

### Testing
Unit Tests:
```bash
python manage.py test
```
Code Coverage:
```bash
coverage run -p manage.py test
coverage combine
coverage html
```
### Code Coverage:

<img src="https://github.com/mjaroszewski1979/quant-catalog/blob/main/cov_report.png">

### Docker info:
* Pull an image from my Docker Hub - click on the icon below
* Create and start a container 
* Pass environment variables to your container
  * with the -e flag or using .env file

```bash
docker run -p 8000:8000 -e SECRET_KEY="<your secret key>" <imagename>
```
```bash
docker run -p 8000:8000 --env-file .env <imagename>
```

### Technologies Used
* Django: Framework for building the application.
* HTML5UP!: Responsive and visually appealing HTML templates.
* Docker: Containerization for easy deployment.
* Selenium: Automated browser testing to ensure application functionality.
* WhiteNoise: Serves static files efficiently without external services.

### Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

### Contact
For any inquiries or issues, please contact https://github.com/mjaroszewski1979/

--------------------------------------------------


![caption](https://github.com/mjaroszewski1979/quant-catalog/blob/main/mockup.png)
  
Code | Docker | Technologies
---- | ------ | ------------
[<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/quant-catalog) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_g.png">](https://hub.docker.com/r/maciej1245/quant-catalog) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/htmlup.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/js1.png"> 

