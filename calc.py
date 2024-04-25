def main():
  """
  Функция main() - это сердце нашего калькулятора.
  Она получает числа от пользователя,
  выполняет выбранную операцию и выводит результат.
  """

  while True:
    try:
      # Получаем первое число от пользователя
      num1 = float(input("Введите первое число: "))

      # Получаем операцию от пользователя
      operation = input("Введите операцию (+, -, *, /): ")

      # Получаем второе число от пользователя
      num2 = float(input("Введите второе число: "))

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
          result = num1 / num2
      else:
        print("Неверная операция. Пожалуйста, используйте +, -, *, /.")
        continue

      # Выводим результат
      print(f"{num1} {operation} {num2} = {result}")

      # Спрашиваем пользователя, хочет ли он продолжить
      again = input("Хотите выполнить еще одно вычисление? (да/нет): ")
      if again.lower() != "да":
        break

    except ValueError:
      print("Неверный формат числа. Пожалуйста, используйте числа.")

if __name__ == "__main__":
  main()
