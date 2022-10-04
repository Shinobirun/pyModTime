from datetime import datetime, time


def tiempo():
    ahora = datetime.now()
    hora_actual: time = time(ahora.hour, ahora.minute)
    hora_sal: time = time(19, 00)

    if hora_actual >= hora_sal:
        print('terminó el horario de trabajo')
    else:
        falta_h: time = hora_sal.hour - hora_actual.hour
        falta_m = (hora_sal.minute - hora_actual.minute)+60
        print('faltan: ', falta_h, falta_m, ' horas para la salida')

    return





