# Port Scanner en Python

Escáner de puertos TCP simple hecho en Python como proyecto de aprendizaje. Recibe una IP y un rango de puertos por consola e informa cuáles están abiertos.

---

## ¿Qué hace?

Intenta conectarse a cada puerto del rango indicado usando sockets TCP. Si la conexión es exitosa (el puerto responde), lo muestra en pantalla. Si no responde en 1 segundo, lo descarta y sigue.

La salida solo muestra puertos abiertos — sin ruido de puertos cerrados.

---

## Tecnologías

- Python 3
- Módulo `socket` (biblioteca estándar — sin dependencias externas)

---

## Uso

```bash
python scanner.py
```

El script pide tres datos por consola:

```
Ingresá la IP a escanear: 192.168.1.1
Puerto inicial: 1
Puerto final: 1024
```

**Salida esperada:**

```
Puerto 22  -> ABIERTO
Puerto 80  -> ABIERTO
Puerto 443 -> ABIERTO
```

Si ningún puerto responde, no se imprime nada.

---

## Notas técnicas

- Usa `AF_INET` (IPv4) y `SOCK_STREAM` (TCP)
- Timeout de 1 segundo por puerto para evitar bloqueos
- `connect_ex()` devuelve `0` si la conexión fue exitosa, cualquier otro valor indica puerto cerrado o inaccesible

---

## Historial de mejoras

| Versión | Cambio |
|---------|--------|
| v1.0 | Muestra todos los puertos (abierto/cerrado) |
| v1.1 | Solo muestra puertos abiertos — salida más limpia |

---

## Contexto

Proyecto de práctica para entender cómo funcionan los sockets y las conexiones TCP a bajo nivel. No está pensado para uso en producción ni como herramienta de auditoría.

---

## Autor

[Carlos Pairoux](https://github.com/carlos-pairoux)
