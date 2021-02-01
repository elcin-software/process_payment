import re
from decimal import Decimal
import datetime


def cardVerification(card):
	if not re.search(r"^[456]\d{3}(-?\d{4}){3}$", card) or re.search(r"(\d)\1{3}", re.sub("-", "", card)):
		return False
	return True


class CardDetails:
	def __init__(self):
		self.CreditCardNumber = None
		self.CardHolder = None
		self.ExpirationDate = None
		self.SecurityCode = None
		self.Amount = None


class Card(CardDetails):
	def __init__(self):
		super(Card, self).__init__()
	
	def Verification(self, **kwargs):
		
		cardsInfo = ["CreditCardNumber", "CardHolder", "ExpirationDate", "Amount"]
		if set(cardsInfo).intersection(kwargs.keys()) != set(cardsInfo):
			print("The card could not be found.")
			return False
		
		if not type(kwargs['CreditCardNumber'] == str and cardVerification(kwargs['CreditCardNumber'])) or not len(kwargs['CreditCardNumber']) == 16:
			print("The card number is not valid.")
			return False
		
		if not type(kwargs['CardHolder']) == str:
			print("The type of card holder is not valid.")
			return False
		
		if kwargs.get('SecurityCode',None) :
			if not (type(kwargs.get('SecurityCode', None)) == str and len(kwargs.get('SecurityCode', None)) == 3) or not kwargs.get('SecurityCode', None).isdigit():
				print("There exists an error about security code.")
				return False

		if not datetime.datetime.strptime(kwargs['ExpirationDate'], "%Y/%m/%d") > datetime.datetime.now():
			print("There exists an error about expiration date of the card.")
			return False
		
		try:
			if not Decimal(kwargs['Amount']) > 0:
				print("The amount is not valid.")
				return False
		except:
			return False
		
		redirecting_to_data = {
			"CreditCardNumber": kwargs['CreditCardNumber'],
			'Amount': kwargs['Amount'],
			'CardHolder': kwargs['CardHolder'],

			'ExpirationDate': kwargs['ExpirationDate']
		}
		if kwargs.get("SecurityCode", None):
			redirecting_to_data.update({"SecurityCode":kwargs.get("SecurityCode")})
		print("The input is successfuly processed.")
		self.redirecting_to_card(**kwargs)
		return True
	
	def redirecting_to_card(self, **kwargs):
		self.CreditCardNumber = kwargs.get('CreditCardNumber', None)
		self.Amount = kwargs.get('Amount', None)
		self.CardHolder = kwargs.get('CardHolder', None)

		self.SecurityCode = kwargs.get('SecurityCode', None)
		self.ExpirationDate = kwargs.get('ExpirationDate', None)
		
		print("The user redirecting has been done successfuly.")
		return True
	
