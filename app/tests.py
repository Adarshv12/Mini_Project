from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class PlayerFormTest(LiveServerTestCase):

    def testform(self):
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/login')
        userid = selenium.find_element('id','username')
        paswd = selenium.find_element('id','password')
        submit = selenium.find_element('id','submit')

        userid.send_keys('adarsh01')
        paswd.send_keys('asdfghjk')

        submit.send_keys(Keys.RETURN)
        assert 'adarsh01' in selenium.page_source