
# Importación de bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# 1. Cargar el dataset MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 2. Visualizar algunas imágenes de ejemplo
def plot_sample_images(X, y, n_samples=5):
    plt.figure(figsize=(10, 2))
    for i in range(n_samples):
        plt.subplot(1, n_samples, i+1)
        plt.imshow(X[i], cmap='gray')
        plt.title(f"Etiqueta: {y[i]}")
        plt.axis('off')
    plt.show()

plot_sample_images(X_train, y_train)

# 3. Preprocesamiento de los datos
# Normalización (convertimos a flotante y normalizamos entre 0 y 1)
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Transformamos las etiquetas a formato one-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 4. Definición del modelo de red neuronal
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))  # Aplanar la imagen 28x28 a un vector 1D
model.add(Dense(128, activation='relu'))  # Capa oculta con 128 neuronas y activación ReLU
model.add(Dense(10, activation='softmax'))  # Capa de salida con 10 neuronas (dígitos 0-9) y activación softmax

# Compilamos el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 5. Entrenamiento del modelo
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# 6. Evaluación del modelo
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = np.argmax(y_test, axis=1)

# Calcular accuracy y f1_score
accuracy = accuracy_score(y_true_classes, y_pred_classes)
f1 = f1_score(y_true_classes, y_pred_classes, average='macro')

print(f"Precisión del modelo: {accuracy * 100:.2f}%")
print(f"F1 Score: {f1:.2f}")

# 7. Mostrar imágenes mal clasificadas
def mostrar_errores(X, y_true, y_pred, n_samples=5):
    errores = np.where(y_true != y_pred)[0]
    plt.figure(figsize=(10, 2))
    for i, idx in enumerate(errores[:n_samples]):
        plt.subplot(1, n_samples, i+1)
        plt.imshow(X[idx], cmap='gray')
        plt.title(f"Pred: {y_pred[idx]}, Real: {y_true[idx]}")
        plt.axis('off')
    plt.show()

mostrar_errores(X_test, y_true_classes, y_pred_classes)