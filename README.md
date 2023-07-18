# Police Complaint System Using Blockchain Technology

Este proyecto busca implementar un sistema de denuncias policiales basado en la tecnología blockchain. El sistema permitirá a los usuarios realizar denuncias policiales de manera descentralizada, sin la necesidad de un intermediario. Además, el sistema permitirá a los usuarios realizar seguimiento de las denuncias realizadas. 

En esta etapa, el proyecto se encuentra en la fase de analisis y diseño. Para ello, se ha realizado un análisis de requerimientos y un diseño de la arquitectura del sistema.

Comenzamos realizando una prueba de estrés con el protocolo de consenso HotStuff. Los resultados de la prueba de estrés se encuentran se pueden ver mediante gráficas en la siguiente tabla de contenidos en la sección de **Benchmarking**.

## Table of Contents
- [Documentation](https://github.com/jlorenzor/police-complaint-system-using-bct/blob/main/documentation)
  - [Proposal](https://github.com/jlorenzor/police-complaint-system-using-bct/blob/main/documentation/Proposal.md)
  - [Diagrams](https://github.com/jlorenzor/police-complaint-system-using-bct/tree/main/documentation/diagrams)
    - [Class Diagram](https://github.com/jlorenzor/police-complaint-system-using-bct/blob/main/documentation/diagrams/class-diagram.md)
    - [Sequence Diagram](https://github.com/jlorenzor/police-complaint-system-using-bct/blob/main/documentation/diagrams/sequence-diagram)
    - [Use Case Diagram](https://github.com/jlorenzor/police-complaint-system-using-bct/blob/main/documentation/diagrams/use-case-diagram)
- [Benchmarking](https://github.com/jlorenzor/police-complaint-system-using-bct/tree/main/hotstuff)
  - [Benchmarking Results](https://github.com/jlorenzor/police-complaint-system-using-bct/tree/main/hotstuff/benchmark/results)
    - [Faults vs TPS - Faults vs Latency - TPS vs Latency](https://github.com/jlorenzor/police-complaint-system-using-bct/blob/main/hotstuff/benchmark/results/plots/Faults.png)
    - [Nodes vs TPS - Nodes vs Latency - TPS vs Latency](https://github.com/jlorenzor/police-complaint-system-using-bct/blob/main/hotstuff/benchmark/results/plots/Nodes.png)
    - [Transaction Size vs TPS - Transaction Size vs Latency - TPS vs Latency](https://github.com/jlorenzor/police-complaint-system-using-bct/blob/main/hotstuff/benchmark/results/plots/Transaction%20Size.png)

## Créditos

Este proyecto utiliza código del repositorio [hotstuff](https://github.com/asonnino/hotstuff) de [asonnino](https://github.com/asonnino). Agradecemos a [asonnino](https://github.com/asonnino) por su trabajo en la implementación del protocolo de consenso HotStuff.

## Licencia

Este proyecto está licenciado bajo la licencia Apache 2.0 - vea el archivo [LICENSE](LICENSE) para más detalles.
