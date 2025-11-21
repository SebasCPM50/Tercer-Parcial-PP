# linear_regression.py
# Basado en el código de descenso de gradiente proporcionado
import numpy as np
import time
import psutil
import os

# Datos de ejemplo
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

# Inicialización de parámetros
w = 0.0  # pendiente
b = 0.0  # intercepto

# Hiperparámetros
learning_rate = 0.01
epochs = 1000

m = len(X)  # número de ejemplos

# Medir memoria antes del entrenamiento
process = psutil.Process(os.getpid())
mem_before = process.memory_info().rss / 1024 / 1024  # MB

# Medir tiempo
start_time = time.time()

# Entrenamiento con descenso de gradiente
for epoch in range(epochs):
    # Predicción del modelo: y_pred = w * X + b
    y_pred = w * X + b

    # Cálculo del error
    error = y_pred - y

    # Cálculo de gradientes (derivadas parciales)
    dw = (2/m) * np.dot(error, X)      # sum(error * X) * 2/m
    db = (2/m) * np.sum(error)          # sum(error) * 2/m

    # Actualización de parámetros
    w -= learning_rate * dw
    b -= learning_rate * db

    # (Opcional) Mostrar el costo cada cierto número de épocas
    if (epoch + 1) % 200 == 0:
        mse = np.mean(error ** 2)
        print(f"Epoch {epoch+1}, MSE: {mse:.4f}, w: {w:.4f}, b: {b:.4f}")

# Medir tiempo y memoria después del entrenamiento
end_time = time.time()
mem_after = process.memory_info().rss / 1024 / 1024  # MB

training_time = end_time - start_time
memory_used = mem_after - mem_before

print("\nModelo entrenado:")
print(f"w = {w:.4f}, b = {b:.4f}")

# Probar el modelo
x_nuevo = 7
y_pred_nuevo = w * x_nuevo + b
print(f"\nPara x = {x_nuevo}, y_pred = {y_pred_nuevo:.4f}")

# Mostrar métricas de desempeño
print(f"\n--- MÉTRICAS DE DESEMPEÑO ---")
print(f"Tiempo de entrenamiento: {training_time:.6f} segundos")
print(f"Memoria usada: {memory_used:.4f} MB")


# =====================================================
# VERSIÓN CON BENCHMARK COMPLETO
# =====================================================

def train_linear_regression(X, y, learning_rate=0.01, epochs=1000, verbose=False):
    """
    Entrena un modelo de regresión lineal usando descenso de gradiente.
    Retorna w, b, tiempo de entrenamiento y memoria usada.
    """
    w = 0.0
    b = 0.0
    m = len(X)

    # Medir memoria antes
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / 1024 / 1024

    # Medir tiempo
    start_time = time.time()

    for epoch in range(epochs):
        # Predicción
        y_pred = w * X + b

        # Error
        error = y_pred - y

        # Gradientes
        dw = (2/m) * np.dot(error, X)
        db = (2/m) * np.sum(error)

        # Actualización
        w -= learning_rate * dw
        b -= learning_rate * db

        if verbose and (epoch + 1) % 200 == 0:
            mse = np.mean(error ** 2)
            print(f"Epoch {epoch+1}, MSE: {mse:.4f}")

    # Métricas finales
    end_time = time.time()
    mem_after = process.memory_info().rss / 1024 / 1024

    training_time = end_time - start_time
    memory_used = mem_after - mem_before

    return w, b, training_time, memory_used


def run_benchmark(n_samples_list=[100, 1000, 10000], n_runs=5):
    """
    Ejecuta benchmarks con diferentes tamaños de datasets.
    """
    print("="*70)
    print("BENCHMARK DE REGRESIÓN LINEAL - PYTHON")
    print("="*70)

    for n_samples in n_samples_list:
        print(f"\n### Dataset: {n_samples} muestras ###")
        print("-"*50)

        times = []
        memories = []

        for run in range(n_runs):
            # Generar datos sintéticos: y = 2*x + 3 + ruido
            np.random.seed(42 + run)
            X = np.random.randn(n_samples)
            y = 2 * X + 3 + np.random.randn(n_samples) * 0.1

            # Entrenar modelo
            w, b, train_time, mem_used = train_linear_regression(
                X, y, 
                learning_rate=0.01, 
                epochs=1000, 
                verbose=False
            )

            times.append(train_time)
            memories.append(mem_used)

            print(f"Run {run+1}: Tiempo={train_time:.6f}s, Memoria={mem_used:.4f}MB, w={w:.4f}, b={b:.4f}")

        # Estadísticas
        avg_time = np.mean(times)
        std_time = np.std(times)
        avg_memory = np.mean(memories)
        std_memory = np.std(memories)

        print("-"*50)
        print(f"PROMEDIO: Tiempo={avg_time:.6f}s, Memoria={avg_memory:.4f}MB")
        print(f"DESVIACIÓN: Tiempo={std_time:.6f}s, Memoria={std_memory:.4f}MB")


if __name__ == "__main__":
    print("\n### EJEMPLO BÁSICO (del código original) ###")
    print("="*70)

    # Ejecutar el ejemplo básico del código original
    X_simple = np.array([1, 2, 3, 4, 5], dtype=float)
    y_simple = np.array([2, 4, 6, 8, 10], dtype=float)

    w, b, train_time, mem_used = train_linear_regression(
        X_simple, y_simple, 
        learning_rate=0.01, 
        epochs=1000, 
        verbose=True
    )

    print(f"\nModelo final: w={w:.4f}, b={b:.4f}")
    print(f"Tiempo: {train_time:.6f}s, Memoria: {mem_used:.4f}MB")

    # Predicción
    x_nuevo = 7
    y_pred = w * x_nuevo + b
    print(f"\nPredicción para x={x_nuevo}: y={y_pred:.4f}")

    # Ejecutar benchmarks completos
    print("\n\n### BENCHMARKS COMPLETOS ###")
    run_benchmark(n_samples_list=[100, 1000, 10000], n_runs=5)
