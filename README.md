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
