# Índice de ECU

1. [ECU-01: Registrar denuncia](#ecu-01-registrar-denuncia)
2. [ECU-02: Consultar estado e historial de denuncia](#ecu-02-consultar-estado-e-historial-de-denuncia)
3. [ECU-03: Asignar caso a un oficial de policía](#ecu-03-asignar-caso-a-un-oficial-de-policía)
4. [ECU-04: Actualizar denuncia](#ecu-04-actualizar-denuncia)
5. [ECU-05: Generar informe de investigación [Trabajo futuro]](#ecu-05-generar-informe-de-investigación-trabajo-futuro)
6. [ECU-06: Generar reporte estadístico [Trabajo futuro]](#ecu-06-generar-reporte-estadístico-trabajo-futuro)

---

## ECU-01: Registrar denuncia

**Descripción:** Permite a los usuarios registar una denuncia policial proporcionando la información requerida.

**Actor(es):** Ciudadano, oficial de policía

**Pre-condiciones:** Ninguna

### **Flujo de eventos**

#### **Flujo principal**
| Paso | Actor | Sistema |
| --- | --- | --- |
| 1 | El ciudadano solicita registar una denuncia. | - |
| 2 | - | El sistema muestra el formulario de denuncia al ciudadano. |
| 3 | El ciudadano completa el formulario con la información relevante. | - |
| 4 | - | El sistema valida y registra la denuncia en la blockchain. |
| 5 | - | El sistema genera un número de referencia y lo muestra al ciudadano como confirmación. |

#### **Flujo alternativo** (Formulario incompleto)
| Paso | Actor | Sistema |
| --- | --- | --- |
| 3a | El ciudadano no completa todos los campos requeridos en el formulario. | - |
| 3b | - | El sistema muestra un mensaje de error al ciudadano indicando los campos faltantes. |
| 3c | - | El flujo vuelve al paso 3 para que el ciudadano complete la denuncia. |

#### **Flujo de excepción** (Error en la validación)
| Paso | Actor | Sistema |
| --- | --- | --- |
| 4a | El sistema encuentra errores en los datos proporcionados por el ciudadano. | - |
| 4b | - | El sistema muestra un mensaje de error al ciudadano indicando los problemas de validación. |
| 4c | - | El flujo vuelve al paso 3 para que el ciudadano corrija los errores en la denuncia. |

Enlaces:
* [Diagrama de clase](class-diagram.md#ecu-01-registrar-denuncia)
* [Diagrama de secuencia](sequence-diagram.md#ecu-01-registrar-denuncia)

[Volver al índice](#índice-de-ecu)

---

## ECU-02: Consultar estado e historial de denuncia

**Descripción:** Permite a los usuarios verificar el estado actual y el historial de una denuncia registrada anteriormente.

**Actor(es):** Ciudadano

**Pre-condiciones:** El ciudadano debe tener un número de referencia de denuncia válido.

### **Flujo de eventos**

#### **Flujo principal**
| Paso | Actor | Sistema |
| --- | --- | --- |
| 1 | El ciudadano ingresa el número de referencia de la denuncia. | - |
| 2 | - | El sistema busca la denuncia correspondiente en la blockchain. |
| 3 | - | El sistema muestra el estado actual de la denuncia y su historial al ciudadano. |

#### **Flujo alternativo** (Número de referencia inválido)
| Paso | Actor | Sistema |
| --- | --- | --- |
| 1a | El ciudadano ingresa un número de referencia inválido. | - |
| 1b | - | El sistema muestra un mensaje de error al ciudadano indicando que el número de referencia es incorrecto. |
| 1c | - | El flujo vuelve al paso 1 para que el ciudadano ingrese un número de referencia válido. |

#### **Flujo de excepción** (Error en la consulta)
| Paso | Actor | Sistema |
| --- | --- | --- |
| 1a | Error al buscar la denuncia en la blockchain. | - |
| 1b | - | El sistema muestra un mensaje de error al ciudadano indicando que no se pudo realizar la consulta en este momento debido a un problema técnico. |
| 1c | - | Se registra el error en un registro de errores para su posterior revisión. |
| 1d | - | El ciudadano puede optar por volver al paso 1 para intentar nuevamente la consulta o finalizar el proceso de consulta. |

Enlaces:
* [Diagrama de clase](class-diagram.md#ecu-02-consultar-estado-e-historial-de-denuncia)
* [Diagrama de secuencia](sequence-diagram.md#ecu-02-consultar-estado-e-historial-de-denuncia)

[Volver al índice](#índice-de-ecu)

---

## ECU-03: Asignar caso a un oficial de policía

**Descripción:** Permite a los funcionarios de policía asignar casos de denuncia a oficiales específicos para su investigación.

**Actor(es):** Oficial de policía

**Pre-condiciones:** El caso de denuncia debe estar disponible y sin asignar.

### **Flujo de eventos**

#### **Flujo principal**
| Paso | Actor | Sistema |
| --- | --- | --- |
| 1 | El oficial de policía selecciona un caso sin asignar. | - |
| 2 | - | El sistema asigna el caso al oficial de policía seleccionado en la blockchain. |

#### **Flujo alternativo** (No hay casos disponibles)
| Paso | Actor | Sistema |
| --- | --- | --- |
| 1a | No hay casos de denuncia sin asignar en el momento. | - |
| 1b | - | El sistema muestra un mensaje al oficial de policía indicando que no hay casos disponibles en este momento. |
| 1c | - | El oficial de policía puede optar por volver al paso 1 para verificar la disponibilidad de casos en un momento posterior o finalizar el proceso de asignación. |

#### **Flujo de excepción** (Error en la asignación)
| Paso | Actor | Sistema |
| --- | --- | --- |
| 1a | Error al asignar el caso al oficial de policía. | - |
| 1b | - | El sistema muestra un mensaje de error al oficial de policía indicando que no se pudo realizar la asignación en este momento debido a un problema técnico. |
| 1c | - | Se registra el error en un registro de errores para su posterior revisión. |
| 1d | - | El oficial de policía puede optar por volver al paso 1 para intentar nuevamente la asignación o finalizar el proceso de asignación. |

Enlaces:
* [Diagrama de clase](class-diagram.md#ecu-03-asignar-caso-a-un-oficial-de-policía)
* [Diagrama de secuencia](sequence-diagram.md#ecu-03-asignar-caso-a-un-oficial-de-policía)

[Volver al índice](#índice-de-ecu)

---

## ECU-04: Actualizar denuncia

**Descripción:** Permite al oficial asignado actualizar una denuncia policial existente.

**Actor(es):** Oficial asignado

**Pre-condiciones:** El oficial asignado debe tener los permisos necesarios y la denuncia debe existir previamente.

### **Flujo de eventos**

#### **Flujo principal**
| Paso | Actor | Sistema |
| --- | --- | --- |
| 1 | El oficial asignado solicita actualizar una denuncia existente. | - |
| 2 | - | El sistema busca la denuncia correspondiente en la blockchain. |
| 3 | - | El sistema muestra la información de la denuncia al oficial asignado. |
| 4 | El oficial asignado realiza las modificaciones necesarias en la denuncia o confirma la cancelación. | - |
| 5 | - | El sistema actualiza la denuncia en la blockchain. |

#### **Flujo alternativo** (Denuncia no encontrada)
| Paso | Actor | Sistema |
| --- | --- | --- |
| 2a | El sistema no encuentra la denuncia en la blockchain. | - |
| 2b | - | El sistema muestra un mensaje de error al oficial asignado indicando que la denuncia no se encontró. |
| 2c | - | El flujo vuelve al paso 1 para que el oficial asignado pueda intentar nuevamente. |

#### **Flujo de excepción** (Error en la conexión)
| Paso | Actor | Sistema |
| --- | --- | --- |
| 2a | Ocurre un error en la conexión con la blockchain. | - |
| 2b | - | El sistema muestra un mensaje de error al oficial asignado indicando que no se pudo acceder a la denuncia en este momento debido a un problema técnico. |
| 2c | - | Se registra el error en un registro de errores para su posterior revisión. |
| 2d | - | El flujo vuelve al paso 1 para que el oficial asignado pueda intentar nuevamente. |

Enlaces:
* [Diagrama de clase](class-diagram.md#ecu-04-actualizar-denuncia)
* [Diagrama de secuencia](sequence-diagram.md#ecu-04-actualizar-denuncia)

[Volver al índice](#índice-de-ecu)

---

## ECU-05: Generar informe de investigación [Trabajo futuro]

**Descripción:** Permite a los oficiales de policía generar un informe detallado sobre la investigación realizada en un caso específico.

**Actor(es):** Oficial de policía

**Pre-condiciones:** El oficial de policía debe tener acceso al caso de denuncia y haber completado la investigación.

### **Flujo de eventos**

#### **Flujo principal**
| Paso | Actor | Sistema |
| --- | --- | --- |
| 1 | El oficial de policía selecciona un caso. | - |
| 2 | - | El sistema consulta los detalles del caso en la blockchain. |
| 3 | - | El sistema muestra los detalles del caso al oficial de policía. |
| 4 | El oficial de policía completa el informe de investigación. | - |
| 5 | - | El sistema registra el informe de investigación en la blockchain. |

Enlaces:
* [Diagrama de clase](class-diagram.md#ecu-05-generar-informe-de-investigación-trabajo-futuro)
* [Diagrama de secuencia](sequence-diagram.md#ecu-05-generar-informe-de-investigación-trabajo-futuro)

[Volver al índice](#índice-de-ecu)

---

## ECU-06: Generar reporte estadístico [Trabajo futuro]

**Descripción:** Permite a los administradores del sistema generar informes estadísticos sobre las denuncias presentadas.

**Actor(es):** Administrador

**Pre-condiciones:** El administrador debe tener acceso autorizado al sistema.

### **Flujo de eventos**

#### **Flujo principal**
| Paso | Actor | Sistema |
| --- | --- | --- |
| 1 | El administrador selecciona los criterios de clasificación deseados. | - |
| 2 | - | El sistema accede a la blockchain y recopila los datos relevantes de las denuncias. |
| 3 | - | El sistema procesa los datos y genera un informe estadístico detallado. |

Enlaces:
* [Diagrama de clase](class-diagram.md#ecu-06-generar-reporte-estadístico-trabajo-futuro)
* [Diagrama de secuencia](sequence-diagram.md#ecu-06-generar-reporte-estadístico-trabajo-futuro)

[Volver al índice](#índice-de-ecu)

