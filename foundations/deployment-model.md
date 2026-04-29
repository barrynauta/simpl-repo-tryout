<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../README.md">🏠 Home</a><br/>
    <a href="README.md">Foundations</a><br/>
        <strong>Deployment model</strong><br/>
</p>
</div>

# Deployment model

The deployment model of Simpl-Open — both the logical agent-and-cluster picture and the technical Kubernetes-and-cloud picture. This page combines two FTA sections that describe the same model from different angles: §2.8.1 captures the logical decomposition (agents per actor type, clusters per agent), and §6.2 captures the technical view (Kubernetes namespaces, ingress, persistence). Read together, they answer the question "what gets deployed where, by whom, on what."

## Logical deployment model — FTA §2.8.1

> Extracted verbatim from `Functional-and-Technical-Architecture-Specifications.md`, lines 1794–1805 (source dated 2026-04-20). Upstream link: [FTA spec §2.8.1](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#281-deployment-model).

####  2.8.1. <a name='Deploymentmodel'></a>Deployment model

The architecture of Simpl-Open follows a loosely coupled self-contained
architecture which groups components into building blocks, capability by
capability.  This approach permits the deployment Simpl-Open agent in
different flavours depending on the type of participant, e.g. an
Infrastructure Provider requires a different subset from the full
Simpl-Open stack than a Data Provider. This modular architecture within
a Data Space is presented on the following figure:

<img src="./media/image18.png" />


---

## Technology deployment view — FTA §6.2

> Extracted verbatim from `Functional-and-Technical-Architecture-Specifications.md`, lines 10912–10952 (source dated 2026-04-20). Upstream link: [FTA spec §6.2](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#62-technology-deployment-view).

###  6.2. <a name='TechnologyDeploymentView'></a>Technology Deployment View

The content presented in this section presents a view on the currently
available release for the GA, Data Provider, Infra Provider and
Consumer. Application Provider view falls behind the scope of the
current release.

The following Technology Deployment View describes how the different
technology components are deployed for all Simpl-Open agent types
(Governance Authority, Data Provider, Infrastructure Provider,
Application Provider, Consumer):

Simpl-Open is designed to be a container-native application and is
provided with all the required deployment artefacts to be deployed on a
pre-existing **Kubernetes Cluster**.

Each agent is deployed inside its own **Kubernetes Namespace**.

Three types of workloads are used:

1.  **Deployment** - used for managing a stateless application workload,
    where any Pod in the Deployment is interchangeable and can be
    replaced if needed.

2.  **StatefulSet** - used to run one or more related Pods that do track
    state somehow (for example, if the workload records data
    persistently). StatefulSet can match Pods with PersistentVolumes.

3.  **DaemonSet** - used for Pods that provide facilities that are local
    to nodes. Every time a node is added to the cluster, and it matches
    the specification in a DaemonSet, the control plane schedules a Pod
    for that DaemonSet onto the new node. Each pod in a DaemonSet
    performs a job similar to a system daemon on a classic Unix / POSIX
    server.

**Kubernetes Services** are used to expose certain components, running
as one or more pods, behind a single outward-facing endpoint, even when
the workload is split across multiple nodes.

<img src="./media/image159.png" />

