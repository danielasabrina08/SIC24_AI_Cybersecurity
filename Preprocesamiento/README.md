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
- (NsisAy) ``` https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-51/detailed-bidirectional-flow-labels/capture20110818.binetflow ```

El archivo ```merge_binetflow.py``` se encarga de concatenar todos los dataframes que se obtuvieron de los enlaces anteriores, este script da como salida un nuevo dataset. Un vez hecho esto el nuevo dataset puede ser usado para la siguiente parte del preprocesamiento.
