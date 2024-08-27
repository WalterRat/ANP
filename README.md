# Аннигиляторная пушка(ANP)

## Описание

Это GUI-приложение на Python, разработанное для загрузки параметров из текстового файла и генерации лога на основе этих параметров. Сгенерированные параметры со значениями записываются в файл `audit_log.txt`, который также можно просмотреть через интерфейс.

## Установка

### Требования

Для работы приложения требуется установленный Python версии 3.x с поддержкой библиотеки `tkinter`.

### Установка зависимостей

Если вы используете виртуальную среду, создайте её и активируйте:

```bash
python -m venv venv
source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
```

Установите необходимые зависимости, используя файл requirements.txt:

```bash
pip install -r requirements.txt
```

### Запуск приложения
Для запуска приложения выполните команду:

```bash
python main.py
```
### Использование
1. Нажмите кнопку "**Подключить файл с параметрами**" для выбора текстового файла, содержащего параметры. Каждый параметр должен быть разделён пробелом в файле.
2. Приложение автоматически создаст поля для ввода значений для каждого параметра.
3. Заполните необходимые значения и нажмите кнопку "**Сгенерировать лог**" для создания команды. Команда будет записана в файл audit_log.txt.
4. Вы можете просмотреть содержимое файла audit_log.txt, нажав кнопку "**Просмотреть audit_log.txt**".

### Структура файла параметров
Файл параметров должен быть текстовым файлом (**.txt**), где параметры записаны в одну строку и разделены пробелами. Пример:

```txt
param1 param2 param3
```
### Дополнительно
Файл **audit_log.txt** создается в той же директории, где запускается приложение. Если файл уже существует, новые записи будут добавлены в конец файла.

