# Tarea-1-24-25: Juego de Disparos en Python

https://github.com/luis-lop-nas/Tarea-1-24-25.git

## Descripción
Este proyecto consiste en un **juego de disparos** desarrollado en Python utilizando los principios de **Programación Orientada a Objetos (POO)**. El objetivo del juego es controlar un personaje principal, disparar a los enemigos, esquivar sus disparos y convertirlos en estrellas para avanzar en el juego. Al derrotar a un enemigo, aparece un jefe final que se mueve más rápido y representa un desafío mayor.

## Estructura del Proyecto
El proyecto está organizado en varias clases que representan los elementos principales del juego. A continuación, se describe la estructura y funcionalidad de cada clase:

### **Clases y Métodos**
#### **Entity**
Clase base que representa cualquier elemento del juego.

- **Atributos**:
  - `x`, `y`: Coordenadas de posición.
  - `image`: Imagen asociada al elemento.
- **Métodos**:
  - `move()`: Mueve el elemento en el juego.
  - `draw()`: Dibuja el elemento en pantalla.

#### **Character** (Hereda de `Entity`)
Clase que representa cualquier personaje con vida dentro del juego.

- **Atributos**:
  - `lives`: Número de vidas.
  - `is_alive`: Indica si el personaje está vivo.
- **Métodos**:
  - `move()`: Mueve al personaje.
  - `shoot()`: Permite al personaje disparar.
  - `collide()`: Maneja las colisiones con otros elementos.

#### **Player** (Hereda de `Character`)
Clase que representa al jugador principal.

- **Atributos**:
  - `score`: Puntuación del jugador.
  - `lives`: Número de vidas (inicialmente 3).
- **Métodos**:
  - `move()`: Mueve al jugador.
  - `shoot()`: Permite al jugador disparar.

#### **Opponent** (Hereda de `Character`)
Clase que representa a los enemigos.

- **Atributos**:
  - `is_star`: Indica si el enemigo ha sido convertido en estrella.
- **Métodos**:
  - `move()`: Mueve al enemigo.
  - `shoot()`: Permite al enemigo disparar.

#### **Boss** (Hereda de `Opponent`)
Clase que representa al jefe final.

- **Atributos**:
  - `speed_multiplier`: Multiplicador de velocidad (el jefe se mueve más rápido).
- **Métodos**:
  - `move()`: Sobrescribe el movimiento para que sea más rápido.

#### **Shot** (Hereda de `Entity`)
Clase que representa los disparos realizados por un personaje.

- **Métodos**:
  - `move()`: Mueve el disparo.
  - `hit_target()`: Verifica si el disparo impacta a un objetivo.

#### **Game**
Clase principal que controla el flujo del juego.

- **Atributos**:
  - `score`: Puntuación del jugador.
  - `player`: Instancia del jugador.
  - `opponent`: Instancia del enemigo o jefe final.
  - `is_running`: Indica si el juego está en ejecución.
- **Métodos**:
  - `start()`: Inicia el juego.
  - `update()`: Actualiza el estado del juego.
  - `end_game()`: Termina el juego.
  - `display_score_and_lives()`: Muestra la puntuación y las vidas del jugador.
  - `remove_opponent()`: Elimina al enemigo actual y genera un jefe final.

---

## Funcionalidades Principales
1. **Registro de Puntuación**:
   - Cada vez que el jugador convierte a un enemigo en estrella, se incrementa su puntuación.

2. **Sistema de Vidas**:
   - El jugador comienza con 3 vidas.
   - Si el jugador es alcanzado por un disparo enemigo, pierde una vida.
   - El juego termina cuando las vidas llegan a 0.

3. **Jefe Final**:
   - Al derrotar a un enemigo, aparece un jefe final que se mueve el doble de rápido.

4. **Mostrar Puntuación y Vidas**:
   - La puntuación y las vidas del jugador se muestran en todo momento.

5. **Victoria**:
   - Si el jugador derrota al jefe final y tiene más de 0 vidas, se muestra un mensaje de victoria.

---

## Requisitos del Sistema
- Python 3.8 o superior.
- Librerías estándar de Python.

---

## Cómo Ejecutar el Juego
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu-usuario/Tarea-1-24-25.git

