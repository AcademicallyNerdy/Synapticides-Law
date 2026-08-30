# Synapticide's Law: Formalizing Systemic AI Cascade Loss (SACL) Across Autonomous Multi-Agent Threat Regimes

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22168188.svg)](https://doi.org/10.5281/zenodo.22168188)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the official LaTeX manuscript, mathematical proofs, and Python Monte Carlo simulation engine for **Synapticide's Law** and the **Systemic AI Cascade Loss (SACL)** framework.

To facilitate immediate enterprise adoption, corporate risk auditing, and M&A cyber due diligence, this repository includes two operational implementation tools for calculating Systemic AI Cascade Loss ($`\text{SACL}`$) and verifying compliance against the **Synapticide Maturity & Containment Framework (SMCF)**:

- **`tools/sacl_audit.py` (CLI Utility):** A lightweight, zero-dependency command-line Python script designed for integration into DevOps pipelines, CI/CD security checks, and automated risk auditing workflows.
- **`tools/colab_sacl_audit_py.ipynb` (Interactive Notebook):** A ready-to-run Google Colab notebook providing an interactive environment for CISOs, enterprise architects, and actuarial underwriters to model custom multi-agent swarm parameters, simulate velocity thresholds, and generate formal SMCF compliance reports without requiring local Python environments.

## Abstract
As cybersecurity threats transition from static credential vulnerabilities to machine-speed autonomous Large Language Model (LLM) agent swarms, traditional single-entity risk frameworks (such as FAIR and ISO 27005) fail to model multi-sided, cross-platform financial destruction. We establish **Synapticide's Law**, a fundamental theorem governing machine-speed cognitive network collapse, and introduce the **Systemic AI Cascade Loss (SACL)** mathematical model.

## Repository Structure
```text
├── paper/                  # Overleaf LaTeX manuscript source files
│   ├── main.tex
│   ├── references.bib
│   ├── docs/               # How-To
│   │   └── ENTERPRISE_INTEGRATION.md
│   ├── figures/
│   │   └── case_study_comparative.tex
│   └── sections/
│       ├── 01_intro.tex
│       ├── 02_math_model.tex
│       ├── 03_axioms.tex
│       ├── 04_case_studies.tex
│       ├── 05_governance.tex
│       ├── 06_simulation.tex
│       └── 07_conclusion.tex
├── simulation/             # Python Monte Carlo simulation engine
│   ├── sacl_monte_carlo.py
│   └── requirements.txt
├── tools/                  # Interactive audit utilities & notebooks
│   ├── sacl_audit.py
│   └── colab_sacl_audit_py.ipynb
├── LICENSE
└── README.md
```

### 🏛️ Enterprise Architecture & GRC Integration

For CISOs, Enterprise Architects (TOGAF), M&A deal teams, and GRC auditors looking to operationalize Synapticide's Law within established corporate governance and security frameworks, see our detailed blueprint:

👉 **[Enterprise Architecture & GRC Integration Guide](docs/ENTERPRISE_INTEGRATION.md)**

#### Key Integration Highlights:
- **TOGAF Phase G & ARB Gates:** Gating CapEx approvals for agent swarms $`M_{\text{swarm}} > 1`$ using quantitative $`\text{VaR}_{95\%}`$ thresholds and $`K_{\text{cb}}`$ circuit breaker verifications.
- **M&A Due Diligence & PPA:** Factoring latent agentic capability escalation into purchase price holdbacks, escrows, and valuation haircuts ($\Delta \text{Valuation}$).
- **NIST CSF 2.0 / ISO 27001 Mapping:** Concrete control overlays for PR.IR-01, DE.CM-01, and Control A.8.23.
- **SIEM/SOAR Playbooks:** Triggering **Automated Synapticide** (sub-300s token revocation and sandbox ejection) at machine speed without manual intervention lag.

## Quickstart: Enterprise SACL Audit Tools

### Option 1: Interactive Google Colab Notebook
Open and run `tools/colab_sacl_audit_py.ipynb` directly in Google Colab to execute interactive scenario modeling, visualize parameter limits, and generate instantaneous SMCF compliance pass/fail audits.

### Option 2: Command-Line Interface (CLI)
Run the audit calculator locally or inside automated CI/CD pipelines:

```bash
# Basic Audit Run
python3 tools/sacl_audit.py --agents 250 --ops 100 --latency 264 --k_cb 1000000

# High-Velocity Swarm Simulation (500 Agents, Unmitigated 11-Day Egress Window)
python3 tools/sacl_audit.py --agents 500 --alpha 1.3 --latency 264 --k_cb 0
```

## License & Intellectual Property

- **Manuscript, Figures, Vectors & Theoretical Framework:**  
  Copyright © 2026. Distributed under the [Creative Commons Attribution 4.0 International License (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to share, copy, and adapt this material in any medium or format, provided appropriate academic credit is given, a link to the license is provided, and any changes are clearly indicated. (LICENSE-CC)

- **Source Code, LaTeX Scripts & Computation Utilities:**  
  Licensed under the open-source [MIT License](LICENSE). 

---

## Citation

If you use, reference, or build upon the *Synapticide's Law* framework or its associated assets in academic literature, software, or media, please cite this work using the following metadata:

**Preferred APA Citation:**
> Rosen, C. (2026). *Synapticide's Law: Formalizing Systemic AI Cascade Loss (SACL) Across Autonomous Multi-Agent Threat Regimes* (Version 2.0.0) [Preprint]. Zenodo. https://doi.org/10.5281/zenodo.22168188

**BibTeX Entry:**
```bibtex
@article{QCH_Version2_2026,
  author       = {[Rosen], [Christi]},
  title        = {{Synapticide's Law: Formalizing Systemic AI Cascade Loss (SACL) Across Autonomous Multi-Agent Threat Regimes}},
  month        = aug,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {v2.0.0},
  doi          = {10.5281/zenodo.22168188},
  url          = {[https://doi.org/10.5281/zenodo.22168188](https://doi.org/10.5281/zenodo.22168188)}
}
