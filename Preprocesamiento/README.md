# 1. Preprocesamiento


### 1.1. Obtencion de los archivos del flujo de datos de red.
---
En esta parte se descargaron los archivos .binetflow los cuales su contenido esta en formato .csv. Estos archivos fueron elegidos en base al dia y el tipo de familia de Botnet a la cual estan asociados. 

Se eligieron los flujos de red de cada familia de botnet para asegurarse de que se puedan detectar diferentes tipos de ataques, ya que cada familia tiene patrones únicos. Esto mejora la generalización y hace que los resultados sean más realistas. Además, comparar cómo el modelo responde a distintas familias permite identificar sus fortalezas y debilidades, ayudando a mejorar su precisión y eficacia en escenarios variados.

Los flujos de red fueron obtenidos de los siguientes enlaces:

- (Virut) ``` https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-54/detailed-bidirectional-flow-labels/capture20110815-3.binetflow ```
- (Sogou) ```https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-48/detailed-bidirectional-flow-labels/capture20110816-2.binetflow```
- (Murlo) ``` https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-49/detailed-bidirectional-flow-labels/capture20110816-3.binetflow ```
- (Neris) ``` https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-50/detailed-bidirectional-flow-labels/capture20110817.binetflow ```
- (RBot) ``` https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-51/detailed-bidirectional-flow-labels/capture20110818.binetflow ```
- (NsisAy) ``` https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-53/detailed-bidirectional-flow-labels/capture20110819.binetflow ```

El archivo ```merge_binetflow.py``` se encarga de concatenar todos los dataframes que se obtuvieron de los enlaces anteriores, este script da como salida un nuevo dataset. Un vez hecho esto el nuevo dataset puede ser usado para la siguiente parte del preprocesamiento.

### 1.2. Acerca del dataset
---

El CTU-13 es un conjunto de datos de tráfico de botnets capturado en la Universidad CTU, República Checa, en 2011. El conjunto de datos CTU-13 consiste en trece capturas (llamadas escenarios) de diferentes muestras de botnets. En cada escenario se ejecutó un malware específico, el cual utilizó varios protocolos y realizó diferentes acciones.

¿Qué es un IDS (Sistema de Detección de Intrusos)? Los Sistemas de Detección de Intrusos (IDS) están presentes para prevenir ataques e infiltraciones a redes, los cuales podrían afectar a la organización. Monitorean el tráfico de red en busca de actividades sospechosas y emiten alertas en caso de problemas.

### Caracteristicas del dataset:

- Categoricas: Proto, SrcAddr, Sport, Dir, DstAddr, Dport, State, , sTos, dTos
- Numericas: Dur, TotPkts, TotBytes, SrcBytes
- Formato de fecha: StartTime

Tipos de IDS:

Detección de intrusos basada en firmas: En este tipo, los ataques entrantes se comparan con una base de datos preexistente de ataques conocidos.
Detección de intrusos basada en anomalías: Utiliza estadísticas para formar un uso de referencia de las redes en diferentes intervalos de tiempo. Se introdujeron para detectar ataques desconocidos.
Basado en dónde descubren, pueden clasificarse en:

Detección de intrusos en red (NIDS)
Detección de intrusos en host (HIDS)
Declaración del Problema Con el aumento del uso de Internet, es muy importante proteger las redes. El riesgo más común para la seguridad de una red es una intrusión, como fuerza bruta, denegación de servicio o incluso infiltración desde dentro de una red. Con los patrones cambiantes en el comportamiento de la red, es necesario cambiar a un enfoque dinámico para detectar y prevenir tales intrusiones.


Cada uno de los escenarios en el conjunto de datos fue procesado para obtener diferentes archivos. Por problemas de privacidad, el archivo pcap completo que contiene todos los datos de fondo, normales y de botnets no está disponible. Sin embargo, el resto de los archivos están disponibles. Cada escenario contiene:


