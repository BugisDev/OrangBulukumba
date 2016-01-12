##How to run OrangBulukumba app in yur Comp.

#Prepare some tools
- clone this repo
```
git clone https://github.com/BugisDev/OrangBulukumba
```
- Open OrangBulukumba directory and make virtualenvironment in it. in this case i use (env) as my virtual environment, You can use your name or others.
```
cd OrangBulukumba
virtualenv env
```
- In this app, i use mysql as my database. So, you must create a database with name orangbulukumba.com. I set it in Config in my app and you can cange it
```
>create database `orangbulukumba.com`
```
- Activate your environment and install requrements package to run this app
```
source env/bin/activate
pip install -r requirements.txt
```
- Use migrate to Migrate models in this app to Your Mysql-server
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
- I have default values in database that is in User_type column and Post_type Column. So you must add it in your mysql-server
```
>INSERT INTO `user_type` (`id`, `type`) VALUES
>(1, 'Super User'),
>(2, 'Admin'),
>(3, 'Author'),
>(4, 'Editor'),
>(5, 'User');


>INSERT INTO `post_type` (`id`, `post_type`, `created_by`, `description`) VALUES
>(1, 'PERTANYAAN', NULL, NULL),
>(2, 'KELUHAN', NULL, NULL),
>(3, 'KRITIK', NULL, NULL),
>(4, 'SARAN', NULL, NULL);
```

# You can Run this app now
```
python manage.py run
```

# Happy testing :)
