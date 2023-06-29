import psycopg2
import random
con=psycopg2.connect('dbname=ecommerce_db user=postgres port=5432 host=localhost password=Murad2004')

cur=con.cursor()


def show(cursor):
    cur.execute(query)
    length = 30
    print(*[desc[0].ljust(30) for desc in cursor.description], sep='')
    print('-'*140)
    result = cur.fetchall()
    for row in result:
        for col in row:
            print(str(col).ljust(length)[:37], end='')
        print()


# query="""
# CREATE TABLE seller(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50)
# );

# CREATE TABLE product(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(50) NOT NULL,
#     price NUMERIC NOT NULL,
#     seller_id INT,
#     CONSTRAINT fk_seller
#         FOREIGN KEY(seller_id)
#             REFERENCES seller(id)
#             ON DELETE CASCADE
# );
# CREATE TABLE tag(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(50) NOT NULL
# );


# CREATE TABLE customer(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50)
# );
# CREATE TABLE wishlist(
#     id SERIAL PRIMARY KEY,
#     customer_id INT,
#     CONSTRAINT fk_customer
#         FOREIGN KEY(customer_id)
#             REFERENCES customer(id)
#             ON DELETE CASCADE
# );
# CREATE TABLE wishlist_products(
#     id SERIAL PRIMARY KEY,
#     product_id INT,
#     customer_id INT,
#     CONSTRAINT fk_customer
#         FOREIGN KEY(customer_id)
#             REFERENCES customer(id)
#             ON DELETE CASCADE,
#     CONSTRAINT fk_product
#         FOREIGN KEY(product_id)
#             REFERENCES product(id)
#             ON DELETE CASCADE
# );
# CREATE TABLE review(
#     id SERIAL PRIMARY KEY,
#     rate NUMERIC,
#     customer_id INT,
#     product_id INT,
#     CONSTRAINT fk_customer
#         FOREIGN KEY(customer_id)
#             REFERENCES customer(id)
#             ON DELETE SET NULL,
#     CONSTRAINT fk_product
#         FOREIGN KEY(product_id)
#             REFERENCES product(id)
#             ON DELETE CASCADE
# );

# CREATE TABLE product_tags(
#     id SERIAL PRIMARY KEY,
#     product_id INT,
#     tag_id INT,
#     CONSTRAINT fk_product_tag
#         FOREIGN KEY(product_id)
#             REFERENCES product(id)
#             ON DELETE CASCADE,
#     CONSTRAINT fk_tag_product
#         FOREIGN KEY(tag_id)
#             REFERENCES tag(id)
#             ON DELETE CASCADE
# );

# """

customer_data=[{
  "name": "Halette Milberry"
}, {
  "name": "Barby Wastell"
}, {
  "name": "Lexie Dragon"
}, {
  "name": "Rosamond Kynston"
}, {
  "name": "Christen Keyson"
}, {
  "name": "Madeline Knottley"
}, {
  "name": "Ruby Loachhead"
}, {
  "name": "Aeriel Knowlden"
}, {
  "name": "Hedy Phillipp"
}, {
  "name": "Harmonia Freckelton"
}, {
  "name": "Rossy Mustchin"
}, {
  "name": "Dulcie Higgonet"
}, {
  "name": "Kala Caldroni"
}, {
  "name": "Nessie Lavery"
}, {
  "name": "Shanta Polotti"
}, {
  "name": "Berty Dampier"
}, {
  "name": "Frans Fosdike"
}, {
  "name": "Lotty Corkhill"
}, {
  "name": "Randie Lawther"
}, {
  "name": "Husain Reye"
}, {
  "name": "Fayre McPhillimey"
}, {
  "name": "Susette Raitie"
}, {
  "name": "Sela Elsmore"
}, {
  "name": "Taddeo Enterlein"
}, {
  "name": "Valma Hutchence"
}, {
  "name": "Micki Gorelli"
}, {
  "name": "Arabelle Najera"
}, {
  "name": "Annemarie Crenage"
}, {
  "name": "Nara Whight"
}, {
  "name": "Borg Downage"
}, {
  "name": "Sheri Moreman"
}, {
  "name": "Hew Dignum"
}, {
  "name": "Jacquenette Caygill"
}, {
  "name": "Margot Cradduck"
}, {
  "name": "Adele Snassell"
}, {
  "name": "Caryl Pevsner"
}, {
  "name": "Gannon Northrop"
}, {
  "name": "Artemas Goodlip"
}, {
  "name": "Lawrence Crockatt"
}, {
  "name": "Sheelagh Cosely"
}, {
  "name": "Doralyn Tripett"
}, {
  "name": "Grove Learman"
}, {
  "name": "Rosanna Pretious"
}, {
  "name": "Earle Sapshed"
}, {
  "name": "Guido Onyon"
}, {
  "name": "Rolfe Panner"
}, {
  "name": "Hilly Dashwood"
}, {
  "name": "Orland Shutt"
}, {
  "name": "Kipp Blacksell"
}, {
  "name": "Umberto Chaman"
}]

# query="""
# INSERT INTO customer(name) VALUES(%s);
# """

# for i in customer_data:
#     cur.execute(query,(i['name'],))


# query="SELECT * FROM customer"


seller_data=[
    {
  "name": "Si Friary"
}, {
  "name": "Scotty Ludlem"
}, {
  "name": "Randa Ifill"
}, {
  "name": "Vanessa Fay"
}, {
  "name": "Tamarra Tossell"
}, {
  "name": "Kennett Dumper"
}, {
  "name": "Jessika Stienham"
}, {
  "name": "Perry Branscombe"
}, {
  "name": "Salaidh Schultz"
}, {
  "name": "Nicolis Stonman"
}, {
  "name": "Michale Brecknock"
}, {
  "name": "Marian Withinshaw"
}, {
  "name": "Lynea Benit"
}, {
  "name": "Cale Giacometti"
}, {
  "name": "Ave Jahnisch"
}, {
  "name": "Aurelea Adshed"
}, {
  "name": "Pavlov Borham"
}, {
  "name": "Lamont McCanny"
}, {
  "name": "Rustie Troyes"
}, {
  "name": "Ivory Vina"
}]

# query="""
# INSERT INTO seller(name) VALUES(%s);
# """

# for i in seller_data:
#     cur.execute(query,(i["name"],))


# query="SELECT * FROM seller"
# cur.execute(query)

tag_data=[
    {
        "title": "Cheese"
    },
    {
        "title": "Chocolate"
    },
    {
        "title": "Vanillia"
    },
    {
        "title": "Vegetable"
    },
    {
        "title": "Vegan"
    },
    {
        "title": "Healthy"
    },
    {
        "title": "Fit"
    },
    {
        "title": "Meal"
    },
    {
        "title": "Fast Food"
    }
]

# query="""
# INSERT INTO tag(title) VALUES(%s);
# """

# for i in tag_data:
#     cur.execute(query,(i['title'],))

# query='SELECT * FROM tag'



seller_ids=[]
for i in range(len(seller_data)):
    seller_ids.append(i+1)



product_data=[
   {
      "title": "M&M Food Market",
      "price": "17.0616609356653"
   },
   {
      "title": "Soprole",
      "price": "11.6234613464323"
   },
   {
      "title": "Kinder",
      "price": "2.62073436454904"
   },
   {
      "title": "Andy Capp's fries",
      "price": "14.6864611770429"
   },
   {
      "title": "Bewley's",
      "price": "7.01804420073426"
   },
   {
      "title": "Vitta Foods",
      "price": "4.5093621385793"
   },
   {
      "title": "Taco Bell",
      "price": "19.1318949810843"
   },
   {
      "title": "Sun-Pat",
      "price": "9.6603184191791"
   },
   {
      "title": "Baskin robbins",
      "price": "16.105171543595"
   },
   {
      "title": "Wendy's",
      "price": "5.43620887838128"
   },
   {
      "title": "Cobblestone",
      "price": "7.22419333514953"
   },
   {
      "title": "Wonder Bread",
      "price": "14.6278888390529"
   },
   {
      "title": "Lavazza",
      "price": "10.305469252777"
   },
   {
      "title": "Kinder",
      "price": "19.4697343713929"
   },
   {
      "title": "Soprole",
      "price": "16.3448767300439"
   },
   {
      "title": "Nabisco",
      "price": "2.48867588838966"
   },
   {
      "title": "Tic Tac",
      "price": "2.60812248457601"
   },
   {
      "title": "Magnum",
      "price": "19.4421954995218"
   },
   {
      "title": "Papadopoulos",
      "price": "19.4472127819654"
   },
   {
      "title": "Wonder Bread",
      "price": "12.7520409541913"
   },
   {
      "title": "Papadopoulos",
      "price": "1.811215852765"
   },
   {
      "title": "Olymel",
      "price": "7.34511601847835"
   },
   {
      "title": "Domino",
      "price": "7.64364533249459"
   },
   {
      "title": "Pizza Hut",
      "price": "12.6648227300797"
   },
   {
      "title": "Red Lobster",
      "price": "10.0007594130005"
   },
   {
      "title": "Andy Capp's fries",
      "price": "18.5981898673802"
   },
   {
      "title": "Secret Recipe",
      "price": "18.6991437984161"
   },
   {
      "title": "Sun-Pat",
      "price": "3.15631274094633"
   },
   {
      "title": "Magnum",
      "price": "10.3542353042188"
   },
   {
      "title": "Heinz",
      "price": "17.7369680049536"
   },
   {
      "title": "Olymel",
      "price": "19.9154627821015"
   },
   {
      "title": "Taco Bell",
      "price": "10.9514749045258"
   },
   {
      "title": "Dunkin' Donuts",
      "price": "11.479457990024"
   },
   {
      "title": "Applebee's",
      "price": "15.7718961763996"
   },
   {
      "title": "Knorr",
      "price": "10.4961827092321"
   },
   {
      "title": "KFC",
      "price": "12.4794360452702"
   },
   {
      "title": "Domino",
      "price": "17.0641279993877"
   },
   {
      "title": "Knorr",
      "price": "2.66790023197788"
   },
   {
      "title": "Kits",
      "price": "18.8862874209351"
   },
   {
      "title": "Dunkin' Donuts",
      "price": "7.84475450163929"
   },
   {
      "title": "Applebee's",
      "price": "13.4456292886499"
   },
   {
      "title": "Nutella",
      "price": "4.63776473637566"
   },
   {
      "title": "Bewley's",
      "price": "13.0057596485157"
   },
   {
      "title": "Kits",
      "price": "1.38640394266062"
   },
   {
      "title": "Nesquik",
      "price": "6.1496629436266"
   },
   {
      "title": "KFC",
      "price": "15.6723103028128"
   },
   {
      "title": "Andy Capp's fries",
      "price": "17.8805946269448"
   },
   {
      "title": "Tic Tac",
      "price": "7.01679017348997"
   },
   {
      "title": "Andy Capp's fries",
      "price": "7.87038087466284"
   },
   {
      "title": "Bel Group",
      "price": "10.6127773935966"
   }
]

# query="""
# INSERT INTO product(title,price,seller_id) VALUES(%s,%s,%s);
# """

# for i in product_data:
#     cur.execute(query,(i['title'],i['price'],random.choice(seller_ids)))

# query="SELECT * FROM product"


customers_ids=[]
for i in range(len(customer_data)):
    customers_ids.append(i+1)


# query="""
# INSERT INTO wishlist(customer_id) VALUES(%s);
# """

# for i in customer_data:
#     cur.execute(query,(random.choice(customers_ids),))

# query="SELECT * FROM wishlist"

# rate NUMERIC,
# #     customer_id INT,
# #     product_id INT,

# query="""
# INSERT INTO review(rate,customer_id,product_id) VALUES(%s,%s,%s);
# """

# for i in customer_data:
#     cur.execute(query,(random.randint(1,5),random.choice(customers_ids),random.randint(1,len(product_data))))

# query='SELECT * FROM review'

# product_id INT,
# #     customer_id INT,

# query="""
# INSERT INTO wishlist_products(product_id,customer_id) VALUES(%s,%s);
# """

# for i in customer_data:
#     cur.execute(query,(random.randint(1,len(product_data)),random.choice(customers_ids)))


# query='SELECT * FROM wishlist_products'

# query="""
# INSERT INTO product_tags(product_id,tag_id) VALUES(%s,%s);
# """

# for i in product_data:
#     cur.execute(query,(random.randint(1,len(product_data)),random.randint(1,len(tag_data))))

# query='SELECT * FROM product_tags'




# query="""
# SELECT *
# FROM product_tags pt
# LEFT JOIN tag t ON pt.tag_id = t.id
# WHERE pt.product_id = 5;
# """

# # query='SELECT * FROM product'

# query="""
# SELECT *
# FROM product 
# LEFT JOIN seller ON product.seller_id = seller.id
# WHERE seller.id = 5;
# """


# query="""
# SELECT *
# FROM wishlist_products 
# LEFT JOIN product  ON wishlist_products.product_id = product.id
# WHERE wishlist_products.customer_id = 2;
# """



# query="""
# SELECT p.id, p.title
# FROM product p
# LEFT JOIN review r ON p.id = r.product_id
# GROUP BY p.id, p.title
# ORDER BY rate DESC
# LIMIT 10;
# """




# # query='''
# #  SELECT * FROM review LEFT JOIN product ON product_id=product.id WHERE product_id=2 ;
# # '''

# # WHERE product_id  IN (SELECT AVG(rate) FROM review  GROUP BY product_id ORDER BY AVG(rate) DESC)



# # query="SELECT * FROM product"

#Burdan basliyir
# Bir teq seçin və həmin teqin məhsullarını göstərin


query="""SELECT * FROM product 
LEFT JOIN product_tags on product_tags.product_id=product.id  WHERE product_tags.tag_id=5"""
         
# Bir məhsul seçin və həmin məhsulların teqlərini göstərin

# query="""SELECT * FROM product_tags
# LEFT JOIN product on product.id=product_tags.product_id WHERE product.id=5
# """
         
# Bir satıcı seçin və həmin satıcının məhsullarını göstərin

# query="""
# SELECT * FROM product
# LEFT JOIN seller on seller.id=product.seller_id WHERE seller.id=5
# """

# Bir müştəri seçin və həmin müştərinin wishlistindəki məhsulları göstərin

# query="""
# SELECT * FROM wishlist_products 
# LEFT JOIN customer on wishlist_products.customer_id=customer.id WHERE customer.id=45
# """

# Review ortalaması ən yüksək olan 10 məhsulu həmin ortalama ilə birlikdə göstərin

# query="""SELECT AVG(rate),product.id FROM product
# LEFT JOIN review on product.id=review.product_id GROUP BY product.id ORDER BY AVG(rate) LIMIT 10"""


# teqləri məhsullarının sayına görə düzün və bunu edərkən də məhsulların sayı da görünsün
# query="""
# SELECT COUNT(product_tags.product_id),product_tags.tag_id FROM product_tags LEFT JOIN tag on product_tags.tag_id=tag.id  GROUP BY product_tags.tag_id ORDER BY COUNT(product_tags.product_id) DESC
# """


# Wishlistindəki məhsulların toplam qiyməti ən çox olan 10 müşətirini göstərin. Bunu edərkən həmin qiymət toplamı da görünsün

# query="""
# SELECT customer.id,SUM(wishlist_products.product_id) FROM customer LEFT JOIN wishlist_products on customer.id=wishlist_products.customer_id GROUP BY customer.id HAVING SUM(wishlist_products.product_id) IS NOT NULL  ORDER BY SUM(wishlist_products.product_id) DESC LIMIT 10
# """


# id-lərinə görə ilk 10 satıcının məlumatlarını və həmin satıcının məhsullarına gələn reviewların ortalamasını göstərin

query="""
SELECT customer.id, AVG(rate) FROM customer LEFT JOIN review on customer.id=review.customer_id GROUP BY customer.id HAVING AVG(rate) IS NOT NULL ORDER BY AVG(rate) DESC LIMIT 10
"""


show(cur)

con.commit()
