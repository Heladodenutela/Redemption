# Redemption · Manual técnico

Este manual explica cómo está hecho *Redemption* por dentro: cómo cumple el enunciado del laboratorio, cómo está organizado el código, por qué algunas cosas están hechas como están y cómo funciona cada sistema y cada mecánica. Está escrito para quien quiera leer, revisar o cambiar el código.

|  |  |
| --- | --- |
| Juego | Redemption |
| Laboratorio | Digital Balance · Laboratorio único |
| Asignatura | Algoritmia y Programación II · NRC 2385 |
| Profesora | Rocío Ramos Rodríguez |
| Monitora | Angélica Baños |
| Equipo | Grupo 1 |
| Integrantes | Adrián Camilo Cáceres Figueroa · Sebastián Pertuz Sánchez · Eduardo Javier Tamara Otero · Daniel Steven Molina Gómez |
| Lenguaje | Java – Processing 4 |
| Entrega | Entrega 3 · 13 de noviembre de 2026 · semestre 2026-30 |

## 1. Cómo el juego cumple el enunciado

Redemption cumple los siete requisitos del código, usa las ocho mecánicas de la lista (se pedían tres) y hace el bonus de archivos. Esta sección dice dónde está cada cosa en el código; las secciones siguientes explican cómo funciona.

**Subtema.** El tema central es **3.1 Gestión del tiempo en redes sociales**: el jugador administra cada día entre estudiar, dormir, hacer ejercicio, compartir con amigos y familia, y usar redes. El juego también integra 3.2 Huella digital (lo que publicas en Aurora+ deja reputación), 3.5 Uso excesivo (notificaciones en la cama, reloj 3 veces más rápido con el celular), 3.8 Seguridad en mensajes privados («¿Confiable o trampa?»), 3.9 Ciudadanía digital (moderar el directo de Camilo, el rumor y lo que dicen de Iris) y 3.10 Bienestar digital (la app Bienestar digital y los rangos sanos).

### Requisitos del código

| # | Requisito | Cómo se cumple | Dónde |
| --- | --- | --- | --- |
| 1 | Arreglos en la lógica principal | Todo el estado del juego vive en arreglos: unos 480 vectores y matrices globales. Las barras son `stats[6]`, las amistades `amistad[60]`, la gente son vectores paralelos `npc*[80]`, el mapa es la matriz `conexiones[220][8]`, los chats `msg[45][80]` y el historial `catHist[12][5]`. Los minijuegos son matrices de objetos que se mueven: `football[9][21]`, `cosas[30][7]`, `balas[120][5]`, `notif[12][8]`. No se usa ArrayList. | Secciones 3, 4, 7, 9 y 12 |
| 2 | Operaciones con cadenas | Todo el contenido son tablas de texto (139 `String[][]`). Las condiciones del guion son un mini lenguaje que se lee letra por letra (`cumple`, `partirComparacion`), los efectos se leen de textos como `"Laura +3 · So +2"` (`aplicarEfectos`), los diálogos diarios tienen su propio formato de texto, las banderas se buscan con una tabla hash calculada desde las letras del nombre, y las nativas prohibidas (`charAt`, `split`, `indexOf`…) están hechas a mano con `substring`, `length` y `equals`. | Secciones 3 y 4 |
| 3 | Funciones y subrutinas | 1.416 funciones propias: 874 subrutinas `void` y 542 funciones que devuelven un valor. Cada sistema tiene las suyas (reloj, mundo, diálogos, celular, cada minijuego) y hay recursión en `cumple` y en `juntarTramo`. | Sección 2 |
| 4 | Validar todas las entradas | Cada tecla y cada click se revisan contra la pantalla y la actividad actual; lo que no corresponde se ignora (detalle abajo). | Sección 2, «Quién recibe el mouse y el teclado» |
| 5 | Sistema de puntajes o indicadores | Seis barras (Social, Notas, Energía, Dinero, Seguidores, Pantalla), cinco categorías de tiempo con rango sano y un puntaje con desglose (`puntaje()`). | Secciones 4 y 14 |
| 6 | Evaluación final del comportamiento digital | El informe «Tus 10 días» (`dibujarInforme`): perfil de tiempo, horas por categoría y por día, seguidores frente a amigos de verdad, tiempo total de pantalla, deuda de sueño, VICIO, días equilibrados y puntaje. | Sección 14 |
| 7 | Al menos dos finales | Once finales (`elegirFinal`) más epílogos por persona (`armarEpilogos`). | Sección 14 |

### Cómo se validan las entradas

| Entrada | Validación |
| --- | --- |
| Teclado | `keyPressed` reparte la tecla según `screen`, `cel` y `actividad`; cada pantalla solo atiende sus teclas. ESC se anula (`key = 0`) para que abra la pausa en vez de cerrar el juego. |
| Mouse | Cada click se convierte al lienzo de 1600 × 900 (`convertirMouse`) y se compara contra el rectángulo de cada botón. El primer receptor que lo usa lo consume; un click fuera de todo no hace nada. |
| Wordle | Solo acepta letras A–Z y Ñ (pasadas a mayúscula), máximo 5 por intento; ENTER solo cuenta con 5 letras; BORRAR no baja de 0. |
| Opciones 1 a 5 | Un número solo elige si esa opción existe y cumple su condición. |
| Plata | Antes de cobrar se revisa que alcance: «No te alcanza: necesitas $X». |
| Inventario | Si está lleno, avisa «Inventario lleno» y no agrega. |
| Alarma | Se mueve de 15 en 15 minutos y queda entre 4:00 y 10:00 con `max` y `min`. |
| Planes | Solo se ofrecen lugares de la lista y las próximas tres horas en punto. |
| Lugares | `motivoCerrado` no deja entrar a un lugar cerrado, pero siempre deja salir hacia la casa. |
| Guardar | Solo en un momento seguro («Termina lo que estás haciendo para guardar»). Sobrescribir una partida y salir piden un segundo click. |
| Archivos | Al cargar, una línea desconocida se ignora y un vector más corto se completa con valores iniciales; un archivo que no existe se detecta con `createInput` antes de leerlo. |

### Mecánicas obligatorias

| Mecánica | En el juego |
| --- | --- |
| Sistema de puntos | `puntaje()`: Notas × 2 + Social × 2 + ejercicio + equilibrio − 40 por VICIO + 5 por logro |
| Logros o insignias | 34 logros con medalla (`LOGROS`, `revisarLogros`) |
| Barra de bienestar digital | Las barras del HUD y la app Bienestar digital, que compara cada categoría con su rango sano |
| Contador de tiempo de pantalla | `stats[ST_PANTALLA]` suma cada medio minuto con el celular abierto; `pantallaHist[]` lo guarda por día |
| Reputación digital | Seguidores, likes, la bandera `MALA_REPUTACIÓN` y los chismes de «Confesiones Aurora» |
| Retos diarios | La tabla `RETOS`: un reto por día en Aurora+ (`ponerReto`, `revisarRetos`) |
| Decisiones con consecuencias | El árbol de diálogo, las escenas y los efectos sobre amistad, barras y banderas |
| Finales múltiples | Once finales y epílogos |

### Bonus y consideraciones

| Punto del enunciado | En el juego |
| --- | --- |
| Bonus de archivos | 3 partidas, `cuenta.txt` (logros, récords, estadísticas, ajustes) y `puntajes.txt`, con `saveStrings` y `loadStrings` (sección 15) |
| Nombre original | Redemption |
| Historia | Un estudiante de primer semestre y sus diez días hasta los parciales, con escenas, eventos y epílogos |
| Dos mundos o fases | Dos mundos: el mundo real (la ciudad) y el mundo digital (el celular, con su propio reloj 3 veces más rápido). Dos fases: días 1 a 5 (gestión y decisiones) y días 6 a 10 (situaciones avanzadas: el rumor, el ciberacoso, las finales y los parciales) |
| Sonidos y efectos | 12 pistas de música: un tema por zona (7), la casa según la hora (3), el título y los minijuegos; la Playlist del celular corta la música y pone su lista. Además, sonido de click, lluvia, fundidos y partículas |
| Instrucciones claras | Tutorial (F1), un cartel de cómo se juega antes de cada minijuego (`AVISOS_MJ`), el cuadro AHORA y los avisos \[E\] y \[R\] |
| Aprendizaje y reflexión | Los rangos sanos, el informe final y minijuegos como «¿Confiable o trampa?», moderar el directo y el editor de fotos |
| Lenguaje | Java – Processing 4 |

## 2. Arquitectura general

### Un solo sketch, dos versiones

El juego es un único archivo, `Redemption.pde`, dentro de la carpeta `Redemption` junto con `data` (imágenes, música) y `partidas` (archivos de guardado). Tiene unas 36.000 líneas (con sus comentarios) y 1.419 funciones, y Processing 4 lo compila como una sola clase de Java.

Junto a él va `Redemption_ordenado.pde`: el mismo código, pero agrupado en unos 70 bloques temáticos con un título comentado (núcleo, caja de balance, vectores, imitaciones, reloj, mundo, personajes, casa, diálogos, celular, cada clase, cada deporte, cada minijuego, guardado, música y datos). Para comprobar que las dos versiones son iguales se ordenan las líneas que no son comentario de ambas y tienen que coincidir una por una.

### Cómo se arma el archivo

El código se escribe en módulos más pequeños (`base3`, `vectores`, `guion`, `datos5`, `inter` a `inter11` y `m12` a `m43`). Un guion de construcción los une y los pasa por estos filtros, en orden:

| Paso | Qué hace |
| --- | --- |
| Unir | Concatena todos los módulos en un solo `.pde`. |
| Guardado | Genera el módulo de guardar y cargar a partir de las variables que existen en el código (sección 15). |
| Tablas | Mete cada tabla grande en su propia función, para que ningún método pase el límite de 64 KB de Java. |
| Sin comentarios | Quita los comentarios de trabajo de los módulos. Al final del armado, otro paso vuelve a poner comentarios generales: una línea encima de cada una de las 1.419 funciones que dice qué hace, el encabezado de cada sección y una presentación al principio del archivo con las reglas del curso. Antes de guardar, comprueba que el código quedó idéntico línea por línea. |
| Sin ternario | Reescribe cada `a ? b : c` como if/else. |
| Sin continue | Cambia cada `continue` por un `if` que encierra lo que seguía en el ciclo. |
| Sin nativas | Cambia `charAt`, `indexOf`, `split`, `trim` y las demás nativas prohibidas por imitaciones propias, y quita la sobrecarga. |
| Lienzo | Cambia `width` y `height` por `ANCHO` y `ALTO`, el lienzo fijo de 1600 × 900. |
| Sin vectores de retorno | Toda función que devolvía un arreglo pasa a ser `void` y deja el resultado en una global `resX`. |
| Compilar | Convierte el archivo a Java y lo compila con `javac` para confirmar que no hay errores. |

La sección 3 explica por qué existe cada uno de estos pasos.

### El ciclo de cada cuadro

**setup()** prepara todo, en este orden:

1. Crea la ventana con `size(1600, 900)` y `noSmooth()`, para que el pixel art no se vea borroso.
2. Carga las imágenes y asigna el fondo de cada mapa.
3. Arma el grafo de mapas con `definirConexiones`.
4. Crea los NPC e inicia las barras y las amistades.
5. Prepara el cielo, las piezas, la utilería, las decoraciones del cuarto y la pantalla de inicio.
6. Llama a `iniciarV20` (balance, eventos y escenas), a `iniciarV23` (cuenta, logros, récords y música) y a `iniciarV25` (límite de cuadros por segundo).

**draw()** corre 60 veces por segundo (o 30 con el límite). Sube el contador de animación `cuadros`, calcula la escala de la ventana, aplica `translate` y `scale` y llama a **dibujarJuego()**, que dibuja todo en coordenadas del lienzo de 1600 × 900. Después tapa con barras negras lo que sobra a los lados.

`dibujarJuego()` es un `switch` sobre la variable `screen`:

| screen | Pantalla |
| --- | --- |
| 0 | Pantalla de inicio |
| 1 | Mundo: casi todo el juego pasa aquí |
| 3 | Partido de rugby de la Copa, que tiene pantalla propia |

**La pantalla de inicio** dibuja el cuarto con la ventana transparente, el logo de Redemption (`dibujarLogoTitulo`, el único lugar donde aparece) y el botón JUGAR con sus tres estados (normal, encima, presionado). Detrás de la ventana hay estrellas animadas guardadas en la matriz `stars[i][0..8]`: cada fila es una estrella y cada columna un dato (posición, radio, velocidad de titileo, fase, sentido y radios de base). Al crearlas se sortea cada posición hasta que no choque con otra ni caiga en la cruz de la ventana. Cada 100 ms la fase avanza y, si se sale del rango 0 a 10, el sentido se invierte. La luz de la ventana (`lux`) imita un amanecer y un anochecer con un contador que sube cada 100 ms: crece de forma logística, sube en línea recta, baja y deshace el crecimiento con los factores guardados en `d[]`.

En `screen 1` el orden es: pausa, luego la pantalla del final, luego el cartel de cómo se juega un minijuego, y si no hay nada de eso, **dibujarMundo()**, que dibuja por capas de atrás hacia adelante:

1. Si hay un viaje en curso, solo la animación del viaje.
2. Mover al personaje.
3. El fondo: una capa `PGraphics` guardada que se vuelve a armar solo si cambia el cielo, el mapa o la escala.
4. La utilería, los objetos y las decoraciones de atrás.
5. Los NPC.
6. El protagonista.
7. Las decoraciones de adelante.
8. La lluvia y los «!» de eventos.
9. Los avisos \[E\] y \[R\].
10. El fundido a negro.
11. El HUD: día, hora, plata, mapa y barras.
12. La actividad en curso.
13. El cuadro AHORA, los logros y las llamadas.
14. El menú.
15. El aviso grande y el tutorial.

Encima va el celular si está abierto (`cel > 0`), y al final `dibujarEncimaV23`: el menú de partidas, el cartel de los minijuegos y la música.

### Las dos máquinas de estados: `cel` y `actividad`

**cel** dice qué pantalla del celular se ve:

| Valor | Pantalla |
| --- | --- |
| 0 | Cerrado |
| 1 | Inicio |
| 2 | Wordle |
| 3 | Flappy |
| 4 | Pong |
| 5 | Lista de chats |
| 6 | Chat abierto |
| 7 | Horario |
| 8 | Ajustes |
| 9 | Pedidazo |
| 10 | Aurora+ |
| 11 | Diario |
| 12 | Relaciones |
| 13 | Logros |
| 14 | Notas |
| 16 | Mapa |
| 17 | Playlist |
| 18 | Batería |
| 19 | Galería |

**actividad** dice qué está haciendo el personaje en el mundo. Es un entero con constantes `ACT_*`:

| Constantes | Grupo |
| --- | --- |
| 0 | Ninguna: caminar libre |
| 1 a 16 | Casa y mundo: sofá, estudiar, insomnio, despertar, lavadora, cartelera, mapa de la plaza, tienda, inventario, karaoke, diálogo, Newton, juego de estudio, reacción |
| 20 a 24 | PixelZone |
| 30 a 42 | Clases: sentado, clase, minijuego de clase, resultado, cinemática |
| 50 a 53 | Deportes |
| 60 a 65 | Gimnasio |
| 70 a 73 | Escena larga, resultados, minijuego de personaje y su resultado |

`dibujarActividad()`, `teclasActividad()` y `clickActividad()` son `switch` sobre esa variable: cada actividad tiene su propia función de dibujo, de teclas y de click. `empezarActividad` y `terminarActividad` hacen los cambios.

### Quién recibe el mouse y el teclado

**mousePressed** pasa el click por una cadena. El primero que lo usa lo «consume» y devuelve `true`:

1. Convierte la posición del mouse de la ventana al lienzo.
2. Suena el click.
3. Pausa.
4. Pantalla final.
5. Cartel del minijuego.
6. Tutorial.
7. Menú de partidas y selector de dificultad, en la pantalla de inicio.
8. En el mundo: menú; viaje (se ignora el click); llamada entrante; actividad, si el celular está cerrado; botón del celular.
9. Los clicks dentro del celular.

**keyPressed** sigue la misma idea:

- ESC no cierra el juego, abre la pausa: se anula poniendo `key = 0`. P también pausa.
- Las teclas del mundo van a `teclasMundo()`, y solo si el celular está cerrado y no hay viaje.
- Las del Wordle solo cuentan cuando `cel == 2`.
- Caminar usa banderas de tecla apretada (A, D, flechas, SHIFT) que `keyReleased` apaga. `moverPersonaje()` las lee en cada cuadro, así el movimiento es suave y no depende de la repetición del teclado.

Los otros eventos: **mouseReleased** suelta lo que se esté arrastrando (notificaciones del insomnio, el tiro del picado); **mouseWheel** hace scroll en chats, Pedidazo e inventario; **mouseMoved** y **mouseDragged** solo convierten las coordenadas.

## 3. Las reglas del código y por qué está hecho así

Varias partes del código se ven distintas a como se escribirían en Java normal. Casi todas tienen la misma razón: **la profesora pidió no usar ciertas herramientas del lenguaje**, para que el curso evalúe cómo resolvemos los problemas con arreglos, cadenas y funciones propias. Cada herramienta prohibida se reemplazó por una versión hecha a mano que da el mismo resultado.

| Regla | Por qué | Cómo se cumple |
| --- | --- | --- |
| Nada de ArrayList ni IntList | Regla de la clase: las listas de Java esconden el manejo del arreglo | Vectores de tamaño fijo con funciones propias para agregar, buscar, quitar y barajar |
| Ninguna función propia devuelve un vector | Regla de la clase | 38 funciones pasaron a ser `void` y dejan el resultado en una global `resNombre`; las 52 tablas `datos_X()` asignan su tabla en vez de devolverla |
| Sin operador ternario | Regla de la clase | Cada `?:` está escrito como if/else. Quedan 0 |
| Sin `continue` | Regla de la clase | Lo que venía después del `continue` va dentro de un `if` con la condición contraria. Quedan 0 |
| Sin `charAt`, `startsWith`, `endsWith`, `indexOf`, `lastIndexOf`, `trim`, `split`, `splitTokens`, `join`, `arrayCopy` ni `append` | Regla de la clase | 456 llamadas cambiadas por imitaciones propias que dan el mismo resultado |
| Sin sobrecarga | Regla de la clase | Cada función tiene su propio nombre |
| Ningún método de más de 64 KB | Límite de Java: un método compilado no puede pasar de 64 KB | Cada tabla grande se llena dentro de su propia función `datos_X()` |

El código sí usa lo que está permitido: `switch` (9), la biblioteca Sound para la música, `createInput` para saber si un archivo existe, `loadStrings` y `saveStrings` para los archivos, recursión, conversiones (`int()`, `str()`, `char()`), `millis()` y las funciones de dibujo, texto, imágenes, color y matemática de Processing.

### Por qué se escribe con módulos y se convierte al final

Los módulos de trabajo sí tienen `continue`, ternarios y llamadas a `split` o `indexOf`, porque así se leen mejor mientras se escribe. Al armar el archivo de entrega, unos programas en Python los convierten automáticamente. Hacerlo a mano en 284 `continue`, 310 ternarios y 456 llamadas era lento y fácil de equivocar; un programa aplica siempre la misma regla y después se puede probar que el resultado es igual (sección 17). El archivo que se entrega, `Redemption.pde`, ya no tiene ninguna de esas cosas.

### Los vectores en lugar de listas

Hay tres formatos, todos declarados del tamaño del peor caso. Si un vector se llena, lo nuevo simplemente no entra; nunca hay un error por desborde.

| Tipo | Formato | Funciones |
| --- | --- | --- |
| `int[]` | La posición `[0]` guarda cuántos elementos hay. Los datos van de `[1]` a `[v[0]]`. | `agregarInt` sube `v[0]` y escribe en esa posición. `tamInt` devuelve `v[0]`. `tieneInt` recorre de 1 a `v[0]`. `quitarIntEn(v, i)` corre los de atrás una casilla y baja `v[0]`. `vaciarInt` pone `v[0] = 0`. `barajarInt` es Fisher–Yates: de atrás hacia adelante cambia cada elemento con uno al azar entre 1 y su posición. |
| `String[]` | Se llena desde `[0]` hasta el primer `null`. | `agregarTexto` escribe en el primer `null`. `tamTexto` cuenta hasta el primer `null`. `quitarTextoEn` corre los de atrás y deja `null` al final. |
| `String[][]` | Una fila por elemento, hasta la primera fila `null`. | `agregarFila`, `tamFilas`, `vaciarFilas`. |

**Por qué el tamaño se cuenta:** una lista de Java sabe su tamaño; un arreglo fijo no. Por eso `tamFilas` cuenta las filas hasta el primer `null`. Como contar cuesta, en los ciclos se calcula una vez antes (`int total = tamFilas(agendaFilas);`) y no en cada vuelta.

### Funciones sin vector de retorno (void + res)

Un programa reescribe cada función que devolvía un arreglo:

```java
// antes
int[] opciones(int mapa, int borde, int obj) { ... return r; }
int[] v = opciones(mapaActual, BORDE_IZQ, -1);

// después
int[] resOpciones;
void opciones(int mapa, int borde, int obj) { ... resOpciones = r; return; }
opciones(mapaActual, BORDE_IZQ, -1);
int[] v = resOpciones;
```

Si la llamada estaba dentro de una expresión, como `tamInt(opciones(...)) > 0`, la función se llama antes y el resultado se guarda en una variable `auxN`. Se respeta el orden y el cortocircuito de `&&` y `||`: si la llamada estaba a la derecha de un `&&`, solo se hace cuando la izquierda es verdadera.

### Sin ternario

| Forma original | Queda así |
| --- | --- |
| `x = c ? a : b;` | `if (c) x = a; else x = b;` |
| `return c ? a : b;` | `if (c) return a; else return b;` |
| `T x = c ? a : b;` | `T x; if (c) x = a; else x = b;` |
| `f(c ? a : b);`, con un solo ternario | `if (c) f(a); else f(b);` |
| Varios ternarios en una sentencia, o uno dentro de un `if (...)` | Variables `auxN` calculadas antes con if/else |

### El `continue` improvisado

Un `continue` salta al final de la vuelta del ciclo. Sin `continue`, lo que seguía se mete dentro de un `if` con la condición contraria: si la condición para saltar no se cumple, se hace el resto; si se cumple, no se hace nada y el ciclo sigue con la vuelta siguiente, que es exactamente lo mismo. El programa `sincontinue.py` lee el código por palabras, busca cada ciclo con `continue` (primero los de más adentro) y aplica una de tres reglas:

| Lo que había | Cómo queda | Veces |
| --- | --- | --- |
| `if (c) continue;` y después el resto del ciclo (varios seguidos se juntan en uno) | `if (!c) { resto }` | 209 |
| `if (c) { A; continue; }` y después el resto | `if (c) { A; } else { resto }` | 16 |
| Un `continue` más adentro (dentro de otro `if`) | Una variable `boolean seguirN = true;` que el `continue` pone en `false`; lo que seguía va dentro de `if (seguirN) { ... }` | 15 |

Ejemplo real (las marcas «!» de los eventos):

```java
// antes
if (!e[10].equals("R")) continue;
int f = personaIndice(e[1]);
if (f < 0 || agendaNPC == null || agendaNPC[f] < 0) continue;
...dibujar la marca...

// después
if (e[10].equals("R")) {
  int f = personaIndice(e[1]);
  if (f >= 0 && agendaNPC != null && agendaNPC[f] >= 0) {
    ...dibujar la marca...
  }
}
```

La condición contraria se escribe limpia cuando no cambia nada: `==` pasa a `!=`, `a || b` pasa a `!a && !b`, y `<` o `>` se voltean solo si los dos lados son enteros. Con decimales queda `!(a < b)`, porque con un `float` inválido (NaN) `!(a < b)` y `a >= b` no dan lo mismo.

### Las imitaciones de las nativas prohibidas

Todas usan solo `length()`, `substring()` y `equals()` de los textos, más `char()` y `str()` para convertir. Ninguna llama a una prohibida: si una necesita otra, llama a la imitación (`partir` usa `posicionDeDesde`).

| Imitación | Equivale a | Cómo funciona |
| --- | --- | --- |
| `letraEn(s, i)` | `s.charAt(i)` | Corta la letra con `substring(i, i+1)` y busca su código en `letraTabla` (explicado abajo). |
| `empiezaCon(s, p)` | `startsWith` | Si `p` es más largo, es falso. Si no, compara `s.substring(0, p.length())` con `p`. |
| `terminaCon(s, p)` | `endsWith` | Compara el final de `s` con `p`. |
| `posicionDe` y `posicionDeDesde` | `indexOf` | Recorre `i` mientras quepa `p` y devuelve la primera `i` donde `substring(i, i+m)` es igual a `p`; si no, −1. |
| `ultimaPosicionDe` | `lastIndexOf` | Lo mismo hacia atrás. |
| `quitarBordes(s)` | `trim` | Avanza dos índices desde los extremos mientras la letra tenga código menor o igual al espacio. |
| `partir(s, d)` | `split` | Primera pasada: cuenta cuántas veces aparece `d`. Segunda: corta los pedazos. Deja los vacíos, igual que la original. |
| `partirTokens(s, d)` | `splitTokens` | Corta en cualquiera de las letras de `d` sin dejar pedazos vacíos. |
| `juntar(v, sep)` | `join` | `juntarTramo` es recursiva: pega la mitad izquierda, el separador y la mitad derecha, para no copiar el mismo texto largo una y otra vez. |
| `copiarEnteros`, `copiarTextos` | `arrayCopy` | Si origen y destino son el mismo vector y el destino va después, copia de atrás hacia adelante para no pisar datos. |
| `alargarEnteros(v, x)` | `append` | Un vector nuevo con un espacio más y `x` al final. |

**Por qué `letraEn` usa una tabla.** Sin `charAt` no hay forma directa de saber qué letra hay en una posición como número. Lo permitido es `str(char(c))`, que va del número a la letra. Entonces, al arrancar, el juego arma una vez `letraTabla` con los 65.536 textos de una sola letra posibles, y para saber el código de una letra la busca en esa tabla. Para que la búsqueda sea corta, recorre la tabla en el orden de `letraOrden`: primero `_` y las mayúsculas (los nombres de las banderas, como `BLOQUEO_3`, se leen todo el tiempo), después dígitos, minúsculas y signos, y al final el resto de Unicode. Así una letra se encuentra en unos 19 pasos en promedio y casi nunca se llega a los caracteres raros, que no están escritos en el código: se generan solos con el ciclo.

### La tabla hash de las banderas

Las banderas son la memoria del guion: cada decisión o hecho es un nombre con un número (`RISA_SOFÍA`, `VICIO`, `BLOQUEO_3`…). Hay hasta 12.000.

**El problema.** Buscar una bandera comparándola con todas sería hasta 12.000 comparaciones, y el juego pregunta por banderas muchas veces por segundo (cada evento, cada condición, cada logro). La primera versión tenía 200 banderas buscadas una por una: se llenaban hacia el día 8 y se perdían sin avisar. Java trae su propia tabla (`HashMap`), pero es una clase de colecciones como `ArrayList`, así que se hizo una a mano con arreglos.

**Cómo funciona.**

- `banderaNombre[12000]` y `banderaValor[12000]` son dos vectores paralelos: la fila `i` es una bandera.
- `banderaIndice[32768]` es la tabla de casillas. Cada casilla guarda la posición + 1 en los vectores; 0 es vacía.
- `codigoBandera(nombre)` convierte el nombre en un número de casilla letra por letra: empieza en 9 y por cada letra hace `h = (h × 25 + código de la letra) % 32768`. Con 9 y 25 ningún par de nombres del juego cae en la misma casilla.
- `posBandera(nombre)` va directo a esa casilla. Si está vacía, la bandera no existe. Si tiene el mismo nombre, ahí está. Si tiene otro nombre (un choque), prueba la casilla siguiente (`h + 1`, sondeo lineal) hasta encontrarla o llegar a una vacía. Devuelve `−1 − h` cuando no la encuentra, para que `sumarBandera` sepa dónde crearla sin buscar otra vez.
- `bandera(nombre)` da el valor (0 si no existe), `sumarBandera` suma o crea y `banderaValor0` la pone en 0.

Como la tabla tiene 32.768 casillas para 12.000 banderas (menos del 37 % llena), casi siempre se encuentra la bandera en la primera casilla: buscar cuesta lo mismo con 10 banderas que con 10.000.

### Sin sobrecarga

| Antes | Ahora | Llamadas cambiadas |
| --- | --- | --- |
| `obj(m, x0, x1, nombre)` | Siempre `obj(..., "")` | 31 |
| `izq(a, b, min)` y `der(a, b, min)` | Siempre con `-1` al final | 71 |
| `desplazamientoMapa` de 3 parámetros | `desplazamientoPorConexion` | 2 |
| `dibujarFondo(mapa)` | `dibujarFondo(mapa, horaDelDia())` | 1 |
| `dibujarCajaDialogo` de 5 parámetros | Recibe `RETRATO_RECORTE` | 1 |
| `textoOpcion(String)` | `textoAntesDeFlecha` | 2 |

Una prueba con reflexión de Java confirma que no quedan dos métodos con el mismo nombre.

## 4. Datos principales

### Todo el contenido está en tablas de texto

Casi todo lo que el jugador lee o vive está en matrices `String[][]`: cada fila es un registro y cada columna un campo, guardados como texto y convertidos con `int()` o `float()` al leerlos. Eso incluye diálogos, escenas, eventos, horarios, clases, minijuegos, logros, objetos y mensajes. Con un solo formato, agregar contenido es agregar una fila, sin tocar la lógica. Por el límite de 64 KB, cada tabla grande se llena dentro de su propia función `datos_X()` al arrancar.

| Tabla | Filas | Columnas | Para qué sirve |
| --- | --- | --- | --- |
| `REAC_RESP` | 551 | 3 | Lo que contesta cada persona según tu respuesta en una charla |
| `ARBOL`, `ARBOL_NUM`, `ARBOL_EXTRA` | 437 + 38 + 78 | 9 | Árbol de diálogo: nodos, opciones, siguiente nodo, efectos y condiciones |
| `ESC_*` (16 tablas) | más de 850 | 5 | Escenas largas: id, rama, quién habla, texto y acción |
| `VARIANTES`, `VARIANTES2` | 69 + 182 | 4 | Otras formas de decir la misma línea según la amistad o el contexto |
| `RESP_V21`, `TEMAS_V21`, `CHARLAS_V21` | 155 + 36 + 37 | 5 / 4 / 9 | Charlas de WhatsApp |
| `AGENDA` | 85 | 8 | Dónde está cada persona a cada hora |
| `HORARIOS` | 44 | 6 | Cuándo abre y cierra cada lugar |
| `CLASES` | 17 | 7 | Horario de clases de los 10 días |
| `EVENTOS20` (une 6 tablas) | 72 | 14 | Eventos con personas |
| `MJ_INFO`, `AVISOS_MJ` | 31 / 53 | 6 / 5 | Datos de cada minijuego y su cartel de cómo se juega |
| `LOGROS` | 32 | 3 | Logros |
| `ITEM_CAT`, `ITEM_USO`, `GUSTOS`, `REGALO_LINEAS` | 54 / 28 / 33 / 33 | 2 a 4 | Objetos: categoría, efecto, a quién le gustan y qué dice al recibirlos |
| `FOTOS_GALERIA` | 47 | 15 | Fotos de la Galería |
| `RETOS` | 1 por día | 5 | Retos diarios de Aurora+ |

### Barras (stats)

Un vector `stats[6]`:

| Índice | Barra | Rango | Inicio |
| --- | --- | --- | --- |
| `ST_SOCIAL` | Social | 0 a 100 | 50 |
| `ST_NOTAS` | Notas | 0 a 100 | 40 |
| `ST_ENERGIA` | Energía | 0 a `energiaMax()` | 80 |
| `ST_DINERO` | Plata (el valor real está en la global `dinero`) | 0 o más | $20 |
| `ST_SEGUIDORES` | Seguidores | 0 o más | 20 |
| `ST_PANTALLA` | Minutos de pantalla de hoy | 0 o más | 0 cada día |

- **`cambiarStat(k, d)`** es la única puerta para cambiar una barra y deja el valor en su rango. Lo que gasta energía pasa antes por `gastoEnergia`, que multiplica el gasto por 1,5.
- **`energiaMax()`** vale 100. Baja a 70 con deuda de sueño 1 y a 50 con deuda 2. Si dormiste menos de 6 horas, queda en 60 como máximo.
- **`nivelSocial()`** convierte Social en un nivel de 0 a 4 con cortes en 20, 40, 60 y 80: Perdedor, Reservado, Normal, Carismático, Popular.
- **La pantalla** se cuenta en `tickReloj`: cada medio minuto con el celular abierto suma a `pantallaMedios`, y `stats[ST_PANTALLA] = pantallaMedios / 2`.

### Banderas

Cada decisión o hecho que el guion necesita recordar es una bandera con nombre y número: `RISA_SOFÍA`, `VICIO`, `PISTA_CAMILO`, `DH_<nodo>` (ya se dijo hoy), `FUE_AMIGO_<persona>` y muchas más. Se guardan en la tabla hash propia explicada en la sección 3.

### Amistad

`amistad[f]` guarda un número de 0 a 100 por persona, en la misma fila `f` que la persona tiene en `DLG_PERSONA`. Hay 60 personas y todas empiezan en 40.

- **`cambiarAmistad(f, v)`.** Subir cuesta más cuando ya son cercanos: por encima de 60 la subida se divide entre 2, y por encima de 80 entre 3, con un mínimo de 1. Bajar no tiene descuento. Luego se limita a 0–100 y `revisarNivelAmistad` deja la bandera `FUE_AMIGO_f` la primera vez que llegan a 60.
- **`estadoAmistad(a)`**: 60 o más es Amigo, 35 o más es Conocido, menos es Molesto.
- **Hitos**: A60 (ya son amigos), A80 (muy cercanos) y BAJA (fueron amigos y ahora están mal). Los diálogos los usan para cambiar de tono.

### Inventario

- **`inventario[40][2]`**: cada fila es `{nombre, cantidad}` y `numInv` dice cuántas filas se usan.
- **`agregarInventario`** suma a la fila si el objeto ya está; si no, agrega una fila nueva; si no cabe, avisa «Inventario lleno».
- La pantalla muestra 12 objetos a la vez (`INV_VISIBLES`); los demás se ven con la rueda del mouse o las flechas.
- `ITEM_CAT` da la categoría de cada objeto, `ITEM_USO` qué hace al usarlo y `GUSTOS` y `REGALO_LINEAS` a quién le gusta como regalo y qué contesta.

### Condiciones: el mini lenguaje de `cumple()`

Casi todas las tablas tienen una columna de condición: un texto que `cumple(c)` evalúa. Es un ejemplo grande de trabajo con cadenas:

1. Si es `null` o está vacía, se cumple.
2. `A | B` se cumple si se cumple alguna.
3. `A & B` se cumple si se cumplen todas.
4. `!A` es la negación.
5. Cada pedazo suelto lo resuelve `cumpleUna`. Los pedazos se resuelven con la recursión de `cumple`, así que se pueden combinar sin límite.

| Forma | Se cumple si… |
| --- | --- |
| `F:NOMBRE` | La bandera existe y es mayor que 0 |
| `AM:Marta>=35` | La amistad con esa persona cumple la comparación |
| `ROM:Sofía>=2` | El nivel de romance cumple la comparación |
| `N:Popular` | El nivel social es ese |
| `CLASE:3:Física`, `FALTO:HOY:Física` | Asististe a esa clase, o hoy había clase y no fuiste |
| `MAPA:2:U5`, `MAPA:*:U5`, `AQUI:U5` | Estuviste en ese mapa ese día, alguna vez, o estás ahí ahora |
| `E:x`, `RESP:id:x`, `HECHO:nodo`, `HOY:x`, `ESCENA:id` | Elegiste, respondiste, hiciste o viste algo |
| `LLUVIA`, `FINDE`, `NOCHE`, `NUNCA` | Está lloviendo, es día 6 o 7, es de noche, o nunca |
| `HORA>=18:30` | La hora cumple la comparación (en minutos) |
| `DIA`, `VICIO`, `NOTAS`, `SOCIAL`, `SEG`, `DINERO`, `ENERGIA`, `DEUDA`, `FALTAS`, `ASIST`, `AMIGOS`, `EQUIL`, `PANTALLA` con una comparación | Ese número del juego cumple la comparación |
| Cualquier otro nombre | Esa bandera cumple la comparación, o es mayor que 0 |

`partirComparacion` busca el operador en este orden: `>=`, `<=`, `!=`, `>`, `<`, `=`. Así `>=` no se confunde con `>`. `comparar(a, op, b)` hace la comparación.

### Efectos: `aplicarEfectos()`

La columna de efectos es un texto con partes separadas por `·`, por ejemplo `Laura +3 · So +2 · En −5 · RISA_SOFÍA`. Cada parte se separa en nombre, signo, número y unidad.

| Nombre | Qué cambia |
| --- | --- |
| `Am` | Amistad con la persona con la que hablas |
| `So`, `Social`, `No`, `Notas`, `En`, `Energía`, `Seg`, `$`, `Dinero` | Esa barra |
| `Faltas` | Faltas |
| `Tiempo` | Avanza el reloj |
| `Redes`, `Estudio`, `Amigos`, `Ejercicio` | Suma minutos (u horas con `h`) a esa categoría del día |
| `Romance`, `Rom` | Puntos de romance |
| Un nombre de persona, o varios con `/` (`Mamá/Papá +2`) | Amistad con cada una |
| Una palabra en MAYÚSCULAS | Esa bandera (+1 si va sola) |
| `NÚMERO` | Esa persona te da su número |

La función devuelve un resumen de lo que cambió, y ese resumen es lo que el jugador ve en el aviso.

## 5. Reloj y tiempo

### Unidades

El tiempo del juego es un solo entero, `horagp`. Cuenta medios minutos desde las 6:00 del día 1, así que un día tiene 2.880 unidades.

| Función | Fórmula | Qué da |
| --- | --- | --- |
| `horaDelDia()` | `(horagp + 720) % 2880` | Hora del día en medios minutos (720 son las 6:00) |
| `minutoAhora()` | `horaDelDia() / 2` | Minuto del día, de 0 a 1439 |
| `diaDelReloj()` | `(horagp + 120) / 2880 + 1` | El día cambia a las **5:00**, no a medianoche: quien trasnocha sigue en «el mismo día» hasta la madrugada |
| `horaTexto(hd)` |  | `"07:30"` para mostrar |

Todas las horas de las tablas (`HORA>=18:30`, horarios, agenda) se pasan a minutos con `aMin("18:30") = 18 × 60 + 30` y se comparan con `minutoAhora()`.

### El latido: `cicloTiempo()`

El reloj usa `millis()` y una marca de inicio `ti`, que se pone al pulsar JUGAR. En cada cuadro:

```java
if (millis() - ti - horagp * 500 > 500) {   // pasó otro medio segundo "de reloj"
  horagp = horagp + 1;                     // medio minuto más de juego
  tickReloj();
}
```

Cada tick son 30 segundos de juego. `tickReloj()` hace el trabajo periódico (sección 13) y termina con `revisarCambioDia()`, que usa un `while (diaDelReloj() > diaRelojVisto)`: si un salto de tiempo cruza varios días, se procesan todos. En cada día nuevo se reinician las categorías y la pantalla del día, se cargan los diálogos y se preparan los eventos, el mundo y las apps.

### Velocidad: cuánto dura una hora

Sin corrección, un tick cada 500 ms haría que una hora del juego durara 60 segundos reales. `ajustarRelojV22()` corre `ti` un poco en cada cuadro para que dure lo que pide la dificultad:

```java
lentitud = MIN_POR_HORA[dificultad];      // { 3.0, 1.5, 1.0 } minutos reales por hora
if (comiendo, en un evento o con el tutorial)  lentitud = lentitud * 2;
if (celular abierto)                            lentitud = lentitud / CEL_RAPIDO;   // 3
restoTi = restoTi + dt * (1 - 1 / lentitud);   // dt = ms reales desde el cuadro anterior
ti = ti + int(restoTi);  restoTi = restoTi - int(restoTi);
```

Si `lentitud` es 1,5, de cada milisegundo real solo ⅔ cuentan para el reloj. Si es menor que 1 (celular abierto), `ti` retrocede y el reloj va más rápido. `restoTi` guarda la fracción que no alcanzó un milisegundo entero, para no perder tiempo por redondeo. Si un cuadro tardó más de un segundo (una pausa, una carga), no se corrige.

| Dificultad | 1 hora del juego | Comiendo o en un evento | Con el celular |
| --- | --- | --- | --- |
| Fácil | 3:00 min | 6:00 min | 1:00 min |
| Normal | 1:30 min | 3:00 min | 0:30 min |
| Difícil | 1:00 min | 2:00 min | 0:20 min |

**Por qué el celular acelera el reloj.** Es la mecánica central del subtema: el jugador siente en el juego que el tiempo en redes se va más rápido de lo que parece.

### Saltos de tiempo: `avanzarTiempo(min)`

Dormir, estudiar, una clase, un viaje, un minijuego o un efecto `Tiempo +30` saltan el reloj de golpe:

```java
horagp = horagp + min * 2;
ti = ti - min * 2 * 500;    // compensa: si no, el reloj se quedaría quieto hasta "alcanzar" el salto
```

Si el salto es de 30 minutos o más, el cielo se recalcula de inmediato.

### Pausa: `alternarPausa()` y `desplazarTiempos()`

Con la pausa abierta, `dibujarJuego()` no llama a `dibujarMundo()`, así que no corre el reloj ni ningún minijuego. El problema es que los temporizadores se guardan como «termina en el `millis()` X», y `millis()` sigue corriendo. Al quitar la pausa se mide cuánto duró y `desplazarTiempos(quieto)` corre hacia adelante todos los relojes: `ti`, las 117 variables de fin, inicio o aviso de cada sistema y minijuego, el nacimiento de cada notificación del insomnio y de cada bicho de la clase de programación. Así, al volver, cada minijuego tiene exactamente el tiempo que le quedaba. Lo mismo pasa mientras está abierto el cartel de cómo se juega un minijuego.

## 6. Mundo y movimiento

### Mapas

La ciudad son 59 mapas, cada uno con código y nombre en `MAPA_COD[]` y `MAPA_NOMBRE[]`, y una constante entera por mapa (`C1 = 0` … `U8 = 22` …).

| Zona | Códigos | Mapas |
| --- | --- | --- |
| Casa | C1–C7 | Frente, pasillo, sala, cocina, tu cuarto (C5), pasillo del cuarto de Lili, patio de ropas |
| Calle | I1–I8 | Interior del bus, paradero de la U, calle a la Plaza, puente peatonal, pasillo a Deportes, paradero del Parque, Terminal, andén de la esquina |
| Universidad | U1–U16 | Portería, escaleras, patio, pasillos, aulas 201, 305 y 104, laboratorio, sala de cómputo, biblioteca, Cantina, Útiles Aurora, enfermería, jardines, kiosco de café |
| Plaza | P1–P7 | Entrada, atrio, Grano Café, PixelZone, Rosa Moda, heladería, puesto de flores |
| Parque | K1–K9 | Entrada, fuente, cerezo, bancas, sendero, pradera, pintor, ajedrez, mercadito |
| Deportes | D1–D7 | Fútbol, rugby, piscina, pista, gimnasio, vestuarios, gradas |
| Fuera | F1–F5 | Esquina, Bar La Esquina, Tienda La Esquinita, empanadas, terraza de Marta |

Cada fondo es pixel art ampliado a 1600 × 900, con el cielo dinámico detrás: los fondos de exteriores tienen el cielo transparente, y la parte transparente deja ver el cielo que el juego pinta según la hora. El mundo es de perfil: el personaje solo se mueve en x, con los pies sobre `pisoMapa[mapa]`.

Los objetos con los que se interactúa son 89, cada uno un tramo de x: `objMapa[o]` (en qué mapa está), `objX[o][0..1]` (el tramo), `objNombre[o]` y `objAccion[o]` (una acción especial, si la tiene). `objetoCercano()` devuelve el objeto cuyo tramo contiene la x del personaje, y ese objeto muestra el aviso **\[E\]**. Cuando cambia un fondo, se ajustan los tramos para que coincidan con lo dibujado: en el patio central (U3) las cuatro puertas (Biblioteca 230–340, Enfermería 550–660, Útiles 880–990 y Cantina 1200–1310) y la x donde apareces al volver de cada lugar.

### El grafo de conexiones

Cómo se pasa de un mapa a otro es una matriz `conexiones[220][8]`, de la que se usan 138 filas. Cada fila es una conexión:

| Columna | Significado |
| --- | --- |
| `CX_ORIGEN` | Mapa de salida |
| `CX_TIPO` | `BORDE_IZQ`, `BORDE_DER` o `INTERACCION` |
| `CX_OBJ` | El objeto, si es por interacción |
| `CX_DESTINO` | Mapa de llegada |
| `CX_MIN` | Minutos de juego que tarda |
| `CX_MODO` | `A_PIE`, `BUS` ($1), `TAXI` ($8) o `TAQUILLA` ($2 más 10 min de espera) |
| `CX_DIA` | 0 = siempre · 6 = solo el día 6 · −6 = todos los días menos el 6 |
| `CX_APARECE` | x donde apareces al llegar; −1 = el borde contrario o el paradero |

Se llena con funciones cortas: `izq(origen, destino, min, aparece)`, `der(...)`, `inter(origen, objeto, destino, min, aparece)`, `bus(...)`, `taxi(...)`, `taquilla(...)`. Todas llaman a `con(...)`, que escribe la fila. De las 138 conexiones, 122 son a pie, 8 en bus, 6 en taxi y 2 en la taquilla.

### Caminar y salir de un mapa

`moverPersonaje()` corre en cada cuadro, solo si no hay celular, menú, viaje ni actividad:

- `dx` es +1 con D o →, y −1 con A o ←. `pjX += dx × velocidad`: 5 px por cuadro caminando y 9 con SHIFT.
- Si `pjX` pasa de 40 o de 1560, `opciones(mapa, borde, −1)` deja en `resOpciones` un vector con la cantidad en `[0]` y los índices de las conexiones de ese borde que valen hoy. Sin ninguna, el borde es una pared. Con una, `elegirOpcion` viaja directo; con varias, abre el menú «¿Hacia dónde caminas?».
- Con \[E\] sobre un objeto, `interactuar()` hace lo mismo con `opciones(mapa, INTERACCION, objeto)`. Si el objeto no tiene conexiones pero sí acción especial (la cama, la tienda, la clase, la mesa), hace la acción.

### Usar una conexión: `usarConexion(c)`

1. **¿Se puede pasar?** Lo decide `motivoCerrado(c)`. Si devuelve un texto, sale como aviso y no se viaja.
2. **¿Alcanza la plata?** Si no, avisa «No te alcanza: necesitas $X». Si alcanza, se cobra.
3. **Microsueño.** En bus y con deuda de sueño de 3 o más, hay 25 % de dormirse y pasarse de parada.
4. **Pantalla de viaje.** En vehículo, o a pie si son 10 minutos o más, sale «Caminando… / Bus / Taxi» durante 2,5 s reales.
5. **`desplazamientoMapa`** hace el cambio: reinicia las conversaciones a medias, ubica al personaje, suma 8 minutos si hoy el bus va lleno, avanza el reloj, hace un fundido desde negro, muestra «U3 · Patio central (+5 min)» y llama a `alEntrarMapa`, que dispara eventos y escenas y anota que estuviste ahí.

### Horarios de los lugares

La tabla `HORARIOS` tiene filas `{tipo, nombre, días, abre, cierra, mapa}`, con días como `"1-5,8-10"`.

- **`diaEn(dias, d)`** parte por comas y acepta días sueltos o rangos con guion.
- **`ventanaAbierta`** acepta horarios que pasan la medianoche: si `abre > cierra` (el bar de 18:00 a 2:00), está abierto si `m ≥ abre` **o** `m < cierra`.
- **`estadoHorario`** devuelve 1 abierto, 0 cerrado o −1 sin horario (siempre abierto). **`proximaApertura`** dice «abre a las 10:00» o «hoy ya no abre».

### Salidas para no quedar atrapado

**El problema.** Antes, un mapa cerrado no dejaba pasar a nadie, ni siquiera a quien ya estaba adentro. Si te quedabas en el Grano Café después de las 18:00, el puesto de flores (el pasillo entre la entrada y el resto de la Plaza) ya había cerrado y quedabas encerrado.

**La regla:** un lugar cerrado no te deja entrar, pero sí pasar si vas en camino a tu casa.

1. **`calcularDistanciaCasa()`** calcula cuántos pasos hay de cada mapa a tu cuarto (C5), con las conexiones que valen hoy. Empieza con `distCasa[C5] = 0` y los demás en −1, y repite: por cada conexión a → b, si b llega a casa y por a el camino sería más corto, `distCasa[a] = distCasa[b] + 1`. Para cuando nada cambia (una relajación tipo Bellman-Ford con pasos de peso 1). Se calcula una vez por día.
2. **`vaHaciaLaCasa(c)`** es verdadero si el destino llega a casa y te acerca: el origen no llega, o el destino está más cerca.
3. **`motivoCerrado(c)`**: si es bus y no pasa a esta hora, no; si el destino está abierto, sí; si va hacia la casa, sí; si no, «X está cerrado · abre a las…».
4. **`avisarSiSoloSalida(c)`** avisa «X ya cerró: puedes pasar, pero solo hacia la salida».
5. Se agregó la calle I2 ↔ I8, que une Fuera con el paradero de la U sin cruzar la universidad.

Una prueba recorre todos los mapas a cada media hora de los 10 días con $0 y confirma que siempre hay camino a casa (sección 17).

## 7. Personajes y agenda

### Hojas de sprites y animación

Cada personaje es una hoja PNG dividida en cuadros de 160 × 240 px: cada **fila** es una animación y cada **columna** un cuadro de esa animación, con 4 cuadros por fila. La tabla `VISOR_DATOS` (173 hojas) describe cada hoja con cinco columnas: variable, archivo, ancho y alto del cuadro, y la lista de animaciones con el formato `fila;columna inicial;cuadros;descripción`, por ejemplo `0;0;4;AFK|1;0;4;AFK acción|4;0;4;caminar izquierda`. El vector `visHojas[]` tiene las imágenes en el mismo orden.

- **`dibujarHoja(hoja, cw, ch, fila, col, x, y, esc)`** dibuja un cuadro sin copiarlo, con la versión de `image()` que recorta: `image(hoja, x, y, cw·esc, ch·esc, col·cw, fila·ch, col·cw + cw, fila·ch + ch)`.
- **`dibujarPersonaje(hoja, fila, col, x, piso)`** lo centra en x (`PJ_CENTRO = 80`) con los pies en el piso (`PJ_PIES = 225`).
- **El cuadro de cada momento** sale del contador `cuadros`, que `draw()` sube en `pasoCuadro` cada vez (1 a 60 FPS, 2 a 30 FPS): `col = (cuadros / velocidad) % 4`. Así las animaciones van igual de rápido con o sin el límite de 30 FPS. `VEL_CAMINAR = 8`, `VEL_CORRER = 5`, `VEL_AFK = 13`.

| Fila del protagonista | Animación |
| --- | --- |
| 0 | Quieto (AFK) |
| 1 | «AFK acción»: una vuelta de 4 cuadros que sale tras 6 segundos sin moverse |
| 4, 5 | Caminar a la izquierda y a la derecha |
| 8, 9 | Correr a la izquierda y a la derecha |
| 10–15 | Sentado, de lado, estudiando, cabeceando, cantando |

Hay una hoja aparte para acostado (240 × 160) y otra para traje de baño. `dibujarProtagonistaEspecial()` decide estos casos antes de la animación normal.

**Utilería.** Los objetos animados del escenario (la cafetera de la casa, el celular cargando, los libros de la biblioteca, los péndulos del laboratorio, el almuerzo y el tinto de la Cantina, el vapor del café de Nico, la nuez del parque, el caballete del pintor) son vectores paralelos `utiIdx`, `utiFila`, `utiMapa`, `utiX` y `utiBase`, llenados con `utileria(hoja, fila, mapa, x, y)`. En la v27 se quitó un marcador azul que flotaba animado en el Aula 305.

### Los NPC: vectores paralelos

Hasta 80 NPC, cada uno en la misma posición `k` de varios vectores:

| Vector | Dato |
| --- | --- |
| `npcHoja[k]` | Su hoja de sprites |
| `npcMapa[k]` | Mapa donde está (−1 si ahora no está en ninguno) |
| `npcX[k]` | Posición |
| `npcMin[k]`, `npcMax[k]` | Tramo por el que camina |
| `npcVel[k]`, `npcDir[k]` | Velocidad y sentido |
| `npcFila[k]`, `npcFilaIzq[k]`, `npcFilaDer[k]` | Fila quieto, caminando a la izquierda y a la derecha |
| `npcPersona[k]` | Su fila en la tabla de personas (−1 si no habla) |

`npcQuieto(...)` crea uno que se queda en su x y `npcRecorre(...)` uno que va y viene. En cada cuadro:

```java
npcX[k] = npcX[k] + npcDir[k] * npcVel[k] * pasoCuadro;   // a 30 FPS avanza el doble por cuadro
if (npcX[k] > npcMax[k]) { npcX[k] = npcMax[k]; npcDir[k] = -1; }   // rebota
if (npcX[k] < npcMin[k]) { npcX[k] = npcMin[k]; npcDir[k] = 1; }
col = ((cuadros + k * 7) / VEL_CAMINAR) % 4;   // desfase k*7: no todos pisan al mismo tiempo
```

### La agenda: dónde está cada persona

La tabla `AGENDA` (85 filas) tiene ocho columnas: persona, días, desde, hasta, mapa, x, fila de animación y «hasta x» (0 = quieto; otro valor = camina entre x y ese valor). Por ejemplo, Sofía almuerza en la Cantina: `{"Sofía", "1-5,8-10", "11:00", "14:00", "U12", "600", "0", "0"}`.

Al empezar, `agendaFilas` se arma uniendo varias fuentes: una fila por cada clase y cada persona que va a ella (el profe al frente, en x = 1350, y los compañeros cada 230 px), la tabla `AGENDA`, las filas de los eventos y la gente de la fiesta.

**`filaAgendaAhora(persona)`** da dos vueltas: en la primera solo mira las filas de un solo día (la fiesta, la Feria); en la segunda, todas. Gana la primera fila cuya ventana de día y hora esté abierta. Si ninguna coincide, la persona no está en ningún mapa.

**`actualizarAgenda()`** revisa a cada persona en este orden: si estás hablando con ella, no se mueve; si hay un evento suyo o un plan por WhatsApp, eso manda; si no, la agenda; si llueve y no sale con lluvia, o hoy está enferma, no aparece. Si la fila elegida cambió, la mueve.

**Cada cuánto corre.** Todos los horarios de la agenda, los eventos y los planes van de 5 en 5 minutos. Por eso `actualizarAgenda()` corre una vez por cada bloque de 5 minutos de juego (`bloqueCincoMin()`, sección 16), y además al cargar una partida, al empezar el día y después de un salto de tiempo.

### Hablar

Con **R**, `npcParaHablar()` busca el NPC con persona más cercano en x, a menos de 110 px. Después `hablar()` decide qué pasa, en orden: si te evita, solo dice su línea de rechazo; si nunca habían hablado, el primer encuentro; si hay un evento con esa persona aquí y ahora, la escena; si hay un plan por WhatsApp, el plan; si no, el diálogo del día (sección 8).

## 8. Diálogos, escenas y eventos

### La charla con R: una cadena por persona

Cada persona tiene una fila en la matriz `dlg[f][40]`, que se vuelve a armar cuando hace falta:

| Columna | Contenido |
| --- | --- |
| `[0]` | Nombre |
| `[1]` | Un texto como `"0010"` que dice quién dice cada línea: 0 = la otra persona, 1 = tú |
| `[2]` | Lo que dice por defecto cuando ya no tiene nada nuevo |
| `[3..]` | La cadena de hoy, línea por línea |

Al lado van dos matrices del mismo tamaño: **`dlgNodo`** marca las líneas que esperan respuesta (`"A:S1"` un nodo del árbol, `"D:12"` un diálogo diario, `"E:persona"` un encargo) y **`dlgEfecto`** guarda el efecto que se aplica al pasar esa línea. `dlgPos[f]` dice por qué línea vas.

**`asignarDialogo(f)`** llena la cadena en este orden: línea de rechazo si te evita (y termina); saludo según tu nivel social; variantes según tus hábitos, lo que hiciste hoy y la amistad; reproche si lo dejaste en visto; línea de reencuentro (Amigo, Conocido o Molesto); comentario si se te nota el sueño; la línea del día; líneas extra cuya condición se cumple; encargo si es personaje de fondo; una charla corta de `PLATICA`; y al final el nodo del árbol que toca hoy, con respuestas. La cadena se rearma al empezar el día, después de cada respuesta y después de los eventos.

**La mesa del comedor** (`mesaFamilia`) arma la cadena de la familia según la hora real del juego: el desayuno de la tabla `CASA` entre las 6:00 y las 8:30 a. m. (los días 1 y 8 con el efecto `MESADA`) y la cena entre las 7:00 y las 9:30 p. m., una vez cada una por día (banderas `DESAYUNO_d` y `CENA_d`). Fuera de esas horas avisa «La mesa está vacía. Desayuno de 6:00 a 8:30 a. m. · cena de 7:00 a 9:30 p. m.», con las mismas horas que revisa el código.

**`avanzarDialogo()`** aplica el efecto de la línea que se termina, se detiene si la siguiente tiene nodo y muestra las opciones, y al final cierra la caja. La caja lleva el retrato (un recorte ampliado del cuadro quieto de la hoja), el nombre y el texto.

### El árbol de diálogo (`ARBOL`, 553 filas)

Cada fila es **una respuesta posible**: `{persona, nodo, día, cuándo, lo que dice el NPC, tu respuesta, condición, efecto, siguiente}`. Las filas con el mismo nodo forman la pregunta y sus opciones; la condición filtra qué opciones ves; **siguiente** lista los nodos que se desbloquean (del mismo día siguen en la misma charla, de otro día salen ese día). Las raíces son los nodos que no son «siguiente» de nadie. `nodoDisponible(f)` elige el primer nodo desbloqueado de esa persona que sea de hoy y cumpla su condición.

Después de responder se aplican los efectos, se marca el nodo como hecho y se guarda la respuesta. La persona reacciona con la línea de `REAC_RESP` (`{nodo, cómo empieza tu respuesta, lo que contesta}`); si no hay, con `REACCIONES` según si el efecto fue bueno, neutro o malo.

### Diálogos diarios

Cada persona tiene una lista numerada de charlas en un formato de texto propio, una línea por cosa:

```
@Persona
#número¦id¦condición¦lo que dice
>condición de la opción¦lo que dices tú¦efectos¦lo que te contesta (// lo parte en dos globos)
```

El juego lo lee al arrancar letra por letra (con las imitaciones de `split` y `startsWith`) y lo pasa a vectores paralelos `dNodoId`, `dNodoCond`, `dNodoLinea`, `dOpTexto`, `dOpEf`, `dOpReac`… La charla 1 sale el primer día que le hablas, la 2 el segundo día distinto, y así. Cada número puede tener varias versiones (sale la primera cuya condición se cumple), y en lugar de un número puede ir un hito de amistad: `#A60`, `#A80` o `#BAJA`. Al responder quedan las banderas `DH_<id>` (ya se habló hoy) y `DX_<id>` (qué opción elegiste).

### Variantes: lo mismo dicho distinto

`VARIANTES` y `VARIANTES2` (251 filas) tienen la forma `{persona, tipo, condición, línea}`. El tipo es H (tus hábitos: vicio, sueño, notas), A (la amistad), D (lo que hiciste hoy) o N (tu nivel social). `varianteDe(tabla, persona, tipo)` devuelve la primera línea de ese tipo cuya condición se cumple. Así una persona te saluda distinto si llevas dos noches sin dormir, si hoy fuiste al gimnasio o si eres Popular. La tabla `EVITA` usa el mismo formato para decidir quién ni te habla.

### Escenas largas (el motor de escenas)

Las 16 tablas `ESC_*` se unen al empezar en `ESCENAS`: 864 filas que forman 72 escenas. Cada fila tiene id, rama (etiqueta; las filas sin etiqueta siguen en orden), quién habla (persona, `Tú` o `*` para narración, con expresión opcional), texto y acción:

| Acción | Qué hace |
| --- | --- |
| (vacía) | Pasa a la fila siguiente |
| `OP:texto#RAMA#efecto#condición\|...` | Opciones: cada una salta a su rama y aplica su efecto |
| `IR:RAMA` | Salta a esa rama |
| `SI:condición#RAMA` | Salta solo si se cumple |
| `EF:efectos` | Aplica efectos y muestra el resumen |
| `MJ:CÓDIGO#RAMA_BIEN#RAMA_MAL` | Abre un minijuego y vuelve por la rama que corresponda |
| `CMD:orden;orden` | Órdenes: `TIEMPO`, `AMIGOS`, `ESTUDIO`, `EJERCICIO`, `REDES`, `ACTOR`, `QUITAR`, `NODO`, `RESP`, `BLOQUEAR`, `FOTOCTX` |
| `FIN` | Termina la escena |

`empezarEscena(id)` busca la primera fila, elige a la persona principal, la anota como vista, cierra el celular y entra en `ACT_ESCENA`. `procesarFilaEscena()` ejecuta las filas sin texto hasta llegar a una con texto, con un tope de 200 vueltas para que una escena mal escrita nunca congele el juego. `avanzarEscena()` espera la elección si hay opciones, abre el minijuego si hay uno, termina, salta o pasa a la siguiente. `terminarEscena()` cuenta la escena como charla, marca el evento como hecho, escribe el diario y, si era la Feria, termina el juego.

### Eventos con personas

`EVENTOS20` une seis tablas en 72 eventos de 14 columnas: id, persona, días, desde, hasta, mapa, x, condición, escena, texto del aviso, modo (R = hablando, A = automático al llegar), invitación por WhatsApp, hora del mensaje y lo que te escribe si no vas. Cada evento tiene un estado `evEstado[k]`: 0 pendiente, 1 hecho, 2 perdido, 3 llegaste pero no lo hiciste.

**`eventoActivo(k)`** es verdadero si está pendiente, hoy es uno de sus días, es su hora, la persona no te bloqueó y se cumple su condición. Las revisiones van en ese orden a propósito: primero las baratas (estado, día y hora) y después las que leen banderas, así la mayoría de los eventos se descartan sin buscar nada. Mientras esté activo, la agenda lleva a la persona al lugar y sobre su cabeza sale un «!» animado.

**`tickEventos()`** manda la invitación por WhatsApp a su hora (solo si esa persona tiene tu número), cuenta la llegada si estás en el lugar y, cuando se pasa la hora sin que llegues, deja el estado 2, la bandera `PERDIÓ_<id>` y su reproche. Al terminar la escena, el evento queda en estado 1 con la bandera `EV_<id>`, que el resto del guion puede preguntar.

### Escenas de mapa y de clase

`ESCENAS_MAPA` tiene filas `{día, desde, hasta, mapa, nodos}`: si estás en ese mapa a esa hora, la escena salta sola como cinemática. Las escenas de clase funcionan igual, pero dentro de la clase (sección 10).

## 9. El celular (mundo digital)

El celular es una imagen de 599 × 803 px dibujada encima del mundo, con el área de pantalla entre `celX1, celY1` y `celX2, celY2`. Cada app es un valor de `cel` (sección 2) y el botón del celular lo abre y lo cierra (`cel = 1` o `cel = 0`). Con el celular abierto el personaje no se mueve, el reloj va 3 veces más rápido y cada medio minuto suma pantalla y tiempo de redes.

### WhatsApp: la matriz de chats

`msg[45][80]` tiene una fila por chat: `[0]` el nombre, `[1]` un texto como `"1010"` que dice quién mandó cada mensaje visible (su largo es cuántos se ven), `[2]` el puesto de recencia y `[3..79]` los textos.

- **Mostrar uno nuevo.** `nuevomensaje("1" + fila)` agrega una letra a `[1]`. Si es de la otra persona y el chat no está abierto, sube `noLeidos[fila]` (la burbuja roja).
- **Orden.** El chat pasa al primer puesto y los demás bajan uno.
- **Escribir uno nuevo.** `agregarMensaje(chat, quién, texto)` lo escribe en la siguiente casilla libre. Si el chat se llenó, corre todo una casilla y borra el más viejo.
- **Scroll.** El alto de cada burbuja se calcula según cuántas líneas ocupa el texto, y la rueda del mouse mueve `msgBarra`.

**Mensajes programados.** `MSG_PROG` y `MSG_PROG_V20` tienen filas `{día, hora, chat, condición, texto, opción 1, efecto 1, opción 2, efecto 2, opción 3, efecto 3}`. Llegan si es el día, ya pasó la hora, se cumple la condición y esa persona tiene tu número. Cada opción aplica su efecto, y «Sin responder» se aplica sola si no contestas en el día.

**Escribir tú.** `TEMAS_V21` tiene `{tipo, lo que escribes, para quién, condición}` y la respuesta sale de `RESP_V21`: gana la fila más específica (la de esa persona antes que la de su círculo, y la de mayor amistad mínima que ya alcanzas). Llega después de unos segundos de «X está escribiendo…».

**Visto.** Si abres un mensaje y no contestas, queda en visto, y esa persona te lo reclama en persona con una línea de `REPROCHE_VISTO`.

### Planes e invitaciones

En un chat aparece **Proponer plan**: lugar de `LUGARES_PLAN` y hora entre las próximas tres en punto. Los planes viven en vectores paralelos `planPersona`, `planDia`, `planMin`, `planLugar` y `planEstado` (0 propuesto, 1 aceptado, 2 cumplido, 3 te esperó, 4 rechazado). `aceptaPlan` dice que sí con amistad de 55 o más, 2 o más días de charla, la persona libre a esa hora (`ocupadoA`) y sin lluvia si es el parque. Llegar arma una escena `PLAN`; cancelar baja la amistad 2; no llegar la baja 6. `INVITA20` guarda las invitaciones que te hacen: un plan, «ven ya» o un reto con minijuego.

### Llamadas

`LLAMADAS` tiene filas `{día, hora, quién, motivo, condición, efecto si contestas, efecto si cuelgas, lo que dice}`. Contestar gasta 3 minutos. Las de motivo «clase» suenan en clase: si contestas, el profe te ve (amistad −4 y Notas −2).

### Aurora+ (la red social) y la reputación

`armarFeed()` arma la lista del día con publicaciones de `REDES_DIA`, `REDES_EXTRA`, `POSTS_GENERICOS`, `CHISMES` y el reto del día. Cada una sale después de su hora y si se cumple su condición (la foto de Sofía dormida solo sale si fuiste a Física). Se ve una a la vez con **Me gusta**, **No me gusta** y **Pasar**:

| Tipo | Me gusta | No me gusta |
| --- | --- | --- |
| amigo | Social +1, Seg +1 | Social −1 |
| chisme | Seg +2, Social −1 | Social +1 |
| tóxico | Seg +3, Social −2 y la bandera `MALA_REPUTACIÓN` | Social +2 |
| meme | Seg +1 |  |
| útil | Notas +1 |  |

Mirar cada publicación gasta 5 minutos de juego; pasarla, 2. **Subir** usa la tabla `SUBIDAS` (`{id, tipo, requisito, texto, tono, efecto, comentarios}`), con 2 subidas por día. Los likes salen de `base = 3 + seguidores / 3`: una publicación buena da `base + 3`, una polémica `base × 1,5 + 2` y una mala `base × 2`. Lo malo da más likes, pero sus efectos cuestan Social: esa es la lección de huella digital.

**Retos diarios.** `RETOS` tiene un reto por día. `ponerReto()` lo mete en el feed y, si lo aceptas, `revisarRetos()` lo da por cumplido cuando haces lo que pide y aplica el premio.

### Galería y editor

`FOTOS_GALERIA` (47 fotos, 15 columnas) dice qué fotos existen, su condición, quién sale, sus cuatro pies de foto y qué pasa si etiquetas bien o mal. `revisarGaleria()` las desbloquea; corre en cada bloque de 5 minutos y al cambiar de mapa, así una foto de «estar aquí a esta hora» sale apenas entras. El editor va en cinco pasos: filtro, recorte, pie de foto, etiquetas y publicar. El blanco y negro se calcula de verdad: `hacerGris()` recorre el vector `pixels[]` y pone cada píxel en `g = 0,3·R + 0,59·G + 0,11·B`. Al publicar, `likes = (6 + seguidores / 3) × multiplicador`: saturado ×1,3, pie exagerado ×1,4 (Social −2), pie polémico ×1,6 (Social −4 y `MALA_REPUTACIÓN`), etiquetar mal ×1,3 con el efecto malo, solo mejores amigos ×0,35 (Social +1).

### Las otras apps

| App | Cómo funciona |
| --- | --- |
| Horario | Una grilla por día: las clases de `CLASES` se pintan solas y los eventos y planes se agregan con `ponerEnHorario`. |
| Ajustes | Alarma (de 4:00 a 10:00 en pasos de 15 min), No molestar y Bienestar digital, que compara los minutos de hoy de cada categoría con `idealMin` e `idealMax`. |
| Pedidazo | Catálogo `PEDIDAZO` `{producto, precio, categoría}`, carrito y envío. Lo pedido llega al otro día desde las 7:00 (`revisarPedidos`). |
| Batería | Abierto baja 0,14 % por tick; cerrado, 0,012 %. En casa carga 0,12 % por tick. En 0 el celular se apaga. |
| Mapa | Muestra la ciudad. Si compartes la ubicación con Mamá, cada mañana revisa si faltaste a clase. |
| Diario, Relaciones, Logros, Notas, Playlist | El diario se escribe solo (`anotarDiario`); `RELACIONES` dibuja quién se lleva con quién; Notas guarda pendientes, pistas y deudas; la Playlist corta la música y pone su lista por 3 horas, y su efecto se gana una vez cada 3 horas (ver «Música por zona y la Playlist»). |

### Música por zona y la Playlist

Las 12 pistas están en `data/musica/` como WAV mono de 22.050 Hz, que es lo que lee la biblioteca Sound de Processing (los temas llegaron en OGG y se convirtieron a WAV). Sus nombres están en el vector `PISTAS`: `menu`, `manana`, `tarde`, `noche`, `minijuego` y los 7 temas de zona `area_1_paradero` … `area_7_fuera_de_la_u`.

`temaDeMapa(m)` dice qué tema le toca a cada mapa usando los rangos de las constantes de los mapas: el frente de la casa, el bus, los paraderos y la Terminal suenan con *Paradero*; el resto de los mapas I1–I8 con *Espacios intermedios*; U1–U16 con *Universidad*; P1–P7 con *Plaza Aurora*; K1–K9 con *Parque Cerezos*; D1–D7 con *Zona deportes* y F1–F5 con *Fuera de la U*. Dentro de la casa devuelve −1 y suena la música de la hora (mañana 5:00–12:00, tarde 12:00–18:30, noche el resto).

`pistaDeseada()` decide en este orden: título o final → `menu`; si hay una lista de la Playlist sonando → su tema; minijuego o juego del celular → `minijuego`; si no, el tema de la zona o el de la hora. `actualizarMusica()` corre en cada cuadro: sube de a poco el volumen de la pista que toca y baja el de las demás, así que al cambiar de zona una se desvanece y la otra entra. Cada pista se carga la primera vez que hace falta (`cargarPista`), para no gastar memoria en las que no suenan.

**La Playlist corta en seco.** `ponerPlaylist(i)` guarda la lista en `listaSonando` y hasta cuándo suena en `listaHasta` (3 horas del juego, medido con `minutoAbs()`), y prende `cortarMusica`. En el siguiente cuadro, `actualizarMusica()` apaga todas las pistas de una vez y pone la de la lista desde el principio, con todo el volumen. Las listas usan los temas que más les quedan: estudiar → *Universidad*, entrenar → *Zona deportes*, calmarse → *Parque Cerezos* (vector `LISTAS_TEMA`). La música se puede cambiar cuando quieras; el efecto en los stats sigue la regla de antes: una vez cada 3 horas (`playlistUlt`). `quitarPlaylist()` pone `listaSonando = 0` y también corta, para que vuelva la música del lugar. Como `listaSonando` y `listaHasta` son variables del juego, se guardan solas en la partida.

### Los juegos del celular

**Wordle.** Una matriz de letras `wrdl[6][5]` (6 intentos de 5 letras) y una de colores `wrdlc[6][5]`: 1 azul (no está), 2 amarillo, 3 verde. Al dar ENTER con 5 letras se copia la secreta en `vec[5]`; la primera pasada pinta de verde las letras en su lugar y las borra de `vec`; la segunda pinta de amarillo cada letra que encuentra en lo que queda de `vec` y también la borra. Así una letra repetida no se pinta dos veces.

**Flappy.** Los tubos son `fpTubos[3][3]` (x, y del hueco, ya dio punto). En cada cuadro `velocidad += gravedad` y `y += velocidad`; cada click pone la velocidad en −12. Los tubos van 6 px a la izquierda y, al salir, saltan `3 × 300` px a la derecha con un hueco nuevo. El choque es de rectángulos.

**Pong.** La pelota es `pgBola[4]`: x, y, velocidad en x, velocidad en y. Rebota en el techo, el piso y la pared derecha. La barra se mueve sola a `pgVelBarra` = 9 px por cuadro y cada click le invierte la dirección. La pelota sale a 6 px por cuadro en x y entre 2 y 4,5 en y; al tocar la barra, su velocidad en x se multiplica por 1,06 con tope 11 y la de y cambia según dónde pegó, entre −7 y 7. En la v27 se bajó todo esto (antes salía a 35 px por cuadro con barra a 25), porque no era jugable.

## 10. Clases y parciales

### El horario y el flujo de una clase

La tabla `CLASES` tiene 17 filas `{día, desde, hasta, materia, mapa, profe, compañeros}`: dos clases los días 1 a 5 y 8 a 9 (7:00 y 9:00) y los tres parciales el día 10 (7:00, 9:00 y 11:00). El estado de cada clase está en `claseEstado[c]`: 0 pendiente, 1 asistió, 2 llegó tarde, 3 falta.

1. **`claseAhoraEn(mapa)`** devuelve la clase de este mapa entre 30 minutos antes y el final.
2. **`tomarClase()`** se activa con \[E\] en los pupitres. Más de 15 minutos tarde (`CLASE_TARDE_MIN`) es estado 2.
3. **`minijuegoDe(c)`** elige el minijuego por la materia: Física → tiro parabólico, Laboratorio → péndulo, Cálculo → todas las que puedas, Álgebra → balanza, Programación → cazabichos.
4. **El minijuego** corre en `ACT_CLASE_JUEGO` y termina con `terminarMinijuegoClase(notas, texto)`, con notas de −1 a 4. Si llegaste tarde se reduce a la mitad; en un parcial se multiplica por 2.
5. **`despuesDelResultado()`** pasa las escenas de esa clase como cinemática.
6. **`terminarClase()`** avanza el reloj hasta el final y lo suma a Estudio, suma las notas (salvo que te hayas dormido: deuda de 3 o más, o energía menor a 15), registra la nota de la materia y rearma los diálogos del profe y los compañeros.

**Faltas.** `revisarClases()` revisa cada tick si una clase pendiente ya terminó: queda como falta, quita 2 de Notas (5 en Física del día 1, donde el profe llama a lista) y esa materia baja 2 puntos.

### Nota por materia y dificultad

- `ramoPuntos[4]` suma lo de cada clase de Física, Cálculo, Álgebra y Programación.
- `notaRamo(r) = 1,5 + Notas / 40 + ramoPuntos[r] × 0,15`, entre 0 y 5. Se pasa con 3,0. Faltar a la evaluación final de una materia la pierde.
- **`nivelClase()`** depende del día: 1 en los días 1–2, 2 en los 3–5, 3 en los 6–9 y 4 el día 10.
- **La dificultad del juego** `difMult` vale 0,75, 1,0 o 1,3. `facil(v) = v / difMult` sirve para lo que debe ser más generoso en Fácil (tiempos, tolerancias) y `dificil(v) = v × difMult` para lo que debe ser más duro en Difícil (velocidades).

Un **parcial** son dos minijuegos seguidos (`parcialEncadenado()`): Física = tiro + péndulo, Cálculo = todas las que puedas + pendiente, Álgebra = balanza dos veces. La nota es la suma de las dos partes por 2.

### Los minijuegos de clase

**Tiro parabólico (Física).** `pyAng` (5 a 85°), `pyPot` (5 a 30), la bala (`pyBX, pyBY, pyVX, pyVY`), el blanco y el viento (0 en el nivel 1, entre −0,06 y 0,06 desde el 2). ESPACIO dispara con `vx = cos(θ) × fuerza` y `vy = −sen(θ) × fuerza`, y en cada cuadro:

```java
pyVX += pyViento;  pyVY += PY_GRAVEDAD;   // 0,35: la gravedad suma a vy, el viento a vx
pyBX += pyVX;      pyBY += pyVY;
```

Antes de disparar se dibuja la parábola simulando la misma física, cada vez más corta según el nivel (`B_PY_PREVIA`). Desde el nivel 3 el blanco se mueve. 3 tiros: 2 aciertos dan +3, 1 da +1 y 0 da −1.

**Péndulo (Laboratorio).** El ángulo es una función del tiempo, `angulo = 50 × sen((millis() − peInicio) × w)` con `w = 0,0025 + nivel × 0,0006`. ESPACIO acierta si `|ángulo| < 6°`, con 350 ms de espera entre intentos. 6 intentos.

**Balanza (Álgebra).** `nuevaEcuacion()` sortea primero la solución `x` entre 1 y 9 y después arma la ecuación para que esa sea la respuesta: `a·x + b = resultado` en el nivel 1 y `a·x + b = d·x + e`, con `e = (a − d)·x + b`, desde el 2. Las 4 opciones son la correcta en una posición al azar y `x + cambio` con cambios sin repetir. Elegir mal inclina la balanza y quita 3 s.

**Cazabichos (Programación).** Cada cosa es una fila de `cosas[30][7]`: x, y, velocidad x, velocidad y, nacimiento, tipo (0 bicho, 1 café, 2 check, 3 llaves, 4 cursor) y viva. Cada pocos ms nace una en la primera fila libre (62 % bichos). En cada cuadro, en un solo ciclo: se libera si pasaron 2,6 s, se mueve y rebota en los bordes, y se dibuja. El click busca con `dist` la fila viva más cercana a menos de 32 px. Nota: `r = cazados / (cazados + escapados) − errores × 0,1`.

**Todas las que puedas (Cálculo).** `nuevaPreguntaCalculo()` arma la pregunta (sumas, tablas, derivadas de `c·xⁿ` y de `a·x² + b·x + k`, límites como `(x² − a²)/(x − a)`) y 3 respuestas falsas con errores típicos. Cada 2 aciertos sube un nivel de pregunta y un error lo baja. La meta es `{4, 5, 6, 7}` aciertos según el nivel.

**Pendiente (parcial de Cálculo).** Se dibuja una recta con pendiente `prM1` y dices si sube, está plana o baja; desde el nivel 3 a veces hay dos rectas y dices cuál es más empinada.

## 11. Deportes, gimnasio y PixelZone

### Copa Aurora

La tabla `COPA` tiene 9 partidos `{día, hora, deporte, ronda, dificultad 1–6, rival, premio, mapa}`: cuartos, semifinal y final de rugby, fútbol y natación, del día 4 al 9. El estado de cada uno está en `copaEstado[k]`: 0 pendiente, 1 ganado, 2 perdido, 3 no te presentaste.

- **`partidoAhora(deporte)`** devuelve el partido si estás en su mapa entre 30 minutos antes y 60 después; si no, se juega una práctica.
- **`registrarPartido(gano, detalle)`** cobra energía (15 un partido, 10 una práctica) y suma 60 minutos de ejercicio. Si ganas: el premio, Social +3, seguidores +10 y la bandera `VICTORIA`; si ganas las tres rondas, `TROFEO_<DEPORTE>`. Si pierdes, quedas fuera.
- **El rival se pone más rápido** a medida que ganas: `vele = VELE_BASE + ganados × VELE_SUBE`.

### Rugby y fútbol: un mismo motor

El rugby se escribió primero y el fútbol es **una copia del mismo motor** con los nombres terminados en S (`footballS`, `cicloFutbolS`…) y lo propio del fútbol encima. Se explica una vez:

- **Datos.** Todo el partido es una matriz `football[9][21]`: las filas 0–3 son tu equipo, las 4–7 el rival y la 8 el balón. Las columnas de cada jugador son x, y, ángulo, ángulo objetivo, giro, movimiento, estado (normal, lanzándose, derribado), temporizador, objetivo, marca, maniobra, carril, rol y decisión. Las del balón: x, y, quién lo tiene (o en el aire, o suelto), origen, destino y progreso del pase.
- **Decisiones cada 100 ms** (`cicloFutbol`): `calcularRoles()` da a cada bot un rol (portador, atacante, perseguidor, marca, ir por el balón, receptor o subir); cada 5 ciclos se reasignan las marcas; cada atacante tiene 5 % de elegir una maniobra (cortar, acercarse, ir profundo, abrirse, regresar).
- **Cada cuadro:** cada jugador gira hacia su ángulo objetivo con inercia y avanza. `intentarTackles()`: un rival a menos de 60 px del portador se lanza con una probabilidad que crece con la cercanía, `lerp(0,05; 0,35; (60 − d)/40)`, apuntando adonde va a estar el portador.
- **Pase:** con click se lanza el balón hacia el mouse; su posición es `lerp(origen, destino, p)` con `p` de 0 a 1. Lo atrapa quien esté a menos de 20 px al llegar; un rival a 16 px puede interceptarlo.

|  | Rugby | Fútbol |
| --- | --- | --- |
| Pantalla | Propia (`screen 3`) | Actividad del mundo |
| Anotar | Llegar con el balón a la zona final (100 px) | Gol entre y 429 y 563, con arqueros |
| Gana | El primero a 5 | El primero a 3; si empatan, penales |
| Extra |  | Cuatro estrategias (`ESTRATEGIAS`), sprint con estamina, tiro cargado y efecto con Q / E |

**Penales y pases largos.** Click en una de las 6 zonas del arco y ESPACIO para detener una barra de fuerza; la zona verde está justo debajo de 0,9. El portero adivina tu zona con probabilidad `0,15 + 0,06 × dificultad + 0,05 × tiro`.

### La marca y la zona verde: gimnasio y más

Varios ejercicios usan la misma mecánica: una **marca** que se mueve entre 0 y 1 y una **zona verde**. Se acierta si `|marca − centro de la zona| ≤ ancho / 2`, y con poca energía la zona es más chica. Se usa en:

| Dónde | Qué cambia |
| --- | --- |
| Barra y pesas | La zona está en 0,82 y mide `0,22 × (0,6 + 0,4 × energía)`; cada acierto acelera la marca 6 %; 3 fallos seguidos y se cae la barra |
| Mancuernas | Dos marcas, una por brazo (← y →); al acertar, la zona salta, se angosta 6 % y la marca acelera 7 % |
| Sesión con el Tanque | Mancuernas, caminadora y press seguidos, con gritos de `GRITOS_BIEN` y `GRITOS_MAL` |
| Respiración de la natación | ESPACIO cuando la burbuja llega al tamaño justo |
| Penales | La barra de fuerza |

Los que son distintos: la **caminadora** (← y → alternados; la franja buena oscila con `centro = 6 + 2,5 × sen(0,45 t)`), el **press** (una aguja de equilibrio que se tuerce sola y se corrige con ← →) y el **ciclismo** (tres carriles; obstáculos en vectores paralelos `cicObsX`, `cicObsCarril`, `cicObsTipo`, `cicObsVivo`, cada vez más seguidos).

### Natación por estilos

100 m contra un rival a velocidad fija `velRival = 100 / (60 − dificultad × 2,8 − ganadas)` m/s. Tu velocidad tiende sola a 0,6 m/s y cada acierto la impulsa. Cada 9 s cambia el estilo: crol (← → al ritmo de un pulso), pecho (repetir una secuencia de flechas), espalda (la flecha que sale; si es roja, la contraria), respiración y, desde el día 6, mariposa.

### PixelZone (arcade)

Cada partida cuesta una ficha o $4 y 15 minutos de juego.

- **Pixel Royale.** Las balas viven en `balas[120][5]` (x, y, velocidad x, velocidad y, viva). `dispararBala` busca la primera fila libre, elige un borde y apunta al jugador con `atan2`, cada vez más rápido y más seguido. Choque si `dist < 17`; 3 vidas.
- **Torre.** Los pisos son `pisos[n][2]` (x y ancho). Al soltar se calcula el traslape con el piso de abajo, `izq = max(x, x_abajo)` y `der = min(x + ancho, x_abajo + ancho_abajo)`, y lo que sobra se corta.
- **Duelo contra Camilo.** Se espera un tiempo al azar de 1,5 a 4 s y sale «¡YA!»; el tiempo de Camilo se sortea entre 210 y 330 ms y baja 6 ms por ronda.

## 12. Minijuegos: el motor común y las mecánicas que se reutilizan

Hay 31 minijuegos de personajes, pero muchos comparten la misma mecánica con otro dibujo y otros datos. En vez de escribir un minijuego por personaje, se escribió **una mecánica y varios «menús» de datos**: el café de Nico, la Cantina, los ramos de flores y la heladería son el mismo código. Esta sección explica cada mecánica una vez y después dice en cuáles se usa.

### El motor común

Todos los minijuegos de personajes pasan por las mismas cuatro piezas:

1. **La tabla `MJ_INFO`**: 31 filas `{código, título, minutos que pasan, categoría, efecto si te va bien, efecto si no}`. La categoría es E (estudio), J (ejercicio), A (amigos), R (redes) o «-» (trabajo).
2. **Se abren desde una escena** con la acción `MJ:CÓDIGO#RAMA_BIEN#RAMA_MAL`, o desde una invitación de WhatsApp de tipo MJ. Antes de jugar sale el cartel de cómo se juega, de la tabla `AVISOS_MJ`, y el reloj se congela mientras está abierto.
3. **Mientras se juega**, `ACT_MJ20` tiene un `switch` por código: `iniciarMJ(c)`, `dibujarMJ(c)` y lo mismo para teclas, clicks y soltar el mouse. El tiempo de cada cuadro sale de `dt20()` (los ms desde el cuadro anterior divididos por 16,7), así todo se mueve igual a 30 o a 60 cuadros por segundo.
4. **`finMJ(puntaje, texto)`**: todos terminan aquí con un puntaje de 0 a 100. Deja las banderas `CÓDIGO_HECHO`, `CÓDIGO_BIEN` (50 o más) y `CÓDIGO_PERFECTO` (100); suma los minutos a su categoría; guarda el récord en la cuenta; aplica el efecto bueno o el malo, y si vino de una escena, la escena sigue por la rama `BIEN` o `MAL`.

Los turnos de trabajo duran según la dificultad: `TURNO_FRACCION = {⅓, ½, 1}`.

### Mecánica 1. Pedidos

**Cómo funciona.** Cada «menú» tiene tres grupos de opciones, A, B y C, con sus nombres, colores y dibujos.

- El cliente pide al azar: `pdPideA`, una lista `pdPideB[]` y `pdPideC`.
- Lo que armas queda en `pdArmA`, `pdArmB[]` y `pdArmC`, con clicks en botones dibujados en grilla.
- `exactitudPedido()` da 25 puntos si A coincide y 25 si C coincide. Los 50 restantes se reparten según cuántos de B están en la posición correcta, y cada B de sobra resta.
- **Paciencia:** el cliente espera 24 s (`1 − t / 24000`), y su cara cambia a mal genio.
- **Propina** con un pedido perfecto: `max(0, 3 − segundos / 8)` pesos.
- **Meta:** `max(2, round(5 × fracción del turno))` pedidos. **Puntaje:** promedio de exactitud por `min(1, atendidos / meta)`.

**Se usa en estos cuatro:**

| Minijuego | Quién | A | B | C |
| --- | --- | --- | --- | --- |
| Heladería | Paola | Recipiente | Hasta 3 sabores en orden | Topping |
| Ramos | Doña Inés (flores) | Papel | Hasta 3 flores en orden | Cinta |
| Almuerzo de la Cantina | Doña Cecilia | Sopa | Seco | Jugo |
| Café de Nico | Nico (kiosco) | 6 cafés | 4 panes | 3 dulces |

En Nico y la Cantina cada opción tiene su dibujo, recortado de una hoja con `cortarHoja`, y la bandeja se dibuja con lo que pusiste.

### Mecánica 2. Ritmo

**Cómo funciona.** Las notas viven en vectores paralelos `rtY[80]`, `rtCarril[80]` y `rtViva[80]`, un «pool» que reutiliza las filas libres. Cada 420 ms (o 840, el 30 % de las veces), divididos por la dificultad, nace una nota arriba en un carril al azar y baja `5,5 × difMult × dt`. Al apretar la tecla de un carril se busca la nota viva más cercana a la línea: a menos de 40 px es «Perfecto» (100) y a menos de 80, «Bien» (60). Si una nota pasa 90 px por debajo, se pierde y la racha se corta. Puntaje: puntos sobre notas.

**Se usa en:** DJ en la terraza de Marta (4 carriles), Al ritmo con Iván y con Pili (3), Trote con Esteban (3) y Reto de baile para ClipU (3, dura 22 s en vez de 30). Solo cambian el fondo, los carriles y los efectos. El karaoke y el micrófono abierto usan la misma idea con su propia matriz `notas[n][3]`.

### Mecánica 3. Ordenar pasos

**Cómo funciona.** `datosOrden(c)` devuelve los conjuntos de pasos de cada escena: un vector cuyo primer texto es el título y los demás son los pasos en orden. `prepararSetOrden()` llena `orOrden[i] = i` y lo baraja con Fisher–Yates («qué paso hay en cada posición de la pantalla»). Las tarjetas están en `y = 180 + i × 95`, así que el click se resuelve con un rectángulo por fila. Si el paso tocado es `orSig`, el que sigue, se marca en `orPuesta[]` y `orSig` sube; si no, es un error. Puntaje: `100 × aciertos / intentos × conjuntos terminados`.

**Se usa en estos ocho:** Tutoría de Cálculo (Laura), Primeros auxilios (enfermera Lidia), Pizarra táctica (Ochoa), Arreglar la bici (Papá), Cocinar el ajiaco (Mamá), Estirar (Marcela), Técnica de barra (el Tanque) y Trasplantar la maceta (Don Pablo). En la receta de Mamá primero se muestra el orden 4,5 s (`orVerHasta`) y después hay que repetirlo de memoria.

### Mecánica 4. Vueltos

**Cómo funciona.** `VT_PRECIO = {1, 1, 2, 3, 2}` para los 5 productos y `VT_BILLETES = {1, 2, 5, 10}`. El cliente compra de 1 a 3 productos y paga con 5, 10 o 20. Armas el vuelto exacto con los billetes y se puede quitar el último. Puntaje: `100 × bien / max(meta, atendidos)` en 70 s por la fracción del turno.

**Se usa en:** la canasta de Andrés (en la Cantina y en el Mercadito) y las empanadas de Doña Mery.

### Mecánica 5. Mantener el mouse en un punto que se mueve

**Cómo funciona.** Un punto se mueve por la pantalla y se cuenta cuánto tiempo está el mouse cerca de él. El puntaje es el porcentaje del tiempo dentro.

| Dónde | Cómo se mueve el punto | Qué se agrega |
| --- | --- | --- |
| Estudiar (escritorio o Biblioteca) | Suma de senos: `cx = 800 + 380·sen(0,9 t) + 120·sen(2,3 t + 1)` | Distracciones de la tabla `DISTRACCIONES`; con poca energía cabeceas. Notas: `round(concentración × 4)`, ×1,5 en la Biblioteca |
| Estudiar con el celular al lado (Sofía, Marlene) | Ruido de Perlin: `atX = 800 + 420 × (noise(t) − 0,5) × 2` | Notificaciones en `atNx`, `atNy`, `atNviva[4]`: cerrarlas no cuesta, abrirlas te deja leyendo 2,2 s |
| Posar para Don Aurelio | Ruido de Perlin, muy poco | Si te sales del círculo de 38 px, él grita |

El ruido de Perlin (`noise`) se usa porque el movimiento se ve natural, no a saltos como con `random`.

### Mecánica 6. Respirar

**Cómo funciona.** Un círculo crece y se encoge en un ciclo de 6 s: la primera mitad es inhalar y la segunda exhalar. En cada cuadro cuenta como bien si mantienes ESPACIO al inhalar y lo sueltas al exhalar. Son 5 ciclos.

**Se usa en:** la entrenadora Paz (piscina), Nadia (piscina) y Sofía (antes del micrófono abierto).

### Otras piezas reutilizadas

- **El editor de fotos** de la Galería (sección 9) es también el minijuego de Paola del día 8.
- **El torneo de PixelZone** con Camilo usa el Pixel Royale y el duelo del arcade (sección 11).
- **El motor de rugby** es también el del fútbol (sección 11), y **la marca y la zona verde** son la base del gimnasio.

### Los minijuegos únicos

| Minijuego | Cómo funciona |
| --- | --- |
| Latte art (Valentina) | La guía es un vector de puntos `ltGuia[n][2]`; el corazón es la curva paramétrica `x = 16·sen³t`, `y = 13·cos t − 5·cos 2t − 2·cos 3t − cos 4t`. Tu trazo se guarda en `ltX[900]` y `ltY[900]` (un punto cada 4 px). `evaluarLatte()` mide cobertura (puntos guía con un punto tuyo cerca) y precisión (puntos tuyos cerca de la guía): `100 × (0,6 × cobertura + 0,4 × precisión)`. |
| Reparar controles (Kevin) | `ctPuerto[6]` es la permutación de qué cable va a cada puerto, barajada con Fisher–Yates. 3 rondas de `4 + ronda` cables; en la tercera la palabra está pintada con la tinta de otro color. |
| Moderar el directo (Camilo) | Comentarios en `mdY[30]`, `mdMsg[30]` y `mdVivo[30]`, sacados de `MOD_MSGS` (50 % buenos, 30 % tóxicos, 20 % spam). Suben por el chat; borrar uno bueno quita espectadores. |
| ¿Confiable o trampa? (Laura) | `trOrden` es un vector con los índices de `TR_MSGS` barajado con `barajarInt`. 6 mensajes, 1 o 2, con la explicación después de cada uno. |
| Pintar el cartel (Lili e Iris) | El lienzo es `cePint[7][10]` y el modelo `CARTEL_MODELO` (7 textos de 10 dígitos). La casilla se calcula dividiendo: `c = (mouseX − 200) / 90`. |
| La cometa (Valeria) | `coY` y `coV`: el click jala, soltar la deja caer, el viento es un paseo al azar y la velocidad se amortigua con `coV *= pow(0.96, dt)`. |
| Buscar a la mamá de Mateo (Julián) | Multitud en vectores `buX`, `buY`, `buCam`, `buSombrero`, `buBolso`. A cualquiera que coincida en todo con la mamá se le cambia algo, para que la descripción sea única. |
| Rondo (Rojas) | 4 compañeros en `RO_POS`; en cada pase se tapan 2 al azar (`roTapado[4]`) y hay que pasarle a uno libre antes de `1700 − 70 × pase` ms. |

## 13. Casa y mundo vivo

### La cama: el minijuego del insomnio

Acostarse (`acostarseCama`) no duerme de una vez: primero hay que pasar 25 s de notificaciones. Esta es la mecánica que muestra el uso excesivo del celular de noche.

Las notificaciones son la matriz `notif[12][8]`: x, y, nacimiento, app (ícono y texto de `NOTIF_TEXTOS`), viva, tipo y velocidad x, y. Hay cuatro tipos: normal (40 %), deslizar (25 %), móvil (20 %) e importante (15 %, de la familia). La dificultad crece con lo que usaste el celular ese día:

```java
d = 1 + pantallaDeHoy / 240 + deudaSueño × 0,15;   // × 0,6 con «No molestar»
```

Sale una cada `lerp(1400, 550, avance) / d` ms y cada una vive `2600 / (0,8 + 0,2·d)` ms. Si una cumple su vida sin que la quites, cuenta como **abierta** («un video más»). Las de deslizar hay que arrastrarlas más de 120 px (el click guarda la x inicial y `mouseReleased` mide la distancia). Las importantes se contestan: Mamá +1, o −2 si la cierras sin responder.

`terminarInsomnio()` calcula cuánto duermes: hasta la alarma (6:00, o 10:00 si te acuestas el día 5 o 6), con máximo 600 minutos, menos 30 por cada notificación abierta, con mínimo 60. Después `dormir(minutos)` baja la deuda de sueño (2 con 10 h o más, 1 con 7 h o más), avanza el reloj, arma el día nuevo y deja la energía en `20 + 10 × horas`.

### Deuda de sueño

`nochesHastaAhora()` cuenta cuántas veces el reloj ya pasó la 1:00 desde el día 1. `revisarDeudaNoche()` sube la deuda en 1 por cada 1:00 nueva en la que no estabas en la cama, aunque la hayas saltado con una actividad larga. Con deuda 1 la energía máxima baja a 70; con 2, a 50 y da estrés; con 3, te duermes en clase y en el bus.

### Lluvia

Cada mañana `decidirLluvia()` decide si llueve: el día 8 llueve seguro de 14:00 a 19:00 (por la escena de Canela bajo la banca), los días 1 y 10 nunca, y los demás con 28 % de probabilidad, empezando entre las 9:00 y las 15:00 por 2 a 4 horas. Mientras llueve se dibujan gotas en los mapas exteriores (vectores `gotaX`, `gotaY`, `gotaV`), los planes en el parque no se aceptan y la gente que no sale con lluvia desaparece de su agenda.

### Romance

Cinco rutas: Sofía, Laura, Marta, Nadia y Valentina (`ROM_PERSONA`). `romancePuntos[5]` suma los `Rom +N` del guion; al llegar a 15 empieza el coqueteo. `romance[5]` es el nivel de cada ruta: 0 nada, 1 coqueteo, 2 cita, 3 pareja, −1 bloqueada. Si hay dos rutas activas, se anota el día (`dobleDesde`) y al día siguiente `revisarChismeRomance()` saca el chisme en «Confesiones Aurora»: ambas rutas quedan bloqueadas y la amistad con ambas baja 30.

### Estrés y vicio

`revisarEstres()` pone la bandera `ESTRES` si perdiste un partido de la Copa, la deuda de sueño es 2 o más, las Notas están por debajo de 40, la amistad con Mamá está por debajo de 30 o es el día 8 después de la 1 p. m. y el rumor no se resolvió. Con estrés, Chato te busca en la esquina.

`VICIO` es una bandera que sube 1 cada vez que aceptas en la esquina. En los deportes vas más lento (`lentitudVicio = max(0,6; 1 − 0,06 × VICIO)`), cambian los saludos de la gente y resta 40 puntos por nivel. Si decides dejarlo (`QUIERE_DEJAR`), cada día entero sin subirlo baja 1.

### El mundo vivo: lo que corre solo

`tickReloj()` y las funciones que encadena revisan cada medio minuto de juego, mires o no: las escenas de mapa y los eventos; los mensajes programados, las charlas, los retos y las respuestas a lo que escribiste; los mensajes sin responder; los avisos del Horario y los pedidos; las faltas a clase y los partidos de la Copa; la lluvia y la deuda de sueño; las llamadas y el chisme de romance; el club y el estrés; y el cambio de día. Tres revisiones que no cambian a cada rato van una vez por bloque de 5 minutos (sección 16): la agenda de la gente, la Galería y los logros.

Al empezar cada día entre el 2 y el 9 se sortea también: alguien enfermo (30 %, no aparece en todo el día), bus lleno (30 %, 8 minutos más por viaje) y oferta del Pedidazo (25 %, envío gratis desde las 12:00). Cada uno queda en el diario.

## 14. Puntaje, evaluación final, logros y finales

### Historial por día (el balance)

Cuatro vectores guardan lo que pasó cada día (el índice es el día, del 1 al 10): `catHist[12][5]` (minutos por categoría), `rangoHist[12]` (cuántas categorías quedaron en su rango, de 0 a 5), `pantallaHist[12]` (minutos de celular) y `diaGuardado[12]`. Las categorías son constantes `CAT_ESTUDIAR=0, CAT_DORMIR=1, CAT_EJERCICIO=2, CAT_AMIGOS=3, CAT_REDES=4`. Durante el día cada acción suma a `catMedios[c]` en medios minutos. El rango sano sale de `idealMin(c, d)` e `idealMax(c, d)`:

| Categoría | Mínimo (min) | Máximo (min) |
| --- | --- | --- |
| Estudiar | 240 (120 sábado y domingo) | 360 (180 sábado y domingo) |
| Dormir | 420 | 540 |
| Ejercicio | 60 | 180 |
| Amigos | 120 | 240 |
| Redes | 30 | 120 |

`registrarDiaV20(d, cats, enRango, pantalla)` guarda el día; con 5 en rango suma `DIA_PERFECTO` y con menos de 30 minutos de pantalla, `DIA_DESCONECTADO`. `diasEquilibrados()` cuenta los días con 4 o más en rango.

### Puntaje

```
puntaje() = 2·Notas + 2·Social + min(200, ejercicio_total / 6)
          + 5·puntosEquilibrio − 40·VICIO + 5·logros
```

Cada término es su propia función (`ptsNotas`, `ptsSocial`, `ptsEjercicio`, `ptsEquilibrio`, `ptsVicio`, `ptsLogros`) para mostrar el desglose en la pausa y en el informe.

### Logros

`LOGROS` tiene 32 filas `{nombre, cómo se consigue, condición}`, y la condición la evalúa `cumple()` (`DIA>=2`, `AMIGOS>=5`, `F:BUEN_DORMIR`…). `revisarLogros()` recorre la tabla; cuando una fila se cumple, `logroHecho[i]` pasa a `true` y no se apaga más. Corre una vez por bloque de 5 minutos de juego y, además, enseguida si cambió el dinero, los seguidores o lo social (lo que puede subir y bajar), para que un logro como «Junta $100» no se pierda si gastas la plata. Los logros de la cuenta se guardan aparte en `cuenta.txt`.

### Fin del juego y qué final te toca

`revisarFinDelJuego()` termina la partida al pasar al día 11 o el día 10 a las 23:30. `terminarJuego(motivo)` marca el fin, suma `GRADUADO` si no hay ramos perdidos, revisa los logros, elige el final y anota la partida en `puntajes.txt`.

`elegirFinal()` es una cadena de `if / else if`: gana el primero que se cumpla.

| Orden | Final | Condición |
| --- | --- | --- |
| 1 | REPROBADO · No te graduaste | `ramosPerdidos() >= 2` |
| 2 | QUEMADO | `VICIO >= 4` o `deudaSueno >= 3.5` |
| 3 | CAMPEON | 2 o más trofeos, o 1 trofeo y `CLUB_DEPORTE` |
| 4 | CEREBRITO | Notas ≥ 85 y 2 o menos amigos de verdad |
| 5 | ESTRELLA | Seguidores ≥ 250 y 2 o menos amigos de verdad |
| 6 | ROMANCE | `parejaFinal() >= 0` y sin `CHISME_ROMANCE` |
| 7 | FAMILIAR | `IRIS_COMPLETA` y buena relación con Lili y la familia |
| 8 | EMPRENDEDOR | dinero ≥ 120 |
| 9 | EQUILIBRADO | `diasEquilibrados() >= 5` |
| 10 | SOLEDAD | `nivelSocial() == 0` y 0 amigos |
| 11 | NORMAL · Diez días después | Todo lo demás |

`amigosDeVerdad()` cuenta las personas con amistad ≥ 60. `ramoPerdido(r)` es `faltoAlFinal(r) || notaRamo(r) < 3.0`. `armarEpilogos()` llena el vector `finEpilogos` con una línea por cada cosa que se cumpla: el romance, Iris y Lili, Mamá, Papá, el rumor, Don Gil, el Club, Chato, la profesora Valdés, el vicio y el final secreto de los animales.

### La evaluación final del comportamiento digital

`finPagina` avanza de 0 a 4 con click o tecla:

| Página | Función | Qué muestra |
| --- | --- | --- |
| 0 | `dibujarFotoFinal` | La foto final con la gente cercana |
| 1 | `dibujarInforme` | El informe «Tus 10 días»: perfil de tiempo, barras por día y categoría, seguidores frente a amigos de verdad, tiempo de pantalla, deuda de sueño, VICIO, días equilibrados, materias y puntaje |
| 2 | `dibujarPaginaFinal` | El final que te tocó |
| 3 | `dibujarEpilogos` | Los epílogos |
| 4 | `dibujarGracias` | «Redemption», el puntaje, los logros y los créditos del Grupo 1 |

`finPagina` se guarda en la partida: cerrar y abrir en el final vuelve a la misma página.

## 15. Archivos: guardar y cargar (bonus)

El juego escribe en la carpeta `partidas` del sketch con `saveStrings` y lee con `loadStrings`. Para leer los archivos no usa `split`, `trim` ni `indexOf`: usa las imitaciones de la sección 3.

### Qué se guarda

| Archivo | Contenido |
| --- | --- |
| `partida1.txt` a `partida3.txt` | Una línea `nombre=valor` por cada variable de la partida (día, hora, mapa, barras, amistades, banderas, chats, diario, eventos, inventario, horario…). La primera línea es `#Redemption=v24`, el formato del archivo |
| `cuenta.txt` | Lo que vale para toda la cuenta: logros con su fecha, récords de minijuegos y de PixelZone, estadísticas, partidas terminadas, mejor puntaje, música, volumen, tamaño de la ventana (`ventana=`) y el límite de 30 FPS (`fps30=`) |
| `puntajes.txt` | Una línea por partida terminada: `fecha;dificultad;puntaje;título;ranura` |

**El código de guardado se genera solo.** Un programa (`guardado.py`) lee todas las variables globales del código y escribe `guardarPartida` y `leerVariable`: cada variable nueva entra sola. Las listas van separadas por un carácter propio y los textos pasan por `escaparTexto` para que un salto de línea o un `=` no rompan el archivo. Lo que no tiene sentido guardar va en la lista `NO_GUARDAR`: las tablas de letras, la ventana, las distancias a casa y los contadores de bloque de 5 minutos, que se recalculan.

### Cuándo se guarda

- **Autoguardado de las 2 a. m.**: `marcaDosAM() = (horagp + 480) / 2880` cambia cada vez que el reloj cruza las 2:00; cuando cambia, se guarda en la ranura actual (si estás en medio de algo, apenas termines).
- Al dormir (`guardarDespuesDeDormir`), desde la pausa (`guardarDesdePausa`, solo si `estadoSeguroGuardar()`), al terminar el juego y al salir con el botón **Salir** de la pausa, que guarda la partida y la cuenta antes de `exit()`.

### Carga y partidas viejas

`cargarPartida(r)` lee cada línea, busca la variable por nombre y le asigna el valor. Las líneas que empiezan con `#` son comentarios, así que un archivo con el encabezado viejo `#DiezDiasEnLaU=v24` también abre. Si un vector del archivo es más corto que el actual (una partida de una versión anterior, antes de agregar personas o eventos), se copia lo que hay y el resto queda con su valor inicial. Una variable que no está en el archivo conserva su valor por defecto, y una línea con una variable que ya no existe se ignora. Antes de leer, `createInput` revisa si el archivo existe.

## 16. Música, ventana y rendimiento

### Música y sonido

Se usa la biblioteca **Sound** de Processing (`SoundFile`). Hay 5 pistas WAV en `data/musica/`, en el vector `PISTAS = {menu, manana, tarde, noche, minijuego}`, más `click.wav`. Cada pista tiene su `SoundFile` en `pistas[]` y su volumen en `pistaVol[]`.

- `cargarPista(i)` carga la pista solo la primera vez que hace falta, y solo si `createInput(ruta)` no es `null`: si falta el archivo, el juego sigue en silencio en vez de fallar.
- `pistaDeseada()` decide cuál suena: inicio y final → menu; rugby, minijuegos y juegos del celular → minijuego; si no, por la hora (5:00–12:00 mañana, 12:00–18:30 tarde, el resto noche).
- `actualizarMusica()` acerca cada `pistaVol[i]` a su volumen objetivo en pasos de `0,02 × pasoCuadro`, así las pistas se mezclan en casi un segundo. El volumen se guarda en `cuenta.txt`.

### Ventana y mouse

El juego dibuja siempre en un lienzo lógico de **1600 × 900** (`ANCHO`, `ALTO`). En cada `draw()` se escala al tamaño real de la ventana y se centra con bandas negras, para que ningún tamaño deforme los dibujos. Como el mouse trabaja en píxeles de ventana, `convertirMouse()` lo pasa al lienzo antes de revisar cualquier click. Los tamaños (`VENTANA_TAMANOS`) son 960 × 540, 1280 × 720, 1366 × 768, 1600 × 900 y 1920 × 1080, solo los que caben en la pantalla.

### Límite de 30 FPS

En Pausa › Ajustes, **Limitar a 30 FPS** cambia `limitar30`. `aplicarFPS()` llama a `frameRate(30)` o `frameRate(60)` y pone `pasoCuadro` en 2 o 1. Se guarda en `cuenta.txt` (`fps30=`). El reloj y los minijuegos nuevos ya usan `millis()`, así que no cambian. Lo que avanzaba una cantidad fija por cuadro se compensa de dos formas:

- **Se repite el paso:** cuando el código es solo lógica, va en un ciclo `for (int pc = 0; pc < pasoCuadro; pc++)`, con resultado idéntico a 60 FPS: caminar, Flappy, Pong, rugby, fútbol y la bala del tiro parabólico.
- **Se multiplica la velocidad por `pasoCuadro`:** la gente que camina, la lluvia, el Pixel Royale, la Torre, los bichos, las notificaciones del insomnio, las barras de penales, el fundido y la música.

### Ahorro de trabajo

En las pruebas, los cuadros «largos» eran los del avance del reloj (cada medio segundo real) y la basura de memoria que dejaba cada cuadro, que obliga a Java a pausar para limpiarla. Se hicieron siete cambios pequeños, sin cambiar lo que pasa en el juego:

| Cambio | Dónde | Por qué |
| --- | --- | --- |
| Contar la agenda una vez | `filaAgendaAhora` | `tamFilas` contaba las filas desde cero en cada vuelta del ciclo |
| Primero el mapa | `dibujarMarcasEventos` | Antes de preguntar si un evento está activo, mira si la persona está en tu mapa, que casi nunca pasa |
| Primero día y hora | `eventoActivo` | Lo barato primero; `bloqueado()` arma un texto y lo busca en la tabla de banderas |
| Mayúsculas primero | `LETRAS_FRECUENTES` | Los nombres de banderas son mayúsculas: de 33 a 19 pasos por letra en promedio |
| Agenda cada 5 min | `tickReloj3` | Todos los horarios van de 5 en 5 minutos |
| Galería cada 5 min o al cambiar de mapa | `tickApps4` | Las fotos de «estar aquí a esta hora» salen apenas entras |
| Logros cada 5 min o si cambia algo que sube y baja | `tickV20` | Que «Junta $100» no se pierda si gastas la plata |

`bloqueCincoMin()` es `(horagp + 2880) / 10`: `horagp` sube 10 cada 5 minutos de juego, y el 2880 evita los números negativos de las 5:30 a. m. del día 1. Medido con 60.000 cuadros simulados, el cuadro del reloj pasó de 2,6 a 1,0 ms, el cuadro normal de 0,089 a 0,054 ms y la basura de 107 a 25 KB por cuadro.

**Memoria recomendada.** Aun con estos cambios, el juego carga cientos de imágenes y miles de textos. Con la memoria por defecto de Processing, Java limpia muy seguido y algunos cuadros se alargan. Por eso el manual de usuario recomienda subirla en Archivo › Preferencias («Increase maximum available memory», 1024 o 2048 MB).

## 17. Pruebas: cómo se verificó

Las pruebas son programas Java que compilan el código convertido de Processing y ejercitan sus funciones sin abrir ventana. Se corren todas después de cada cambio, y la entrega final las pasa todas.

| Prueba | Qué revisa | Resultado |
| --- | --- | --- |
| `PruebaNativas` | Las imitaciones contra las funciones originales de Java con miles de textos al azar y casos límite (vacíos, separadores pegados, `null`, espacios duros) | 10 de 10 |
| `PruebaV26` | Los bloques de 5 minutos, que la agenda no se revise dentro del bloque y sí al empezar el siguiente, la foto del atardecer al entrar al Parque, «Emprendedor» aunque gastes la plata, `eventoActivo` igual al orden viejo en 111.600 casos, `letraEn` correcta con tildes y signos | 18 de 18 |
| `PruebaV25` | El mismo movimiento a 30 y a 60 FPS (caminar, NPC, Flappy, Pong, Royale, rugby), la opción en la cuenta y partidas viejas | 15 de 15 |
| `PruebaV24`, `PruebaV23`, `PruebaV22` | Ventana, guardado y carga (crean estado, guardan, reinician, cargan y comparan), cuenta, logros, récords, música, balance, carteles de minijuegos | 48, 89 y 72 |
| `PruebaV21A/C/D`, `PruebaV20G/H/I/J` | Eventos, escenas, celular, finales y que 74 pantallas se dibujen con sprites sin errores | 25, 23, 28, 24, 16, 28 y 74 |
| `PruebaTeclasDev` | Los 29 minijuegos de personajes arrancan y terminan | 29 de 29 |
| `PruebaCompletista` | Una partida completa que intenta vivir todo: charlas, diarios, eventos, escenas | Sin errores |
| `DbgSalidas` | Todos los mapas, a cada media hora de los 10 días y con $0: siempre hay camino a casa | 0 mapas sin salida |
| Reflexión | Que no queden dos métodos con el mismo nombre (sin sobrecarga) | 0 |

Además, el guion de construcción compila con `javac` el archivo final y revisa que ningún método pase el límite de 64 KB, y que no quede ningún `continue`, ternario ni nativa prohibida.

### Pruebas de equivalencia

Cuando un cambio no debe cambiar nada (quitar los `continue`, reordenar revisiones), se probó que el juego hace exactamente lo mismo: la versión de antes y la de después jugaron las mismas ocho partidas simuladas, con un reloj falso y las mismas teclas y clicks al azar (misma semilla); cuatro de ellas recorren los 10 días, con minijuegos y celular. En cada punto revisado, todas las variables del juego quedaron iguales en las dos versiones.

### Rendimiento

`Perfil` simula 60.000 cuadros (cambios de mapa, caminar, celular, minijuegos) y mide el tiempo de cada cuadro y la memoria que deja. Con él se encontraron los cambios de la sección 16.

### La versión ordenada

`Redemption_ordenado.pde` se arma desde el archivo final cambiando de lugar funciones y variables, sin tocar su texto. Se comprueba que las líneas de código de las dos versiones, ordenadas, coinciden una por una (30.860 líneas), y la versión ordenada también compila y pasa las pruebas.

## 18. Los juegos con pantalla propia: ajedrez, Moderador, ModerIA y parqués

Estos cuatro juegos no usan el motor de minijuegos: cada uno tiene su propio caso en el `switch (screen)` de `dibujarJuego()`, igual que el rugby. Mientras están abiertos no se llama `cicloTiempo()`, así que el reloj, los NPC y el celular se quedan quietos.

| `screen` | Juego | Se abre desde | Prefijo de sus nombres |
| --- | --- | --- | --- |
| 4 | Ajedrez | Las mesas del Parque (`accionDeObjeto("Jugar ajedrez")`) | `aj` / `AJ_` |
| 5 | Moderador | PixelZone, opción 4 de las máquinas (`jugarArcade(3)`) | `td` / `TD_` |
| 6 | ModerIA | Quinto ícono de la primera fila del celular | `ia` / `IA_` |
| 7 | Parqués | La mesa del comedor fuera de las comidas (`mesaFamilia()`) | `pq` / `PQ_` |

Los cuatro siguen el mismo patrón:

1. `iniciarX()` guarda `xDesde = millis()`, pone `cel = 0` y cambia `screen`.
2. En el `draw`, el caso de su `screen` pide el cartel morado (`pedirAvisoMJ`) la primera vez, y luego llama `actualizarX()` y `dibujarX()`.
3. `mousePressed` llama `clickX()`; el ajedrez también usa `mouseReleased` para soltar la pieza arrastrada.
4. `salirX()` corre el reloj con `desplazarTiempos(millis() - xDesde)`, suma el tiempo de la partida con `avanzarTiempo` y da los stats con `aplicarEfectos`. Cada `xDesde` está en `desplazarTiempos()`, así el tiempo que el cartel morado estuvo abierto no se cuenta dos veces.

Las tablas grandes (pesos, niveles, mensajes) se llenan en funciones `datos_…()` y no en la declaración. Java guarda los valores iniciales de las variables globales dentro del constructor, que tiene el mismo límite de 64 KB que cualquier método; con estas tablas declaradas directamente, el juego ya no compilaba.

### Ajedrez: reglas completas y una red de perceptrones

El tablero es `ajTablero[8][8]` (positivo = blancas, negativo = negras) y `ajInfo[7]` guarda el turno, los cuatro enroques y la casilla de captura al paso. Las jugadas se generan en dos pasos: `ajGenerarPseudo` saca las jugadas según cómo se mueve cada pieza y `ajGenerarLegales` se queda con las que no dejan al propio rey en jaque (las prueba en una copia del tablero). Las jugadas se guardan en vectores paralelos (`ajLegF1`, `ajLegC1`, `ajLegF2`, `ajLegC2`, `ajLegPromo`). Se verificó contando todas las posiciones posibles desde el inicio: 20, 400, 8.902 y 197.281 a 1, 2, 3 y 4 jugadas, que son los números oficiales.

El bot no busca en profundidad. Para cada jugada legal:

1. Hace la jugada en una copia (`ajBotB`).
2. Calcula 9 características de la posición (`ajCalcularCaracteristicas`): material, movilidad, centro, avance de peones, protección del rey, desarrollo, amenazas, espacio y peones débiles. Cada una es "blancas menos negras" dividida por un número para que quede cerca de −1 a 1.
3. Pasa esas 9 entradas por una red 9 → 16 → 8 → 1 con activación tanh (`ajCapa`, `ajEvaluar`). La salida va de −1 (ganan negras) a 1 (ganan blancas).

Juega la jugada con mejor salida para su color. Los pesos se entrenaron aparte en Python (carpeta `entrenamiento_ajedrez` del repositorio) con posiciones ya evaluadas por un motor. Hay varios modelos (`AJ_W1S[modelo]`, etc.) y el jugador escoge contra cuál juega; cada modelo se llena en su propia función `datos_AJ_MODELO_n()`. Si nadie gana en 120 medias jugadas, o solo quedan los reyes, son tablas.

### Moderador: niveles en una matriz

Cada nivel es una fila de `TD_NIVELES`:

| Posición | Qué guarda |
| --- | --- |
| \[0\] | 1 si el nivel está desbloqueado |
| \[1\] | Número del fondo (`mapa_N+1.png`) |
| \[2\] | n = cuántos lugares para torres hay |
| siguientes 2n | x, y de cada lugar |
| el resto | Las olas: `-1`, los segundos que dura la ola y después pares (cantidad, enemigo) hasta el siguiente `-1` |

El camino va aparte, en `TD_CAMINOS`: el origen y cada punto de giro. Al empezar el nivel se calcula la distancia acumulada hasta cada punto (`tdCamLargo`), y cada enemigo guarda solo cuánto ha avanzado (`E_AVANCE`); `tdPosicion(avance)` convierte ese número en x, y. Los enemigos vivos están en `tdEne[160][13]` (x, y, vida, velocidad, tipo, avance, estado…). Las torres apuntan al enemigo más adelantado dentro de su alcance.

El Firewall no dispara: pone un muro en el punto del camino más cercano (`tdAvanceMasCercano`), y un enemigo no puede pasar de `tdMuroAvance - 18`, así que se amontonan detrás del muro. Al llegar al nivel 5 cada torre escoge una rama, que le cambia la mecánica (por ejemplo, el rayo aturde o la bomba deja fuego). Los niveles ganados se guardan como banderas (`TD_GANO_n`), así quedan en la partida guardada sin agregar variables.

### ModerIA: una neurona que aprende en vivo

Los 50 mensajes están en `IA_MSJ`: quién lo manda, el texto, 10 rasgos en 0 o 1 (grosería, risa, apodo, daño, gritos, enlace, pide plata o datos, desconocido, amable, se repite) y el tipo de verdad. La neurona no lee el texto: solo ve los 10 rasgos.

Cada neurona calcula `sigmoide(w · x + b)` y aprende con la regla delta cada vez que el jugador etiqueta un mensaje:

```latex
w_i \leftarrow w_i + \eta \, (y - \hat{y}) \, x_i
```

donde η es la tasa de aprendizaje que escoge el jugador (0.05, 0.2 o 0.8), y la etiqueta y es la del jugador, no la verdad. Por eso, si el jugador etiqueta mal, la red aprende mal. El nivel 1 usa una neurona (bueno o malo); el nivel 2 usa cuatro (una por tipo) y gana la más segura. La prueba usa mensajes que la red nunca vio y se califica con el tipo de verdad.

El nivel 3 son perceptrones clásicos con activación escalón (sale 1 si `w1·x1 + w2·x2 + b > 0`) que el jugador configura a mano para armar compuertas Y, O y Y-NO. La compuerta Coordinación recibe la salida de la compuerta Acoso, así que se ve cómo se encadenan.

La ventaja en el juego está en `filtroModeria()`: devuelve 1 + 0.15 por cada nivel ganado y multiplica el tiempo entre notificaciones en el minijuego de estudiar con el celular al lado y en el del insomnio.

### Parqués: el tablero en una tabla y bots de reglas fijas

El camino de la cruz son 28 casillas guardadas en orden en `PQ_CAMINO` (columna, fila). Cada ficha guarda cuánto ha avanzado desde su salida (`pqPos[jugador][ficha]`: −1 cárcel, 0 a 27 camino, 28 y 29 pasillo, 30 meta), y la casilla real es `(jugador × 7 + avance) mod 28`. Los seguros son las casillas 0, 2 y 5 de cada tramo de 7 (`pqSeguro`).

Los bots no usan IA: `pqPuntajeJugada` le pone puntos a cada jugada posible según su personalidad y juegan la de más puntos. Lili suma mucho por comer, Papá suma por quedar en un seguro y resta si queda a 12 casillas o menos de un rival, y la abuela suma por llevar más lejos su ficha. Se probaron 2.000 partidas solo entre bots y todas terminaron.

### Rendimiento

Al medir qué gastaba más tiempo en cada cuadro, salía primero `filaHoja`: cada cuadro, por cada objeto dibujado, volvía a partir el texto de `VISOR_DATOS` ("0;0;4;AFK|1;0;4;…") para saber qué fila de la hoja usar. Ahora `prepararFilasHojas()` lo parte una sola vez y guarda los números en `visFilas[hoja][fila]`; se comprobó que da exactamente lo mismo en las 719 combinaciones. Lo mismo con la narración: el texto sin corchetes se calcula una vez por texto y no en cada cuadro.
