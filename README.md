### Parcial Paradigmas

# Punto #1

# Diagramas de Flujo: Paradigmas de Programación Concurrente y Cálculo PI

## Introducción

Este repositorio contiene dos diagramas de flujo que comparan dos paradigmas de programación distintos para resolver el problema de **Regresión Lineal Distribuida**. Los diagramas muestran cómo cada paradigma aborda la ejecución paralela de tareas y la comunicación entre procesos.

---

## ¿Por qué estos dos paradigmas?

Cuando quieres que múltiples tareas se ejecuten "al mismo tiempo", tienes al menos dos formas principales de hacerlo:

1. **Programación Concurrente**: Varias tareas comparten recursos (memoria, datos) y el programa informa qué está pasando en cada momento.
2. **Cálculo PI**: Varios procesos completamente independientes que solo se comunican a través de "canales" especiales (como si fueran teléfonos dedicados).

---

## 📊 Diagrama 1: Paradigma de Programación Concurrente

### ¿Qué es?

La **programación concurrente** es un estilo donde el programa principal crea varias tareas que se ejecutan "casi al mismo tiempo". Cada tarea puede acceder a datos compartidos y el programa va informando sobre el progreso de cada una.

**Es como una fábrica donde:**
- El gerente (programa principal) crea 3 grupos de obreros
- Todos trabajan en el mismo espacio (comparten recursos)
- El gerente constantemente chequea qué está haciendo cada grupo
- Cuando todos terminan, el gerente combina los resultados

### Características Principales

| Característica | Explicación |
|---|---|
| **3 Tareas simultáneas** | Tarea 1, Tarea 2 y Tarea 3 se ejecutan al mismo tiempo |
| **Memoria compartida** | Las tareas pueden acceder a los mismos datos |
| **Sincronización explícita** | Hay un contador que verifica cuándo todas terminan |
| **Informes constantes** | El programa imprime qué está haciendo cada tarea |
| **Orden finalmente secuencial** | Los resultados se combinan en orden al final |

### Flujo Paso a Paso

```
1. INICIO
   └─ El programa imprime: "Sistema iniciado"

2. CREACIÓN
   └─ Se crean 3 tareas
   └─ El programa imprime: "Creando tareas..."
   └─ Inicializar contador en 0

3. EJECUCIÓN PARALELA (Las 3 tareas avanzan simultáneamente)

   Tarea 1:                          Tarea 2:                          Tarea 3:
   - Procesar datos A    |           - Procesar datos B    |           - Procesar datos C
   - Calcular            |           - Calcular            |           - Calcular
   - Reportar progreso   |           - Reportar progreso   |           - Reportar progreso
   - Incrementar contador|           - Incrementar contador|           - Incrementar contador

4. SINCRONIZACIÓN
   └─ Esperar a que contador llegue a 3
   └─ El programa verifica: ¿contador == 3?

5. COMBINACIÓN
   ├─ Si SÍ: Combinar resultados de las 3 tareas
   │         Mostrar resultado final
   │         Liberar recursos
   │         Imprime: "Sistema finalizado"
   │
   └─ Si NO: Manejar error
            Imprime: "ERROR: Tareas incompletas"

6. FIN
```

### Ventajas

✅ **Simple de entender**: Es como tareas trabajando en paralelo  
✅ **Buena para datos compartidos**: Las tareas pueden acceder a los mismos datos  
✅ **Fácil de depurar**: Se puede ver el progreso de cada tarea  

### Desventajas

❌ **Limitado en escalabilidad**: Compartir mucha memoria es problemático con muchas tareas  
❌ **Problemas de sincronización**: Riesgo de que dos tareas modifiquen los mismos datos  
❌ **Difícil de predecir**: El orden de ejecución puede variar  

### Ejemplo de Salida en Consola

```
Sistema iniciado
Creando tareas...
Tarea 1 iniciada
Tarea 2 iniciada
Tarea 3 iniciada
Tarea 1 ejecutando...
Tarea 2 ejecutando...
Tarea 3 ejecutando...
Tarea 1 en progreso 50%
Tarea 3 en progreso 50%
Tarea 2 en progreso 50%
Tarea 1 completada
Tarea 2 completada
Tarea 3 completada
Recolectando resultados...
Combinando datos...
Resultado Final: [dato1 + dato2 + dato3]
Tiempo total: 2.5 segundos
Sistema finalizado exitosamente
```

---

## 📊 Diagrama 2: Paradigma de Programación Cálculo PI

### ¿Qué es?

El **Cálculo PI** es un modelo teórico de programación donde tenemos **procesos completamente independientes** que se comunican exclusivamente a través de **canales**. Los procesos no comparten memoria, solo intercambian mensajes.

**Es como un centro de llamadas donde:**
- Hay 1 coordinador y 3 agentes de ventas
- Cada agente tiene su propio teléfono (canal)
- El coordinador solo se comunica por teléfono
- Los agentes solo hacen caso cuando reciben una llamada
- Al terminar, reportan por su teléfono

### Características Principales

| Característica | Explicación |
|---|---|
| **1 Coordinador + 3 Trabajadores** | Procesos completamente independientes |
| **4 Canales privados** | canal_datos, canal_gradientes, canal_parametros, canal_control |
| **Comunicación por mensajes** | Solo se comunican a través de canales |
| **Sincronización implícita** | Los canales sincronizan automáticamente |
| **Mayor escalabilidad** | Fácil agregar más procesos |
| **Sin memoria compartida** | Cada proceso tiene sus propios datos |

### Flujo Paso a Paso

```
1. INICIO
   └─ Sistema imprime: "Sistema Cálculo PI iniciado"

2. CREACIÓN DE PROCESOS Y CANALES
   ├─ Crear 1 proceso coordinador
   ├─ Crear 3 procesos trabajadores
   └─ Crear 4 canales privados:
      ├─ canal_datos (para distribuir datos)
      ├─ canal_parametros (para enviar parámetros)
      ├─ canal_gradientes (para recibir resultados)
      └─ canal_control (para señales)

3. INICIALIZACIÓN
   ├─ Coordinador crea parámetros iniciales: θ = [0.5, 0.3]
   ├─ Coordinador envía datos por canal_datos
   ├─ Los trabajadores reciben EN ESPERA del canal_datos:
   │  ├─ Trabajador 1 recibe partición 1
   │  ├─ Trabajador 2 recibe partición 2
   │  └─ Trabajador 3 recibe partición 3
   └─ El programa reporta lo que pasa

4. DISTRIBUCIÓN DE PARÁMETROS INICIALES
   ├─ Coordinador envía θ por canal_parametros
   ├─ Cada trabajador recibe EN ESPERA:
   │  ├─ Trabajador 1: "θ recibido"
   │  ├─ Trabajador 2: "θ recibido"
   │  └─ Trabajador 3: "θ recibido"
   └─ Los trabajadores están listos para trabajar

5. CICLO PRINCIPAL (se repite varias veces)

   FASE A - CÁLCULO EN PARALELO:
   (Los 3 trabajadores calculan al mismo tiempo)

   Trabajador 1:                     Trabajador 2:                     Trabajador 3:
   - Calcular ∇f₁ = [0.2, 0.1]  |   - Calcular ∇f₂ = [0.15, 0.12] |   - Calcular ∇f₃ = [0.25, 0.08]
   - Envía por canal_gradientes  |   - Envía por canal_gradientes  |   - Envía por canal_gradientes
   - Espera nuevo mensaje        |   - Espera nuevo mensaje        |   - Espera nuevo mensaje

   FASE B - AGREGACIÓN EN COORDINADOR:
   ├─ Coordinador espera 3 gradientes en canal_gradientes
   ├─ Recibe ∇f₁ de Trabajador 1
   ├─ Recibe ∇f₂ de Trabajador 2
   ├─ Recibe ∇f₃ de Trabajador 3
   └─ Imprime: "Los 3 gradientes recibidos"

   FASE C - ACTUALIZACIÓN EN COORDINADOR:
   ├─ Calcular promedio: ∇f_prom = (∇f₁+∇f₂+∇f₃)/3 = [0.20, 0.10]
   ├─ Actualizar: θ_nuevo = θ - α × ∇f_prom = [0.48, 0.29]
   ├─ Verificar convergencia: ¿||θ_nuevo - θ|| < ε?
   └─ Imprime: "Parámetros actualizados"

6. DECISIÓN DE CONVERGENCIA

   ├─ Si SÍ convergió:
   │  ├─ Enviar STOP por canal_control a todos
   │  ├─ Todos los trabajadores reciben STOP y finalizan
   │  ├─ Coordinador muestra parámetros finales
   │  └─ Imprime: "Convergencia alcanzada"
   │
   └─ Si NO convergió:
      ├─ Enviar CONTINUAR por canal_control
      ├─ Enviar θ_nuevo por canal_parametros
      ├─ Los trabajadores despiertan y calculan de nuevo
      └─ Vuelven a FASE A (Cálculo en paralelo)

7. FIN
   └─ Cuando converge: "Sistema finalizado exitosamente"
```

### Ventajas

✅ **Altamente escalable**: Puedes agregar más procesos sin problemas  
✅ **Sin conflictos de memoria**: Cada proceso tiene sus propios datos  
✅ **Fácil de razonar**: La comunicación es explícita y clara  
✅ **Seguro**: Un proceso no puede interferir con otro  

### Desventajas

❌ **Más abstracto**: Es más difícil de entender que la concurrencia simple  
❌ **Overhead de canales**: Más lento que compartir memoria directamente  
❌ **Mayor complejidad**: Hay que diseñar bien los canales  

### Ejemplo de Salida en Consola

```
Sistema Cálculo PI iniciado
Canales creados:
- canal_datos
- canal_gradientes
- canal_parametros
- canal_control
Coordinador: Parámetros iniciales θ = [0.5, 0.3]
Coordinador: Enviando particiones a los 3 trabajadores
Trabajador 1: Datos recibidos
Trabajador 2: Datos recibidos
Trabajador 3: Datos recibidos
Coordinador: Enviando parámetros iniciales
Trabajador 1: θ recibido = [0.5, 0.3]
Trabajador 2: θ recibido = [0.5, 0.3]
Trabajador 3: θ recibido = [0.5, 0.3]

--- ITERACIÓN 1 ---
Trabajador 1: Calculando ∇f₁ = [0.2, 0.1]
Trabajador 2: Calculando ∇f₂ = [0.15, 0.12]
Trabajador 3: Calculando ∇f₃ = [0.25, 0.08]
Trabajador 1: Gradiente enviado
Trabajador 2: Gradiente enviado
Trabajador 3: Gradiente enviado
Coordinador: Esperando 3 gradientes...
Coordinador: Recibido ∇f₁ de Trabajador 1
Coordinador: Recibido ∇f₂ de Trabajador 2
Coordinador: Recibido ∇f₃ de Trabajador 3
Coordinador: ∇f_prom = [0.20, 0.10]
Coordinador: Actualizando θ
Coordinador: θ_nuevo = [0.48, 0.29]
Coordinador: Verificar convergencia
Coordinador: Enviando CONTINUAR a Trabajadores
Coordinador: Broadcast de nuevos parámetros

--- ITERACIÓN 2 ---
[Repite el proceso...]

--- CONVERGENCIA ALCANZADA ---
Coordinador: Convergencia alcanzada
Coordinador: Enviando STOP a Trabajadores
Trabajador 1: Finalizando...
Trabajador 2: Finalizando...
Trabajador 3: Finalizando...
Parámetros finales: θ = [0.48, 0.29]
Iteraciones completadas: 5
Sistema finalizado exitosamente
```

---

## 🔄 Comparación Lado a Lado

### Concurrencia vs Cálculo PI

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

## 💡 Analogías para Entender Mejor

### Programación Concurrente = Equipo en una Oficina

```
┌─────────────────────────────────────┐
│     OFICINA (Memoria Compartida)    │
│                                      │
│  Persona 1      Persona 2   Persona 3│
│   [Working]      [Working]   [Working]│
│     en A           en B         en C │
│                                      │
│  Jefe: "¿Dónde van?"                │
│  Jefe: "Persona 1 42% hecha"        │
│  Jefe: "Persona 2 completada"       │
│  Jefe: "Esperando Persona 3..."     │
└─────────────────────────────────────┘

Todos usan el mismo espacio y herramientas.
El jefe constantemente chequea qué hace cada uno.
```

### Cálculo PI = Centro de Llamadas

```
┌────────────┐         Canales         ┌────────────┐
│Coordinador ├────────────────────────>│Trabajador 1│
│            │ "Aquí están tus datos"  │            │
│            │                         │ "Listo"    │
│            |<────────────────────────┤            │
│            │ "Calcula el gradiente"  │            │
│            ├────────────────────────>│            │
│            │                         │ Calculando │
│            │ "Envía el resultado"    │            │
│            │                         │ ∇f₁ enviado│
│            │<────────────────────────┤            │
└────────────┘                         └────────────┘

  Similar con Trabajador 2 y 3 por canales separados.

Cada uno tiene su teléfono (canal).
Solo se comunican por teléfono.
El coordinador no ve qué hacen, solo recibe mensajes.
```

---

## 🎯 Casos de Uso

### Usa Concurrencia cuando:
- Las tareas necesitan compartir muchos datos
- El problema es relativamente simple
- Ejecutas en una sola máquina
- El rendimiento es crítico (sin overhead de canales)

### Usa Cálculo PI cuando:
- Quieres máxima modularidad y escalabilidad
- Tienes muchos procesos independientes
- Trabajas en sistemas distribuidos (múltiples máquinas)
- Quieres evitar problemas de sincronización compleja
- Necesitas garantías de seguridad (un proceso no afecta a otro)

---

## 📝 Cómo Leer los Diagramas

### Para el diagrama Concurrente:

1. **Sigue la línea de arriba a abajo**
2. **Cuando veas `fork`**: Las tareas ahora van en paralelo (lee los 3 brazos simultáneamente)
3. **Lee las notas**: Esas son las cosas que el programa imprime
4. **Cuando regresa a una línea**: Los procesos se sincronizaron (se esperaron mutuamente)
5. **El `if`**: Es la decisión: ¿Todas completaron? Sí o No

### Para el diagrama Cálculo PI:

1. **Sigue de arriba a abajo como antes**
2. **Cuando veas `fork`**: Los procesos avanzan en paralelo
3. **Las acciones de cada proceso**: Esperar, Calcular, Enviar (por sus canales)
4. **Las notas**: Qué se imprime en consola (para debugging)
5. **Después del fork**: El coordinador recolecta todos los mensajes
6. **El `if`**: Decisión: ¿Convergió? Sí → STOP. No → CONTINUAR

---

## 🚀 Próximos Pasos

Para implementar estos diseños, necesitarías:

### Programación Concurrente:
- Usar `threads` en Java, Python (`threading`), C++ (`pthread`)
- Usar `locks` o `mutex` para sincronización
- Usar contadores o `barriers` para esperar tareas

### Cálculo PI:
- Usar un lenguaje que soporte paso de mensajes:
  - Erlang, Go, Akka, MPI (para paralelo)
  - O implementar con sockets/HTTP para sistemas distribuidos

---

## 📚 Recursos para Aprender Más

### Programación Concurrente:
- "The Art of Multiprocessor Programming" - Herlihy & Shavit
- Documentación oficial de threading en tu lenguaje

### Cálculo PI:
- "Communicating Sequential Processes" - Tony Hoare (CSP)
- Documentación de Erlang o Go para ejemplos prácticos

---

## ❓ Preguntas Frecuentes

**P: ¿Cuál es más rápido?**  
R: Concurrencia es generalmente más rápida (menos overhead), pero Cálculo PI es más escalable.

**P: ¿Puedo usar ambos juntos?**  
R: Sí, muchos sistemas usan concurrencia dentro de procesos y Cálculo PI entre procesos.

**P: ¿Es Cálculo PI solo teoría?**  
R: No, lenguajes como Erlang y Go lo implementan en la práctica.

**P: ¿Por qué se llama "Cálculo PI"?**  
R: Porque el símbolo π se usa para representar procesos (del griego "proceso").

---

## 📄 Estructura del Repositorio

```
.
├── README.md                          (este archivo)
├── diagrama_concurrente_CORREGIDO.puml (Diagrama 1)
├── diagrama_pi_CORREGIDO.puml         (Diagrama 2)
├── ejemplos/
│   ├── concurrencia_python.py         (Ejemplo en Python)
│   ├── calculus_pi_go.go              (Ejemplo en Go)
│   └── README_ejemplos.md
└── recursos/
    ├── refencias_teoricas.md
    └── enlaces_utiles.md
```

---

## 👤 Autor

Documento de referencia para estudiantes de paradigmas de programación.

## 📄 Licencia

Libre para usar con propósitos educativos.

---

## 📞 Dudas o Sugerencias

Si hay algo que no entiendes o quieres más detalle sobre algún aspecto, consulta las secciones correspondientes de este README.

**Recuerda:** La programación concurrente es complicada. Tómate tu tiempo para entenderla bien.
