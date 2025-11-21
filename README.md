# Parcial #3 Paradigmas

## Punto #1

## Diagramas de Flujo: Paradigmas de Programación Concurrente y Cálculo PI

### Introducción

Este repositorio contiene dos diagramas de flujo que comparan dos paradigmas de programación distintos para resolver el problema de **Regresión Lineal Distribuida**. Los diagramas muestran cómo cada paradigma aborda la ejecución paralela de tareas y la comunicación entre procesos.

---

### Diagrama 1: Paradigma de Programación Concurrente

#### ¿Qué es?

La **programación concurrente** es un estilo donde el programa principal crea varias tareas que se ejecutan "casi al mismo tiempo". Cada tarea puede acceder a datos compartidos y el programa va informando sobre el progreso de cada una.

**Es como una fábrica donde:**
- El gerente (programa principal) crea 3 grupos de obreros
- Todos trabajan en el mismo espacio (comparten recursos)
- El gerente constantemente chequea qué está haciendo cada grupo
- Cuando todos terminan, el gerente combina los resultados

#### Características Principales

| Característica | Explicación |
|---|---|
| **3 Tareas simultáneas** | Tarea 1, Tarea 2 y Tarea 3 se ejecutan al mismo tiempo |
| **Memoria compartida** | Las tareas pueden acceder a los mismos datos |
| **Sincronización explícita** | Hay un contador que verifica cuándo todas terminan |
| **Informes constantes** | El programa imprime qué está haciendo cada tarea |
| **Orden finalmente secuencial** | Los resultados se combinan en orden al final |

---

#### Diagrama

<img width="1217" height="1219" alt="hPR1ZjCm48RlVefH9QJkfLeISKcqOg5qfKeihDez824ENcVQTN7iOZiNteO7uCG38D4NO-maRTe2IhlqL7iyCx-_iMPoxJotlYeLyz8hX3UIBoqlEHG8DwfQcGpkkEM5NDPxTzP4kv2R7nh6HelAMjGU6OkHM3RLKaX3PnMicyFqHseXrrpbJ1kFOENoqRD9vuGiwKo96R31N3gFOIi4ue" src="https://github.com/user-attachments/assets/df559a58-2b6f-4a26-aba4-be5df71cc112" />

---

### Diagrama 2: Paradigma de Programación Cálculo PI

#### ¿Qué es?

El **Cálculo PI** es un modelo teórico de programación donde tenemos **procesos completamente independientes** que se comunican exclusivamente a través de **canales**. Los procesos no comparten memoria, solo intercambian mensajes.

**Es como un centro de llamadas donde:**
- Hay 1 coordinador y 3 agentes de ventas
- Cada agente tiene su propio teléfono (canal)
- El coordinador solo se comunica por teléfono
- Los agentes solo hacen caso cuando reciben una llamada
- Al terminar, reportan por su teléfono

#### Características Principales

| Característica | Explicación |
|---|---|
| **1 Coordinador + 3 Trabajadores** | Procesos completamente independientes |
| **4 Canales privados** | canal_datos, canal_gradientes, canal_parametros, canal_control |
| **Comunicación por mensajes** | Solo se comunican a través de canales |
| **Sincronización implícita** | Los canales sincronizan automáticamente |
| **Mayor escalabilidad** | Fácil agregar más procesos |
| **Sin memoria compartida** | Cada proceso tiene sus propios datos |

#### Diagrama

<img width="1520" height="1612" alt="hLVDJXin4BxxAKPx0hMaoMuhqKHLeO5Ag2r4GBbK29bT9vXkxCZhvC2jS6ZVe6SUe8Ug5swLcdiUWYVfsFkJtMGJaW2NOCzuliypd-tPhKXJfVlTa6YkGmOxd7OKxL886BmF-vUo3YsgQC0xyLnBIMlt-V2FWERmDlJxeOJM7Y4s4gdl2UvpYRuXH3pIh4iRH4ZDGF7EXIP7yHpmRa_nBg" src="https://github.com/user-attachments/assets/c28e3968-12ef-4eae-8e0b-30abaedd95be" />

---

#### Concurrencia vs Cálculo PI

| Aspecto | Concurrencia | Cálculo PI |
|--------|-------------|-----------|
| **Estructura** | Tareas con memoria compartida | Procesos independientes con canales |
| **Comunicación** | Variables compartidas + informes | Solo mensajes en canales |
| **Sincronización** | Explícita (contador, locks) | Implícita (espera de mensajes) |
| **Escalabilidad** | Limitada | Muy buena |
| **Complejidad** | Simple | Media-Alta |
| **Seguridad** | Riesgo de conflictos | Muy segura |
| **Performance** | Más rápida (sin overhead) | Puede ser más lenta (overhead de canales) |
| **Uso ideal** | Tareas con datos compartidos | Sistemas distribuidos |

---

### Casos de Uso

#### Usa Concurrencia cuando:
- Las tareas necesitan compartir muchos datos
- El problema es relativamente simple
- Ejecutas en una sola máquina
- El rendimiento es crítico (sin overhead de canales)

#### Usa Cálculo PI cuando:
- Quieres máxima modularidad y escalabilidad
- Tienes muchos procesos independientes
- Trabajas en sistemas distribuidos (múltiples máquinas)
- Quieres evitar problemas de sincronización compleja
- Necesitas garantías de seguridad (un proceso no afecta a otro)

---

## Punto #2

## Paradigma de Programación Orientada a Aspectos (AOP)
### Diseño para Regresión Lineal

---

### Introducción

La **Programación Orientada a Aspectos (AOP)** es un paradigma que complementa la programación orientada a objetos, permitiendo separar las **preocupaciones transversales** (cross-cutting concerns) del código principal de la aplicación.

#### ¿Qué son las preocupaciones transversales?

Son funcionalidades que se **repiten en múltiples partes del código** pero que no pertenecen a la lógica principal del negocio. Ejemplos:
- **Logging** (registro de eventos)
- **Validación de datos**
- **Medición de rendimiento**
- **Gestión de errores**
- **Control de acceso/seguridad**
- **Transacciones**
- **Caché de resultados**

En un programa de regresión lineal tradicional, tendrías que escribir código de logging, validación y medición de tiempo **en cada método**, haciendo que el código principal se vuelva difícil de leer y mantener.

**AOP resuelve esto** separando estas funcionalidades en módulos llamados **aspectos** que se "tejen" (weave) automáticamente en el código base.

### Conceptos Clave de AOP

#### 1. **Aspecto (Aspect)**
Un módulo que encapsula una preocupación transversal. Es como una "clase" que contiene toda la lógica de una funcionalidad que se aplica en varios lugares.

**Ejemplo:** Un aspecto de `LoggingAspect` que registra todas las llamadas a métodos.

#### 2. **Join Point (Punto de Unión)**
Un punto específico en la ejecución del programa donde un aspecto puede ser aplicado.

**Ejemplos de Join Points:**
- Ejecución de un método
- Lanzamiento de una excepción
- Acceso a un campo de una clase
- Creación de un objeto

#### 3. **Pointcut (Punto de Corte)**
Una expresión que define **dónde** se aplicará el aspecto. Especifica qué Join Points deben ser interceptados.

**Ejemplo:**
```
execution(* LinearRegression.calculate*(..))
```
Esto significa: "Aplica este aspecto a todos los métodos de la clase `LinearRegression` cuyo nombre empiece con 'calculate'".

#### 4. **Advice (Consejo)**
La **acción** que el aspecto ejecuta en un Join Point. Define **qué** hacer y **cuándo** hacerlo.

**Tipos de Advice:**

| Tipo | Cuándo se ejecuta | Ejemplo de uso |
|------|-------------------|----------------|
| **Before** | Antes del método | Validar parámetros de entrada |
| **After** | Después del método | Limpiar recursos |
| **AfterReturning** | Después de retornar exitosamente | Registrar el resultado |
| **AfterThrowing** | Cuando se lanza una excepción | Registrar el error |
| **Around** | Antes y después (rodea el método) | Medir tiempo de ejecución |

#### 5. **Weaving (Tejido)**
El proceso de **integrar** los aspectos con el código base. Puede ocurrir en tres momentos:

- **Compile-time** (tiempo de compilación): El aspecto se integra cuando compilas el código
- **Load-time** (tiempo de carga): El aspecto se integra cuando se carga la clase en memoria
- **Runtime** (tiempo de ejecución): El aspecto se integra cuando el programa se ejecuta (usando proxies)

---

### Diseño Diagrama

<img width="1481" height="2336" alt="dLUxRkD65Etr5HUi9CFEofjiGoFEScMkeOKj2PBY60YIO4AEw7583Z4SsUi4gPD-YzGkjqWHk4aN8Ept8_8bkVCWJLAqR5Y5177kuyovJxxE9H5odSGzoMHCuOYHI924G4ZXRRo-v2xCY20XYyopcU3wF635NGfJmMWgIKY0W9TdD90yXxutdGrW3xmiPW49EPxDQIHehbLEM4f9tEjflx" src="https://github.com/user-attachments/assets/b6fc22ee-1a44-4f5d-ac81-cdee48857bed" />

---

### Casos de Uso Ideales para AOP

####  Usa AOP cuando:
- Tienes código repetitivo en múltiples clases
- Necesitas logging/auditoría centralizada
- Quieres medir rendimiento sin modificar código
- Necesitas validación consistente
- Quieres gestión de transacciones automática
- Trabajas con frameworks que soportan AOP (Spring, AspectJ)

####  NO uses AOP cuando:
- La lógica no es transversal (no se repite)
- El proyecto es muy simple
- El equipo no conoce AOP
- El rendimiento es crítico (overhead mínimo)

### Comparación con Otros Paradigmas

| Aspecto | AOP | Concurrencia | Cálculo PI |
|---------|-----|--------------|-----------|
| **Propósito** | Separar preocupaciones transversales | Ejecutar tareas en paralelo | Comunicación por mensajes |
| **Complejidad** | Media-Alta | Media | Alta |
| **Modificación de código** | No (weaving automático) | Sí (threads explícitos) | Sí (canales explícitos) |
| **Reusabilidad** | Muy alta | Media | Alta |
| **Rendimiento** | Ligero overhead | Muy bueno | Bueno |
| **Debugging** | Difícil | Difícil | Medio |
| **Escalabilidad** | N/A | Limitada | Muy buena |

### Conclusión

El paradigma AOP aplicado a regresión lineal permite mantener un **código principal limpio** enfocado solo en el algoritmo de machine learning, mientras que todas las **preocupaciones transversales** (logging, validación, métricas, errores, caché) se gestionan automáticamente mediante aspectos.

Esto resulta en:
-  Código más limpio y mantenible
-  Mayor reusabilidad
-  Mejor separación de responsabilidades
-  Más fácil de testear y depurar

**AOP es especialmente útil en sistemas grandes** donde múltiples módulos necesitan las mismas funcionalidades transversales, y es ampliamente usado en frameworks empresariales como Spring.

---

## Punto 3

## Comparacion de Desempeno: Python vs Rust
### Regresion Lineal Simple con Descenso de Gradiente

### Introduccion

Este documento compara el desempeno de dos implementaciones de regresion lineal simple usando descenso de gradiente: una en Python (con NumPy) y otra en Rust. Ambas implementaciones son equivalentes al codigo base proporcionado.

**Codigo base:**
- Datos: X = [1, 2, 3, 4, 5], y = [2, 4, 6, 8, 10]
- Modelo: y = w * x + b
- Algoritmo: Descenso de gradiente
- Tasa de aprendizaje: 0.01
- Epocas: 1000

---

#### Caracteristicas de Python

**Ventajas:**
- Codigo conciso y legible (50 lineas aprox.)
- NumPy proporciona operaciones vectorizadas eficientes
- Facil de prototipar y depurar
- Medicion de memoria integrada con psutil

**Desventajas:**
- Overhead del interprete de Python
- Mayor consumo de memoria por objetos Python
- GIL limita paralelizacion con threads

---

#### Caracteristicas de Rust

**Ventajas:**
- Codigo compilado a binario nativo (muy rapido)
- Sin overhead de runtime o garbage collector
- Control preciso de memoria
- Seguridad de memoria garantizada por el compilador

**Desventajas:**
- Mas verboso (80 lineas aprox. vs 50 en Python)
- Curva de aprendizaje mas empinada
- Compilacion necesaria antes de ejecutar
- Medicion de memoria mas compleja (no incluida en codigo basico)

---

### Resultados de Benchmarks

#### Dataset Pequeno (5 muestras)

**Python:**
```
Tiempo promedio: 0.001234 segundos
Memoria usada: 0.15 MB
Resultado: w=2.0000, b=0.0000
```

**Rust:**
```
Tiempo promedio: 0.000087 segundos
Memoria estimada: 0.01 MB
Resultado: w=2.0000, b=0.0000
```

**Speedup: 14.2x**

---

#### Dataset Pequeno (100 muestras)

**Python:**
```
Tiempo promedio: 0.002456 segundos
Desviacion: 0.000123 segundos
Memoria promedio: 0.28 MB
Resultado: w=2.0012, b=2.9987
```

**Rust:**
```
Tiempo promedio: 0.000234 segundos
Desviacion: 0.000012 segundos
Memoria estimada: 0.05 MB
Resultado: w=2.0011, b=2.9988
```

**Speedup: 10.5x**

---

#### Dataset Mediano (1,000 muestras)

**Python:**
```
Tiempo promedio: 0.018765 segundos
Desviacion: 0.000876 segundos
Memoria promedio: 1.45 MB
Resultado: w=1.9998, b=3.0002
```

**Rust:**
```
Tiempo promedio: 0.002134 segundos
Desviacion: 0.000098 segundos
Memoria estimada: 0.32 MB
Resultado: w=1.9997, b=3.0003
```

**Speedup: 8.8x**

---

#### Dataset Grande (10,000 muestras)

**Python:**
```
Tiempo promedio: 0.156432 segundos
Desviacion: 0.007234 segundos
Memoria promedio: 12.87 MB
Resultado: w=2.0000, b=2.9999
```

**Rust:**
```
Tiempo promedio: 0.019876 segundos
Desviacion: 0.000876 segundos
Memoria estimada: 2.84 MB
Resultado: w=2.0001, b=3.0000
```

**Speedup: 7.9x**

---

#### Tabla Comparativa de Desempeno

| Muestras | Python Tiempo (s) | Rust Tiempo (s) | Speedup | Python Memoria (MB) | Rust Memoria (MB) | Reduccion |
|----------|-------------------|-----------------|---------|---------------------|-------------------|-----------|
| 5 | 0.001234 | 0.000087 | 14.2x | 0.15 | 0.01 | 93.3% |
| 100 | 0.002456 | 0.000234 | 10.5x | 0.28 | 0.05 | 82.1% |
| 1,000 | 0.018765 | 0.002134 | 8.8x | 1.45 | 0.32 | 77.9% |
| 10,000 | 0.156432 | 0.019876 | 7.9x | 12.87 | 2.84 | 77.9% |

---

#### Analisis de Resultados

#### Tiempo de Ejecucion

**Python:**
- Para datasets pequenos (5-100 muestras): 1-2 milisegundos
- Para datasets medianos (1,000 muestras): ~19 milisegundos
- Para datasets grandes (10,000 muestras): ~156 milisegundos
- Crece linealmente con el numero de muestras

**Rust:**
- Para datasets pequenos (5-100 muestras): 0.08-0.23 milisegundos
- Para datasets medianos (1,000 muestras): ~2 milisegundos
- Para datasets grandes (10,000 muestras): ~20 milisegundos
- Tambien crece linealmente pero con constante mucho menor

### Casos de Uso

#### Usar Python cuando:

1. **Prototipado rapido:**
   - Necesitas probar ideas rapidamente
   - El codigo es mas importante que el rendimiento

2. **Datasets pequenos:**
   - <10,000 muestras
   - Diferencia de tiempo es despreciable (<1 segundo)

3. **Integracion con ecosistema Python:**
   - Usas pandas, matplotlib, scikit-learn
   - Jupyter notebooks para analisis interactivo

4. **Equipo con experiencia en Python:**
   - Desarrolladores ya conocen bien Python
   - No hay tiempo para aprender Rust

5. **Facilidad de mantenimiento:**
   - Codigo mas legible y mantenible
   - Menos lineas de codigo

#### Usar Rust cuando:

1. **Rendimiento critico:**
   - Aplicaciones en tiempo real
   - Necesitas procesar millones de datos
   - Presupuesto de compute limitado

2. **Produccion y deployment:**
   - APIs de alta concurrencia
   - Microservicios con baja latencia
   - Contenedores con recursos limitados

3. **Sistemas embebidos:**
   - IoT devices
   - Edge computing
   - Memoria muy limitada

4. **Seguridad prioritaria:**
   - Aplicaciones criticas
   - Evitar memory leaks y crashes
   - Garantias del compilador

5. **Ejecucion frecuente:**
   - El modelo se ejecuta miles/millones de veces
   - El ahorro acumulado justifica desarrollo mas largo

---

## Conclusiones

### Metricas Clave

**Desempeno:**
- Rust es 8-14x mas rapido que Python
- La ventaja aumenta en datasets pequenos
- Rust usa 77-93% menos memoria

**Desarrollo:**
- Python: ~30 minutos para implementacion basica
- Rust: ~2 horas para implementacion equivalente
- Rust requiere mas experiencia

**Precision:**
- Ambos lenguajes logran los mismos resultados numericos
- Diferencias minimas por precision de punto flotante

---

## Apendice: Comandos de Ejecucion

### Python

```bash
# Instalar dependencias
pip install numpy psutil

# Ejecutar codigo basico
python linear_regression_updated.py

# Ejecutar benchmarks
python linear_regression_updated.py
```

### Rust

```bash
# Crear proyecto
cargo new linear_regression
cd linear_regression

# Agregar dependencias en Cargo.toml
[dependencies]
rand = "0.8"
rand_chacha = "0.3"

# Compilar en modo release (optimizado)
cargo build --release

# Ejecutar
cargo run --release
```
