from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:

    x = browser.find_element_by_css_selector("#treasure").get_attribute("valuex")
    y = calc(x)

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    # вводит ответ в поле
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("tgdlg")

    # вводит ответ в поле
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("ykykdh")

    # вводит ответ в поле
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("khho")

    #находит кнопку обзор и загружает txt файл
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    upload = browser.find_element(By.ID, "file")
    upload.send_keys(file_path)

    #нажимает ОК в модальном окне
    confirm = browser.switch_to.alert
    confirm.accept()

    #переход на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    WebDriverWait(browser, "время ожидания работы счетчика").until(
        EC.text_to_be_present_in_element((By.ID, "ИД текста"), "текст для сравнения")) // Задаем
    счетчик
    ожидания
    btn = browser.find_element_by_id("book") // Объявляем
    кнопку
    btn.click() // И
    прокликиваем


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


    #ищет значение для расчета и нажимает кнопку
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer").send_keys(y)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()