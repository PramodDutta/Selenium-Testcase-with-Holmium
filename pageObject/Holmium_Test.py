from selenium import webdriver
import unittest
import nose
from holmium.core import Page, Element, Locators, TestCase


class LoginPage(Page):
    userNameText = Element(Locators.NAME, 'userName')
    passwordText = Element(Locators.NAME, 'password')
    submitButton = Element(Locators.NAME, 'login')

    def login(self):
        self.userNameText.send_keys("techdutta")
        self.passwordText.send_keys("test123")
        self.submitButton.submit()


class LoginTest(TestCase):
    def setUp(self):
        self.page = LoginPage(self.driver,
                              "http://demoaut.com/")

    def test_Login(self):
        self.page.login()
        self.assertEqual(self.driver.title,
                         "Find a Flight: Mercury Tours:")

    def tearDown(self):
        self.driver.close()
