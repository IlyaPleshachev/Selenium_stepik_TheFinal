from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_should_see_login_link(browser): #тест наличия перехода на страницу логина
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                     # открываем страницу
    page.should_be_login_link()     # выполняем метод страницы — проверяем наличие страницы логина
    
def test_guest_can_go_to_login_page(browser): #тест перехода на страницу логина
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_guest_can_use_login_page(browser): #тест перехода на страницу логина
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_login_page()          # выполняем метод страницы — переходим на страницу логина
