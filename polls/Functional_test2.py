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

        #link = self.browser.find_element_by_id('id_logout')

        span = self.browser.find_element(By.XPATH, '//span[text()="Logout"]')
        self.assertIn('Logout', span.text)

    def test_edicion(self):
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

        link = self.browser.find_element_by_id('id_editar')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel2')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo2')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3179998899')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino21@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:\PycharmProjects\uniandes.jpg')

        #nombreUsuario = self.browser.find_element_by_id('id_username')
        #nombreUsuario.send_keys('juan645')

        #clave = self.browser.find_element_by_id('id_password')
        #clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)

        nombre = self.browser.find_element_by_id('id_nombre')
        self.assertIn('Juan Daniel2', nombre.text)