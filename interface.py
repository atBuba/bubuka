from flask import Flask, request, render_template
from transformers import BertTokenizer, BertForSequenceClassification
import torch

app = Flask(__name__)

model_path = 'model'

model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained(model_path)


categories = ['Грусть/Печаль/Страдания', 'Оптимизм/Веселье/Счастье', 'Новый год/Рождество', 
        'Любовь/Романтика', 'Патриотическая песня', 'Лето', 'Осень'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            probabilities = torch.sigmoid(logits).cpu().numpy()[0]
        results = {cat: prob for cat, prob in zip(categories, probabilities)}
        sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
        return render_template('index.html', text=text, results=sorted_results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



