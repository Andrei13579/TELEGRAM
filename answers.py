import random
    
answers = {
    'Привет': ['Хай', 'Хелоу', 'Привет', 'Hello', 'Пр'],
    'Как дела?': ['Норм', 'Ужас', ':(', ':)', '^_____^'],
    'Какая погода за окном?': ['Иди сам посмотри!', 'Хватит играть. Уже погоду посмотреть не можеш', 'Думаеш я знаю', 'Мне лень', '🌈'],
    'Как тебя зовут?': ['Siri', 'Алиса', 'RSmartBot', 'PythonBot', 'Мой разраб лентяй не придумал имени:['],
    'Сколько тебе дней?': ['0', 'Я только родился', 'Секрет', 'Не скажу', 'А тебе какая разница'],
    'Который час?': ['00:00', 'Вон туда в низ в углу посмотри', 'Я не знаю', 'send_gif', 'Не скажу']
}

def get_answer(qustion):
    if answers.get(qustion) == None:
        return 'Не пон'
    else:
        answer = random.choice(answers.get(qustion))
        if answer == 'send_gif':
           pass
        else:
            return answer

