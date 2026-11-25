# Funciones generales: hash y listas

En el curso no podíamos usar HashMap, ArrayList ni IntList, así que hicimos nuestras propias versiones con vectores normales. Este documento explica cómo quedaron.

Todas las funciones están en `Redemption.pde`.

---

## Hash

### Para qué lo necesitábamos

El juego guarda muchas "banderas": cosas que ya pasaron en la historia, cada una con un nombre y un número. Por ejemplo `VICIO = 2`, `PISTA_CALCULO = 1` o `NUM_Laura = 1`. Pueden llegar a ser miles, y el código pregunta por ellas todo el tiempo (más de 100 lugares llaman a `bandera()`).

Si las guardáramos en un vector y las buscáramos una por una, cada pregunta tendría que recorrer todo el vector. Por eso armamos una tabla hash: con el nombre calculamos directamente en qué casilla debería estar, y casi siempre la encontramos al primer intento.

### Los vectores que usa

```java
final int MAX_BANDERAS = 12000;
final int BAND_TABLA = 32768;
String[] banderaNombre = new String[MAX_BANDERAS];  // el nombre de cada bandera
int[] banderaValor = new int[MAX_BANDERAS];         // su número
int[] banderaIndice = new int[BAND_TABLA];          // la tabla hash
int banderasN = 0;                                  // cuántas banderas hay
```

- `banderaNombre` y `banderaValor` van en paralelo: la bandera número 5 tiene su nombre en `banderaNombre[5]` y su valor en `banderaValor[5]`.
- `banderaIndice` es la tabla hash. En cada casilla guarda en qué posición de esos dos vectores está la bandera, **sumándole 1**. Así un 0 significa que la casilla está vacía.

### Cómo se imitó, función por función

**`codigoBandera(nombre)`: la función hash.** Convierte el nombre en un número de casilla entre 0 y 32767. Recorre el nombre letra por letra, multiplica lo que lleva por 25, le suma el código de la letra y saca el residuo para no pasarse del tamaño de la tabla.

```java
int codigoBandera(String n) {
  int h = 9;
  for (int i = 0; i < n.length(); i++) {
    h = (h * 25 + letraEn(n, i)) % BAND_TABLA;
  }
  return h;
}
```

Probamos varios números y con 9 y 25 ningún par de nombres del juego cae en la misma casilla.

**`posBandera(nombre)`: buscar.** Va a la casilla que da `codigoBandera`:
- Si está vacía, la bandera no existe.
- Si tiene una bandera con ese mismo nombre, la encontró.
- Si tiene otra bandera (una colisión), prueba la casilla siguiente y sigue así. Esto se llama sondeo lineal.

Si la encuentra, devuelve la posición. Si no, devuelve un número negativo que dice en qué casilla libre iría (`-1 - casilla`). Así la siguiente función no tiene que buscar otra vez.

```java
int posBandera(String n) {
  int h = codigoBandera(n);
  while (banderaIndice[h] != 0) {
    int i = banderaIndice[h] - 1;
    if (banderaNombre[i].equals(n)) return i;
    h = (h + 1) % BAND_TABLA;
  }
  return -1 - h;
}
```

**`bandera(nombre)`: leer, como `get`.** Si la bandera existe devuelve su valor, y si no devuelve 0. Por eso nunca hay que crear una bandera antes de preguntar por ella.

**`sumarBandera(nombre, cantidad)`: escribir, como `put`.** Si la bandera ya existe, le suma la cantidad. Si no existe, la agrega al final de los dos vectores y anota su posición en la casilla libre que le dio `posBandera`.

**`banderaValor0(nombre)`: poner en 0.** Busca la bandera y deja su valor en cero, sin borrarla.

### Un ejemplo completo

Cuando en un diálogo el efecto dice `VICIO +1`, el juego llama `sumarBandera("VICIO", 1)`:

1. `posBandera("VICIO")` calcula la casilla con `codigoBandera`.
2. La primera vez esa casilla está vacía, así que devuelve un negativo.
3. `sumarBandera` guarda "VICIO" y el 1 en la siguiente posición libre (por ejemplo la 37) y pone `banderaIndice[casilla] = 38`.
4. Después, `bandera("VICIO")` va directo a esa casilla, ve el 38, mira la posición 37, confirma que el nombre es "VICIO" y devuelve 1.

### Comparación con HashMap

| HashMap de Java | Lo nuestro |
| --- | --- |
| `mapa.get(nombre)` | `bandera(nombre)` |
| `mapa.put(nombre, mapa.get(nombre) + v)` | `sumarBandera(nombre, v)` |
| `mapa.put(nombre, 0)` | `banderaValor0(nombre)` |
| `mapa.containsKey(nombre)` | `posBandera(nombre) >= 0` |
| `mapa.size()` | `banderasN` |
| `hashCode()` | `codigoBandera(nombre)` |

La diferencia es que nuestra tabla tiene tamaño fijo: caben máximo 12000 banderas. Si se llenara, `sumarBandera` escribe un aviso en la consola y no guarda la bandera nueva. En una partida normal se usan muchas menos.

---

## Listas

### La idea

Una lista es un vector al que se le pueden agregar y quitar cosas sin saber de antemano cuántas van a ser. Como no podíamos usar ArrayList ni IntList, creamos los vectores con un tamaño máximo y llevamos la cuenta de cuántos elementos tienen. Usamos tres formas:

**1. Lista de enteros (`int[]`).** La casilla 0 guarda cuántos elementos hay, y los elementos van de la casilla 1 a la `v[0]`. Por eso se crea con una casilla de más: para guardar hasta 12 números se crea `new int[13]`.

```
v = [3, 40, 7, 15, 0, 0, ...]
     ^  ^   ^  ^
     |  elementos 1 a 3
     hay 3
```

**2. Lista de textos (`String[]`).** Los textos van seguidos desde la casilla 0 y la lista termina en la primera casilla que esté en `null`. Aquí no hay contador.

**3. Tabla de filas (`String[][]`).** Funciona igual que la lista de textos, pero cada casilla es una fila completa. Termina en la primera fila `null`.

Las tres tienen el mismo límite: si el vector se llena, agregar no hace nada.

### Cada función y su equivalente

**Lista de enteros (como IntList o `ArrayList<Integer>`)**

| Nuestra función | Operación de lista | Qué hace |
| --- | --- | --- |
| `agregarInt(v, x)` | `add(x)` / `append(x)` | Suma 1 al contador y pone `x` en esa casilla |
| `tamInt(v)` | `size()` | Devuelve `v[0]` |
| `tieneInt(v, x)` | `contains(x)` / `hasValue(x)` | Recorre de 1 a `v[0]` buscando `x` |
| `posEnLista(v, x)` | `indexOf(x)` | Igual, pero devuelve la posición (0 si no está) |
| `quitarIntEn(v, i)` | `remove(i)` | Corre los de atrás una casilla y resta 1 al contador |
| `vaciarInt(v)` | `clear()` | Pone el contador en 0 |
| `barajarInt(v)` | `shuffle()` | Revuelve los elementos cambiando cada uno con otro al azar |

**Lista de textos (como StringList o `ArrayList<String>`)**

| Nuestra función | Operación de lista | Qué hace |
| --- | --- | --- |
| `agregarTexto(v, x)` | `add(x)` | Pone `x` en la primera casilla `null` |
| `tamTexto(v)` | `size()` | Cuenta casillas hasta encontrar un `null` |
| `tieneTexto(v, x)` | `contains(x)` | Recorre hasta el `null` comparando con `equals` |
| `quitarTextoEn(v, i)` | `remove(i)` | Corre los de atrás y deja `null` la última |
| `vaciarTexto(v)` | `clear()` | Pone todas las casillas en `null` |

**Tabla de filas (como `ArrayList<String[]>`)**

| Nuestra función | Operación de lista | Qué hace |
| --- | --- | --- |
| `agregarFila(m, fila)` | `add(fila)` | Pone la fila en la primera casilla `null` |
| `tamFilas(m)` | `size()` | Cuenta filas hasta el primer `null` |
| `vaciarFilas(m)` | `clear()` | Pone todas las filas en `null` |
| `unirTablas(a, b)` | `addAll(b)` | Crea una tabla nueva con las filas de `a` y después las de `b` |

**Copiar y crecer (reemplazan `arrayCopy` y `append` de Processing)**

| Nuestra función | Nativa que reemplaza | Qué hace |
| --- | --- | --- |
| `copiarEnteros(de, i0, a, j0, n)` | `arrayCopy` | Copia `n` enteros de un vector a otro |
| `copiarTextos(de, i0, a, j0, n)` | `arrayCopy` | Lo mismo con textos |
| `alargarEnteros(v, x)` | `append(v, x)` | Crea un vector con una casilla más y pone `x` al final |

Un detalle de `copiarEnteros` y `copiarTextos`: si copias dentro del mismo vector hacia adelante, copian de atrás para adelante. Si no lo hicieran así, se pisarían los datos antes de copiarlos.

### Por qué algunas funciones no devuelven el vector

Otra regla del curso era que nuestras funciones no podían devolver un vector. Entonces `unirTablas` y `alargarEnteros` son `void` y dejan el resultado en una variable global que empieza por `res`:

```java
unirTablas(ARBOL, ARBOL_EXTRA);
ARBOL = resUnirTablas;   // el resultado se lee de aquí
```

### Ejemplo de uso

```java
int[] vistos = new int[13];   // caben 12

agregarInt(vistos, 4);        // vistos = [1, 4, ...]
agregarInt(vistos, 9);        // vistos = [2, 4, 9, ...]

if (!tieneInt(vistos, 4)) agregarInt(vistos, 4);   // no lo agrega dos veces

for (int i = 1; i <= tamInt(vistos); i++) {
  println(vistos[i]);         // 4 y 9
}

vaciarInt(vistos);            // vistos = [0, ...]
```

El recorrido va de 1 a `tamInt`, no de 0, porque la casilla 0 es el contador.
