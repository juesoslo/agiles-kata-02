__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        #self.browser = webdriver.Firefox()
        self.browser = webdriver.Chrome("C:\\PycharmProjects\\chromedriver.exe")
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        nombreUsuario = self.browser.find_element_by_id('id_username1')
        nombreUsuario.send_keys('juan645')

        clave = self.browser.find_element_by_id('id_password1')
        clave.send_keys('clave123')

        botonEnviar = self.browser.find_element_by_id('id_grabar1')
        botonEnviar.click()
        self.browser.implicitly_wait(3)

        link = self.browser.find_element_by_id('id_login')

        span = self.browser.find_element(By.XPATH, '//span[text()="Logout"]')
        self.assertIn('Logout', span.text)