import numpy as np
from keras.models import model_from_json

arquivo = open('classificador_breast.json', 'r')
estrutura = arquivo.read()
arquivo.close()

classificador = model_from_json(estrutura)
classificador.load_weights('classificador_breast.h5')

