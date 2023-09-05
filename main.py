import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


def message_probability(user_message, recognized_words):
    message_certainty = 0

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))
    return int(percentage * 100)


def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words)

    response('Hola', ['hola', 'saludos', 'buenas'])
    response('Estoy bien ¿y tu?', ['como', 'estas', 'vas', 'sientes', 'que', 'tal'])
    response('Mi lenguaje favorito es Python', ['lenguaje', 'programacion', 'favorito', 'gusta'])
    response('Prefiero el frio', ['frio', 'calor', 'gusta'])
    response('Porque en ese lenguaje me crearon', ['python'])
    response('Soy de CUCEI', ['eres', 'vienes', 'donde'])
    response('Axel, el mejor programador de todos', ['dueño', 'quien'])
    response('Pez', ['2', 'mas', 'dos'])
    response(['Amo la pizza', 'Me encantan las hamburguesas', 'Soy fit, asi que, pura ensalada con salmon'][random.randrange(3)], ['comida', 'platillo','favorita','gusta','mas'])
    response('No hay de que', ['gracias', 'te lo agradezco', 'thanks', 'muchas'])
    response('¿Por que, que?', ['por', 'qué'])
    response('No, tu eres el mejor :)', ['excelente', 'bien'])

    best_match = max(highest_prob, key=highest_prob.get)
    return unknown() if highest_prob[best_match] < 1 else best_match


def unknown():
    response = ['¿Puedes decirlo de nuevo?', 'No estoy seguro', 'Búscalo en Google'][random.randrange(3)]
    return response


while True:
    print("Bot: " + get_response(input('Humano: ')))