def main():
  """
  Функция main() - это сердце нашего калькулятора.
  Она позволяет вводить целые числа и выполнять операции в консоли,
  выводя десятичные результаты с точностью до 10 знаков после запятой.
  """

  while True:
    try:
      # Получаем первое число
      num1 = int(input("Введите первое число: "))

      # Получаем операцию
      operation = input("Введите операцию (+, -, *, /): ")

      # Получаем второе число
      num2 = int(input("Введите второе число: "))

      # Вычисляем результат
      if operation == "+":
        result = num1 + num2
      elif operation == "-":
        result = num1 - num2
      elif operation == "*":
        result = num1 * num2
      elif operation == "/":
        if num2 == 0:
          print("Деление на ноль невозможно!")
          continue
        else:
          result = num1 / num2  # Деление с плавающей запятой
      else:
        print("Неверная операция. Пожалуйста, используйте +, -, *, /.")
        continue

      # Форматируем десятичный результат
      if operation == "/" and isinstance(result, float):
        result = f"{result:.10f}"  # Ограничение до 10 знаков после запятой

      # Выводим результат
      print(f"{num1} {operation} {num2} = {result}")

      # Спрашиваем, хочет ли пользователь продолжить
      again = input("Хотите выполнить еще одно вычисление? (да/нет): ").lower()
      if again != "да":
        break

    except ValueError:
      print("Неверный формат. Используйте целые числа и операторы (+, -, *, /).")

if __name__ == "__main__":
  main()
