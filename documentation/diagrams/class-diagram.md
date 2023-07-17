# Índice de Diagramas de Clase

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
classDiagram
    class Complaint {
        +referenceNumber: String
        +information: String
        +status: String
        +date: Date
        +registerComplaint(information: String): void
        +validateInformation(): Boolean
        +generateReferenceNumber(): String
    }

    class Citizen {
        +name: String
        +identification: String
        +submitComplaint(complaint: Complaint): void
    }

    class System {
        +displayForm(): void
        +registerComplaintInBlockchain(complaint: Complaint): void
        +displayMessage(message: String): void
    }

    Citizen --> Complaint: Submits complaint
    Complaint --> System: Registers in the system
    System --> Citizen: Displays message to user
```

Enlaces:

- [Especificación de caso de uso](use-case-specification.md#ecu-01-registrar-denuncia)
- [Diagrama de secuencia](sequence-diagram.md#ecu-01-registrar-denuncia)

[Volver al índice](#índice-de-diagramas-de-clase)

---

## ECU-02: Consultar estado e historial de denuncia

**Descripción:** Permite a los usuarios verificar el estado actual y el historial de una denuncia registrada anteriormente.

**Actor(es):** Ciudadano

**Pre-condiciones:** El ciudadano debe tener un número de referencia de denuncia válido.

```mermaid
classDiagram
    class Complaint {
        +referenceNumber: String
        +information: String
        +status: String
        +history: String[]
        +date: Date
        +checkStatus(): String
        +checkHistory(): String[]
    }

    class Citizen {
        +name: String
        +identification: String
        +checkComplaint(referenceNumber: String): Complaint
    }

    class System {
        +searchComplaint(referenceNumber: String): Complaint
        +displayStatusAndHistory(complaint: Complaint): void
        +displayMessage(message: String): void
    }

    Citizen --> System: Query complaint
    System --> Complaint: Search complaint
    Complaint --> System: Provide status and history
    System --> Citizen: Display status and history
```

Enlaces:

- [Especificación de caso de uso](use-case-specification.md#ecu-02-consultar-estado-e-historial-de-denuncia)
- [Diagrama de secuencia](sequence-diagram.md#ecu-02-consultar-estado-e-historial-de-denuncia)

[Volver al índice](#índice-de-diagramas-de-clase)

---

## ECU-03: Asignar caso a un oficial de policía

**Descripción:** Permite a los funcionarios de policía asignar casos de denuncia a oficiales específicos para su investigación.

**Actor(es):** Oficial de policía

**Pre-condiciones:** El caso de denuncia debe estar disponible y sin asignar.

```mermaid
classDiagram
    class Complaint {
        +referenceNumber: String
        +information: String
        +status: String
        +history: String[]
        +date: Date
        +checkStatus(): String
        +checkHistory(): String[]
    }

    class Citizen {
        +name: String
        +identification: String
        +checkComplaint(referenceNumber: String): Complaint
    }

    class System {
        +searchComplaint(referenceNumber: String): Complaint
        +displayStatusAndHistory(complaint: Complaint): void
        +displayMessage(message: String): void
    }

    Citizen --> System: Check complaint
    System --> Complaint: Search complaint
    Complaint --> System: Provide status and history
    System --> Citizen: Display status and history
```

Enlaces:

- [Especificación de caso de uso](use-case-specification.md#ecu-03-asignar-caso-a-un-oficial-de-policía)
- [Diagrama de secuencia](sequence-diagram.md#ecu-03-asignar-caso-a-un-oficial-de-policía)

[Volver al índice](#índice-de-diagramas-de-clase)

---

## ECU-04: Actualizar denuncia

**Descripción:** Permite al oficial asignado actualizar una denuncia policial existente.

**Actor(es):** Oficial asignado

**Pre-condiciones:** El oficial asignado debe tener los permisos necesarios y la denuncia debe existir previamente.

```mermaid
classDiagram
    class Complaint {
        +referenceNumber: String
        +information: String
        +status: String
        +date: Date
        +updateInformation(information: String): void
        +cancelComplaint(): void
    }

    class AssignedOfficer {
        +name: String
        +rank: String
        +updateComplaint(complaint: Complaint, information: String): void
        +cancelComplaint(complaint: Complaint): void
    }

    class System {
        +searchComplaint(referenceNumber: String): Complaint
        +updateComplaint(complaint: Complaint, information: String): void
        +cancelComplaint(complaint: Complaint): void
        +displayMessage(message: String): void
    }

    AssignedOfficer --> System: Requests to update complaint
    System --> Complaint: Searches for complaint
    Complaint --> System: Provides complaint
    System --> AssignedOfficer: Allows updating or canceling complaint

```

Enlaces:

- [Especificación de caso de uso](use-case-specification.md#ecu-04-actualizar-denuncia)
- [Diagrama de secuencia](sequence-diagram.md#ecu-04-actualizar-denuncia)

[Volver al índice](#índice-de-diagramas-de-clase)

---

## ECU-05: Generar informe de investigación [Trabajo futuro]

**Descripción:** Permite a los oficiales de policía generar un informe detallado sobre la investigación realizada en un caso específico.

**Actor(es):** Oficial de policía

**Pre-condiciones:** El oficial de policía debe tener acceso al caso de denuncia y haber completado la investigación.

```mermaid
classDiagram
    class CaseReport {
        +referenceNumber: String
        +information: String
        +status: String
        +date: Date
    }

    class InvestigationReport {
        +title: String
        +content: String
        +date: Date
        +generateReport(): void
    }

    class PoliceOfficer {
        +name: String
        +rank: String
        +selectCase(caseReport: CaseReport): void
        +completeReport(investigationReport: InvestigationReport): void
    }

    class System {
        +getCaseDetails(referenceNumber: String): CaseReport
        +registerReport(investigationReport: InvestigationReport): void
    }

    PoliceOfficer --> System: Select case and complete report
    System --> CaseReport: Query case details
    CaseReport --> System: Provide case details
    System --> InvestigationReport: Register investigation report

```

Enlaces:

- [Especificación de caso de uso](use-case-specification.md#ecu-05-generar-informe-de-investigación-trabajo-futuro)
- [Diagrama de secuencia](sequence-diagram.md#ecu-05-generar-informe-de-investigación-trabajo-futuro)

[Volver al índice](#índice-de-diagramas-de-clase)

---

## ECU-06: Generar reporte estadístico [Trabajo futuro]

**Descripción:** Permite a los administradores del sistema generar informes estadísticos sobre las denuncias presentadas.

**Actor(es):** Administrador

**Pre-condiciones:** El administrador debe tener acceso autorizado al sistema.

```mermaid
classDiagram
    class Complaint {
        +referenceNumber: String
        +information: String
        +status: String
        +date: Date
    }

    class StatisticalReport {
        +title: String
        +data: Object
        +generationDate: Date
        +generateReport(): void
    }

    class Administrator {
        +name: String
        +authorizedAccess: Boolean
        +selectCriteria(criteria: Object): void
        +generateStatisticalReport(): StatisticalReport
    }

    class System {
        +accessBlockchain(): Object
        +collectData(criteria: Object): Object
        +processData(data: Object): StatisticalReport
    }

    Administrator --> System: Select criteria and generate report
    System --> Complaint: Access complaint data
    System --> StatisticalReport: Generate statistical report
```

Enlaces:

- [Especificación de caso de uso](use-case-specification.md#ecu-06-generar-reporte-estadístico-trabajo-futuro)
- [Diagrama de secuencia](sequence-diagram.md#ecu-06-generar-reporte-estadístico-trabajo-futuro)

[Volver al índice](#índice-de-diagramas-de-clase)
