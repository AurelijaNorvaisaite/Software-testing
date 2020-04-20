from db import DB

_expected_tables = ("users", "products", "orders")


class User:
    def __init__(self, id_, username, first_name, last_name, email):
        self.id_ = id_
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


class Product:
    def __init__(self, id_, name, sku, in_storage, ordered):
        self.id_ = id_
        self.name = name
        self.sku = sku
        self.in_storage = in_storage
        self.ordered = ordered


class Order:
    def __init__(self, user_obj, product_obj, amount, is_paid):
        self.user = user_obj
        self.product = product_obj
        self.amount = amount
        self.is_paid = is_paid

    @property
    def user_id(self):
        return self.user.id_

    @property
    def product_id(self):
        return self.product.id_


class PlantShop:
    def __init__(self):
        self.__db = DB()
        self.__validate_db()

    def __validate_db(self):
        """Checks if the DB has all the necessary tables"""
        tables = self.__db.list_tables()
        for table in _expected_tables:
            if table not in tables:
                raise InvalidDBException(f"{table} table missing")

    def get_user_by_name(self, name):
        """Returns user object"""
        for i, u in enumerate(self.__db.get_table("users")):
            if u["username"] == name:
                return User(i, u["username"], u["first_name"], u["last_name"], u["email"])
        return None

    def get_user_by_id(self, id_):
        """Returns user object"""
        u = self.__db.get("users", id_)
        return User(id_, u["username"], u["first_name"], u["last_name"], u["email"])

    def insert_user(self, user_obj):
        user_dict = {
            "username": user_obj.username,
            "first_name": user_obj.first_name,
            "last_name": user_obj.last_name,
            "email": user_obj.email,
        }
        self.__db.insert("users", user_dict)

    def get_product_by_name(self, name):
        """Returns product object"""
        for i, p in enumerate(self.__db.get_table("products")):
            if p["name"] == name:
                return Product(i, p["name"], p["sku"], p["in_storage"], p["ordered"])
        return None

    def get_product_by_id(self, id_):
        """Returns product object"""
        p = self.__db.get("products", id_)
        return Product(id_, p["name"], p["sku"], p["in_storage"], p["ordered"])

    def insert_product(self, product_obj):
        product_dict = {
            "name": product_obj.name,
            "sku": product_obj.sku,
            "in_storage": product_obj.in_storage,
            "ordered": product_obj.ordered,
        }
        self.__db.insert("products", product_dict)

    def update_product(self, id_, product_obj):
        product_dict = {
            "name": product_obj.name,
            "sku": product_obj.sku,
            "in_storage": product_obj.in_storage,
            "ordered": product_obj.ordered,
        }
        self.__db.update("products", id_, product_dict)

    def get_order_by_id(self, id_):
        o = self.__db.get("orders", id_)
        u = self.get_user_by_id(o["user_id"])
        p = self.get_product_by_id(o["product_id"])
        return Order(u, p, o["amount"], o["paid"])

    def insert_order(self, order_obj):
        # verify that User.id and Product.id are in DB
        self.get_user_by_id(order_obj.user_id)
        p = self.get_product_by_id(order_obj.product_id)
        order_dict = {
            "user_id": order_obj.user_id,
            "product_id": order_obj.product_id,
            "amount": order_obj.amount,
            "paid": order_obj.is_paid,
        }
        self.__db.insert("orders", order_dict)
        p.in_storage -= order_obj.amount
        p.ordered += order_obj.amount
        self.update_product(order_obj.product_id, p)


class InvalidDBException(Exception):
    pass
