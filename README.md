# Тестовое задание 

### Загрузка модели

Поскольку модель слишком большая, необходимо скачать папку с моделью и токенизатором из [гугл диска](https://drive.google.com/drive/folders/1iC3Drhlkoo_fvF2yXPVPhLxSBjmmWetE?usp=sharing) и сохранить, как папку model.

Должна получиться следующая иерархия
```
bubuka/
├── interface.py
├── model/
│   ├── config.json
│   ├── pytorch_model.bin
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   ├── vocab.txt
└── templates/
    └── index.html
```

### Запуск проекта

Web-приложение запускается командой 
```bash
python interface.py
```

### Работа Web-приложения

Приложение запускается на http://127.0.0.1:5000

Интерфейс приложения

![Снимок экрана 2024-09-16 в 12 09 46](https://github.com/user-attachments/assets/94863be7-06ca-449a-9922-992ecce50e4f)

Для анализа текста необходимо вставить текст в поле для ввода и нажать кнопку Классифицировать.

![Снимок экрана 2024-09-16 в 12 12 32](https://github.com/user-attachments/assets/9cf12f03-1d70-4df3-b361-d570570a326c)
