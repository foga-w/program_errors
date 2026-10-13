from wo import add, divide
import unittest

#Создаём специальный тестовый класс на базе модуля TestCase
class Testing(unittest.TestCase):
    """Шаг 1. Метод setup вызывается из класса TestCase перед каждым тестом. """
    def setUp(self):
        """ Подготовка данных, общих для всех проводимых тестов. """
        self.a = 10
        self.b = 5
    """ Шаг 2.  Метод teardown вызывается из класса Testcase после каждого теста """
    def tearDown(self):
        """ 
        Очистка данных после каждого теста 
         -> Закрытие файлов
         -> Закрытие соединений с базами данных
         -> Очистка переменных и т.д.
        """
        pass
    """ Методы для проведения тестов; каждый тест это отдельный метод, 
    имя которого всегда должно начинатся с test_ """
    def test_add(self):
        """ Тестирование функции add():
        
        Данные для проведения теста (Arrange) заранее подготовлены в методе setup """
        excepteted = 15
        """ Действия (Act)"""
        result = add(self.a, self.b)
        """ Проверка (assert)"""
        #Функция AssertEqual проверяет равенство преполагаемого результата действительному полученному значению.
        self.assertEqual(result, excepteted)
        
    def test_divide(self):
        """Тестирование функции divide():"""
    
        exepted = 2 # Ожидаемый результат
        result = divide(self.a, self.b)
        """ Проверка на работспособность функции """
        self.assertEqual(result, exepted)
        
    def test_divide_raise(self):
        """ Проверка исключений """
        with self.assertRaises(ValueError):
            divide(self.a, 0)
        
""" ========== Тестирование =========="""

if __name__ == "__main__":
    unittest.main()





# """ ------------- Проверка сложения --------"""
# # A1: Подготовка входных данных
# a, b = 2, 3
# expected = 5
# # A2: Вызов функции
# result = add(a,b)
# # A3: Проверка результатов
# assert result == expected, f'Ожидание {expected}, Резуыльтат: {result}'
# print("Тест 1 пройден")

# """ ------------- Проверка деления --------"""
# # A1: Подготовка входных данных
# a, b = 10, 2
# expected = 5
# # A2: Вызов функции
# result = divide(a,b)
# # A3: Проверка результатов
# assert result == expected, f'Ожидание {expected}, Результат: {result}'
# print("Тест 2 пройден")

# """ ------------- проверка исключения --------"""
# # A1: Подготовка входных данных
# a, b = 0, 10
# # A2: Вызов функции
# try:
#     result = divide(a,b)
#     assert False, 'Ожидали ValueError, но исключения не возникло'
# except ValueError as error:
#     assert str(error) == 'Деление на ноль невозможно'
# # A3: Проверка результатов
# print('Тест 3 пройден')

