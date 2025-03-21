# Инженерный Калькулятор

Инженерный калькулятор с графическим интерфейсом, поддерживающий различные темы, языки и математические функции. Программа написана на Python с использованием библиотеки `tkinter`.

## Особенности
- **12 тем оформления**: Выберите цветовую схему, которая подходит именно вам.
- **Поддержка 10 языков**: Английский, русский, испанский, французский, немецкий, итальянский, португальский, японский, корейский, китайский.
- **Математические функции**:
  - Тригонометрические функции (`sin`, `cos`, `tan`, `asin`, `acos`, `atan`).
  - Гиперболические функции (`sinh`, `cosh`, `tanh`).
  - Логарифмы (`log`, `log10`), экспонента (`exp`), факториал (`!`), корень (`sqrt`).
  - Константы: число π, число e, золотое сечение (φ).
- **Пасхалка**: Введите "1000-7" в поле ввода, чтобы активировать скрытый режим.
- **Простой интерфейс**: Удобное управление через меню и кнопки.

## Установка

### Требования
- Python 3.x
- Библиотеки: `tkinter`, `math`

### Шаги для запуска
1. Убедитесь, что у вас установлен Python. Если нет, скачайте его [здесь](https://www.python.org/downloads/).
2. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-репозиторий/calculator.git
   cd calculator
   ```
3. Запустите программу:
   ```bash
   python calculator.pyw
   ```

Если вы хотите создать исполняемый файл `.exe`, используйте [PyInstaller](https://www.pyinstaller.org/):
```bash
pip install pyinstaller
pyinstaller --noconsole --onefile calculator.pyw
```

Готовый файл будет находиться в папке `dist/`.

## Использование
1. Введите математическое выражение в текстовое поле.
2. Нажмите кнопку "=" для вычисления результата.
3. Для очистки поля ввода используйте кнопку "C".
4. Переключите тему или язык через меню в верхней части окна.

### Пасхалка
Введите "1000-7" в поле ввода, чтобы активировать скрытый режим. Программа начнет создавать новые окна с последовательным уменьшением числа на 7.

## Поддерживаемые языки
Программа поддерживает следующие языки:
- Английский
- Русский
- Испанский
- Французский
- Немецкий
- Итальянский
- Португальский
- Японский
- Корейский
- Китайский

## Дополнительно
- **Темы**: Все темы доступны через меню "Темы". Выберите цветовую схему, которая лучше всего подходит для вашего настроения.
- **О программе**: В меню "О программе" вы найдете информацию об авторе.

## Автор
Автор программы: **walababa**  

--

### Примечания
- Если вы хотите добавить больше языков или тем, отредактируйте соответствующие словари в коде.
- Программа была протестирована на Windows. Если вы используете другую операционную систему, могут потребоваться дополнительные настройки.
