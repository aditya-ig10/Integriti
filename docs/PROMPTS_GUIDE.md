# Integriti Development Prompts Guide
## Detailed Implementation Prompts for Each Component

### 🏗️ Architecture & Infrastructure Prompts

#### Prompt 1: Microservices Architecture Setup
```
Create a production-ready microservices architecture for the Integriti national security platform with the following requirements:

1. **Core Services:**
   - Authentication Service (JWT, OAuth2, RBAC)
   - Detection Engine Service (AI/ML models)
   - Attribution Service (forensic analysis)
   - Threat Intelligence Service (graph analysis)
   - Analytics Service (real-time processing)
   - API Gateway (rate limiting, routing)

2. **Infrastructure:**
   - Docker containers with multi-stage builds
   - Kubernetes deployment manifests
   - Helm charts for package management
   - Prometheus monitoring with Grafana dashboards
   - ELK stack for centralized logging

3. **Databases:**
   - PostgreSQL cluster for transactional data
   - Neo4j for graph data
   - Elasticsearch for search and analytics
   - Redis cluster for caching and sessions

4. **Message Queuing:**
   - Apache Kafka for event streaming
   - RabbitMQ for task queues
   - Dead letter queues for error handling

Include proper health checks, graceful shutdowns, and auto-scaling configurations.
```

#### Prompt 2: Security-First Infrastructure
```
Implement enterprise-grade security infrastructure for the Integriti platform including:

1. **Network Security:**
   - Zero-trust network architecture
   - VPC with private subnets
   - Network segmentation and firewall rules
   - DDoS protection and WAF

2. **Secrets Management:**
   - HashiCorp Vault integration
   - Kubernetes secrets encryption
   - Certificate management with auto-renewal
   - Environment-specific secret rotation

3. **Compliance & Auditing:**
   - SOC 2 Type II compliance framework
   - GDPR/CCPA compliance mechanisms
   - Comprehensive audit logging
   - Tamper-evident log storage

4. **Container Security:**
   - Image vulnerability scanning
   - Runtime security monitoring
   - Network policies and service mesh
   - Security context constraints

Create security policies, incident response procedures, and compliance checklists.
```

### 🤖 AI/ML Detection Engine Prompts

#### Prompt 3: Advanced LLM Detection Models
```
Develop state-of-the-art LLM detection models for the Integriti platform with these specifications:

1. **Model Architecture:**
   - Ensemble of RoBERTa, T5, and custom transformer models
   - Multi-head attention mechanisms for different text features
   - Adversarial training to resist evasion attacks
   - Knowledge distillation for model compression

2. **Training Infrastructure:**
   - MLflow for experiment tracking
   - Kubeflow pipelines for ML workflows
   - Distributed training with multiple GPUs
   - Hyperparameter optimization with Optuna

3. **Feature Engineering:**
   - Stylometric features (sentence length, punctuation patterns)
   - Semantic embeddings (BERT, sentence transformers)
   - Statistical features (perplexity, entropy, token probabilities)
   - Linguistic features (POS tags, dependency parsing)

4. **Performance Requirements:**
   - >95% accuracy on balanced test sets
   - <100ms inference time per document
   - Robust against adversarial examples
   - Explainable predictions with confidence scores

Include data preprocessing pipelines, model evaluation metrics, and continuous learning capabilities.
```

#### Prompt 4: Multi-Modal Content Analysis
```
Create a comprehensive multi-modal analysis system that processes:

1. **Text Analysis:**
   - Content similarity detection
   - Narrative structure analysis
   - Emotional sentiment scoring
   - Propaganda technique identification

2. **Metadata Analysis:**
   - Account creation patterns
   - Posting frequency analysis
   - Geolocation consistency checks
   - Device fingerprinting

3. **Social Graph Analysis:**
   - Viral propagation patterns
   - Bot network detection
   - Influence mapping
   - Coordination behavior analysis

4. **Cross-Platform Correlation:**
   - Content synchronization detection
   - Cross-platform user linking
   - Campaign orchestration identification
   - Platform-specific adaptation analysis

Implement real-time processing pipelines with Apache Spark, feature stores for consistent data access, and automated model retraining based on new threat patterns.
```

### 🔍 Attribution & Forensics Prompts

#### Prompt 5: Forensic Watermarking System
```
Develop advanced forensic capabilities for LLM output attribution:

1. **Watermarking Techniques:**
   - Statistical watermarking using token distribution manipulation
   - Cryptographic watermarks with digital signatures
   - Steganographic techniques for hidden markers
   - Blockchain-based provenance tracking

2. **Model Fingerprinting:**
   - Layer-wise activation analysis
   - Token probability distribution fingerprints
   - Model-specific bias detection
   - Version identification techniques

3. **Attribution Pipeline:**
   - Content source identification
   - Model family classification
   - Training data inference
   - Generation parameter estimation

4. **Legal Framework:**
   - Digital evidence chain of custody
   - Court-admissible forensic reports
   - Expert witness support systems
   - Regulatory compliance validation

Include integration with major LLM providers (OpenAI, Anthropic, Google) and support for emerging watermarking standards.
```

#### Prompt 6: Advanced Stylometric Analysis
```
Build sophisticated stylometric analysis for threat actor attribution:

1. **Linguistic Features:**
   - Author-specific writing patterns
   - Cultural and regional language markers
   - Professional domain indicators
   - Educational background inference

2. **Deep Learning Models:**
   - Siamese networks for author verification
   - Graph neural networks for style relationships
   - Transformer-based style embeddings
   - Few-shot learning for new author identification

3. **Temporal Analysis:**
   - Writing style evolution tracking
   - Campaign progression analysis
   - Operational pattern recognition
   - Time-zone and activity correlation

4. **Cross-Lingual Analysis:**
   - Multi-language style transfer detection
   - Translation artifact identification
   - Native language influence analysis
   - Cultural adaptation detection

Implement real-time analysis capabilities with confidence scoring and similarity ranking for threat actor databases.
```

### 🌐 Graph-Based Intelligence Prompts

#### Prompt 7: Disinformation Network Mapping
```
Create advanced graph neural network systems for threat intelligence:

1. **Graph Construction:**
   - Multi-layer network representation (users, content, platforms)
   - Temporal edge weighting
   - Cross-platform entity resolution
   - Dynamic graph updating

2. **GNN Models:**
   - GraphSAGE for large-scale inductive learning
   - GAT (Graph Attention Networks) for important node identification
   - Graph autoencoders for anomaly detection
   - Temporal GNNs for evolution analysis

3. **Analysis Capabilities:**
   - Community detection algorithms
   - Influence propagation modeling
   - Bot network identification
   - Coordination pattern recognition

4. **Visualization & Interaction:**
   - Interactive graph exploration interface
   - Real-time network updates
   - Drill-down investigation tools
   - Collaborative annotation systems

Integrate with Neo4j graph database and implement scalable graph processing using Apache Spark GraphX.
```

#### Prompt 8: Cross-Platform Intelligence Fusion
```
Develop comprehensive cross-platform intelligence correlation:

1. **Data Integration:**
   - Unified content schemas across platforms
   - Entity resolution and deduplication
   - Cross-platform user identity linking
   - Temporal event correlation

2. **Platform Connectors:**
   - Twitter/X API v2 integration
   - Meta (Facebook/Instagram) Graph API
   - TikTok Research API
   - Telegram Bot API
   - YouTube Data API
   - Reddit API

3. **Real-Time Processing:**
   - Streaming data ingestion
   - Event-driven architecture
   - Backpressure handling
   - Data quality validation

4. **Correlation Algorithms:**
   - Content similarity matching
   - Temporal pattern analysis
   - Behavioral fingerprinting
   - Campaign orchestration detection

Include rate limiting, API error handling, and compliance with platform terms of service.
```

### 🔐 Privacy & Security Prompts

#### Prompt 9: Privacy-Preserving Analytics
```
Implement cutting-edge privacy-preserving techniques:

1. **Differential Privacy:**
   - Epsilon-delta privacy guarantees
   - Laplace and Gaussian noise mechanisms
   - Privacy budget management
   - Composition theorems implementation

2. **Federated Learning:**
   - Secure aggregation protocols
   - Byzantine-robust averaging
   - Communication-efficient algorithms
   - Model poisoning defenses

3. **Homomorphic Encryption:**
   - SEAL library integration
   - Encrypted computation on text features
   - Key management and rotation
   - Performance optimization

4. **Zero-Knowledge Proofs:**
   - zk-SNARKs for computation verification
   - Privacy-preserving authentication
   - Proof generation and verification
   - Scalability optimizations

Create privacy-preserving analytics pipelines that maintain >90% utility while providing formal privacy guarantees.
```

#### Prompt 10: International Compliance Framework
```
Build comprehensive regulatory compliance system:

1. **Multi-Jurisdiction Support:**
   - GDPR (European Union)
   - CCPA (California)
   - PIPEDA (Canada)
   - LGPD (Brazil)
   - Data localization requirements

2. **Automated Compliance:**
   - Data mapping and classification
   - Consent management systems
   - Automated data retention policies
   - Right to erasure implementation

3. **Audit & Reporting:**
   - Compliance monitoring dashboards
   - Automated report generation
   - Violation detection and alerting
   - Remediation workflow management

4. **International Data Sharing:**
   - Standard Contractual Clauses (SCCs)
   - Adequacy decision verification
   - Transfer impact assessments
   - Cross-border audit trails

Include legal framework documentation and consultation with privacy attorneys.
```

### 📊 Analytics & Visualization Prompts

#### Prompt 11: Real-Time Threat Dashboard
```
Create an advanced threat intelligence dashboard:

1. **Frontend Architecture:**
   - React with TypeScript
   - Redux for state management
   - WebSocket connections for real-time updates
   - Progressive Web App (PWA) capabilities

2. **Visualization Components:**
   - D3.js for custom network graphs
   - Plotly for statistical charts
   - Leaflet for geospatial mapping
   - Timeline visualization for temporal analysis

3. **Interactive Features:**
   - Drill-down investigation workflows
   - Multi-dimensional filtering
   - Collaborative annotation tools
   - Export functionality (PDF, CSV, JSON)

4. **Performance Optimization:**
   - Virtual scrolling for large datasets
   - Lazy loading and code splitting
   - Efficient data structures
   - Caching strategies

Implement responsive design, accessibility features (WCAG 2.1), and support for multiple languages.
```

#### Prompt 12: Predictive Analytics Engine
```
Develop advanced predictive capabilities:

1. **Time Series Models:**
   - LSTM networks for trend prediction
   - Prophet for seasonal decomposition
   - ARIMA models for baseline comparison
   - Ensemble methods for improved accuracy

2. **Anomaly Detection:**
   - Isolation Forest for multivariate anomalies
   - Autoencoders for reconstruction errors
   - One-class SVM for outlier detection
   - Statistical process control charts

3. **Risk Scoring:**
   - Multi-factor risk models
   - Threat severity classification
   - Confidence interval estimation
   - Explainable risk factors

4. **Early Warning Systems:**
   - Threshold-based alerting
   - Trend change detection
   - Escalation procedures
   - Automated response triggers

Include model performance monitoring, automatic retraining pipelines, and integration with alerting systems.
```

### 🔄 Integration & Deployment Prompts

#### Prompt 13: SIEM Integration Framework
```
Create comprehensive SIEM integration capabilities:

1. **Supported Platforms:**
   - Splunk Universal Forwarder
   - IBM QRadar DSM
   - Microsoft Sentinel connector
   - ArcSight SmartConnector
   - Elastic SIEM integration

2. **Data Formats:**
   - CEF (Common Event Format)
   - LEEF (Log Event Extended Format)
   - STIX/TAXII for threat intelligence
   - Custom JSON schemas

3. **Real-Time Streaming:**
   - Kafka connectors for each SIEM
   - Buffering and retry mechanisms
   - Error handling and dead letter queues
   - Performance monitoring

4. **Alert Correlation:**
   - Multi-source event correlation
   - Threat actor attribution
   - Campaign tracking
   - Risk scoring integration

Include configuration management, testing frameworks, and documentation for security operations centers.
```

#### Prompt 14: CI/CD and Deployment Automation
```
Implement enterprise-grade DevSecOps pipeline:

1. **CI/CD Pipeline:**
   - GitHub Actions workflows
   - Multi-environment deployment (dev/staging/prod)
   - Automated testing (unit, integration, e2e)
   - Security scanning (SAST, DAST, dependency check)

2. **Infrastructure as Code:**
   - Terraform modules for cloud resources
   - Ansible playbooks for configuration
   - Helm charts for Kubernetes deployment
   - GitOps with ArgoCD

3. **Monitoring & Observability:**
   - Prometheus metrics collection
   - Grafana dashboard templates
   - Jaeger distributed tracing
   - ELK stack for log aggregation

4. **Disaster Recovery:**
   - Automated backup procedures
   - Cross-region replication
   - Recovery time objectives (RTO)
   - Recovery point objectives (RPO)

Include blue-green deployment strategies, rollback procedures, and performance benchmarking.
```

### 🎯 Specialized Analysis Prompts

#### Prompt 15: Advanced Threat Actor Profiling
```
Develop comprehensive threat actor analysis capabilities:

1. **Behavioral Analysis:**
   - Attack pattern recognition (MITRE ATT&CK)
   - Tactical, Techniques, and Procedures (TTPs)
   - Campaign lifecycle analysis
   - Resource allocation patterns

2. **Attribution Framework:**
   - Multi-source intelligence fusion
   - Confidence scoring systems
   - Evidence correlation engines
   - Analyst collaboration tools

3. **Predictive Modeling:**
   - Next attack prediction
   - Target selection modeling
   - Campaign evolution forecasting
   - Resource requirement estimation

4. **Counter-Intelligence:**
   - Deception detection
   - False flag identification
   - Attribution obfuscation analysis
   - Counter-narrative development

Include integration with threat intelligence feeds, collaboration with international partners, and support for classified information handling.
```

### 📋 Quality Assurance & Testing Prompts

#### Prompt 16: Comprehensive Testing Framework
```
Create thorough testing and validation systems:

1. **Automated Testing:**
   - Unit tests with 95%+ coverage
   - Integration testing for all APIs
   - End-to-end testing scenarios
   - Performance load testing

2. **Red Team Exercises:**
   - Adversarial attack simulations
   - Evasion technique testing
   - Social engineering scenarios
   - Physical security assessments

3. **Model Validation:**
   - Cross-validation frameworks
   - Adversarial robustness testing
   - Fairness and bias evaluation
   - Explainability validation

4. **Security Testing:**
   - Penetration testing automation
   - Vulnerability scanning
   - Security code review
   - Compliance validation

Include continuous testing in CI/CD pipelines, test data management, and performance benchmarking against industry standards.
```

---

## 🚀 Quick Start Implementation Order

### Week 1-2: Foundation
1. Use **Prompt 1** to set up basic architecture
2. Use **Prompt 2** to implement security infrastructure
3. Set up development environment and CI/CD

### Week 3-6: Core Detection
1. Use **Prompt 3** for LLM detection models
2. Use **Prompt 4** for multi-modal analysis
3. Implement basic training pipelines

### Week 7-10: Advanced Analysis
1. Use **Prompt 5** for forensic capabilities
2. Use **Prompt 7** for graph analysis
3. Use **Prompt 11** for basic dashboard

### Week 11-16: Integration & Privacy
1. Use **Prompt 9** for privacy features
2. Use **Prompt 13** for SIEM integration
3. Use **Prompt 8** for cross-platform fusion

### Week 17-20: Production Readiness
1. Use **Prompt 14** for deployment automation
2. Use **Prompt 16** for comprehensive testing
3. Use **Prompt 12** for predictive analytics

*Each prompt is designed to be self-contained while building upon previous components. Adjust timelines based on team size and expertise.*
