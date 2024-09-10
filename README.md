Nama : Shaney Zoya Fiandi

NPM : 2306215923

Kelas : PBP A

Tautan PWS : https://pbp.cs.ui.ac.id/web/project/shaney.zoya/yarnsie

## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)**

***a. Membuat sebuah proyek Django baru***

1. Sebagai langkah awal, saya membuat repositori baru di GitHub dengan nama *yarnsie*. Di laptop, saya juga membuat direktori lokal bernama *yarnsie* yang telah diinisialisasi dengan git.

2. Di terminal *yarnsie*, langkah pertama yang saya lakukan adalah membuka terminal dan membuat virtual environment dengan perintah "python3 -m venv env", kemudian mengaktifkan virtual environment tersebut menggunakan "source env/bin/activate".

3. Selanjutnya, saya menginstal beberapa dependensi yang tercantum dalam file requirements.txt, seperti django, gunicorn, whitenoise, psycopg2-binary, requests, dan urllib3. Dependensi ini diperlukan agar proyek dapat berjalan dengan baik. Instalasi dilakukan dengan menjalankan perintah "pip install -r requirements.txt".

4. Langkah terakhir, saya membuat proyek Django bernama yarnsie dengan menjalankan perintah "django-admin startproject yarnsie ." di terminal. Proses ini menghasilkan sebuah file bernama "manage.py".

***b. Membuat aplikasi dengan nama main pada proyek tersebut***

1. Saya memulai dengan membuka terminal dan mengakses direktori yarnsie menggunakan perintah cd path yarnsie untuk memastikan saya berada di lokasi proyek yang tepat.

2. Langkah berikutnya adalah mengaktifkan virtual environment dengan mengetikkan perintah "source env/bin/activate" agar lingkungan pengembangan khusus proyek ini siap digunakan.

3. Setelah lingkungan aktif, saya membuat aplikasi baru bernama main dengan menjalankan "python manage.py startapp main". Ini menghasilkan folder main yang berisi struktur dasar aplikasi Django yang dibutuhkan.

4. Terakhir, saya memastikan aplikasi main terhubung dengan proyek Django dengan menambahkan 'main' ke daftar INSTALLED_APPS di file settings.py. Langkah ini penting agar aplikasi main dikenali dan dapat berfungsi dalam proyek utama yarnsie.

***Melakukan routing pada proyek agar dapat menjalankan aplikasi main***
1. Pertama-tama, saya mengakses file urls.py di proyek yarnsie.

2. Kemudian, saya menambahkan kode berikut ke dalam file urls.py:

```from django.contrib import admin
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

3. Perintah from django.urls import path, include berfungsi untuk membawa rute URL dari aplikasi main ke dalam file urls.py proyek yarnsie, sehingga memungkinkan pengaturan URL aplikasi tersebut dalam proyek utama.

***Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut(name, price, description)***

Di file `models.py` pada aplikasi **main**, saya mengimpor `models` dari `django.db`. Selanjutnya, saya mendefinisikan sebuah kelas bernama `Product` yang mewarisi dari `models.Model`. Ini digunakan untuk membuat model basis data di Django, di mana setiap atribut dalam kelas tersebut akan menjadi kolom dalam tabel di basis data.
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
```
 
 ***Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.***
1. Di file views.py aplikasi main, saya membuat fungsi show_main yang menyimpan dictionary dengan pasangan key dan value. Key digunakan dalam template HTML untuk mengakses data, sedangkan value berisi informasi yang ingin ditampilkan.
```
from django.shortcuts import render
from .models import Product

def main(request):
    context = {
        'name': 'Shaney Zoya Fiandi',
        'npm': '2306215923',
        'app_name': 'Yarnsie',
        'class': 'PBP C',
    }
    return render(request, 'main.html', context)

def products(request):
    product_list = Product.objects.all()
    context = {
        'products': product_list,
    }
    return render(request, 'products.html', context)
```

2. from django.shortcuts import render digunakan untuk merender template HTML dengan data context yang disediakan, yang kemudian ditampilkan kepada pengguna.

3. from .models import Product mengimpor model Product dari file models.py di aplikasi main. Model ini memungkinkan kita untuk mengambil data produk dari basis data.

4. Berikut adalah template HTML yang saya buat untuk menampilkan nama aplikasi, nama, npm, dan kelas:
```
<!DOCTYPE html>
<html lang="en">
<head>
    {% load static %}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ app_name }}</title>
    <link rel="stylesheet" href="{% static 'main/main.css' %}">
</head>
<body>
    <div class="creator-info">
        <p>Created by: {{ name }} - {{ npm }} - {{ class }}</p>
    </div>

    <div class="welcome">
        <h3>Welcome to {{ app_name }}.</h3>
    </div>

    <div class="products">
        {% for product in products %}
        <div class="product-box">
            <h1>{{ product.name }}</h1>
            <p>Description: {{ product.description }}</p>
            <p class="price">Price: Rp{{ product.price }}</p>
            <p class="rating">Rating: {{ product.rating }} / 10</p>
            <p class="stock">Stock Left: {{ product.stock }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```
5. Key dalam context diakses menggunakan kurung kurawal ganda {{...}} dalam template HTML, yang memungkinkan data dari context ditampilkan di halaman web Django.

***Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py***
1. Pertama-tama, saya membuat file urls.py di dalam direktori main.

2. Selanjutnya, saya mengisi file urls.py dengan kode berikut:
```
from django.urls import path
from . import views
from main.views import main
from main.views import products

urlpatterns = [
    path('', views.main, name='main'),
    path('', views.products, name='products'),
]
```
***Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet***
1. Setelah masuk ke akun PWS, saya membuat proyek baru dengan nama "yarnsie".
   
2. Selanjutnya, saya menyimpan Project Credentials dan Project Command yang diperlukan untuk login dengan username dan password ketika diminta oleh terminal.
  
3. Di file settings.py proyek Django yarnsie, saya menambahkan URL deployment PWS ke dalam daftar ALLOWED_HOSTS.

```
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "shaney-zoya-yarnsie.pbp.cs.ui.ac.id"]
```

## **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
https://drive.google.com/file/d/18Y-OE_a3bRIGe3q1DHLVUiE9LLVmX8H9/view?usp=sharing

1. Permintaan Client: Pengguna membuka URL di browser mereka, yang mengirimkan permintaan ke server Django. Permintaan ini bisa berupa permintaan untuk sebuah halaman web atau data tertentu.

2. urls.py: Django menangani permintaan dengan mencocokkan URL yang diminta dengan pola yang ada di urls.py. Setelah ditemukan, Django mengarahkan permintaan tersebut ke fungsi yang relevan di views.py.

3. views.py: File views.py bertanggung jawab untuk menjalankan logika aplikasi, memproses data, dan jika perlu, berinteraksi dengan database melalui models.py.

4. models.py: Di sini, models.py bertugas berkomunikasi dengan database untuk mengambil atau menyimpan data yang diperlukan oleh views.py.

5. Template HTML: Data yang diproses di views.py kemudian dirender ke dalam template HTML, menghasilkan halaman web yang siap ditampilkan.

6. Respon Client: Django mengirimkan halaman web yang telah dirender kembali ke browser pengguna untuk ditampilkan.

Keterkaitan antara urls.py, views.py, models.py, dan file HTML:
1. urls.py bertindak sebagai pengarah, mengarahkan permintaan ke fungsi di views.py.
   
3. views.py melaksanakan logika aplikasi dan, jika diperlukan, mengakses data dari models.py yang berhubungan dengan database.
  
5. models.py mengelola data yang diminta oleh views.py dan mengirimkan data tersebut kembali.
  
7. views.py kemudian menggunakan template HTML untuk merender data dan mengirimkan hasilnya sebagai respons ke client.

## **Jelaskan fungsi git dalam pengembangan perangkat lunak!**
Berikut adalah beberapa fungsi utama Git dalam pengembangan perangkat lunak:

- **Melacak Perubahan:** Git mencatat setiap perubahan yang dibuat pada kode sumber. Ini memungkinkan pengembang untuk melihat riwayat perubahan, membandingkan versi, dan memahami bagaimana kode telah berkembang dari waktu ke waktu.

- **Menyimpan Versi Kode:** Dengan Git, Anda dapat menyimpan berbagai versi kode sumber. Ini memungkinkan Anda untuk kembali ke versi sebelumnya jika ada masalah dengan perubahan terbaru, atau untuk menguji fitur baru tanpa mempengaruhi kode stabil.

- **Kolaborasi Tim:** Git memudahkan kerja sama antar pengembang dengan memungkinkan beberapa orang bekerja pada bagian kode yang berbeda secara bersamaan. Git menyediakan fitur seperti branching dan merging, yang memfasilitasi penggabungan perubahan dari berbagai pengembang dengan cara yang terstruktur dan aman.

- **Branching dan Merging:** Git memungkinkan pengembang untuk membuat cabang (branch) yang terpisah dari kode utama. Ini berguna untuk mengembangkan fitur baru atau memperbaiki bug tanpa mempengaruhi kode utama. Setelah pengembangan selesai, cabang dapat digabungkan (merge) kembali ke cabang utama.

- **Manajemen Konfigurasi dan Deployment:** Git digunakan untuk mengelola konfigurasi aplikasi dan memudahkan proses deployment dengan menyediakan cara untuk menyimpan dan melacak konfigurasi yang berbeda dalam repositori.


## **Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
Django sering dipilih sebagai framework pemula dalam pembelajaran pengembangan perangkat lunak karena beberapa alasan:

- **Pendekatan "Batteries-Included":** Django mengikuti prinsip "batteries-included," artinya framework ini datang dengan banyak fitur built-in yang siap digunakan. Ini termasuk sistem autentikasi, panel admin, ORM (Object-Relational Mapping), dan banyak lagi. Dengan menyediakan banyak alat dasar, Django memudahkan pemula untuk memulai tanpa perlu mengonfigurasi berbagai komponen secara terpisah.

- **Dokumentasi yang Lengkap:** Django memiliki dokumentasi yang sangat lengkap dan jelas. Dokumentasi ini mencakup panduan, tutorial, dan referensi API yang memudahkan pemula untuk memahami dan menggunakan framework ini dengan efektif.

- **Konsistensi dan Struktur:** Django mempromosikan struktur proyek yang konsisten dan pola desain yang jelas. Ini membantu pemula untuk memahami bagaimana mengorganisir kode mereka secara efektif dan mengikuti praktik terbaik dalam pengembangan perangkat lunak.

- **Keamanan:** Django memiliki fokus yang kuat pada keamanan. Fitur-fitur built-in seperti perlindungan terhadap serangan CSRF (Cross-Site Request Forgery) dan XSS (Cross-Site Scripting) membantu pemula mempelajari praktik keamanan yang baik sejak awal.

- **Komunitas Aktif:** Django memiliki komunitas yang besar dan aktif. Dukungan komunitas ini mencakup forum, grup diskusi, dan berbagai sumber daya lainnya yang membantu pemula mendapatkan bantuan dan berbagi pengetahuan.

## **Mengapa model pada Django disebut sebagai ORM?**
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena ia menghubungkan objek Python dengan tabel dalam basis data relasional. Dengan ORM, pengembang dapat bekerja dengan objek Python untuk melakukan operasi basis data tanpa menulis query SQL secara langsung. Model Django menyediakan pemetaan otomatis antara atribut model dan kolom tabel, memungkinkan pengelolaan relasi antar tabel, serta validasi dan constraint data. ORM juga mempermudah migrasi skema basis data dengan menghasilkan skrip migrasi otomatis berdasarkan perubahan pada model, sehingga menyederhanakan dan mempercepat interaksi dengan basis data.
