import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker
import random
from django.contrib.auth.models import User
from products.models import Product , Review , Brand , ProductImages


def add_brand(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpeg','5.jpeg','6.png','7.png']
    for _ in range(n):
        Brand.objects.create(
            name = fake.name() ,
            image = f"brands/{images[random.randint(0,5)]}"
        )

    print(f"{n} Brands Was Added")

def add_products(n):
    fake = Faker()
    flags =["New","Sale","Feature"]
    brands = Brand.objects.all()
    images = ['1.jpg','2.png','3.jpeg','4.jpg','5.jpg','6.jpeg','7.jpeg','8.jpg','9.jpg','10.jpeg','11.jpeg','12.jpg','13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpeg','19.jpeg','20.jpeg']
    for _ in range(n):
        Product.objects.create(
            name = fake.name() ,
            image = f"products/{images[random.randint(0,5)]}",
            price = round(random.uniform(20.99,99.99),2),
            subtitle = fake.text(max_nb_chars = 350),
            description = fake.text(max_nb_chars = 4000),
            sku = random.randint(1000,1000000),
            quantity = random.randint(5,100),
            flag = random.choice(flags),
            brand = random.choice(brands)
        )

    print(f"{n} Products Was Added")

def add_products_images(n):
    products = Product.objects.all()
    images = ['1.jpg','2.png','3.jpeg','4.jpg','5.jpg','6.jpeg','7.jpeg','8.jpg','9.jpg','10.jpeg','11.jpeg','12.jpg','13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpeg','19.jpeg','20.jpeg']
    for _ in range(n):
        ProductImages.objects.create(
            image = f"products/{images[random.randint(0,18)]}",
            product = random.choice(products)
        )
    print(f"{n} Products Images Was Added")


def add_users(n):
    fake = Faker()
    for _ in range(n):
        User.objects.create(
            username =fake.name() ,
            email = fake.email(),
            password = '123456'
        )

    print(f"{n} Users Was Added")


def add_review(n):
    fake = Faker()
    users = User.objects.all()
    product = Product.objects.all()

    for _ in range(n):
        Review.objects.create(
            user = random.choice(users) ,
            product = random.choice(product) ,
            review = fake.text(max_nb_chars = 100) ,
            rate = random.randint(1,5)
        )


    print(f"{n} Reviews Was Added")



# add_brand(100)
# add_products(1000)
# add_users(10)
# add_review(2000)
add_products_images(2000)









































