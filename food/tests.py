from django.test import TestCase
from .models import *

# Create your tests here.


class DataTest(TestCase):
    def setUp(self):
        self.food = Food.objects.create(name="Momo", price=120,
                                        description="This is kfc.", photo="")
        self.user = User.objects.create_user(
            username="Ram", password="123456789", email="ram@gmail.com")
        self.customer = Customer.objects.create(
            user_id=self.user.id, address="ktm", contact=987262778)
        Category.objects.create(name="Dessert")
        CartItem.objects.create(cus_id_id=self.customer.id,
                                food_id_id=self.food.id, quantity=2)
        Order.objects.create(cus_id_id=self.customer.id,
                             food_id_id=self.food.id, quantity=4)

    # def testFood(self):
    #     t = Food.objects.get(name="Momo")
    #     self.assertEqual(t.name, 'Momo')

    # def testuser(self):
    #     c = Customer.objects.get(user_id=self.user.id)
    #     self.assertEqual(c.address, 'ktm')

    # def testCategory(self):
    #     cat = Category.objects.get(name="Dessert")
    #     self.assertEqual(cat.name, 'Dessert')

    # def testCartItem(self):
    #     item = CartItem.objects.get(cus_id_id=self.customer.id)
    #     self.assertEqual(item.quantity, 2)

    def testOrder(self):
        orde = Order.objects.get(cus_id_id=self.customer.id)
        self.assertEqual(orde.quantity, 4)
