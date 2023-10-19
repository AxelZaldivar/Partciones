import csv
import random
import matplotlib.pyplot as plt

# Partición aleatoria simple
def random_split(data, train_size):
    random.shuffle(data)
    split_index = int(train_size * len(data))
    train_set = data[:split_index]
    test_set = data[split_index:]
    return train_set, test_set

# Partición estratificada
def stratified_split(data, train_size):
    class_groups = {}
    for row in data:
        class_label = row[-1]
        if class_label not in class_groups:
            class_groups[class_label] = []
        class_groups[class_label].append(row)

    train_set, test_set = [], []

    for class_label, class_data in class_groups.items():
        random.shuffle(class_data)
        split_index = int(train_size * len(class_data))
        train_set.extend(class_data[:split_index])
        test_set.extend(class_data[split_index:])

    return train_set, test_set

# Partición por clase
def class_split(data, train_size):
    class_groups = {}
    for row in data:
        class_label = row[-1]
        if class_label not in class_groups:
            class_groups[class_label] = []
        class_groups[class_label].append(row)

    train_set, test_set = [], []

    for class_data in class_groups.values():
        random.shuffle(class_data)
        split_index = int(train_size * len(class_data))
        train_set.extend(class_data[:split_index])
        test_set.extend(class_data[split_index:])

    return train_set, test_set

# Partición por grupos de características
def feature_group_split(data, feature_index):
    if feature_index < 0 or feature_index >= len(data[0]):
        print("Invalid feature index.")
        return
    
    train_set, test_set = random_split(data, 0.7)

    train_feature_values = [float(row[feature_index]) for row in train_set]
    test_feature_values = [float(row[feature_index]) for row in test_set]

    plt.scatter(train_feature_values, [1] * len(train_feature_values), label='Train Set')
    plt.scatter(test_feature_values, [2] * len(test_feature_values), label='Test Set')
    plt.title(f'Feature Group Split (Feature {feature_index})')
    plt.yticks([1, 2], ['Train Set', 'Test Set'])
    plt.xlabel(f'Feature {feature_index}')
    plt.legend()

# Partición personalizada
def custom_split(data, train_indices):
    train_set = [data[i] for i in train_indices]
    test_set = [data[i] for i in range(len(data)) if i not in train_indices]
    return train_set, test_set

# Cargar el dataset
with open('irisbin.csv', 'r') as file:
    reader = csv.reader(file)
    dataset = list(reader)

# Ejemplo de uso de los métodos
train_set1, test_set1 = random_split(dataset, 0.7)
train_set2, test_set2 = stratified_split(dataset, 0.7)
train_set3, test_set3 = class_split(dataset, 0.7)
feature_group_split(dataset, 0)
train_indices = [0, 2, 4, 6]
train_set5, test_set5 = custom_split(dataset, train_indices)

# Visualización de los datos seleccionados
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.scatter([float(row[0]) for row in train_set1], [float(row[1]) for row in train_set1], label='Train Set')
plt.scatter([float(row[0]) for row in test_set1], [float(row[1]) for row in test_set1], label='Test Set')
plt.title('Random Split')
plt.legend()

plt.subplot(2, 3, 2)
plt.scatter([float(row[0]) for row in train_set2], [float(row[1]) for row in train_set2], label='Train Set')
plt.scatter([float(row[0]) for row in test_set2], [float(row[1]) for row in test_set2], label='Test Set')
plt.title('Stratified Split')
plt.legend()

plt.subplot(2, 3, 3)
plt.scatter([float(row[0]) for row in train_set3], [float(row[1]) for row in train_set3], label='Train Set')
plt.scatter([float(row[0]) for row in test_set3], [float(row[1]) for row in test_set3], label='Test Set')
plt.title('Class Split')
plt.legend()

plt.subplot(2, 3, 5)
plt.scatter([float(row[0]) for row in train_set5], [float(row[1]) for row in train_set5], label='Train Set')
plt.scatter([float(row[0]) for row in test_set5], [float(row[1]) for row in test_set5], label='Test Set')
plt.title('Custom Split')
plt.legend()

plt.subplot(2, 3, 4)
feature_group_split(dataset, 0)

plt.show()