import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Las guaguas del ITLA laboran de lunes a viernes en horario corrido desde las 8: 00 a.m. a 10:00 p.m. y sábados 9:00 a.m. a 6:00 p.m., debe de tener su ticket para usar el transporte', ['transporte', 'tranporte', 'guagua', 'ticket', 'tickets', 'bus'], single_response = True)


        response('El horario de clases depende de las materias seleccionadas, de modo general los horarios de clases del tecnólogo varían de 8:00am a 10:00pm, reiteramos que depende de las materias seleccionadas por el estudiante.', ['clases', 'clase'], single_response = True)


        response('El instituto tecnologico las americas ITLA imparte las siguientes carreras: seguridad informatica, analita y ciencias de datos, desarrolo de software, mutimedia, sonido, diseño industrial, mecatronica, redes de la informatica', ['carrera', 'carrera', 'materia', 'materias'], single_response = True)

        response('Vienvenido al instituto las americas el ITLA. como te podemos ayudar?', ['hola', 'klk', 'saludos', 'buenas', 'hi', 'hello'], single_response = True)

        response('Autopista las americas km 27 la caleta boca chica', ['ubicacion', 'direccion', 'ubicados', 'ubucado'], single_response = True)

        response('La inscripcion tienen un costo de $6,640 y los creditos $520 ', ['precios', 'precio', 'costo', 'costos', 'inscripcion', 'creditos, credito'], single_response = True)

        response('Laboramos  Luneas a Viernes de 8:00am a 5:00pm', ['horario', 'abierto', 'cierran', 'abren'], single_response = True)
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))