from datetime import date, time, datetime, timedelta

def wdate():
    data_atual = date.today()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%d-%m-%Y'))
    print(data_atual.strftime('%A/%B/%Y'))
    data_atual_str = data_atual.strftime('%d/%m/%y')
    print(type(data_atual))
    print(type(data_atual_str))

def wtime():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    print(type(horario))
    print(horario.strftime('%H: %M: %S'))

def wdatetime():
    data_hora_atual = datetime.now()
    print(data_hora_atual)
    print(data_hora_atual.strftime('%d/ %m/ %Y'))
    print(data_hora_atual.strftime('%H: %M: %S'))
    print(data_hora_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_hora_atual.strftime('%c'))
    print(data_hora_atual.year)
    print(data_hora_atual.weekday())
    tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
    print(tupla[data_hora_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    data_string = '10/03/2020 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)


if __name__ == '__main__':
    #wdate()
    #wtime()
    wdatetime()
