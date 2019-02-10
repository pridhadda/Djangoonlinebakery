from decimal import Decimal
from django.conf import settings
from .models import Prod


class Cart(object):
	def __init__(self,request):
		'''Intialize the cart'''
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			#save empty cart in sesssion
			cart = self.session[settings.CART_SESSION_ID]={}
		self.cart=cart




	def add(self,product,quantity=1,update_quantity=False):

		'''add a product teh cart or update'''
		product_id = str(product.id)
		if product_id not in self.cart:

			self.cart[product_id] = {'quantity': 0,'price':str(product.price)}


		if update_quantity:
			self.cart[product_id]['quantity']= quantity

		else:
			self.cart[product_id]['quantity'] += quantity

		self.save()





	def save(self):
	#update the session cart
	self.session[settings.CART_SESSION_ID]=self.cart
	#mark session as modified
	self.session.modified  = True
	


	
	def remove(self,product):
		'''remove prdouct'''
		product_id=str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()



	def __iter__(self):
		'''Iterate over items in cart and get products from db'''
		product_ids = self.cart.keys()
		#get product objects and add them tovcart
		products = Prod.objects.filter(id__in=product_ids)
		for product in products:
			self.cart[str(product.id)]['product']= product


		for item in self.cart.values():
			item['price']= Decimal(item['price'])
			item['total_price']= item['price']* item['quantity']
			yeild item




	def __len__(self):
		'''count all items in cart'''
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(Decimal(item['price'])* item['quantity'] for item in self.cart.values())



	def clear(self):
		self.session[settings.CART_SESSION_ID]={}
		self.session.modified= True
				






	
		
