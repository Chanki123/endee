## Why a Vector Database?
Traditional databases perform exact or keyword-based searches, which fail to
capture semantic meaning in text. In this project, study notes are converted into
vector embeddings so that conceptually similar content can be retrieved even
when exact keywords do not match.

Endee is used as the vector database to efficiently store and search these
high-dimensional embeddings, enabling fast and accurate semantic search.

## Design Decisions
- Semantic Search was chosen as the use case because it clearly demonstrates
  the core value of a vector database.
- The project is structured to separate data ingestion, search logic, and
  configuration, following clean software design principles.
- Endee is treated as an external service, making the system scalable and
  easy to extend in real-world deployments.

## Scalability and Future Scope
In a production environment, Endee would run as a dedicated vector database
service (for example, using Docker or container orchestration). Additional
features such as Retrieval Augmented Generation (RAG), PDF ingestion, and
multi-user search can be built on top of this foundation without changing
the core architecture.

## Endee Setup Note
Endee is a high-performance vector database that runs as a service.
For this project, Endee can be deployed using Docker as provided by the official repository.
Due to environment and access constraints, this project focuses on demonstrating
the correct workflow, integration points, and usage of Endee as a vector database.

