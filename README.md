# BreastCancer

Nesse projeto, foi constuida uma Rede Neural aplicada para resolução de um problema de categorização de cancers entre benigno e maligno. Para o treinamento da rede foi usado de um dataset disponivel na internet.

Inicialmente foi feita uma rede simples, com 16-16-1 neuronios, tendo nas 2 primeiras etapas a ativação dos neuronios pela função relu, e o neuronio de output com a função sigmoid, assim retornando um valor binario, que pode facilmente ser decodficado nos estados do problema.

Foi feito tambem um algoritmo para turning da rede neural. Usando da tecnica de GridSearchCV, foi testado diversas variações de redes neurais para o problema proposto e por fim foi retornado quais foram os melhores resultados obtidos, em acuracia.

Por fim foram implementados, um codigo para exportamento da rede neural em forma de arquivo .h5, como tambem um arquivo para importar a rede.
