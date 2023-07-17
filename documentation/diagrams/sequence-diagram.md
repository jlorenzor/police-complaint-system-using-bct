# Índice de Diagramas de Secuencia

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

```mermaid
sequenceDiagram
    participant Ciudadano as Ciudadano
    participant Sistema as Sistema

    Ciudadano ->> Sistema: Solicita registrar una denuncia
    activate Sistema
    Sistema ->> Ciudadano: Muestra el formulario de denuncia
    deactivate Sistema
    activate Ciudadano
    Ciudadano ->> Sistema: Completa el formulario con la información relevante
    deactivate Ciudadano
    activate Sistema
    alt Denuncia registrada exitosamente
        Sistema ->> Sistema: Valida y registra la denuncia en la blockchain
        Sistema ->> Ciudadano: Genera y muestra número de referencia como confirmación
    else Formulario incompleto
        Sistema ->> Ciudadano: Muestra mensaje de error (campos faltantes)
    else Error en la validación
        Sistema ->> Ciudadano: Muestra mensaje de error (problemas de validación)
    end
    deactivate Sistema
```
Enlaces:
* [Especificación de caso de uso](use-case-specification.md#ecu-01-registrar-denuncia)
* [Diagrama de clase](class-diagram.md#ecu-01-registrar-denuncia)

[Volver al índice](#índice-de-diagramas-de-secuencia)

---

## ECU-02: Consultar estado e historial de denuncia

**Descripción:** Permite a los usuarios verificar el estado actual y el historial de una denuncia registrada anteriormente.

**Actor(es):** Ciudadano

**Pre-condiciones:** El ciudadano debe tener un número de referencia de denuncia válido.

```mermaid
sequenceDiagram
    participant Ciudadano as Ciudadano
    participant Sistema as Sistema

    Ciudadano ->> Sistema: Ingresa el número de referencia de la denuncia
    activate Sistema
    alt Consulta exitosa
        Sistema ->> Sistema: Busca la denuncia en la blockchain
        Sistema ->> Ciudadano: Muestra el estado actual de la denuncia y su historial
    else Número de referencia inválido
        Sistema ->> Ciudadano: Muestra mensaje de error (número de referencia incorrecto)
    else Error en la consulta
        Sistema ->> Ciudadano: Muestra mensaje de error (problema técnico)
        Sistema ->> Sistema: Registra el error en un registro de errores
    end
    deactivate Sistema
```
Enlaces:
* [Especificación de caso de uso](use-case-specification.md#ecu-02-consultar-estado-e-historial-de-denuncia)
* [Diagrama de clase](class-diagram.md#ecu-02-consultar-estado-e-historial-de-denuncia)

[Volver al índice](#índice-de-diagramas-de-secuencia)

---

## ECU-03: Asignar caso a un oficial de policía

**Descripción:** Permite a los funcionarios de policía asignar casos de denuncia a oficiales específicos para su investigación.

**Actor(es):** Oficial de policía

**Pre-condiciones:** El caso de denuncia debe estar disponible y sin asignar.

```mermaid
sequenceDiagram
    participant Oficial as Oficial de Policía
    participant Sistema as Sistema

    Oficial ->> Sistema: Selecciona un caso sin asignar
    activate Sistema
    alt Asignación exitosa
        Sistema ->> Sistema: Asigna el caso al oficial de policía en la blockchain
        Sistema ->> Oficial: Muestra mensaje de confirmación
    else No hay casos disponibles
        Sistema ->> Oficial: Muestra mensaje (no hay casos disponibles)
    else Error en la asignación
        Sistema ->> Oficial: Muestra mensaje de error (problema técnico)
        Sistema ->> Sistema: Registra el error en un registro de errores
    end
    deactivate Sistema
```
Enlaces:
* [Especificación de caso de uso](use-case-specification.md#ecu-03-asignar-caso-a-un-oficial-de-policía)
* [Diagrama de clase](class-diagram.md#ecu-03-asignar-caso-a-un-oficial-de-policía)

[Volver al índice](#índice-de-diagramas-de-secuencia)

---

## ECU-04: Actualizar denuncia

**Descripción:** Permite al oficial asignado actualizar una denuncia policial existente.

**Actor(es):** Oficial asignado

**Pre-condiciones:** El oficial asignado debe tener los permisos necesarios y la denuncia debe existir previamente.

```mermaid
sequenceDiagram
    participant Oficial as Oficial Asignado
    participant Sistema as Sistema

    Oficial ->> Sistema: Solicita actualizar una denuncia existente
    activate Sistema
    Sistema ->> Sistema: Busca la denuncia correspondiente en la blockchain
    alt Denuncia encontrada
        Sistema ->> Oficial: Muestra la información de la denuncia
        Oficial ->> Sistema: Realiza las modificaciones necesarias en la denuncia o confirma la cancelación
        Sistema ->> Sistema: Actualiza la denuncia en la blockchain
        Sistema ->> Oficial: Muestra mensaje de confirmación
    else Denuncia no encontrada
        Sistema ->> Oficial: Muestra mensaje de error (denuncia no encontrada)
    else Error en la conexión
        Sistema ->> Oficial: Muestra mensaje de error (problema técnico)
        Sistema ->> Sistema: Registra el error en un registro de errores
    end
    deactivate Sistema
```
Enlaces:
* [Especificación de caso de uso](use-case-specification.md#ecu-04-actualizar-denuncia)
* [Diagrama de clase](class-diagram.md#ecu-04-actualizar-denuncia)

[Volver al índice](#índice-de-diagramas-de-secuencia)

---

## ECU-05: Generar informe de investigación [Trabajo futuro]

**Descripción:** Permite a los oficiales de policía generar un informe detallado sobre la investigación realizada en un caso específico.

**Actor(es):** Oficial de policía

**Pre-condiciones:** El oficial de policía debe tener acceso al caso de denuncia y haber completado la investigación.

```mermaid
sequenceDiagram
    participant Oficial as Oficial de Policía
    participant Sistema as Sistema

    Oficial ->> Sistema: Selecciona un caso
    activate Sistema
    Sistema ->> Sistema: Consulta los detalles del caso en la blockchain
    Sistema ->> Oficial: Muestra los detalles del caso
    Oficial ->> Sistema: Completa el informe de investigación
    Sistema ->> Sistema: Registra el informe de investigación en la blockchain
    Sistema ->> Oficial: Muestra mensaje de confirmación
    deactivate Sistema
```

Enlaces:
* [Especificación de caso de uso](use-case-specification.md#ecu-05-generar-informe-de-investigación-trabajo-futuro)
* [Diagrama de clase](class-diagram.md#ecu-05-generar-informe-de-investigación-trabajo-futuro)

[Volver al índice](#índice-de-diagramas-de-secuencia)

---

## ECU-06: Generar reporte estadístico [Trabajo futuro]

**Descripción:** Permite a los administradores del sistema generar informes estadísticos sobre las denuncias presentadas.

**Actor(es):** Administrador

**Pre-condiciones:** El administrador debe tener acceso autorizado al sistema.

```mermaid
sequenceDiagram
    participant Administrador as Administrador
    participant Sistema as Sistema

    Administrador ->> Sistema: Selecciona los criterios de clasificación deseados
    activate Sistema
    Sistema ->> Sistema: Accede a la blockchain y recopila los datos relevantes de las denuncias
    Sistema ->> Sistema: Procesa los datos y genera un informe estadístico detallado
    Sistema ->> Administrador: Muestra el informe estadístico
    deactivate Sistema
```

Enlaces:
* [Especificación de caso de uso](use-case-specification.md#ecu-06-generar-reporte-estadístico-trabajo-futuro)
* [Diagrama de clase](class-diagram.md#ecu-06-generar-reporte-estadístico-trabajo-futuro)

[Volver al índice](#índice-de-diagramas-de-secuencia)
