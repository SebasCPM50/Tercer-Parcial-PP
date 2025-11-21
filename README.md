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


