# Application Functional Capability Model Framework

**Document ID:** AFCM-2026-001
**Author:** Enterprise Architecture Team
**Domain:** Enterprise Architecture -- Application Portfolio
**Date:** 2026-02-08
**Version:** 1.0
**Status:** Draft
**Owner:** IT Architecture Team Leader
**Organization:** Cenovus Energy

---

## 1. Introduction

### 1.1 What Is an Application Functional Capability Model?

An Application Functional Capability Model (AFCM) is a structured taxonomy that describes **what applications do** -- the discrete functional capabilities that software applications provide, independent of any specific product, vendor, or technology. It is a classification framework that allows an Enterprise Architecture team to evaluate, compare, and categorize applications based on the functions they deliver rather than the brand names they carry.

Where a product catalogue lists applications by name and vendor, the AFCM abstracts away from specific products and instead asks: *What functional capabilities does this application deliver to the organization?*

Examples of functional capabilities include: data quality management, predictive analytics, workflow automation, API management, reservoir simulation, and general ledger processing. These are things that applications **do**, and many different products may deliver the same functional capability in different ways.

### 1.2 How the AFCM Differs from a Business Capability Model (BCM)

It is essential to understand the distinction between these two complementary models:

| Dimension | Business Capability Model (BCM) | Application Functional Capability Model (AFCM) |
|-----------|--------------------------------|------------------------------------------------|
| **Perspective** | Business perspective | Technology perspective |
| **Answers the question** | "What does the business do?" | "What do applications do?" |
| **Scope** | Business functions, outcomes, and value streams | Software functions, features, and technical services |
| **Independence** | Independent of how the business is organized or what technology it uses | Independent of which specific application or vendor delivers the capability |
| **Examples** | "Reservoir Management", "Crude Marketing", "Financial Reporting" | "Reservoir Simulation", "Data Visualization", "General Ledger Processing" |
| **Stability** | Very stable -- business capabilities rarely change | Moderately stable -- functional categories evolve with technology trends |
| **Owner** | Business leadership / EA | Enterprise Architecture |

**The BCM maps WHAT the business does. The AFCM maps WHAT applications do.**

### 1.3 How the Two Models Connect

The BCM and AFCM are connected through a many-to-many relationship:

- **Business capabilities are ENABLED BY application functional capabilities.** For example, the business capability "Production Optimization" may be enabled by the functional capabilities "Real-Time Data Historian", "Predictive Analytics", and "Process Simulation".
- **A single application functional capability may ENABLE multiple business capabilities.** For example, "Workflow Automation" enables "Procurement", "Regulatory Compliance", "Capital Project Governance", and many other business capabilities.
- **A single business capability may REQUIRE multiple functional capabilities.** For example, "Crude Marketing" may require "Financial Modelling", "Data Visualization", "Integration via API", and "Document Management".

This mapping is the critical linkage that allows the EA team to:
1. Understand which technology capabilities underpin which business capabilities.
2. Identify gaps where business capabilities lack adequate technology support.
3. Identify redundancy where multiple applications deliver the same functional capability.
4. Prioritize technology investments based on business capability importance.

### 1.4 How to Use This Framework

This framework supports several key EA activities:

**Application Assessment and Classification**
When evaluating a new or existing application, use this taxonomy to identify which functional capabilities the application delivers. Assign the relevant capability IDs (e.g., 2.3, 7.6, 10.2) to the application record. This creates a standardized, comparable view across the entire application portfolio.

**Portfolio Rationalization**
By mapping all applications to their functional capabilities, the EA team can identify:
- **Redundancy:** Multiple applications delivering the same functional capability (e.g., three different applications all providing 2.1 Dashboard & Scorecard Reporting).
- **Gaps:** Functional capabilities that the business needs but no current application delivers.
- **Consolidation opportunities:** Applications with overlapping functional capabilities that could be consolidated onto fewer platforms.

**Vendor and Product Evaluation**
When evaluating new products, map the vendor's features to this taxonomy. This allows objective, apples-to-apples comparison across competing products.

**Technology Roadmap Planning**
Identify which functional capability areas are maturing, declining, or emerging to inform investment decisions and sunset planning.

**Integration with the BCM**
For each application, map its functional capabilities (from this AFCM) to the business capabilities (from the BCM) that it enables. This creates a complete traceability chain: Business Capability <-- enabled by --> Functional Capability <-- delivered by --> Application.

---

## 2. Functional Capability Taxonomy

The following taxonomy defines 15 functional domains. Each domain contains specific functional capabilities numbered hierarchically (Domain.Capability). Each capability includes a description and the oil and gas business contexts where it is most commonly required.

---

### 1. Data Management

**Description:** Capabilities related to the storage, organization, movement, quality assurance, and governance of data across the enterprise. Data Management capabilities underpin virtually every other functional domain and are foundational to an integrated oil and gas operation.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 1.1 | Relational Data Storage | Storing and retrieving structured data in relational database systems with ACID compliance. | Enterprise-wide; ERP, production, financial, land, and regulatory data stores. |
| 1.2 | NoSQL / Document Storage | Storing and retrieving semi-structured or unstructured data in non-relational data stores (document, key-value, graph, columnar). | IoT sensor data, well log data, seismic metadata, equipment telemetry. |
| 1.3 | Data Warehouse / Lakehouse | Centralized analytical data repositories that consolidate data from multiple source systems for reporting and analytics. | Corporate reporting, production analytics, financial consolidation, ESG reporting. |
| 1.4 | Extract, Transform, Load (ETL/ELT) | Moving data between systems with transformation logic to reconcile formats, schemas, and business rules. | Production accounting, financial close, regulatory submissions, data migration. |
| 1.5 | Data Quality Management | Profiling, cleansing, standardizing, and monitoring data to ensure accuracy, completeness, and consistency. | Master data for wells, facilities, partners, vendors; regulatory reporting accuracy. |
| 1.6 | Master Data Management (MDM) | Establishing and maintaining a single authoritative source for critical business entities (wells, facilities, partners, materials, cost centres). | Well master, facility register, vendor master, material master, chart of accounts. |
| 1.7 | Data Cataloguing & Discovery | Indexing, tagging, and making data assets searchable and discoverable across the organization. | Enterprise data governance, self-service analytics enablement, data literacy. |
| 1.8 | Data Lineage & Provenance | Tracking the origin, transformation, and movement of data across systems to support auditability and trust. | SOX compliance, regulatory reporting, production allocation traceability. |
| 1.9 | Data Virtualization | Providing a unified view of data from multiple sources without physically moving or replicating the data. | Cross-domain analytics, real-time operational views combining ERP, SCADA, and historian data. |
| 1.10 | Data Archival & Retention | Managing the lifecycle of data including archival to lower-cost storage and deletion per retention policies. | Regulatory retention requirements, well records, seismic data, financial records. |
| 1.11 | Real-Time Data Streaming | Ingesting and processing continuous data streams with low latency for operational and analytical use. | SCADA data, IoT sensor feeds, commodity price feeds, safety system events. |
| 1.12 | Data Governance & Policy Enforcement | Defining and enforcing policies for data ownership, classification, access, and usage across the organization. | Enterprise-wide data governance programs, regulatory compliance, privacy. |

---

### 2. Analytics & Reporting

**Description:** Capabilities related to analyzing data and presenting insights to support operational and strategic decision-making. In oil and gas, analytics spans everything from daily production reporting to multi-year reservoir performance forecasting.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 2.1 | Dashboard & Scorecard Reporting | Presenting key metrics and KPIs in visual, interactive dashboards with drill-down capabilities. | Executive dashboards, production performance, HSE scorecards, financial KPIs. |
| 2.2 | Operational Reporting | Generating recurring, structured reports for day-to-day operational management and regulatory submission. | Daily production reports, well status reports, royalty reports, shift reports. |
| 2.3 | Ad-Hoc Query & Self-Service BI | Enabling business users to create their own queries, reports, and visualizations without IT involvement. | Engineering analysis, land administration, finance ad-hoc analysis, supply chain. |
| 2.4 | Data Visualization | Rendering data in charts, graphs, maps, and other visual formats to facilitate pattern recognition and communication. | Decline curve analysis, production trends, cost variance, reservoir performance. |
| 2.5 | Predictive Analytics | Applying statistical and machine learning models to historical data to forecast future outcomes. | Production forecasting, equipment failure prediction, commodity price modelling. |
| 2.6 | Prescriptive Analytics | Recommending optimal actions based on analytical models and constraints to improve decision-making. | Well spacing optimization, turnaround scheduling, blending optimization. |
| 2.7 | Embedded Analytics | Integrating analytical capabilities directly within operational applications so users access insights in context. | Analytics embedded in ERP, production accounting, maintenance management. |
| 2.8 | Geospatial Analytics | Analyzing data with a spatial dimension to identify geographic patterns, proximities, and correlations. | Well performance by area, pipeline integrity mapping, environmental monitoring. |
| 2.9 | Statistical Analysis | Performing advanced statistical methods including regression, hypothesis testing, and time-series analysis. | Reservoir engineering, process engineering, quality assurance, environmental monitoring. |
| 2.10 | Report Scheduling & Distribution | Automating the generation and delivery of reports on defined schedules to designated recipients. | Regulatory filing deadlines, board reporting, partner reporting, shift handover. |

---

### 3. Process Automation

**Description:** Capabilities related to automating business processes, workflows, and tasks to reduce manual effort, improve consistency, and accelerate cycle times. In oil and gas, process automation spans office workflows, field operations, and everything in between.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 3.1 | Workflow Automation | Defining and executing multi-step business processes with routing, conditions, and notifications. | AFE approvals, MOC processes, procurement requisitions, regulatory submissions. |
| 3.2 | Robotic Process Automation (RPA) | Automating repetitive, rule-based tasks by mimicking human interactions with application user interfaces. | Invoice processing, data entry across legacy systems, report generation, reconciliation. |
| 3.3 | Business Process Management (BPM) | Modelling, orchestrating, monitoring, and optimizing end-to-end business processes across systems. | Capital project governance, well delivery, turnaround planning, incident management. |
| 3.4 | Approval Routing & Escalation | Managing approval hierarchies with delegation, escalation rules, and SLA tracking. | AFE approvals, invoice approvals, MOC approvals, permit-to-work, contractor onboarding. |
| 3.5 | Task Scheduling & Orchestration | Scheduling and sequencing automated tasks, batch jobs, and processes across systems. | Nightly batch processing, production allocation runs, data loads, report generation. |
| 3.6 | Forms & Data Capture | Providing digital forms for structured data collection with validation rules and conditional logic. | Field inspections, safety observations, well test data, environmental sampling. |
| 3.7 | Business Rules Engine | Externalizing and managing business rules that drive automated decisions outside of application code. | Royalty calculations, production allocation, compliance checks, pricing rules. |
| 3.8 | Low-Code / No-Code Application Development | Enabling rapid application development through visual, drag-and-drop interfaces with minimal coding. | Departmental tools, field data capture apps, custom dashboards, process apps. |
| 3.9 | Notification & Alert Management | Sending targeted notifications and alerts to users based on events, thresholds, or workflow states. | Alarm notifications, approval reminders, compliance deadlines, safety alerts. |
| 3.10 | Document Generation & Templating | Automatically generating documents from templates using data from business systems. | Contracts, regulatory filings, well completion reports, board presentations. |

---

### 4. Integration & Connectivity

**Description:** Capabilities related to connecting applications, systems, data sources, and devices to enable data flow and process coordination across the enterprise. Integration is particularly critical in oil and gas where IT and OT systems must work together seamlessly.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 4.1 | API Management | Publishing, securing, versioning, and monitoring APIs for controlled access to application services and data. | ERP integration, partner data exchange, mobile app backends, cloud service access. |
| 4.2 | Enterprise Service Bus (ESB) | Providing a centralized middleware platform for routing, transforming, and orchestrating messages between systems. | Legacy system integration, ERP to subsystem communication, canonical data model. |
| 4.3 | Integration Platform as a Service (iPaaS) | Cloud-based integration platform for connecting SaaS, on-premise, and hybrid applications. | SaaS-to-SaaS integration, cloud migration, hybrid cloud connectivity. |
| 4.4 | Event Streaming & Messaging | Publishing and subscribing to real-time event streams and asynchronous messages between systems. | SCADA data distribution, IoT event processing, real-time production events. |
| 4.5 | Managed File Transfer (MFT) | Securely transferring files between internal systems, partners, and external parties with tracking and audit. | Regulatory file submissions, partner data exchange, bank file transfers, EDI. |
| 4.6 | OPC / SCADA Connectivity | Connecting to operational technology systems using OPC-UA/DA, Modbus, and other industrial protocols. | SCADA to historian, SCADA to IT systems, field device integration. |
| 4.7 | Database Connectivity & Replication | Connecting directly to databases for data extraction, replication, or change data capture (CDC). | Data warehouse loading, cross-system data sync, disaster recovery replication. |
| 4.8 | EDI & B2B Integration | Exchanging structured business documents with external partners using EDI, AS2, or similar B2B protocols. | Supplier purchase orders, invoices, shipping notices, crude nominations. |
| 4.9 | Webhook & Event Notification | Providing HTTP-based event notifications to trigger actions in subscribing systems when events occur. | SaaS application integration, CI/CD pipelines, monitoring alert routing. |
| 4.10 | Data Federation & Virtual Integration | Querying data across multiple sources through a unified virtual layer without physical data movement. | Cross-domain reporting, operational dashboards combining IT and OT data. |
| 4.11 | IoT Device Connectivity | Connecting to and managing Internet of Things (IoT) devices including sensors, gateways, and edge devices. | Remote well monitoring, pipeline sensors, tank level monitoring, environmental sensors. |

---

### 5. User Experience & Collaboration

**Description:** Capabilities related to how users interact with applications and collaborate with each other. Effective user experience and collaboration capabilities are critical for dispersed oil and gas workforces spanning head office, field operations, and remote locations.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 5.1 | Web Portal & Intranet | Providing a browser-based interface for accessing information, applications, and services from a unified entry point. | Corporate intranet, employee self-service, partner portals, contractor portals. |
| 5.2 | Mobile Application Support | Delivering application functionality on mobile devices (phones and tablets) for field and remote use. | Field inspections, mobile work orders, remote approvals, safety observations. |
| 5.3 | Unified Communications | Integrating voice, video, messaging, and presence into a single communication platform. | Team collaboration, field-to-office communication, emergency response. |
| 5.4 | Team Collaboration Workspaces | Providing shared digital workspaces for teams to collaborate on projects, documents, and tasks. | Project teams, turnaround planning, joint venture coordination, well delivery. |
| 5.5 | Real-Time Chat & Messaging | Enabling instant text-based communication between individuals and groups with persistent history. | Operational coordination, shift handover, cross-functional communication. |
| 5.6 | Video Conferencing | Providing live video communication for meetings, presentations, and remote collaboration. | Remote site meetings, vendor reviews, board meetings, training sessions. |
| 5.7 | Email & Calendar Management | Managing electronic mail, calendaring, scheduling, and meeting coordination. | Enterprise-wide communication, meeting scheduling, resource booking. |
| 5.8 | Notification & Push Alerts | Delivering contextual alerts and notifications to users across channels (email, mobile push, in-app, SMS). | Safety alerts, approval requests, system notifications, escalation notices. |
| 5.9 | Knowledge Management & Wiki | Creating, organizing, and sharing institutional knowledge in searchable, collaborative knowledge bases. | Operational procedures, engineering standards, lessons learned, best practices. |
| 5.10 | Survey & Feedback Collection | Gathering structured feedback from users, employees, or stakeholders through surveys and polls. | Employee engagement, safety culture surveys, post-project reviews, vendor feedback. |

---

### 6. Security & Access Control

**Description:** Capabilities related to protecting applications, data, and users from unauthorized access, threats, and compliance violations. Security capabilities are especially critical in oil and gas where operational technology environments, sensitive production data, and regulatory requirements create a broad threat surface.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 6.1 | Authentication & Single Sign-On (SSO) | Verifying user identity and providing seamless access across multiple applications through federated authentication. | Enterprise SSO, multi-factor authentication, contractor access, cloud app access. |
| 6.2 | Authorization & Role-Based Access Control | Controlling what authenticated users can access and perform based on roles, attributes, and policies. | ERP role design, data-level security, field system access, partner data segregation. |
| 6.3 | Privileged Access Management (PAM) | Securing, monitoring, and auditing elevated-privilege accounts used for system administration. | Server administration, database administration, SCADA system access, vendor remote access. |
| 6.4 | Data Encryption (at rest and in transit) | Protecting data confidentiality through encryption during storage and transmission. | Financial data, personal information, seismic data, proprietary reservoir models. |
| 6.5 | Audit Logging & Monitoring | Recording and monitoring user and system activities for security investigation and compliance purposes. | SOX compliance, access reviews, incident investigation, regulatory audit trail. |
| 6.6 | Data Loss Prevention (DLP) | Detecting and preventing unauthorized transmission of sensitive data outside approved boundaries. | Intellectual property protection, PII protection, financial data controls. |
| 6.7 | Identity Governance & Lifecycle | Managing the full lifecycle of user identities including provisioning, access reviews, and deprovisioning. | Joiner-mover-leaver processes, contractor lifecycle, SOX access reviews. |
| 6.8 | Secrets & Certificate Management | Securely storing and rotating API keys, passwords, certificates, and other secrets used by applications. | API security, service account management, TLS certificate lifecycle. |
| 6.9 | Threat Detection & Response | Identifying and responding to security threats including intrusion detection, SIEM, and incident response. | SOC operations, OT security monitoring, ransomware detection, insider threat. |
| 6.10 | Vulnerability Management | Scanning for, prioritizing, and remediating security vulnerabilities in applications and infrastructure. | Application security, infrastructure patching, OT vulnerability assessment. |
| 6.11 | Network Segmentation & Zero Trust | Enforcing network-level access controls and micro-segmentation to limit lateral movement. | IT/OT network segmentation, cloud network security, remote access architecture. |

---

### 7. AI & Machine Learning

**Description:** Capabilities related to applying artificial intelligence and machine learning techniques to automate decisions, generate insights, and augment human capabilities. AI/ML adoption in oil and gas is accelerating across exploration, production optimization, maintenance, and corporate functions.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 7.1 | ML Model Training & Development | Building, training, and validating machine learning models using historical data and feature engineering. | Production forecasting models, equipment failure models, image recognition models. |
| 7.2 | ML Model Deployment & Inference | Deploying trained models into production for real-time or batch inference on new data. | Real-time well optimization, predictive maintenance scoring, anomaly detection. |
| 7.3 | Natural Language Processing (NLP) | Extracting meaning, entities, sentiment, and structure from unstructured text data. | Regulatory document analysis, incident report classification, contract review. |
| 7.4 | Computer Vision & Image Recognition | Analyzing images and video to detect objects, anomalies, and patterns using visual AI. | Pipeline corrosion detection, flare monitoring, PPE compliance, drone inspection. |
| 7.5 | Generative AI & Large Language Models | Generating text, code, summaries, and other content using large pre-trained language models. | Document drafting, code generation, knowledge assistant, meeting summarization. |
| 7.6 | Optimization & Operations Research | Applying mathematical optimization to find optimal solutions under constraints. | Production scheduling, blending optimization, logistics routing, capital allocation. |
| 7.7 | Anomaly Detection | Identifying unusual patterns in data that deviate from expected behaviour for alerting and investigation. | Equipment anomaly detection, pipeline leak detection, financial fraud detection. |
| 7.8 | Recommendation Systems | Suggesting actions, items, or configurations based on patterns, preferences, and context. | Spare parts recommendations, well design optimization, training recommendations. |
| 7.9 | MLOps & Model Lifecycle Management | Managing the end-to-end lifecycle of ML models including versioning, monitoring, retraining, and governance. | Model registry, drift detection, A/B testing, model performance monitoring. |
| 7.10 | AI-Powered Search & Retrieval | Enhancing search with AI to understand intent, rank relevance, and retrieve answers from knowledge bases. | Technical document search, procedure lookup, enterprise knowledge retrieval. |

---

### 8. Geospatial & Mapping

**Description:** Capabilities related to capturing, storing, analyzing, and visualizing data with a geographic or spatial dimension. Geospatial capabilities are a distinguishing requirement for oil and gas, where nearly every asset -- wells, pipelines, facilities, lease boundaries -- has a location.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 8.1 | Geographic Information System (GIS) | Storing, managing, and visualizing spatial data with layered maps and geographic databases. | Land management, pipeline mapping, well mapping, environmental assessment. |
| 8.2 | Spatial Data Analysis | Performing geographic calculations including proximity, overlay, buffer, and network analysis. | Well spacing analysis, pipeline route optimization, environmental impact zones. |
| 8.3 | Well Mapping & Visualization | Displaying well locations, trajectories, lateral extents, and associated attributes on maps. | Drilling planning, production visualization, regulatory compliance, land administration. |
| 8.4 | Pipeline Route Management | Mapping, managing, and analyzing pipeline routes, rights-of-way, and associated infrastructure. | Integrity management, regulatory compliance, expansion planning, ROW management. |
| 8.5 | Land & Mineral Rights Management | Managing spatial data related to surface and mineral rights, lease boundaries, and land agreements. | Land acquisition, lease management, royalty administration, surface access. |
| 8.6 | Remote Sensing & Satellite Imagery | Acquiring and analyzing imagery from satellites, drones, and aerial surveys for monitoring and assessment. | Environmental monitoring, leak detection, construction progress, vegetation assessment. |
| 8.7 | Field Mapping & GPS Data Collection | Capturing geographic data in the field using GPS-enabled devices and mobile mapping applications. | Well site surveys, pipeline inspections, environmental sampling, facility mapping. |
| 8.8 | 3D Subsurface Visualization | Displaying and interacting with three-dimensional representations of subsurface geology and well data. | Reservoir characterization, well planning, geological interpretation. |
| 8.9 | Location Intelligence & Geocoding | Converting addresses and descriptions to coordinates and enriching data with location-based context. | Vendor locations, incident mapping, regulatory jurisdiction determination. |

---

### 9. Simulation & Modelling

**Description:** Capabilities related to creating mathematical representations of physical systems, financial scenarios, or operational processes to predict behaviour and evaluate alternatives. Simulation is a core competency in oil and gas, particularly in reservoir engineering, process engineering, and financial planning.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 9.1 | Reservoir Simulation | Modelling fluid flow through porous media to predict reservoir performance and optimize recovery strategies. | Reservoir management, well placement, EOR evaluation, reserves estimation. |
| 9.2 | Process Simulation | Modelling chemical and physical processes in facilities (e.g., separation, fractionation, upgrading). | Facility design, debottlenecking, energy optimization, emissions reduction. |
| 9.3 | Financial Modelling & Valuation | Building quantitative models to project financial performance, value assets, and evaluate investments. | Asset acquisition/divestiture, capital budgeting, reserves reporting, strategic planning. |
| 9.4 | Scenario Planning & What-If Analysis | Evaluating multiple future scenarios by varying assumptions and parameters to assess outcomes. | Commodity price scenarios, development plan options, risk assessment, strategic planning. |
| 9.5 | Decline Curve Analysis | Modelling production decline over time to forecast future production volumes and remaining reserves. | Reserves estimation, production forecasting, well economics, acquisition evaluation. |
| 9.6 | Pipeline Hydraulic Modelling | Simulating fluid flow through pipeline networks to assess capacity, pressure, and operational constraints. | Pipeline design, capacity planning, operational optimization, integrity assessment. |
| 9.7 | Wellbore Simulation | Modelling wellbore conditions including pressure, temperature, and flow to optimize drilling and completion. | Well design, artificial lift optimization, well intervention planning. |
| 9.8 | Structural & Mechanical Simulation | Simulating mechanical stress, fatigue, and structural integrity of physical assets and equipment. | Pressure vessel design, structural assessment, turnaround scope planning. |
| 9.9 | Monte Carlo & Probabilistic Analysis | Running probabilistic simulations using random sampling to quantify uncertainty and risk distributions. | Reserves estimation, project cost risk, production forecasting uncertainty. |
| 9.10 | Digital Twin | Creating a real-time virtual replica of a physical asset or process fed by live data for monitoring and optimization. | Facility digital twins, well digital twins, pipeline digital twins. |

---

### 10. Real-Time Monitoring & Control

**Description:** Capabilities related to observing, recording, and controlling physical processes and equipment in real time. These capabilities bridge the IT/OT boundary and are fundamental to safe and efficient oil and gas operations.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 10.1 | SCADA (Supervisory Control and Data Acquisition) | Monitoring and controlling remote field equipment and processes through centralized supervisory systems. | Well site monitoring, pipeline operations, facility operations, water management. |
| 10.2 | Data Historian | Time-series data storage optimized for high-frequency, high-volume operational data with long retention. | Production data, process data, equipment telemetry, environmental monitoring data. |
| 10.3 | Alarm Management | Configuring, prioritizing, and managing operational alarms to ensure appropriate operator response. | Control room operations, safety system alarms, equipment threshold alerts. |
| 10.4 | Process Control (DCS/PLC) | Executing automated control logic to maintain process variables within set points using distributed control systems. | Facility process control, compressor control, injection systems, separation. |
| 10.5 | Edge Computing & Gateway | Processing data at or near the source (field level) to reduce latency and bandwidth requirements. | Remote well optimization, field data preprocessing, intermittent connectivity sites. |
| 10.6 | Condition Monitoring | Continuously monitoring equipment condition parameters (vibration, temperature, pressure) to detect degradation. | Rotating equipment, pumps, compressors, heat exchangers, motors. |
| 10.7 | Remote Operations & Visualization | Providing centralized visibility and control over geographically dispersed field assets. | Integrated operations centre, remote well pad monitoring, pipeline surveillance. |
| 10.8 | Safety Instrumented Systems (SIS) | Managing safety-critical control functions that bring processes to a safe state when hazardous conditions are detected. | Emergency shutdown, fire and gas detection, high-integrity pressure protection. |
| 10.9 | Video Surveillance & Monitoring | Capturing and monitoring live video feeds from operational sites for security and safety purposes. | Facility perimeter security, flare monitoring, tank farm surveillance, remote site monitoring. |
| 10.10 | Emissions Monitoring & Reporting | Measuring, recording, and reporting greenhouse gas and other emissions from operational sources. | Regulatory reporting, carbon management, ESG disclosure, leak detection and repair. |

---

### 11. Document & Content Management

**Description:** Capabilities related to creating, storing, organizing, versioning, and retrieving documents and digital content. Oil and gas organizations generate enormous volumes of technical documents, engineering drawings, regulatory filings, and operational records that must be managed throughout their lifecycle.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 11.1 | Document Storage & Repository | Providing secure, organized storage for documents and files with folder structures and metadata. | Engineering documents, contracts, regulatory filings, well files, HSE records. |
| 11.2 | Version Control & Check-In/Check-Out | Tracking document revisions, maintaining version history, and managing concurrent access. | Engineering drawings, procedures, contracts, regulatory submissions. |
| 11.3 | Records Management & Retention | Classifying documents as records and managing retention schedules, holds, and disposition per policy. | Regulatory retention, well records, financial records, legal hold, audit records. |
| 11.4 | Enterprise Search & Discovery | Enabling full-text and metadata-based search across document repositories to find information quickly. | Cross-repository search, engineering document retrieval, policy lookup. |
| 11.5 | Document Archival & Long-Term Preservation | Preserving documents in durable formats for long-term retention beyond active operational use. | Well abandonment records, historical production records, regulatory archives. |
| 11.6 | Engineering Document Management | Specialized management of engineering drawings, P&IDs, datasheets, and technical specifications with revision control. | Facility engineering, capital projects, turnaround planning, MOC documentation. |
| 11.7 | Digital Signature & E-Signature | Enabling legally binding electronic signatures on documents and forms. | Contract execution, regulatory submissions, approval documentation, land agreements. |
| 11.8 | Content Collaboration & Co-Authoring | Allowing multiple users to simultaneously create and edit documents in real time. | Report writing, procedure development, project documentation, presentation creation. |
| 11.9 | Optical Character Recognition (OCR) | Converting scanned documents and images into machine-readable text for search and processing. | Digitizing legacy paper records, invoice processing, historical well file conversion. |
| 11.10 | Media Asset Management | Managing rich media assets including images, video, audio, and 3D models with metadata and access control. | Drone inspection footage, facility photographs, training videos, 3D models. |

---

### 12. Financial Management

**Description:** Capabilities related to managing the financial operations of the enterprise including accounting, budgeting, forecasting, treasury, and tax. Financial management capabilities are critical for oil and gas companies that deal with complex joint ventures, royalty obligations, commodity accounting, and multi-jurisdictional tax requirements.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 12.1 | General Ledger & Chart of Accounts | Recording and classifying all financial transactions in a structured chart of accounts. | Corporate accounting, joint venture accounting, cost centre reporting. |
| 12.2 | Accounts Payable | Processing vendor invoices, managing payment terms, executing payments, and reconciling payables. | Vendor payments, contractor payments, field ticket processing, intercompany. |
| 12.3 | Accounts Receivable | Managing customer billing, revenue recognition, collections, and receivables reconciliation. | Crude sales, NGL sales, by-product sales, joint venture billings. |
| 12.4 | Budgeting & Planning | Creating, managing, and tracking operational and capital budgets with version control and workflow. | Annual budget cycle, capital budget, operating budget, rolling forecasts. |
| 12.5 | Financial Forecasting | Projecting future financial performance using models, trends, and scenario assumptions. | Cash flow forecasting, revenue forecasting, cost forecasting, guidance preparation. |
| 12.6 | Financial Consolidation & Close | Aggregating financial results from subsidiaries and business units with eliminations and adjustments. | Monthly/quarterly close, SEC reporting, intercompany elimination, currency translation. |
| 12.7 | Treasury & Cash Management | Managing cash positions, banking relationships, debt, investments, and liquidity. | Cash pooling, debt management, commodity hedging settlement, banking operations. |
| 12.8 | Tax Management | Calculating, reporting, and managing corporate taxes including income tax, royalties, and indirect taxes. | Income tax provision, royalty calculation, GST/HST, US state tax, transfer pricing. |
| 12.9 | Fixed Asset Accounting | Tracking the financial lifecycle of capital assets including capitalization, depreciation, and disposal. | Well assets, facility assets, pipeline assets, right-of-use assets, impairment. |
| 12.10 | Joint Venture Accounting | Managing financial arrangements with joint venture partners including billing, netting, and audit. | Operating agreements, joint interest billing, partner audits, cash calls. |
| 12.11 | Production Revenue Accounting | Tracking commodity production volumes, pricing, and revenue allocation for accounting and royalty purposes. | Crown royalty, freehold royalty, overriding royalty, production sharing. |
| 12.12 | Procurement & Spend Management | Managing purchasing processes from requisition through payment including sourcing, contracts, and catalogs. | Material procurement, services procurement, strategic sourcing, contract management. |

---

### 13. Asset & Maintenance Management

**Description:** Capabilities related to managing the lifecycle of physical assets and the maintenance programs that keep them operating safely and efficiently. Asset-intensive industries like oil and gas rely heavily on these capabilities to maximize production, minimize downtime, and ensure regulatory compliance.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 13.1 | Asset Registry & Hierarchy | Maintaining a structured registry of all physical assets with parent-child relationships and attributes. | Well inventory, facility equipment, pipeline segments, vehicles, IT assets. |
| 13.2 | Work Order Management | Creating, assigning, tracking, and closing maintenance work orders with labour, materials, and cost tracking. | Corrective maintenance, field maintenance, facility maintenance, turnaround work. |
| 13.3 | Preventive Maintenance Scheduling | Scheduling recurring maintenance activities based on time, usage, or condition triggers. | Rotating equipment PM, safety device testing, pipeline pigging, vehicle maintenance. |
| 13.4 | Predictive Maintenance | Using data analytics and condition monitoring to predict when equipment will fail and schedule maintenance proactively. | Compressor monitoring, pump analysis, heat exchanger fouling, ESP monitoring. |
| 13.5 | Reliability Engineering | Analyzing equipment failure patterns, calculating reliability metrics, and identifying improvement opportunities. | RCA, FMEA, bad actor programs, reliability growth analysis. |
| 13.6 | Inspection Management | Planning, executing, recording, and tracking equipment inspections per regulatory and engineering requirements. | Pressure vessel inspection, pipeline integrity, safety device inspection, API inspections. |
| 13.7 | Turnaround & Shutdown Planning | Planning and managing major facility shutdowns including scope, schedule, resources, and cost. | Refinery turnaround, SAGD turnaround, upgrader outage, plant shutdown. |
| 13.8 | Inventory & Spare Parts Management | Managing maintenance materials and spare parts including stock levels, reorder points, and warehouse locations. | Warehouse management, critical spares, consignment stock, bill of materials. |
| 13.9 | Mobile Maintenance Execution | Enabling maintenance technicians to receive, execute, and close work orders on mobile devices in the field. | Field technicians, facility operators, contractors, inspectors. |
| 13.10 | Asset Performance Management (APM) | Monitoring and optimizing the performance of physical assets using analytics, KPIs, and benchmarking. | OEE tracking, production efficiency, energy efficiency, asset ranking. |
| 13.11 | Permit to Work & Safety Management | Managing work permits, lockout/tagout, job safety analyses, and other safety controls for maintenance activities. | Hot work permits, confined space, energy isolation, simultaneous operations. |

---

### 14. Project & Portfolio Management

**Description:** Capabilities related to planning, executing, and governing projects and programs, as well as managing the portfolio of investments. Oil and gas companies manage large capital portfolios spanning drilling programs, facility construction, turnarounds, and technology initiatives.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 14.1 | Project Planning & Scheduling | Creating and managing project schedules including tasks, dependencies, milestones, and critical path. | Drilling programs, facility construction, pipeline projects, IT projects. |
| 14.2 | Resource Management & Allocation | Assigning and balancing people, equipment, and materials across projects based on availability and skill. | Engineering resource allocation, rig scheduling, contractor management. |
| 14.3 | Project Cost Tracking & Earned Value | Monitoring actual project costs against budget, calculating earned value metrics, and forecasting at-completion costs. | Capital project cost control, AFE tracking, drilling cost tracking. |
| 14.4 | Portfolio Governance & Prioritization | Evaluating, selecting, and prioritizing investments across a portfolio based on strategic criteria and constraints. | Capital allocation, technology investment prioritization, project ranking. |
| 14.5 | Stage-Gate & Approval Workflow | Managing projects through defined phases with formal review gates and approval decision points. | Capital project stage-gate, technology projects, M&A processes. |
| 14.6 | Change Management & Change Orders | Tracking and approving changes to project scope, schedule, and cost with impact assessment. | Construction change orders, scope changes, AFE supplements. |
| 14.7 | Risk & Issue Management | Identifying, assessing, and tracking project risks and issues with mitigation plans and ownership. | Project risk registers, issue logs, risk-adjusted scheduling. |
| 14.8 | Contractor & Vendor Management | Managing contractor qualifications, performance, contracts, and field mobilization. | Drilling contractors, construction contractors, engineering consultants. |
| 14.9 | Timesheet & Progress Reporting | Capturing time worked, progress measurements, and status updates from project teams and contractors. | Construction progress, drilling day reports, engineering timesheets. |
| 14.10 | Benefits Realization Tracking | Measuring and reporting whether projects deliver the expected business benefits after completion. | Post-implementation reviews, ROI tracking, value realization. |

---

### 15. Compliance & Risk Management

**Description:** Capabilities related to ensuring the organization meets its regulatory obligations, manages enterprise risks, and maintains governance controls. Oil and gas companies face extensive regulatory requirements from energy regulators, environmental agencies, securities regulators, and health and safety authorities.

| ID | Functional Capability | Description | Common O&G Business Contexts |
|----|----------------------|-------------|------------------------------|
| 15.1 | Regulatory Reporting & Filing | Preparing and submitting regulatory reports and filings to government agencies in required formats and timelines. | AER reporting, SEC filings, NEB reporting, emissions reporting, royalty reporting. |
| 15.2 | Audit Management | Planning, executing, tracking, and reporting on internal and external audit activities and findings. | SOX audits, operational audits, partner audits, regulatory audits, IT audits. |
| 15.3 | Enterprise Risk Assessment | Identifying, evaluating, and prioritizing risks across the organization with probability and impact scoring. | Enterprise risk register, operational risk, financial risk, strategic risk. |
| 15.4 | Governance, Risk & Compliance (GRC) Platform | Providing an integrated platform for managing governance policies, risk assessments, and compliance controls. | SOX compliance, policy management, control testing, risk dashboards. |
| 15.5 | Privacy & Data Protection Management | Managing personal data inventories, consent, data subject requests, and privacy impact assessments. | PIPEDA compliance, employee privacy, contractor data, customer data. |
| 15.6 | Policy & Procedure Management | Creating, reviewing, approving, distributing, and attesting to organizational policies and procedures. | HSE policies, IT policies, operational procedures, corporate governance. |
| 15.7 | Incident & Non-Conformance Management | Recording, investigating, and managing incidents, near-misses, and non-conformance events with corrective actions. | HSE incidents, spills, equipment failures, quality deviations, security incidents. |
| 15.8 | Environmental Compliance Management | Tracking environmental permits, monitoring obligations, remediation activities, and environmental liabilities. | Environmental approvals, monitoring programs, reclamation, liability tracking. |
| 15.9 | Health & Safety Management | Managing occupational health and safety programs including hazard assessments, training, and medical surveillance. | Hazard assessments, safety training records, exposure monitoring, fit testing. |
| 15.10 | License & Permit Management | Tracking regulatory licenses, permits, and approvals with expiry dates, renewal requirements, and conditions. | Well licences, facility permits, pipeline permits, water licences, land dispositions. |
| 15.11 | Third-Party Risk Management | Assessing and monitoring risks associated with vendors, contractors, and other third parties. | Vendor security assessments, contractor prequalification, supply chain risk. |
| 15.12 | ESG Reporting & Disclosure | Collecting, validating, and reporting environmental, social, and governance metrics to stakeholders and frameworks. | TCFD, SASB, CDP, GHG inventory, diversity metrics, Indigenous engagement. |

---

## 3. Quick Reference Index

The following index provides a compact reference for all 15 functional domains and their capability counts:

| Domain ID | Functional Domain | Capability Count | Capability ID Range |
|-----------|------------------|-----------------|---------------------|
| 1 | Data Management | 12 | 1.1 -- 1.12 |
| 2 | Analytics & Reporting | 10 | 2.1 -- 2.10 |
| 3 | Process Automation | 10 | 3.1 -- 3.10 |
| 4 | Integration & Connectivity | 11 | 4.1 -- 4.11 |
| 5 | User Experience & Collaboration | 10 | 5.1 -- 5.10 |
| 6 | Security & Access Control | 11 | 6.1 -- 6.11 |
| 7 | AI & Machine Learning | 10 | 7.1 -- 7.10 |
| 8 | Geospatial & Mapping | 9 | 8.1 -- 8.9 |
| 9 | Simulation & Modelling | 10 | 9.1 -- 9.10 |
| 10 | Real-Time Monitoring & Control | 10 | 10.1 -- 10.10 |
| 11 | Document & Content Management | 10 | 11.1 -- 11.10 |
| 12 | Financial Management | 12 | 12.1 -- 12.12 |
| 13 | Asset & Maintenance Management | 11 | 13.1 -- 13.11 |
| 14 | Project & Portfolio Management | 10 | 14.1 -- 14.10 |
| 15 | Compliance & Risk Management | 12 | 15.1 -- 15.12 |
| | **Total** | **158** | |

---

## 4. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-02-08 | Enterprise Architecture Team | Initial framework creation. |
