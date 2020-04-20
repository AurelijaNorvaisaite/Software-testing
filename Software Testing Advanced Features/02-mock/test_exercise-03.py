import pytest
from plant_shop import PlantShop
from unittest.mock import patch
from db import _users, _products, _orders

@pytest.fixture
def plant_shop():
    return PlantShop()

@pytest.fixture
def override_db_user():
    with patch("db.DB.get_table") as patched_db:
        patched_db.return_value = _users
        yield patched_db

@pytest.fixture
def override_db_get_user_by_id():
    with patch("db.DB.get") as patched_db:
        patched_db.side_effect = IndexError
        yield patched_db

@pytest.fixture
def override_db_product():
    with patch("db.DB.get_table") as patched_db:
        patched_db.return_value = _products
        yield patched_db

@pytest.fixture
def override_db_order():
    with patch("db.DB.get") as patched_db:
        patched_db.return_value = _orders
        yield patched_db


def test_user_init(plant_shop, override_db_user, override_db_get_user_by_id):
    assert plant_shop.get_user_by_name("kloseby0") is not None
    assert plant_shop.get_user_by_name("rpeele1") is not None
    assert plant_shop.get_user_by_name("lmangin2") is not None
    assert plant_shop.get_user_by_name("ssima3") is not None
    with pytest.raises(IndexError):
        plant_shop.get_user_by_id(4)

def test_product_init(plant_shop, override_db_product, override_db_get_user_by_id):
    assert plant_shop.get_product_by_name("Pale Blue-eyed Grass") is not None
    assert plant_shop.get_product_by_name("Sudangrass") is not None
    assert plant_shop.get_product_by_name("Climbing Bedstraw") is not None
    assert plant_shop.get_product_by_name("Pedilanthus") is not None
    assert plant_shop.get_product_by_name("Ames' Lady's Tresses") is not None
    with pytest.raises(IndexError):
        plant_shop.get_user_by_id(5)

def test_order_init(plant_shop):
    o = plant_shop.get_order_by_id(0)
    assert o is not None
    assert o.user_id == 0
    assert o.product_id == 1
    assert o.amount == 3
    assert o.is_paid is True
    with pytest.raises(IndexError):
        plant_shop.get_order_by_id(1)
