from datetime import datetime
import random

def get_current_planet_positions() -> str:
    planets = [
        "Солнце в Весах",
        "Луна в Раке", 
        "Меркурий в Скорпионе",
        "Венера в Деве",
        "Марс в Скорпионе",
        "Юпитер в Тельце",
        "Сатурн в Рыбах"
    ]
    
    aspects = [
        "Солнце в гармоничном аспекте с Юпитером",
        "Луна соединяется с Венерой",
        "Марс в оппозиции к Сатурну",
        "Меркурий ретроградный",
        "Венера в трине с Нептуном"
    ]
    selected_planets = random.sample(planets, 3)
    selected_aspects = random.sample(aspects, 2)
    
    return f"{', '.join(selected_planets)}. {', '.join(selected_aspects)}"

def calculate_aspect(birth_date: datetime) -> str:
    month = birth_date.month
    day = birth_date.day
    
    zodiac_sign = get_zodiac_sign(month, day)
    
    predictions = {
        "Овен": "Энергичный день! Ваша инициатива будет вознаграждена.",
        "Телец": "День для наслаждения и комфорта. Побалуйте себя.",
        "Близнецы": "Отличный день для общения и новых знакомств.",
        "Рак": "Время для семьи и домашнего уюта.",
        "Лев": "Звёзды говорят о творческом подъёме!",
        "Дева": "День для планирования и организации дел.",
        "Весы": "Гармония и красота будут вашими спутниками.",
        "Скорпион": "Глубокие инсайты и трансформация ждут вас.",
        "Стрелец": "Время для путешествий и расширения горизонтов.",
        "Козерог": "День для достижения целей и карьерного роста.",
        "Водолей": "Неожиданные идеи и инновации придут к вам.",
        "Рыбы": "Интуиция будет особенно сильна сегодня."
    }
    
    base_prediction = predictions.get(zodiac_sign, "Хороший день для самоанализа.")
    
    additional = random.choice([
        " Обратите внимание на сны.",
        " Хороший день для медитации.",
        " Избегайте поспешных решений.",
        " Прислушайтесь к своей интуиции."
    ])
    
    return f"{base_prediction}{additional}"

def get_zodiac_sign(month: int, day: int) -> str:
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Стрелец"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козерог"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    else:
        return "Рыбы"