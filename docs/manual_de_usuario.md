# Redemption · Manual de usuario

*Redemption* es un juego de simulación de vida sobre el uso saludable del tiempo y de las redes sociales. Este manual explica cómo instalarlo, cómo se juega y qué hace cada parte, para que cualquier persona lo pueda jugar sin ayuda.

|  |  |
| --- | --- |
| Juego | Redemption |
| Laboratorio | Digital Balance · Laboratorio único |
| Asignatura | Algoritmia y Programación II · NRC 2385 |
| Profesora | Rocío Ramos Rodríguez |
| Monitora | Angélica Baños |
| Equipo | Grupo 1 |
| Integrantes | Adrián Camilo Cáceres Figueroa · Sebastián Pertuz Sánchez · Eduardo Javier Tamara Otero · Daniel Steven Molina Gómez |
| Entrega | Entrega 3 · 13 de noviembre de 2026 · semestre 2026-30 |

Los recuadros que dicen **\[Espacio para foto\]** marcan dónde va una captura del juego.

## 1. Cómo jugar

Eres un estudiante de primer semestre y tienes **diez días** para llegar bien a los parciales del día 10 sin descuidar el sueño, el ejercicio, tus amigos, tu familia ni tu salud digital. Ganas cuando terminas con tu vida en equilibrio: no se puede hacer todo, así que cada hora es una decisión.

### Paso 1. Abre el juego

Abre `Redemption.pde` en Processing 4 y dale ▶ (Ejecutar). Si es la primera vez, mira la sección 2: hay que instalar la biblioteca **Sound** y se recomienda subir la memoria de Processing.

> **\[Espacio para foto 1\]** Pantalla de inicio: el cuarto, el logo de Redemption arriba y el botón JUGAR.

### Paso 2. Elige la dificultad y empieza

En la pantalla de inicio elige la dificultad abajo en el centro (Fácil, Normal o Difícil) y haz click en **JUGAR**. El juego pregunta en cuál de los 3 espacios guardar la partida. Si es tu primera vez, elige **Fácil**: el reloj va más despacio.

> **\[Espacio para foto 2\]** El menú de partidas con los 3 espacios para guardar.

### Paso 3. Mira la escena y el tutorial

La historia empieza un lunes a las 5:30 a. m. con la alarma. Pasa las líneas con **ESPACIO**, **ENTER**, **E** o click. Después sale el tutorial; lo vuelves a abrir cuando quieras con **F1**.

### Paso 4. Apéndete los controles básicos

| Para | Usa |
| --- | --- |
| Caminar | A / D o ← / → (SHIFT para correr) |
| Usar puertas, la cama, el paradero, tiendas | E |
| Hablar con alguien | R |
| Elegir una respuesta | 1 a 5 o click |
| Abrir el celular | Click en el botón de abajo a la izquierda |
| Pausa | ESC o P |

### Paso 5. Lee la pantalla

> **\[Espacio para foto 3\]** El mundo con el personaje en su cuarto: el día, la hora y la plata arriba a la izquierda, las barras debajo, el cuadro AHORA arriba a la derecha y el celular abajo a la izquierda.

- **Arriba a la izquierda:** el día, la hora, tu plata, el lugar donde estás y tus barras (Social, Notas, Energía, Dinero, Seguidores y Pantalla).
- **Arriba a la derecha:** el cuadro **AHORA** dice lo más importante que tienes que hacer en este momento.
- **Encima del personaje:** lo que tienes cerca y la tecla para usarlo, por ejemplo «\[E\] Puerta» o «\[R\] Hablar con Sofía».
- **Un «!» sobre una persona:** tiene algo importante para ti (un evento).

### Paso 6. Tu primer día

1. Sal de tu cuarto caminando hacia la derecha y baja hasta el **frente del edificio**.
2. En el **paradero**, presiona **E** y toma el bus a la U ($1, 30 minutos). Física empieza a las 7:00.
3. En la U, pasa los torniquetes, sube al **Aula 201** y usa los **pupitres** con **E**: empieza la clase y su minijuego.
4. A las 9:00 tienes Cálculo en el **Aula 305**. Después tienes la tarde libre: almuerza, habla con la gente, haz ejercicio o trabaja.
5. Vuelve a la casa, come con tu familia en la **mesa del comedor** (cena de 7:00 a 9:30 p. m.) y acuéstate en tu **cama** con **E** antes de la medianoche.

> **\[Espacio para foto 4\]** Una clase: el minijuego de tiro parabólico de Física.

### Paso 7. Usa el celular con cuidado

El celular es el **mundo digital**: WhatsApp, la red social Aurora+, tus fotos y tus juegos. Mientras está abierto, el reloj corre **3 veces más rápido** y todo cuenta como tiempo de pantalla. Contesta los mensajes importantes y ciérralo.

> **\[Espacio para foto 5\]** El celular abierto en la pantalla de inicio con sus apps.

### Paso 8. Equilibra tu día

Todo lo que haces gasta tiempo en una de cinco categorías: **Estudiar, Dormir, Ejercicio, Amigos y familia, y Redes**. Cada una tiene un rango sano por día (sección 5). Un día con 4 o 5 categorías en su rango cuenta como **equilibrado** y te da energía y social extra al día siguiente. En el celular, **Ajustes › Bienestar digital** te dice cómo vas.

### Paso 9. Guarda

El juego guarda solo cada noche a las 2:00 a. m. También puedes guardar en la pausa (**ESC**) con el botón **Guardar partida**. El botón **Salir** cierra el juego.

### Paso 10. Llega al día 10

El día 10 son los parciales: Física a las 7:00, Cálculo a las 9:00 y Álgebra a las 11:00. En la noche es la Feria Aurora en el patio de la U. Al final ves tu **evaluación del comportamiento digital**, tu puntaje y uno de los once finales posibles.

> **\[Espacio para foto 6\]** La pantalla de resultados del final con las barras de cada categoría.

## 2. Instalar y abrir el juego

El juego corre en **Processing 4** (modo Java) en Windows, macOS o Linux. Solo necesita la biblioteca **Sound** para la música.

### Lo que necesitas

| Qué | Dónde se consigue |
| --- | --- |
| Processing 4 | processing.org › Download |
| Biblioteca Sound | En Processing: Sketch › Importar biblioteca › Gestionar bibliotecas › buscar «Sound» › Install |
| La carpeta del juego | `Redemption`, con `Redemption.pde` y la carpeta `data` adentro |

### Abrir el juego

1. Copia la carpeta `Redemption` completa a tu carpeta de sketches (en Windows suele ser `Documentos\Processing`). El nombre de la carpeta y el del archivo `.pde` tienen que ser iguales: Processing no abre un sketch si no coinciden.
2. Abre `Redemption.pde` con Processing 4.
3. Dale ▶ (Ejecutar). La primera vez tarda unos segundos en compilar.

La carpeta `data` tiene las imágenes, la música y los dibujos de los minijuegos. Tiene que estar al lado del `.pde`. Si falta alguna imagen, el juego no se cae: dibuja un reemplazo sencillo. La carpeta `partidas` se crea sola la primera vez que guardas.

> **\[Espacio para foto 7\]** La carpeta Redemption abierta: Redemption.pde, data y partidas.

### Recomendado: subir la memoria del juego

Redemption es un juego grande: carga cientos de imágenes y tiene miles de líneas de diálogo. Con la memoria que Processing trae por defecto, Java tiene que limpiar la memoria muy seguido, y eso se nota como cuadros que se alargan o pequeñas trabas. Se recomienda subirla antes de jugar:

1. En Processing, abre **Archivo › Preferencias**.
2. Marca la casilla **«Increase maximum available memory»** (en español, **«Aumentar memoria máxima disponible»**).
3. Escribe **1024** MB. Si tu computador tiene 8 GB de RAM o más, puedes poner **2048**.
4. Dale **OK** y vuelve a ejecutar el juego.

Si después de cambiarla sale el error *«Could not run the sketch (Target VM failed to initialize)»*, pediste más memoria de la que tu computador puede dar: baja el número (por ejemplo a 1024) y prueba otra vez.

> **\[Espacio para foto 8\]** La ventana de Preferencias de Processing con la casilla de la memoria marcada.

Si el juego sigue trabándose, en la pausa está la opción **Limitar a 30 FPS** (sección 16).

## 3. La historia y los dos mundos

Redemption trata la **gestión del tiempo en redes sociales** (subtema 3.1 del laboratorio Digital Balance) y toca también la huella digital, el uso excesivo del celular, la seguridad en los mensajes, la ciudadanía digital y el bienestar digital.

### La historia

Eres un estudiante de primer semestre de la Universidad Santa Aurora. Vives con tu mamá Claudia, tu papá Ernesto y tu hermana menor Lili; la Abuela Nena llega el fin de semana. La historia empieza un lunes a las 5:30 a. m.: Física es a las 7:00 con el profe Mendoza y el bus sale del paradero de la esquina.

En diez días conoces compañeros, profesores y gente de la ciudad. Puedes entrar a la Copa Aurora, trabajar en la Plaza, ir a la fiesta de Marta, ayudar a tu familia o pasar la noche en el celular. Al final de cada día el juego mira cómo repartiste el tiempo, y el día 10 te evalúa.

### Los dos mundos

|  | El mundo real | El mundo digital |
| --- | --- | --- |
| Qué es | La casa, la universidad, la Plaza, el parque, el complejo de deportes y la calle | El celular: WhatsApp, Aurora+, la Galería, el Diario, los juegos y más |
| Cómo se entra | Caminando y con E en puertas y paraderos | Con el botón del celular, abajo a la izquierda |
| El reloj | Corre normal | Corre 3 veces más rápido |
| Lo que cuenta | Estudiar, dormir, ejercicio y amigos | Redes y tiempo de pantalla |
| Las decisiones | Ir a clase, a quién ayudas, a dónde vas | Qué publicas, a quién contestas, qué crees, a quién dejas en visto |

Los dos mundos están conectados: una foto que subes cambia lo que la gente te dice en persona, y una noche en el celular te deja sin energía para la clase.

> **\[Espacio para foto 9\]** Lado a lado: el patio de la U (mundo real) y el chat de WhatsApp (mundo digital).

### Las dos fases

| Fase | Días | De qué se trata |
| --- | --- | --- |
| Fase 1 · Gestión y decisiones | 1 a 5 (lunes a viernes) | Aprendes la rutina: clases, transporte, horarios, trabajos y las primeras decisiones en redes, como aceptar a tu mamá en Aurora+, qué subir de la fiesta del viernes y reconocer mensajes trampa. |
| Fase 2 · Situaciones avanzadas | 6 a 10 (fin de semana y semana de parciales) | Vienen los problemas difíciles: el rumor del parcial filtrado (día 8), lo que dicen de Iris en los grupos (ciberacoso), las finales de la Copa, las deudas, los parciales del día 10 y la evaluación final. |

## 4. Controles

Todo se juega con teclado y mouse. Las teclas que no sirven en un momento se ignoran, así que no hay forma de dañar nada apretando de más.

| Tecla o mouse | Qué hace |
| --- | --- |
| A / D o ← / → | Caminar a la izquierda o a la derecha |
| SHIFT (sostenido) | Correr |
| E | Usar lo que tienes al frente: puertas, paraderos, objetos, tiendas, la cama, el escritorio, la mesa |
| R | Hablar con la persona que tienes cerca; en un diálogo, pasar a la siguiente línea |
| 1 a 5 | Elegir una respuesta en un diálogo, una opción de un menú o un producto en una tienda |
| ESPACIO, ENTER o E | Pasar las escenas y cerrar el cartel que explica cada minijuego |
| TAB o T | Abrir y cerrar el inventario |
| Q o BORRAR | Cerrar una ventana o salir de una actividad |
| ESC o P | Pausa: el reloj se queda quieto |
| F1 | Tutorial |
| Click en el celular (abajo a la izquierda) | Abrir el celular y usar sus apps |
| Rueda del mouse | Subir y bajar en los chats, Aurora+, el inventario y las listas |
| Mouse | Botones de los menús y casi todos los minijuegos |

Encima del personaje sale siempre lo que tienes cerca y la tecla para usarlo, por ejemplo **\[E\] Paradero** o **\[R\] Hablar con Laura**. Si un lugar está cerrado, dice «· cerrado». Un **•** al lado del nombre de una persona quiere decir que tiene algo nuevo que contarte.

Cada minijuego explica sus controles en un cartel antes de empezar. Los más usados son:

| En | Controles |
| --- | --- |
| Rugby y fútbol | W A S D o flechas para moverte, click para pasar o tacklear |
| Juegos de ritmo | Las flechas (o A S D, o D F J K) cuando la nota pasa por la línea |
| Gimnasio y natación | ESPACIO y las flechas en el momento justo |
| Trabajos (helados, flores, café) | Click en los botones de la derecha y en ENTREGAR |
| Wordle | Escribir letras, ENTER para probar la palabra, BORRAR para corregir |

> **\[Espacio para foto 10\]** El aviso «\[E\] Paradero» sobre el personaje en el frente del edificio.

## 5. La pantalla y los indicadores

Arriba a la izquierda están el día, la hora, tu plata y el lugar; debajo, seis barras. Arriba a la derecha, el cuadro **AHORA**. Abajo a la izquierda, el botón del celular, que late cuando tienes algo sin leer.

> **\[Espacio para foto 11\]** Acercamiento a las barras de la esquina superior izquierda.

### Las seis barras

| Barra | Qué mide | Qué la sube o la baja |
| --- | --- | --- |
| Social (0–100) | Qué tan conectado estás con la gente. Al lado sale tu nivel: Perdedor, Reservado, Normal, Carismático o Popular | Hablar, planes y eventos la suben; dejar en visto y quedar mal la bajan |
| Notas (0–100) | Tu rendimiento en la U | Ir a clase, los minijuegos de clase, estudiar y las tutorías la suben; faltar la baja |
| Energía | Cuánto aguantas | Dormir y comer la suben; casi todo la gasta. Sin energía rindes menos |
| Dinero | Tu plata | Los trabajos y la Copa la suben; el bus, la comida y las tiendas cuestan |
| Seguidores | Tu alcance en Aurora+ | Publicar y que te reaccionen |
| Pantalla | Tu tiempo con el celular hoy | Cada minuto con el celular abierto suma |

### Las cinco categorías del día

Todo lo que haces gasta tiempo en una de estas categorías. Al terminar el día el juego revisa si cada una quedó en su rango sano:

| Categoría | Rango sano por día |
| --- | --- |
| Estudiar | 4 a 6 horas (días 6 y 7: 2 a 3 horas) |
| Dormir | 7 a 9 horas |
| Ejercicio | 1 a 3 horas |
| Amigos y familia | 2 a 4 horas |
| Redes | 30 minutos a 2 horas |

Con 4 categorías en su rango, el día cuenta como **equilibrado**: al otro día tienes +10 de energía y +2 de social. Con las 5, además, tus amistades fuertes (60 o más) suben un punto. En el celular, **Ajustes › Bienestar digital** muestra cuánto llevas hoy en cada una.

### Lo que no se ve en las barras

- **VICIO:** sube si aceptas el cigarro de la esquina. Cada punto quita 40 al puntaje final y te hace 6 % más lento en los deportes. Un día entero sin la esquina lo baja en 1, si decides dejarlo.
- **Estrés:** aparece si pierdes un partido de la Copa, debes mucho sueño, tus notas bajan de 40, te peleas con tu mamá o el rumor del día 8 no se aclara. Con estrés, Chato te busca en la esquina.
- **Deuda de sueño:** sube cada noche que pasas la 1:00 a. m. sin dormir. Con deuda baja tu energía máxima, y con mucha te duermes en clase o en el bus.
- **Reputación:** lo que publicas y lo que apoyas en Aurora+ queda en tu historia. Lo tóxico da más likes, pero la gente lo recuerda.

## 6. El tiempo y el sueño

El reloj nunca se detiene, salvo en la pausa y mientras lees el cartel de un minijuego. Cada cosa que haces gasta minutos y los suma a una de las cinco categorías.

| Dificultad | 1 hora del juego dura | Con el celular abierto |
| --- | --- | --- |
| Fácil | 3 minutos reales | 1 minuto |
| Normal | 1 minuto y medio | 30 segundos |
| Difícil | 1 minuto | 20 segundos |

- **El celular:** mientras está abierto, el tiempo corre 3 veces más rápido. Revisar «cinco minutos» se vuelve media hora.
- **Comiendo o en un evento:** el reloj va al doble de lento, para que alcances a leer.
- **Viajar:** caminar entre lugares cercanos toma de 1 a 3 minutos; el bus, de 10 a 30; las caminatas largas, hasta hora y media.
- **Comer en casa:** en la mesa del comedor, con **E**. El desayuno es de **6:00 a 8:30 a. m.** y la cena de **7:00 a 9:30 p. m.**; fuera de esas horas la mesa está vacía y el juego te dice los horarios. Comer toma 30 minutos, sube la energía y cuenta como tiempo con la familia. Los lunes (días 1 y 8) el desayuno trae la mesada de tu papá.
- **El cambio de día:** el día nuevo empieza a las 5:00 a. m. Si no duermes, igual cambia.

### Dormir

En tu cuarto, usa la cama con **E**. Antes de dormirte sale el minijuego de las notificaciones: el celular no te deja dormir (sección 12).

- Duermes hasta la alarma, con un máximo de 10 horas y un mínimo de 1.
- La alarma suena a las 6:00. La cambias en **Ajustes** del celular, de 4:00 a 10:00. Los días 5 y 6 suena a las 10:00.
- Cada notificación que se te pasa en la cama te quita 30 minutos de sueño.
- Al despertar, tu energía queda en 20 + 10 por cada hora dormida.
- Si duermes 8 horas o más abriendo una notificación o ninguna, ganas el logro **Buen dormir**.
- El modo **No molestar** del celular hace más fácil quedarse dormido.

> **\[Espacio para foto 12\]** El minijuego de las notificaciones en la cama.

### La deuda de sueño

| Deuda | Qué pasa |
| --- | --- |
| 1 o más | Tu energía máxima baja a 70 |
| 2 o más | Tu energía máxima baja a 50 y te da estrés |
| 3 o más | Te duermes en clase (la clase no suma) y en el bus te puedes pasar de parada |

Dormir 7 horas o más baja la deuda en 1; dormir 10 horas, en 2.

## 7. Moverse por la ciudad

La ciudad tiene 59 lugares en 7 zonas. Para pasar de uno a otro caminas hasta el borde de la pantalla o usas con **E** una puerta, un arco, una escalera o un paradero. Si hay varias formas de ir, sale un menú para elegir. Arriba sale el lugar al que llegaste y cuánto tiempo tomó, por ejemplo «U3 · Patio central (+5 min)».

| Zona | Lugares | Cómo se llega |
| --- | --- | --- |
| Casa | Frente del edificio, pasillo, sala, cocina y comedor, tu cuarto, pasillo del cuarto de Lili, patio de ropas | Es donde empiezas. El paradero está en el frente del edificio |
| Calles | Paradero de la U, calle hacia la Plaza, puente peatonal, paradero del Parque, Terminal de buses, Andén de la esquina | Bus, taxi o a pie desde la casa |
| Universidad | Portería, escaleras, patio central, pasillos, Aula 201 (Física), Laboratorio, Aula 305 (Cálculo), Aula 104 (Álgebra), Sala de cómputo 2, Biblioteca, Cantina, Útiles Aurora, Enfermería, Jardines, Kiosco de café | Por los torniquetes de la portería (Paradero de la U). En el patio central, cada puerta lleva a la Biblioteca, la Enfermería, Útiles Aurora y la Cantina |
| Plaza (centro comercial) | Entrada, puesto de flores, atrio, Grano Café, PixelZone, Rosa Moda, Heladería | Bus o taxi hasta la Plaza, o a pie |
| Parque | Entrada, fuente, cerezo, bancas, sendero de trote, pradera, zona del pintor, ajedrez; el día 6, el mercadito | Paradero del Parque |
| Deportes | Canchas de fútbol y rugby, gradas, pista, gimnasio, vestuarios, piscina | Por el pasillo techado desde el Kiosco de la U |
| Fuera de la U | Esquina, Bar La Esquina, Tienda La Esquinita, empanadas, terraza de Marta (fiesta del día 5) | Por la salida con arco de rosas de los Jardines, o por la calle desde el Paradero de la U |

> **\[Espacio para foto 13\]** El patio central de la U con las puertas de la Biblioteca, la Enfermería, Útiles y la Cantina.

### Transporte

| Medio | Precio | Horario | Nota |
| --- | --- | --- | --- |
| A pie | Gratis | Siempre | Entre zonas tarda: casa–Parque 50 min, casa–Plaza 70 min, casa–U 90 min |
| Bus | $1 | 5:00 a 23:00 | De 10 a 30 minutos. Con mucha deuda de sueño te puedes dormir y pasarte |
| Taxi de Don Beto | $8 | Siempre | El más rápido: de 10 a 15 minutos |
| Bus de la Terminal | $2 | Siempre | Desde la Terminal de buses |

Si no te alcanza la plata, el juego te dice cuánto necesitas y no te cobra. Algunos días el bus va lleno y tarda 8 minutos más.

### Horarios de los lugares

| Lugar | Abre |
| --- | --- |
| Universidad | Días 1–5 y 8–10 de 6:40 a 19:00; día 6 de 6:40 a 12:00; día 7 cerrada |
| Plaza: atrio y Grano Café | 6:00 a 21:00 (el Grano, el día 7 hasta las 23:00) |
| Plaza: puesto de flores | 9:00 a 18:00 |
| Plaza: Rosa Moda / Heladería / PixelZone | 10:00–21:00 / 11:00–21:00 / 12:00–22:00 |
| Deportes | 6:00 a 21:00 |
| Bar La Esquina | 18:00 a 2:00 |
| Tienda La Esquinita / empanadas | 6:00–23:00 / 17:00–23:00 |
| Mercadito del parque | Solo el día 6, de 8:00 a 14:00 |

### Nunca te quedas encerrado

Un lugar cerrado no te deja entrar, pero siempre te deja salir hacia tu casa. Si se te pasa la hora en el Grano Café, puedes cruzar el centro comercial cerrado hasta la calle; si sales tarde del gimnasio, cruzas los Jardines de la U hasta la calle. Al pasar por un lugar cerrado sale el aviso «ya cerró: puedes pasar, pero solo hacia la salida», y no puedes volver a entrar hasta que abra. Desde cualquier paradero puedes volver a pie, aunque no tengas plata.

## 8. Hablar con la gente

Acércate a alguien y presiona **R**. La persona dice lo que tiene para ese día y a veces te da opciones: elígelas con **1 a 5** o con el mouse. Cada respuesta tiene consecuencias, y la persona reacciona a lo que elegiste.

> **\[Espacio para foto 14\]** Un diálogo con opciones de respuesta y el retrato de la persona.

- **Amistad (0 a 100):** cada persona tiene la suya y empieza en 40. Sube con buenas respuestas, planes cumplidos, regalos y eventos; baja si la dejas en visto, la plantas o la tratas mal. Con 60 o más es una amistad de verdad. En el celular, la app **Relaciones** dibuja tu círculo: una línea gruesa es una amistad fuerte y una roja, una amistad que se está perdiendo.
- **La gente se acuerda:** si fuiste a la fiesta, si llegaste a tiempo, si contestaste, si hoy fuiste al gimnasio o llevas dos noches sin dormir. Alguien con quien quedaste muy mal te puede evitar o bloquear.
- **Charla del día:** cada día hay algo nuevo que hablar. Con las personas que ves seguido salen conversaciones especiales cuando la amistad sube a 60 y a 80, o si se cae.
- **El número:** algunas personas te dan su número cuando ya se conocen. Desde ahí te escriben por WhatsApp y te invitan a planes.
- **Regalos:** con **TAB** abres el inventario y puedes regalar lo que compraste. A cada persona le gustan cosas distintas.
- **Romance:** con Sofía, Laura, Marta, Nadia o Valentina la amistad puede pasar a coqueteo, cita y pareja. Si coqueteas con dos a la vez, al día siguiente sale el chisme en «Confesiones Aurora»: las dos rutas se cierran y la amistad con ambas baja 30.

### Las personas principales

| Grupo | Quiénes |
| --- | --- |
| Familia | Mamá (Claudia), Papá (Ernesto), Lili (tu hermana), Abuela Nena |
| Compañeros de la U | Sofía, Laura, Marta, Camilo, Andrés, Nadia, Kevin, Julián, Bruno |
| Gente de la ciudad | Iris (la amiga de Lili), Valentina (Grano Café), Paola (heladería), Nico (kiosco de café), Doña Inés (flores), Doña Cecilia (Cantina), Don Gil, Chato y Lucho (la esquina) |
| Profesores | Prof. Mendoza (Física), Prof. Ramírez (Cálculo), Prof. Salazar (Álgebra), Profa. Valdés (Programación), Prof. Núñez |
| Entrenadores | Rojas, Paz, Ochoa y Bermúdez «Tanque» |
| Animales | Newton, Canela y Tuerca (se pueden acariciar con E) |

## 9. El celular (el mundo digital)

El botón está abajo a la izquierda. Una burbuja roja avisa que tienes algo sin leer. Mientras el celular está abierto el personaje no se mueve, el tiempo corre 3 veces más rápido y todo cuenta como tiempo de **Redes** y de **Pantalla**. Para cerrarlo, vuelve a hacer click en el botón.

> **\[Espacio para foto 15\]** La pantalla de inicio del celular con todas las apps.

| App | Para qué sirve |
| --- | --- |
| WhatsApp | Chats con la gente y los grupos (salón, familia, club, Los del Fondo). Abajo está la barra «Responder a…»: al tocarla salen las respuestas posibles. Hay notas de voz y el «está escribiendo…». A cada persona le puedes escribir tú una vez por día. |
| Planes por chat | Dentro de un chat, **Proponer plan**: eliges lugar y hora. La persona acepta según la amistad y lo que tenga que hacer; el plan queda en tu Horario. Llegar sube la amistad; plantarla o cancelar la baja. La gente también te invita. |
| Aurora+ | La red social. Ves una publicación a la vez y eliges Me gusta, No me gusta o Pasar. Lo que publican los demás depende de lo que ha pasado. Puedes subir tus fotos: lo que publicas cambia tus seguidores y lo que la gente piensa de ti. |
| Galería | Las fotos que desbloqueas al estar en ciertos lugares y momentos. Desde aquí se suben a Aurora+ con el editor: filtro, recorte, pie de foto y etiquetas. |
| Horario | Tus clases, los parciales y los planes que aceptaste, día por día. |
| Ajustes | Alarma (4:00 a 10:00), **No molestar** (menos notificaciones de noche) y **Bienestar digital**: cuánto llevas hoy en cada categoría frente a su rango sano. |
| Pedidazo | Pedir cosas a la casa: comida, regalos y decoraciones para tu cuarto. Llegan al otro día desde las 7:00. |
| Diario | Lo que pasó cada día, escrito solo. |
| Relaciones | El mapa de tu círculo y qué tan fuerte es cada amistad. |
| Logros | Los 34 logros y cuáles tienes. |
| Notas | Lo pendiente: los parciales, las deudas y las pistas para los exámenes. |
| Mapa | La ciudad y dónde estás. Tu mamá te pide compartir la ubicación. |
| Playlist | Tres listas: para estudiar (Notas +1), para entrenar (Energía +4) y para calmarte (Energía +2, Social +1). Al tocar una, se corta la música que suena y empieza esa lista, que dura 3 horas del juego. La música se puede cambiar cuando quieras, pero el efecto solo se gana una vez cada 3 horas. El botón de abajo quita la lista y vuelve la música del lugar. Normalmente, cada zona tiene su propio tema (paraderos, calles, la U, la Plaza, el Parque, Deportes y Fuera de la U); dentro de la casa la música cambia según la hora. |
| Batería | Se gasta con el celular abierto y se carga en tu casa y mientras duermes. Si llega a 0 %, el celular se apaga. |
| Wordle, Flappy y Pong | Juegos del celular (sección 12). Divertidos, pero cuentan como tiempo de redes. |
| ModerIA | Entrenas una IA para moderar mensajes (sección 12). Cada nivel que ganes entrena el filtro de tu celular: menos notificaciones al estudiar y al intentar dormir. |

> **\[Espacio para foto 16\]** Un chat de WhatsApp con la barra «Responder a…» abierta.

> **\[Espacio para foto 17\]** Una publicación en Aurora+ con los botones Me gusta, No me gusta y Pasar.

**Llamadas:** tu mamá y otras personas te llaman. Si estás en clase, contestar tiene costo con el profesor; no contestar también tiene costo con quien llama.

### Cuidado con

- **Dejar en visto:** leer un mensaje y no contestar baja la amistad, y te lo reclaman en persona.
- **Notificaciones de noche:** en la cama, cada una que se te pasa te quita sueño.
- **Lo que publicas:** una foto polémica o un pie de foto exagerado da más likes, pero baja tu Social y deja mala reputación. Etiquetar a alguien en una foto que no le gusta le duele.
- **Mensajes trampa:** hay mensajes que piden datos, prometen premios o traen links raros. El minijuego «¿Confiable o trampa?» enseña a reconocerlos.
- **Chismes:** compartir un chisme sube seguidores y baja tu Social. El rumor del día 8 se puede investigar y aclarar.

## 10. Clases y parciales

Para tomar una clase llega a su salón a la hora y usa los pupitres (o los computadores) con **E**. Cada clase es un minijuego corto: lo bien que te vaya da las notas de esa clase. Después el reloj salta hasta el final de la clase y ese tiempo cuenta como **Estudiar**.

| Día | 7:00 a 9:00 | 9:00 a 11:00 |
| --- | --- | --- |
| 1 | Física (Aula 201, Prof. Mendoza) | Cálculo (Aula 305, Prof. Ramírez) |
| 2 | Álgebra (Aula 104, Prof. Salazar) | Programación (Sala de cómputo 2, Profa. Valdés) |
| 3 | Física | Cálculo |
| 4 | Álgebra | Programación |
| 5 | Laboratorio de Física (Laboratorio) | Programación (entrega) |
| 6 y 7 | Sin clases | Sin clases |
| 8 | Física (repaso) | Cálculo (repaso) |
| 9 | Álgebra (repaso) | Programación (entrega final) |
| 10 | **PARCIAL de Física** | **PARCIAL de Cálculo**; a las 11:00, **PARCIAL de Álgebra** |

### El minijuego de cada clase

| Clase | Minijuego | Cómo se juega |
| --- | --- | --- |
| Física | Tiro parabólico | Ajusta el ángulo (↑ ↓) y la fuerza (← →) y dispara con ESPACIO. Tienes 3 tiros; desde el día 3 hay viento y después el blanco se mueve. |
| Laboratorio de Física | El péndulo | Presiona ESPACIO justo cuando el péndulo pase por la franja verde del centro. |
| Cálculo | Todas las que puedas (15 s) | Responde con 1–4 o click todas las preguntas que puedas. Si aciertas seguido se ponen difíciles; si fallas, vuelven las fáciles. |
| Álgebra | La balanza | Elige el valor de x que equilibra la balanza (1–4 o click). Son varias rondas. |
| Programación | Cazabichos | Haz click en las mariquitas que salen sobre el código. El café, el check verde, las llaves { } y el cursor NO son bichos. |

> **\[Espacio para foto 18\]** El minijuego de la balanza de Álgebra.

### Reglas de las clases

- **Llegar tarde:** tienes 15 minutos de gracia. Después entras al fondo y la clase da la mitad de las notas.
- **Dormirte en clase:** con mucha deuda de sueño o menos de 15 de energía te duermes y la clase no suma.
- **Faltar:** la clase se pierde, las notas bajan y tus compañeros lo comentan. El día 1 el profe de Física llama a lista.
- **Contestar el celular en clase:** el profesor lo nota y bajan tus notas.
- **Los parciales (día 10)** tienen dos partes seguidas: Física = tiro parabólico + péndulo; Cálculo = todas las que puedas + pendiente rápida (decir si la recta sube, baja o es plana); Álgebra = la balanza dos veces. Valen el doble que una clase normal.
- **La nota de cada materia** va de 0,0 a 5,0 y se pasa con 3,0. Sale de tus Notas y de lo que sacaste en cada clase de esa materia. Si faltas al parcial (o a la entrega final de Programación), pierdes la materia.
- **Con dos materias perdidas** el final es «No te graduaste».
- **Estudiar por fuera:** en el escritorio de tu cuarto o en la mesa de la Biblioteca (rinde 1,5 veces más). Laura da tutorías, y la app Notas guarda las pistas para los parciales.

## 11. Deportes, la Copa Aurora y el gimnasio

El complejo de Deportes abre de 6:00 a 21:00 y se llega por el pasillo techado del Kiosco de la U. Todo lo que hagas aquí cuenta como **Ejercicio** y gasta energía. Con VICIO eres más lento.

### La Copa Aurora

Te inscribes desde el mensaje de Alertas del celular (o entrando al club de rugby). Cada partido es un minijuego: llega al lugar entre media hora antes y una hora después. Si pierdes uno, quedas eliminado de ese deporte. Ganar da plata, +3 de Social y +10 seguidores; ganar los tres partidos de un deporte da su trofeo.

| Día y hora | Deporte | Ronda | Rival | Premio |
| --- | --- | --- | --- | --- |
| 4 · 15:00 | Rugby | Cuartos | Ingeniería B | $8 |
| 5 · 15:00 | Fútbol | Cuartos | Arquitectura | $8 |
| 6 · 10:00 | Natación | Cuartos | Biología | $8 |
| 6 · 16:00 | Rugby | Semifinal | Derecho | $12 |
| 7 · 10:00 | Fútbol | Semifinal | Economía | $12 |
| 7 · 16:00 | Natación | Semifinal | Medicina | $12 |
| 8 · 15:00 | Rugby | Final | Los Roca (Medicina) | $25 |
| 9 · 15:00 | Fútbol | Final | Ingeniería A | $25 |
| 9 · 17:00 | Natación | Final | Nadia (la campeona) | $25 |

> **\[Espacio para foto 19\]** Un partido de rugby de la Copa.

### Los juegos de cada lugar

| Lugar (usar con E) | Juego | Cómo se juega |
| --- | --- | --- |
| Cancha de rugby | Rugby (práctica o partido) | W A S D para moverte. Con el balón, click para pasarlo; sin el balón, click para tacklear. Lleva el balón a la zona del rival. Gana el primero a 5. |
| Cancha de fútbol | Picado 3 contra 3 | W A S D o flechas, SHIFT corre, Q / E dan efecto. Click en un punto para pasar (en el arco es tiro; mantén para más fuerza). Sin el balón, click para barrer. Gana el primero a 3 goles; si empatan, penales. |
| Arco de la cancha de fútbol | Penales y pases | Click en la zona del arco y ESPACIO para la fuerza; después, ESPACIO cuando la marca pase por tu compañero. |
| Piscina (trampolín) | Natación por tramos | 100 m que cambian de estilo: CROL (← → alternando), PECHO (repite las flechas), ESPALDA (la flecha que sale; si es roja, la contraria). ESPACIO para respirar y en la pared para el viraje. |
| Pista de atletismo (bicicleta) | Ciclismo | ↑ ↓ cambian de carril, → pedalea más fuerte, ← frena. Esquiva conos, palomas y ciclistas lentos. |
| Gimnasio · Caminadora | Caminadora | Alterna ← → y mantén la velocidad en la franja verde. |
| Gimnasio · Barra | Press con equilibrio | Machaca ESPACIO para subir y centra la aguja con ← →; arriba, aguanta 1 segundo centrado. |
| Gimnasio · Mancuernas | Mancuernas dobles | ← (brazo izquierdo) y → (brazo derecho) cuando cada marca esté en su zona verde. |
| Gimnasio (con el Tanque) | Repeticiones | ESPACIO cuando la marca esté en lo verde; cada vez va más rápido. |

En los vestuarios te cambias y te bañas. Los entrenadores Rojas, Ochoa, Paz y el Tanque te invitan al **Club del Deporte**, que tiene sus propias sesiones (sección 13).

## 12. Los minijuegos

Antes de cada minijuego sale un cartel que explica cómo se juega y sus controles; se cierra con ESPACIO, ENTER, E o click, y mientras está abierto el reloj no corre. Cada minijuego da un resultado de 0 a 100: con 50 o más te fue bien y con 100 fue perfecto. Al terminar, el reloj avanza lo que dura esa actividad.

> **\[Espacio para foto 20\]** El cartel que explica un minijuego antes de empezar.

### Los que se juegan igual

Varios trabajos y favores usan la misma mecánica con otro dibujo. Si aprendes uno, sabes jugar todos los de su grupo.

| Mecánica | Cómo se juega | Dónde sale |
| --- | --- | --- |
| **Pedidos** | El pedido del cliente sale a la izquierda. Arma lo que pide con los botones de la derecha, en el mismo orden, y dale ENTREGAR. Si te equivocas, «Botar y empezar». El cliente pierde la paciencia si te demoras. | Heladería de Paola (recipiente, sabores, topping) · Ramos de Doña Inés (papel, flores, cinta) · Almuerzo de la Cantina con Doña Cecilia (sopa, seco, jugo) · Café de Nico (café, pan, dulce) |
| **Ritmo** | Las notas bajan por carriles. Toca la tecla del carril cuando la nota pase por la línea. | DJ en la terraza de Marta (4 carriles: D F J K) · Al ritmo con Iván y Pili · Trote con Esteban · Reto de baile para ClipU · Micrófono abierto del Grano (← ↓ ↑ →) |
| **Ordenar pasos** | Los pasos están revueltos. Tócalos en el orden correcto, del primero al último. En la receta de Mamá, primero ves el orden unos segundos y después lo repites de memoria. | Tutoría de Laura · Primeros auxilios con la enfermera Lidia · Pizarra táctica de Ochoa · Arreglar la bici con Papá · Cocinar con Mamá · Estirar con Marcela · Técnica de barra con el Tanque · Trasplantar con Don Pablo |
| **Vueltos** | El cliente paga con un billete. Toca las monedas y billetes hasta dar el vuelto exacto (lo que pagó menos el total) y dale «Entregar vuelto». | La canasta de Andrés (Cantina y Mercadito) · Las empanadas de Doña Mery |
| **Concentración** | Mantén el mouse dentro del círculo que se mueve. Cuando llega una notificación, ciérrala con la X: si la abres, pierdes el hilo un rato. | Estudiar en el escritorio o la Biblioteca · Estudiar con Sofía · El puesto del silencio de Marlene |
| **Respirar** | El círculo crece y se encoge. Mantén ESPACIO mientras crece y suéltalo cuando se encoja. | Sofía antes del micrófono · Nadia en la piscina · La entrenadora Paz |

### Los que son únicos

| Minijuego | Con quién y dónde | Cómo se juega |
| --- | --- | --- |
| Latte art | Valentina · Grano Café, día 6 | Mantén el click y sigue la figura punteada (corazón, hoja, tulipán). |
| Posar para Don Aurelio | Parque, zona del pintor | Deja el mouse quieto dentro del círculo aunque se mueva un poquito. |
| Reparar controles | Kevin · PixelZone | Une cada cable con el puerto de su mismo color. Ojo: en el último, la palabra está pintada de otro color. |
| Moderar el directo | Camilo · PixelZone, día 8 | Borra con click los comentarios tóxicos y el spam; deja los buenos. |
| ¿Confiable o trampa? | Laura, por WhatsApp, día 5 | Lee 6 mensajes y decide: 1 = confiable, 2 = trampa (estafa, cadena, link raro). |
| Editor de fotos | Galería del celular · Paola, día 8 | Elige recorte, filtro, etiqueta y pie de foto, y súbela a Aurora+. |
| Pintar el cartel | Lili e Iris | Elige un color y pinta las casillas igual que el modelo. |
| La cometa de Valeria | Parque, pradera | Mantén el click o ESPACIO para jalar; suelta para que baje. Que no salga de la franja verde. |
| Buscar a la mamá de Mateo | Julián · atrio de la Plaza, día 6 | Encuentra entre la gente a la señora que describe Mateo. Son 3 rondas. |
| Rondo con Rojas | Cancha de fútbol | Pásale a un compañero libre (en verde) antes de que se acabe el tiempo. Son 12 pases. |

> **\[Espacio para foto 21\]** El turno en la heladería de Paola (mecánica de pedidos).

### Casa, Plaza y celular

| Minijuego | Dónde | Cómo se juega |
| --- | --- | --- |
| No poder dormir | Tu cama, cada noche | Quita las notificaciones antes de que se te pasen. Las que dicen DESLIZA se arrastran. Las de tu familia se contestan. |
| Pixel Royale | PixelZone | Esquiva todo lo que cae el mayor tiempo posible. Tienes 3 vidas. Flechas o W A S D. |
| Torre | PixelZone | Suelta cada piso encima del anterior con ESPACIO o click. Lo que sobresale se cae. |
| Duelo de reflejos | PixelZone, con Camilo | Espera el «¡YA!» y presiona ESPACIO antes que Camilo. |
| Flappy | Celular | Click para volar y pasar por el hueco de los tubos. |
| Pong | Celular | Cada click cambia la dirección de tu barra. No dejes pasar la bola. La bola empieza despacio y acelera un poco con cada golpe. |
| Wordle | Celular | Adivina la palabra de 5 letras en 6 intentos. Verde: en su lugar · amarillo: está en otro lugar · azul: no está. Solo acepta letras. |

Las clases tienen sus propios minijuegos (sección 10) y los deportes los suyos (sección 11).

### Los juegos con pantalla propia

Cuatro juegos ocupan toda la pantalla. Mientras juegas, el reloj y el resto del juego se detienen; al salir pasa el tiempo que duró la partida y recibes lo que ganaste.

| Juego | Dónde está | Qué te da |
| --- | --- | --- |
| Ajedrez | Parque, en las mesas de ajedrez (**E** frente a una mesa) | Ganar: Notas +2 y Social +1. Tablas: Notas +1 y Social +1. Perder: Notas +1 |
| Moderador (tower defense) | PixelZone, en las máquinas: opción **4**, gratis | Cada nivel ganado por primera vez: Seg +3 y Social +1 |
| ModerIA | Celular, app **ModerIA** | Cada nivel ganado por primera vez: Notas +2 y el filtro de notificaciones |
| Parqués | Casa, mesa del comedor, fuera de las comidas (de 9:00 a. m. a 11:00 p. m.) | Ganar: Social +2 y Energía +2. Perder: Social +1 |

**Ajedrez.** Juegas con las blancas contra el señor de las mesas.

- Antes de empezar escoges contra qué modelo juegas: el **1 (El clásico)** remata más; el **2 (El preciso)** evalúa mejor pero se conforma con tablas.
- Click en tu pieza y luego en la casilla, o arrástrala. Los puntos marcan a dónde puede ir; el círculo, una pieza que se puede comer. Al coronar, el peón se vuelve dama.
- Él responde solo. Si nadie gana en 60 jugadas cada uno, son tablas. Rendirse cuenta como perder.
- Ganarle da el logro **Garry Kasparov**.

**Moderador.** Spam, bots y haters bajan por el camino hacia tu feed. Si llegan 20, pierdes. Son 5 niveles y cada nivel ganado abre el siguiente.

- Click en un círculo para construir una torre; click en una torre para mejorarla o venderla (devuelve el 70 %). Al pasar al nivel 5 escoges una de dos ramas.
- Los enemigos: Spam, Bot (rápido), Hater (más vida), Verificado falso (tiene armadura), Virus (al morir se parte en 3 bots) y la Cadena viral, el jefe del nivel 5.
- **ESPACIO** pausa, **N** trae la siguiente ola cuando ya salieron todos los enemigos y el botón **x2** acelera.

| Torre | Qué hace | Rama A | Rama B |
| --- | --- | --- | --- |
| Reportar (60) | Flecha a un enemigo, rápida | Ráfaga: varias flechas a la vez | Certero: ignora armadura y hace tiros críticos |
| Baneo (90) | Rayo que salta a 3 enemigos | Tormenta: salta a más y no pierde daño | Suspensión: aturde |
| Bomba de reportes (120) | Explota en un área, lenta | Racimo: suelta minibombas | Fuego: deja el suelo ardiendo |
| Firewall (100) | Muro de fuego en el camino que detiene y amontona a los enemigos | Muralla: aguanta el doble y los empuja hacia atrás | Infierno: quema fuerte alrededor |

**ModerIA.** Le enseñas a una IA a moderar mensajes: tú dices qué es cada uno y ella aprende de eso. Si le enseñas mal, aprende mal.

1. **¿Bueno o malo?** Etiquetas 16 mensajes y la IA aprende de cada uno. Luego la entrenas (escoges la tasa de aprendizaje y le das 20 vueltas) y la pruebas con 16 mensajes que nunca vio. Tiene que acertar el 80 %.
2. **¿Qué tipo de mensaje es?** Lo mismo con cuatro tipos (bueno, burla, amenaza y estafa) y 20 mensajes. Meta: 80 %.
3. **¿A quién se lo mando?** Ajustas los pesos y el sesgo de cuatro compuertas (Acoso, Psicóloga, Coordinación y Bloquear) hasta que sus tablas queden en verde. **Probar el sistema** manda 20 mensajes y todos tienen que llegar a su lugar.

Cada nivel ganado hace que las notificaciones lleguen 15 % más espaciadas cuando estudias con el celular al lado y cuando no puedes dormir (hasta 45 %). Ganar los tres da el logro **Entrenador de IAs**.

**Parqués.** Juegas con las fichas amarillas contra Lili (agresiva: come siempre que puede), Papá (cuidadoso: busca los seguros) y la abuela Nena (corredora: mueve la más adelantada).

- Das la vuelta a la cruz y entras por el pasillo de tu color hasta la meta del centro. Gana el primero que meta las 4 fichas.
- Tira los dados, escoge un dado y luego la ficha que brilla. Al pasar el mouse sobre una ficha se marca dónde caería. Si solo hay una jugada posible, se hace sola.
- Con pares salen todas tus fichas de la cárcel y vuelves a tirar (hasta 3 veces). Sin fichas afuera tienes 3 intentos para sacar pares.
- Si caes sobre otra ficha fuera de un seguro (las salidas y las estrellas), la mandas a la cárcel. Para entrar a la meta necesitas el número exacto.

## 13. Los eventos de los personajes

Los eventos son las historias de cada personaje. Cada uno pasa en un lugar, unos días y unas horas. Cuando un evento está activo, la persona aparece en ese lugar con un **!** encima, y el cuadro AHORA te avisa; algunos te invitan antes por WhatsApp. Háblale con **R** para empezar la escena. Si no llegas a tiempo, el evento se pierde y la persona lo recuerda.

> **\[Espacio para foto 22\]** Una persona con el «!» encima esperando un evento.

Hay 72 eventos. Los que tienen requisito solo salen si se cumple (cierta amistad, o una respuesta que diste antes). Estos son los principales:

| Personaje | Días | Hora | Dónde | Qué pasa | Cuándo sale |
| --- | --- | --- | --- | --- | --- |
| Iris | 1–5 | 15:30–18:00 | Parque, fuente | La amiga de Lili está en la fuente del parque | Siempre |
| Mamá (Claudia) | 1 | 19:00–21:30 | Cocina y comedor | Primera cena de la semana | Siempre |
| Lili | 2–3 | 6:15–7:30 | Cocina y comedor | Lili necesita ayuda con su cartel de ciencias | Siempre |
| Nico | 2–5 | 7:00–15:00 | Kiosco de café | Atender el kiosco de Nico | Siempre |
| Paola | 2–5 | 15:00–18:00 | Heladería | Paola necesita una mano en la heladería | Siempre |
| Doña Mery | 2–9 | 17:00–22:00 | Puesto de empanadas | Doña Mery está desbordada de clientes | Siempre |
| Lili | 3–9 | 1:00–3:00 | Tu cuarto | Lili toca tu puerta de madrugada con su celular | Si llevas 2 h o más de pantalla ese día |
| Doña Inés | 3–7 | 10:00–17:00 | Puesto de flores | Ayudar con los ramos | Siempre |
| Doña Cecilia | 3 | 11:00–15:00 | La Cantina | Servir el almuerzo | Si le ofreciste ayuda |
| Andrés | 3 | 12:00–14:00 | La Cantina | Ayudar con la canasta | Si le respondiste «Respeto…» |
| Chato | 3–9 | 18:00–23:30 | Bar La Esquina | La esquina (un cigarro): sube el VICIO si aceptas | Si tienes estrés |
| Laura | 4 | 14:00–17:30 | Biblioteca | Tutoría de Cálculo | Amistad con Laura de 40 o más |
| Nadia | 4 y 5 | 15:00–17:30 | Piscina | Nadia te reta en la piscina | Amistad con Nadia de 35 o más |
| Marta | 5 | 17:00–20:00 | Terraza de Marta | El sonido de la fiesta (DJ) | Amistad con Marta de 35 o más |
| Andrés | 6 | 9:00–13:00 | Parque, Mercadito | El Mercadito del Parque | Amistad con Andrés de 40 o más |
| Papá (Ernesto) | 6 | 10:00–13:00 | Patio de ropas | Arreglar la bici vieja | Siempre |
| Valentina | 6 | 14:00–18:00 | Grano Café | Tu turno en el Grano (latte art) | Si le dijiste «Cuenta conmigo…» |
| Mamá (Claudia) | 7 | 11:00–14:00 | Cocina y comedor | Cocinar el ajiaco | Amistad con Mamá de 45 o más |
| Camilo | 7 | 15:30–17:30 | PixelZone | Torneo con Los del Fondo | Amistad con Camilo de 40 o más |
| El salón | 8 | 12:40–16:00 | Por WhatsApp | Alguien filtró el parcial de Cálculo: el misterio del rumor | Si fuiste a la fiesta o a Programación |
| Marta | 8 | 17:00–21:00 | Patio central | Resolver el rumor con el salón | Si estás investigando |
| Lili | 8 | 18:00–20:30 | Sala | El cumpleaños de Lili | Siempre |
| Camilo | 8 | 20:00–22:00 | PixelZone | El primer directo de Camilo (moderar) | Si le ofreciste ayuda |
| Laura | 9 | 18:00–20:30 | Grano Café | Grupo de estudio | Amistad con Laura de 55 o más |
| Sofía | 9 | 20:30–22:30 | Parque, entrada | Caminar con Sofía | Amistad con Sofía de 65 o más |
| Mamá (Claudia) | 9 | 20:30–23:00 | Sala | Mamá quiere hablar contigo | Siempre |
| Todos | 10 | 19:00–23:30 | Patio central | Feria Aurora, ceremonia de la Copa y foto final | Siempre |

Los demás eventos son de gente de la ciudad y de los entrenadores (Don Pablo, Marlene, Iván, Don Aurelio, Doña Rosa, el Prof. Núñez, Esteban, Kevin, la enfermera Lidia, Rojas, Ochoa, Paz, el Tanque, Marcela, Bruno, Pili, Don Fabio, Valeria, Julián, Don Gil e Iris). Las visitas de tus amigos a la casa salen si los invitaste.

**Lo que deciden los eventos:** tus amistades y romances, la plata, las notas, el VICIO, el rumor del día 8 (quien lo investiga lo puede aclarar) y lo que sale en los epílogos del final.

## 14. Puntaje, evaluación final, logros y finales

### El puntaje

Se ve en la pausa (pestaña Resumen) y al final:

| Parte | Cómo se calcula |
| --- | --- |
| Notas | Notas × 2 |
| Social | Social × 2 |
| Ejercicio | 10 puntos por hora de ejercicio, máximo 200 |
| Equilibrio | 5 puntos por cada categoría que quedó en su rango, sumando los 10 días |
| VICIO | −40 por cada punto |
| Logros | 5 puntos por cada logro |

### La evaluación de tu comportamiento digital

El día 10, después de la Feria Aurora y la ceremonia de la Copa, salen las pantallas del final, una tras otra (click o tecla para pasar):

1. **La foto final** con la gente cercana.
2. **El informe «Tus 10 días»:** tu perfil de tiempo (en qué se te fue la semana), las horas de cada categoría día por día, **seguidores frente a amigos de verdad** en dos barras, los días equilibrados de 10, el tiempo total en el celular, la deuda de sueño, el VICIO, cuántas veces dijiste que no, las materias perdidas, los logros y el **puntaje final**.
3. **Tu final** (tabla de abajo).
4. **Los epílogos:** qué pasó con cada persona (Lili e Iris, tu mamá, tu papá, el rumor, el romance, la esquina…).
5. **Gracias por jugar**, con los créditos del Grupo 1.

> **\[Espacio para foto 23\]** El informe «Tus 10 días» con las barras por día.

### Los finales

Se revisan en este orden y sale el primero que se cumpla:

| Final | Cuándo sale |
| --- | --- |
| No te graduaste | Perdiste 2 o más materias |
| Quemado | VICIO de 4 o más, o mucha deuda de sueño al final |
| Campeón de la Copa Aurora | 2 trofeos, o 1 trofeo y estar en el Club del Deporte |
| Cerebrito | Notas de 85 o más y 2 amigos de verdad o menos |
| Estrella de Aurora+ | 250 seguidores o más y 2 amigos de verdad o menos |
| Con ella, en la foto | Terminaste en pareja sin chisme de por medio |
| La casa llena | Viviste las historias de Iris y tienes buena relación con Lili y con tu familia |
| Emprendedor | Terminaste con $120 o más |
| Equilibrio | 5 días equilibrados o más |
| Solo en la foto | Nivel social Perdedor y ningún amigo de verdad |
| Diez días después | Ninguno de los anteriores |

### Los 34 logros

Son de tu cuenta: una vez ganados, salen ganados en las tres partidas. Cuando ganas uno sale un cartel dorado.

| Logro | Cómo se gana |
| --- | --- |
| Primer día | Sobrevive al lunes. |
| Puntual | Llega a tiempo a Física el día 1. |
| Buen dormir | Duerme 8 horas o más en tu cama sin abrir más de una notificación. |
| Día perfecto | Las 5 categorías en su rango en un día. |
| Equilibrista | Tres días equilibrados (4 de 5 en rango). |
| Desconectado | Un día con menos de 30 min de celular. |
| Cinco de verdad | Cinco amistades de 60 o más. |
| Popular | Llega al nivel social Popular. |
| Cien seguidores | Llega a 100 seguidores. |
| Influencer | Llega a 300 seguidores. |
| Barra arriba | Completa el press de banca. |
| Búfalo de oro | Gana el trofeo de rugby. |
| Botín de oro | Gana el trofeo de fútbol. |
| Pez dorado | Gana el trofeo de natación. |
| Espalda recta | Di que no a tres ofertas de vicio. |
| Barista | Haz un latte art bueno en el Grano. |
| Heladero | Atiende bien un turno en la heladería. |
| DJ de la terraza | Pon la música de la fiesta de Marta. |
| Moderador | Salva el primer directo de Camilo. |
| Detective | Descubre de dónde salió el rumor del parcial. |
| Ojo de fotógrafo | Sube una foto bien editada. |
| No caigo | Detecta todos los mensajes trampa. |
| Hermano del año | Haz que el cumpleaños de Lili sea inolvidable. |
| Amiga de la familia | Vive las cuatro historias de Iris. |
| Canela en casa | Adopta a Canela. |
| Corazón | Empieza una relación. |
| Club del Deporte | Entra al Club del Deporte. |
| Emprendedor | Junta $100. |
| Cero faltas | Asiste a 12 clases. |
| Honesto | Di la verdad cuando costaba. |
| Semestre aprobado | Pasa todas las materias. |
| Diez días | Termina la historia. |
| Garry Kasparov | Gánale a la máquina en el ajedrez del parque, como Kasparov a Deep Blue en 1996. |
| Entrenador de IAs | Gana los 3 niveles de ModerIA. |

## 15. Guardar y cargar

El juego guarda en archivos de texto dentro de la carpeta `partidas` del juego. Hay **3 espacios** para partidas.

- **Solo:** cada noche a las **2:00 a. m.** del juego. Si a esa hora estás en un minijuego, una escena o una conversación, se guarda apenas termines (si duermes, al despertar). Sale el aviso «Partida N guardada (automático, 2:00 a. m.)».
- **Cuando quieras:** en la pausa, botón **Guardar partida N**. Si estás en medio de algo, te pide que termines primero.
- **Al salir:** el botón **Salir** de la pausa pide un segundo click para confirmar («¿Seguro? Click otra vez»). Antes de cerrar guarda la partida, si estás en un momento seguro, y tu cuenta.
- **Al terminar el juego** también se guarda.
- **Partida nueva:** apenas eliges el espacio, queda apartado como «Partida nueva · todavía sin guardar». Si eliges un espacio que ya tenía una partida, te pide confirmar con otro click antes de borrarla.
- **Continuar:** en la pantalla de inicio muestra las 3 partidas con su resumen (día, hora, dificultad, plata y puntaje) y la fecha real en que se guardaron. El botón se apaga si no hay ninguna.

> **\[Espacio para foto 24\]** El menú Continuar con las tres partidas y su resumen.

| Archivo | Qué guarda |
| --- | --- |
| `partida1.txt` a `partida3.txt` | Todo lo de esa partida: día, hora, lugar, barras, amistades, chats, diario, eventos, inventario, horario… |
| `cuenta.txt` | Lo que vale para las 3 partidas: logros (con su fecha), récords de minijuegos y de PixelZone, estadísticas, música, volumen, tamaño de la ventana y el límite de 30 FPS |
| `puntajes.txt` | Una línea por partida terminada: fecha, dificultad, puntaje y final |

En **RÉCORDS** (pantalla de inicio) ves las estadísticas de la cuenta, el mejor puntaje de cada minijuego, las partidas terminadas y los logros.

No borres ni edites estos archivos a mano mientras el juego está abierto. Si un archivo de partida viene de una versión anterior del juego, igual abre: lo que falte toma su valor inicial.

## 16. Pausa, ajustes y rendimiento

**ESC o P** abre la pausa. El reloj se queda quieto y los minijuegos no pierden tiempo.

La pausa y el celular nunca están abiertos al tiempo. Con el celular abierto, **ESC** lo cierra y **P** no hace nada; la pausa se abre con el celular cerrado.

| Pestaña | Qué tiene |
| --- | --- |
| Resumen | Tu puntaje y de dónde sale cada parte |
| Logros | Los 34 logros y cuáles tienes |
| Notas | Cómo vas en cada materia |
| Ajustes | Dificultad, música (prender y volumen), sonido de los clicks, **tamaño de la ventana** y **Limitar a 30 FPS** |
| Controles | Todas las teclas |

Abajo están los botones **Continuar**, **Guardar partida N** y **Salir**.

> **\[Espacio para foto 25\]** La pausa abierta en la pestaña Ajustes.

### Si el juego va lento o se traba

1. **Sube la memoria de Processing** (sección 2). Es lo que más ayuda: con poca memoria Java se detiene a limpiar muy seguido y algunos cuadros se alargan.
2. **Prende Limitar a 30 FPS** en Pausa › Ajustes. El juego dibuja la mitad de cuadros por segundo, pero todo se mueve a la misma velocidad: solo se ve un poco menos suave. Queda guardado para las próximas partidas.
3. **Usa una ventana más pequeña** (1280 × 720 o 960 × 540) desde el botón PANTALLA de la pantalla de inicio o en Ajustes.
4. **Cierra otros programas pesados** mientras juegas.

Guardar tarda un instante, así que es normal un saltico al guardar.

## 17. Consejos y preguntas frecuentes

### Consejos

- Mira el Horario cada mañana: las clases son a las 7:00 y a las 9:00, y el bus de la casa a la U tarda 30 minutos.
- No abras el celular «un momentico»: corre 3 veces más rápido. Revisa Bienestar digital en Ajustes para ver cómo vas.
- Duerme antes de la medianoche y activa No molestar: dormir bien sube la energía y evita dormirte en clase.
- Contesta los chats. Dejar en visto cuesta amistades.
- La plata se gana en los turnos (Grano, heladería, kiosco de Nico, Cantina, canasta de Andrés, PixelZone) y en la Copa.
- Los días 6 y 7 no hay clases: buen momento para eventos, familia, deporte y el mercadito.
- Piensa antes de publicar: lo polémico da likes, pero la gente lo recuerda.
- El día 10 son los parciales: llega descansado y con las pistas de la app Notas.

### Preguntas frecuentes

| Pregunta | Respuesta |
| --- | --- |
| Processing no abre el juego | La carpeta y el archivo deben llamarse igual: `Redemption` y `Redemption.pde`. |
| No suena la música | Instala la biblioteca Sound en Processing y revisa Ajustes › Música. Revisa también que la carpeta data/musica tenga los archivos .wav (los temas de cada zona se llaman area\_1 a area\_7). |
| Sale «Target VM failed to initialize» | Pediste demasiada memoria en las Preferencias. Bájala a 1024 MB. |
| El juego se traba a ratos | Sube la memoria y prende Limitar a 30 FPS (sección 16). |
| La ventana no cabe en mi pantalla | Botón PANTALLA en la pantalla de inicio o Ajustes en la pausa: elige 1280 × 720 o 960 × 540. |
| ¿Y si me quedo sin plata lejos de la casa? | Desde cualquier paradero puedes volver caminando. Tarda más, pero siempre se puede. |
| ¿Y si un lugar cierra conmigo adentro? | Puedes salir hacia la calle aunque esté cerrado; lo que no puedes es volver a entrar. |
| ¿Y si el bus ya no pasa? | El bus va de 5:00 a 23:00. De noche, toma el taxi de Don Beto ($8) o camina. |
| ¿Por qué la mesa del comedor está vacía? | Solo hay comida en el desayuno (6:00 a 8:30 a. m.) y en la cena (7:00 a 9:30 p. m.), una vez cada una por día. |
| ¿Por qué alguien ya no me habla igual? | Lo dejaste en visto, lo plantaste o tu amistad bajó. Míralo en Relaciones. |
| ¿Por qué no sale un evento? | Revisa el día, la hora y el requisito en la sección 13. |
