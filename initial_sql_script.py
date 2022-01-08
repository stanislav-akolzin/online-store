'''Scrip for initial filling database'''
import psycopg2


con = psycopg2.connect(
    database='test_base',
    user='django_user',
    password='123',
    host='127.0.0.1',
    port='5432',
)

cur = con.cursor()
cur.execute('''INSERT INTO store_itemcategory (id, name, description) VALUES
                                (1, 'Books', 'Paper and electronic books'),
                                (2, 'Cars', 'Sport cars and SUVs'),
                                (3, 'Aircrafts', 'Passenger aircrafts of different manufacturers'),
                                (4, 'Smartphones', 'Smartphones from the whole world'),
                                (5, 'Computers', 'Personal computers')
                                ;''')
cur.execute('''INSERT INTO store_item (id, name, description, price, quantity, category_id) VALUES
                                (1, 'Java for beginners', 'Book for beginners in Java programming language by Shildt', 18.22, 4, 1),
                                (2, 'Clean code', 'Robert Martin (of Ancle Bob) wrote perfect book about principles or making good code', 14.50, 5, 1),
                                (3, 'Harry Potter', 'Story about little wizzard who stuied in wizzard school and encountered with powerful creatures', 8.20, 20, 1),
                                (4, 'Ferrari F-430', 'Probably the most beautiful car ever made', 350000, 2, 2),
                                (5, 'Volkswagen Tuareg', 'Modern comfortable SUV for suitable for most families', 90000, 7, 2),
                                (6, 'Audi SQ5', 'Sport SUV. Suitable for outdoor as well as for track', 140000, 3, 2),
                                (7, 'Boeing 737', 'Most widespread aircraft in the world', 10000000, 4, 3),
                                (8, 'Airbus A320', 'Second widespread passenger aircraft in the world', 11000000, 4, 3),
                                (9, 'Boeing 747', 'JumboJet. First double deck passenger aircraft in the world. One of the most perfect ones!', 28000000, 2, 3),
                                (10, 'Airbus A380', 'The hugest aircraft in the world. Has two deck from nose to tail.', 400000000, 3, 3),
                                (11, 'Airbus A350', 'One of the most modetn passenger aircrafts in the world.', 280000000, 4, 3),
                                (12, 'Boeing 787', 'DreamLiner. Very quite and comfortable', 300000000, 3, 3),
                                (13, 'Tu-154', 'Soviet passenger aircraft. Very loud but also very fast. Is not produced nowadays.', 1000000, 1, 3),
                                (14, 'Aibus A220', 'Former Bombardier. Small regional passenger aircraft', 1200000, 5, 3),
                                (15, 'Boeing 777', 'Tiple seven guy. Very popular amoung aircompanies on intercontinental routes.', 3200000000, 3, 3),
                                (16, 'Airbus A330 neo', 'Model came to replace A330. This one is more efficient and comfortable.', 2900000000, 2, 3),
                                (17, 'Boeing 707', 'Old aircraft. Is not used by companies nowadays.', 500000, 1, 3),
                                (18, 'Boeing 767', 'Widebody passenger aircraft mostly used to long routes.', 1500000000, 2, 3),
                                (19, 'iPhone XS', 'Smartphone from American brand Apple.', 800, 20, 4),
                                (20, 'Samsung Galaxy S21', 'Korean brand. Has good camera.', 850, 20, 4),
                                (21, 'Xiaomi mi10', 'Chineese brand. Fast enough.', 700, 15, 4),
                                (22, 'Slow computer', 'Intel celerone, 4 Gb, HDD 500 Gb', 300, 5, 5),
                                (23, 'Fast computer', 'Intel Core i9, 32 Gb, SSD 1Tb', 1200, 8, 5)
                                ;''')
cur.execute('''INSERT INTO store_itemchange (id, item_id, date, initial_quantity, new_quantity) VALUES
                                (1, 1, '2021-11-21 18:00:00+03', 0, 4),
                                (2, 2, '2021-11-21 18:00:00+03', 0, 5),
                                (3, 3, '2021-11-21 18:00:00+03', 0, 20),
                                (4, 4, '2021-11-21 18:00:00+03', 0, 2),
                                (5, 5, '2021-11-21 18:00:00+03', 0, 7),
                                (6, 6, '2021-11-21 18:00:00+03', 0, 3),
                                (7, 7, '2021-11-21 18:00:00+03', 0, 4),
                                (8, 8, '2021-11-21 18:00:00+03', 0, 4),
                                (9, 9, '2021-11-21 18:00:00+03', 0, 2),
                                (10, 10, '2021-11-21 18:00:00+03', 0, 3),
                                (11, 11, '2021-11-21 18:00:00+03', 0, 4),
                                (12, 12, '2021-11-21 18:00:00+03', 0, 3),
                                (13, 13, '2021-11-21 18:00:00+03', 0, 1),
                                (14, 14, '2021-11-21 18:00:00+03', 0, 5),
                                (15, 15, '2021-11-21 18:00:00+03', 0, 3),
                                (16, 16, '2021-11-21 18:00:00+03', 0, 2),
                                (17, 17, '2021-11-21 18:00:00+03', 0, 1),
                                (18, 18, '2021-11-21 18:00:00+03', 0, 2),
                                (19, 19, '2021-11-21 18:00:00+03', 0, 20),
                                (20, 20, '2021-11-21 18:00:00+03', 0, 20),
                                (21, 21, '2021-11-21 18:00:00+03', 0, 15),
                                (22, 22, '2021-11-21 18:00:00+03', 0, 5),
                                (23, 23, '2021-11-21 18:00:00+03', 0, 8)
                                ;''')
con.commit()
con.close()