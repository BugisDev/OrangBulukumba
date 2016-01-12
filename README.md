##CARA MENJALANKAN APLIKASI ORANGBULUKUMBA DI KOMPUTER ANDA

#Mempersiapkan alat untuk menjalankan aplikasi
- clone repository orangbulukumba
```
git clone https://github.com/BugisDev/OrangBulukumba
```
- Buka folder orangbulukumba dan buat virtual environment di dalam folder tersebut. Disini saya membuat environment dengan nama (env), Anda dapat membuat dengan nama yang berbeda sesuai keinginan anda.
```
cd OrangBulukumba
virtualenv env
```
- Pada aplikasi ini, saya menggunakan MYSQL-server sebagai database. Jadi, Anda harus membuat database dengan nama `orangbulukumba.com`. Nama database dapat dirubah pada file config/base.py, jadi anda dapat merubah sesuai keinginan anda.
```
>mysql -u root -p
[enter your password db]
>create database `orangbulukumba.com`
```
- Aktifkan virtual environment yang telah anda buat sebelumnya, kemudian install paket yang dibutuhkan untuk membuat aplikasi ini
```
source env/bin/activate
pip install -r requirements.txt
```
- Gunakan Flask-migrate untuk melakukan migrasi dari modeling yang ada pada aplikasi ini ke database yang telah anda buat sebelumnya.
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
- Pada aplikasi ini, terdapat Data default yang harus ada untuk menjalankan aplikasi ini, Jadi anda harus menambahkan ke database.
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

# Aplikasi OrangBulukumba siap dijalankan
```
python manage.py run
```

# Happy testing :)
