import pytest
import requests
import json

from application.configuration import FLASK_RUN_HOST, FLASK_RUN_PORT

url = "http://{}:{}".format(FLASK_RUN_HOST, FLASK_RUN_PORT)


def request_invalid_test():
    response = requests.get("{}/ProcessPayment".format(url))
    
    assert response.status_code >= 400


def payment_without_data():
    card_data = {}
    response = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data),
                             headers={"Content-Type": "application/json"})
    assert response.status_code == 400

def external_services_wrong_info():
    card_data_1 = {"CreditCardNumber": "abch129556iktojw","CardHolder":"annie jack","SecurityCode": "123",
"ExpirationDate": "2020/3/2","Amount": 666.6}
    card_data_2 = {"CreditCardNumber": "1237895436723456", "CardHolder": "annie jack", "SecurityCode": "111",
                   "ExpirationDate": "2022/8/27", "Amount": 666.6}
    response_1 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_1), headers={"Content-Type":"application/json"})
    response_2 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_2), headers={"Content-Type": "application/json"})
    
    assert response_1.status_code == 400
    assert response_2.status_code == 200

def argument_problem():
    card_data = dict(CreditCardNumbers="7893412341234", CardHoldewr="annie jack", SecurityCode="123", ExpirationDate="2020/3/2", Amount=289.3)
    response = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data), headers={"Content-Type": "application/json"})
    assert response.status_code == 400
  

def external_services_expiration_data():
    # testing the ExpirationDate different case, when date is more then present and when date is past of present date
    card_data_1 = {"CreditCardNumber": "abch1234589ijojw", "CardHolder": "annie jack", "SecurityCode": "456",
                   "ExpirationDate": "2022/10/13", "Amount": 789.3}
    card_data_2 = {"CreditCardNumber": "1234567890123456", "CardHolder": "annie jack", "SecurityCode": "456",
                   "ExpirationDate": "2019/12/1", "Amount": 789.3}
    
    response_1 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_1), headers={"Content-Type": "application/json"})
    response_2 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_2),
                               headers={"Content-Type": "application/json"})
    
    assert response_1.status_code == 200
    assert response_2.status_code == 400
    
def securtiy_code_for_test():
    # testing for SecurityCode cases
    card_data_1 = {"CreditCardNumber": "abch123456ijiojw", "CardHolder": "annie jack", "SecurityCode": "456",
                   "ExpirationDate": "2022/13/13", "Amount": 789.3}
    card_data_2 =  {"CreditCardNumber": "abch123456ijiojw", "CardHolder": "annie jack", "ExpirationDate": "2022/12/13", "Amount": 789.3}
    card_data_3 = {"CreditCardNumber": "abch123456ijiojw", "CardHolder": "annie jack", "SecurityCode": 456,
                   "ExpirationDate": "2022/12/13", "Amount": 789.3}

    response_1 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_1),
                               headers={"Content-Type": "application/json"})
    
    response_2 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_2),
                               headers={"Content-Type": "application/json"})
    response_3 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_3),
                               headers={"Content-Type": "application/json"})
    assert response_1.status_code == 200
    assert response_2.status_code == 200
    assert response_3.status_code == 400
    
def amount_multipled_with_true_input():
    # testing the cases where for different amount input different external payment method invoke
    card_data_1 = {"CreditCardNumber": "1784567890123098", "CardHolder": "annie jack", "SecurityCode": "456",
                   "ExpirationDate": "2022/2/28", "Amount": 19}
    card_data_2 = {"CreditCardNumber": "1784567890123098", "CardHolder": "annie jack", "SecurityCode": "456",
                   "ExpirationDate": "2022/2/28", "Amount": 546}
    card_data_3 = {"CreditCardNumber": "1784567890123098", "CardHolder": "annie jack", "SecurityCode": "456",
                   "ExpirationDate": "2022/2/28", "Amount": 987}
    
    response_1 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_1), headers={"Content-Type":"application/json"})
    response_2 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_2), headers={"Content-Type":"application/json"})
    response_3 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_3), headers={"Content-Type":"application/json"})
    
    assert response_1.status_code == 200
    assert response_2.status_code == 200
    assert response_3.status_code == 200



