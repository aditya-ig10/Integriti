# Integriti Project Structure

```
Integriti/
├── README.md                    # Project overview and getting started
├── ROADMAP.md                   # 48-week development roadmap
├── PROMPTS_GUIDE.md            # Detailed implementation prompts
├── TECHNICAL_SPECS.md          # Technical architecture specifications
├── LICENSE                     # Project license
├── .gitignore                  # Git ignore rules
├── docker-compose.yml          # Local development environment
├── requirements.txt            # Python dependencies
├── pyproject.toml             # Python project configuration
│
├── docs/                       # Documentation
│   ├── api/                   # API documentation
│   ├── architecture/          # System architecture docs
│   ├── deployment/            # Deployment guides
│   ├── security/              # Security documentation
│   ├── user-guides/           # User manuals
│   └── compliance/            # Regulatory compliance docs
│
├── src/                       # Source code
│   ├── core/                  # Core platform components
│   │   ├── auth/             # Authentication service
│   │   ├── detection/        # AI detection engine
│   │   ├── attribution/      # Forensics service
│   │   ├── intelligence/     # Threat intelligence
│   │   ├── analytics/        # Analytics service
│   │   └── sharing/          # Intelligence sharing
│   │
│   ├── ml/                    # Machine learning models
│   │   ├── detection/        # LLM detection models
│   │   ├── attribution/      # Attribution models
│   │   ├── graph/            # Graph neural networks
│   │   └── training/         # Training pipelines
│   │
│   ├── api/                   # API layer
│   │   ├── rest/             # REST API endpoints
│   │   ├── graphql/          # GraphQL schemas
│   │   └── streaming/        # Real-time APIs
│   │
│   ├── web/                   # Web dashboard
│   │   ├── components/       # React components
│   │   ├── pages/            # Dashboard pages
│   │   ├── hooks/            # Custom React hooks
│   │   └── utils/            # Utility functions
│   │
│   ├── data/                  # Data processing
│   │   ├── ingestion/        # Data collection
│   │   ├── processing/       # Stream processing
│   │   ├── storage/          # Database models
│   │   └── pipelines/        # ETL pipelines
│   │
│   └── utils/                 # Shared utilities
│       ├── crypto/           # Cryptographic functions
│       ├── privacy/          # Privacy-preserving techniques
│       ├── monitoring/       # Observability tools
│       └── compliance/       # Compliance validators
│
├── infrastructure/            # Infrastructure as Code
│   ├── terraform/            # Terraform modules
│   ├── kubernetes/           # K8s manifests
│   ├── helm/                 # Helm charts
│   ├── ansible/              # Configuration management
│   └── docker/               # Docker configurations
│
├── models/                    # Pre-trained models
│   ├── detection/            # Detection model artifacts
│   ├── attribution/          # Attribution models
│   ├── graph/                # GNN models
│   └── benchmarks/           # Benchmark datasets
│
├── tests/                     # Test suites
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   ├── e2e/                  # End-to-end tests
│   ├── performance/          # Load testing
│   └── security/             # Security tests
│
├── scripts/                   # Utility scripts
│   ├── setup/                # Environment setup
│   ├── deployment/           # Deployment scripts
│   ├── migration/            # Database migrations
│   └── monitoring/           # Monitoring setup
│
├── configs/                   # Configuration files
│   ├── development/          # Dev environment config
│   ├── staging/              # Staging config
│   ├── production/           # Production config
│   └── local/                # Local development
│
└── .github/                   # GitHub workflows
    ├── workflows/            # CI/CD pipelines
    ├── ISSUE_TEMPLATE/       # Issue templates
    └── PULL_REQUEST_TEMPLATE.md
```

## Key Components Overview

### Core Services (`src/core/`)
- **Authentication Service**: OAuth2, JWT, RBAC implementation
- **Detection Engine**: Real-time LLM content detection
- **Attribution Service**: Forensic analysis and watermarking
- **Intelligence Service**: Graph-based threat analysis
- **Analytics Service**: Predictive analytics and reporting
- **Sharing Service**: International intelligence federation

### ML Models (`src/ml/`)
- **Detection Models**: Ensemble of transformer-based classifiers
- **Attribution Models**: Stylometric and forensic analysis
- **Graph Models**: Social network analysis with GNNs
- **Training Pipelines**: Automated model training and validation

### Infrastructure (`infrastructure/`)
- **Terraform**: Cloud resource provisioning
- **Kubernetes**: Container orchestration
- **Helm**: Package management for K8s
- **Ansible**: Configuration management
- **Docker**: Containerization definitions

### Web Dashboard (`src/web/`)
- **React Frontend**: Modern, responsive user interface
- **Real-time Updates**: WebSocket connections for live data
- **Visualization**: D3.js charts and network graphs
- **Collaboration**: Multi-user investigation tools

## Development Workflow

1. **Setup**: Use `scripts/setup/` for local environment
2. **Development**: Work in feature branches with tests
3. **Testing**: Run comprehensive test suites
4. **Deployment**: Automated via GitHub Actions
5. **Monitoring**: Continuous observability and alerting

## Security Considerations

- All sensitive configurations in `configs/` are encrypted
- API keys and secrets managed via environment variables
- Security scanning integrated in CI/CD pipeline
- Regular dependency updates and vulnerability checks
