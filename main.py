import time

# Obtenemos la fecha y hora actual
hora_actual = time.localtime().tm_hour

# Comprobamos si es hora de ir a casa
if hora_actual >= 19:
    print("Es hora de ir a casa.")
else:
    # Calculamos el tiempo que queda de trabajo
    tiempo_restante = (19 - hora_actual) * 60 # Convertimos a minutos
    print("Todavía quedan {} minutos de trabajo.".format(tiempo_restante))
