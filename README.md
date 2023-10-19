# Partciones
En este archivo se explican los 5 métodos de partición implementados en el algoritmo. Todos se dividen en dos conjuntos, uno de prueba y otro de entrenamiento. El porcentaje de particion de los datos es de 0.7 para todos los métodos, pero es completamente personalizable.

1) random_split: Realiza una partición aleatoria simple de los datos en conjuntos de entrenamiento y prueba. Permite determinar la proporción de datos que se asignará al conjunto de entrenamiento y de prueba.

2) stratified_split: Realiza una partición estratificada de los datos, lo que significa que mantiene la misma proporción de clases en el conjunto de entrenamiento y prueba. Permite determinar la proporción de datos que se asignará al conjunto de entrenamiento.

3) class_split: Realiza una partición de los datos basada en clases. Cada clase se divide en un conjunto de entrenamiento y un conjunto de prueba. Este método permite determinar la proporción de datos que se asignará al conjunto de entrenamiento.

4) feature_group_split: Realiza una partición de datos basada en un índice de característica específico. Los datos se dividen en conjuntos de entrenamiento y prueba, y se crea un gráfico para visualizar la división de datos según el valor de la característica especificada.

5) custom_split: Realiza una partición personalizada de los datos. Se pueden especificar los índices que se asignan al conjunto de entrenamiento, mientras que los demás datos se asignan al conjunto de prueba.

![image](https://github.com/AxelZaldivar/Partciones/assets/89545307/eb816b30-0ee2-4b21-a0e1-f8ce49c42909)
