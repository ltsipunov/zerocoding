**Перед запуском убедитесь, что:**
- ваш проект Django настроен и работает
- модель `Film` определена в вашем приложении
- файл `Films.csv` находится в доступном месте
- вы запускаете скрипт в окружении Django (например, через `manage.py shell` или внутри команды Django)

---

### Скрипт для загрузки данных из CSV в базу данных Django

import csv
import os
import django

# Укажите путь к вашему проекту Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from your_app_name.models import Film  # замените на ваше приложение

csv_file_path = 'Films.csv'  # путь к вашему CSV файлу

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')  # разделитель - точка с запятой
    for row in reader:
        title = row['Название']
        description = row['Краткое описание']
        review = row['Обзор']
        # Создаем и сохраняем объект Film
        film = Film(title=title, description=description, review=review)
        film.save()

print('Данные успешно импортированы!')
```

---

### Инструкции:
1. **Замените `your_project_name.settings`** на название вашего проекта Django.
2. **Замените `your_app_name`** на имя вашего приложения, где находится модель `Film`.
3. Убедитесь, что файл `Films.csv` находится в той же папке или укажите полный путь к нему.
4. Запустите этот скрипт в окружении Django, например через `manage.py shell` или как отдельный скрипт, запустив `python script_name.py`.

---

Если потребуется более автоматизированное решение или команда Django, я могу помочь с созданием management-команды.