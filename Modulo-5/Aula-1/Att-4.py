import datetime

agora = datetime.datetime.now()

print("Data: {:02}/{:02}/{}".format(agora.day, agora.month, agora.year))
print("Hora: {:02}:{:02}".format(agora.hour, agora.minute))