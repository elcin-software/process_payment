from application.services_about_payment.info_payment import Card


class PaymentGateway:
	def __init__(self, repeat=0):
		self.repeat = repeat
		self.gateway = None
		
	def __repr__(self):
		return "<{}>".format("PaymentGateway")
	
	def connect(self, gateway=None, details=None):
		if gateway != None:
			if self.authenticate(details):
				return True
		return False
	
	def authenticate(self, details=None):
		if details != None:
			return True
		return False
	
	def pay(self, amount, user_details=None, gateway=None):
		if gateway is None:
			gateway = self.gateway
		while self.repeat + 1 > 0:
			if self.connect(gateway, user_details):
				print("Successfuly, {} payment in gateway {}".format(amount, self.gateway))
				return True
			self.repeat -= 1
		return False

class ExternalServices:
	def __init__(self, amount, card_details=None):
		self.amount = amount
		self.card_details = card_details
	
	def make_payment(self):
		try:
			payment_mode = None
			if self.amount <= 20:
				payment_mode = CheapPaymentGateway()
			elif 20 < self.amount < 500:
				payment_mode = ExpensivePaymentGateway()
			elif self.amount >= 500:
				payment_mode = PremiumPaymentGateway()
			else:
				return False
			
			status = payment_mode.pay(self.amount, self.card_details)
			return status
		except:
			return False


class PremiumPaymentGateway(PaymentGateway):
	def __init__(self, repeat=3):
		super(PremiumPaymentGateway, self).__init__(repeat)
		self.gateway = "PremiumPaymentGatway"
	
	def __repr__(self):
		return "<PremiumPaymentGateway>"


class ExpensivePaymentGateway(PaymentGateway):
	def __init__(self, repeat=1):
		super(ExpensivePaymentGateway, self).__init__(repeat)
		self.gateway = "ExpensivePaymentGateway"
	
	def __repr__(self):
		return "<ExpensivePaymentGateway>"


class CheapPaymentGateway(PaymentGateway):
	def __init__(self, repeat=0):
		super(CheapPaymentGateway, self).__init__(repeat)
		self.gateway = "CheapPaymentGateway"
	
	def __repr__(self):
		return "<CheapPaymentGateway>"




