import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense

arq = pd.read_csv('cancer.csv')
arq['diagnosis'] = arq['diagnosis'].replace('M', 0)
arq['diagnosis'] = arq['diagnosis'].replace('B', 1)

previsores = arq.drop(['id', 'diagnosis', 'Unnamed: 32'], axis=1)
classe = arq['diagnosis']

classificador = Sequential()
classificador.add(Dense(units = 16, activation = 'relu', 
                        kernel_initializer = 'random_uniform', input_dim = 30))
classificador.add(Dense(units = 16, activation = 'relu', 
                        kernel_initializer = 'random_uniform'))
classificador.add(Dense(units = 1, activation = 'sigmoid'))

otimizador = keras.optimizers.Adam(lr = 0.001, decay = 0.0001, clipvalue = 0.5)
classificador.compile(optimizer = otimizador, loss = 'binary_crossentropy',
                      metrics = ['binary_accuracy'])
classificador.fit(previsores, classe,
                  batch_size = 10, epochs = 100)

classificador_json = classificador.to_json()
with open('classificador_breast.json', 'w') as json_file:
    json_file.write(classificador_json)
classificador.save_weights('classificador_breast.h5')
