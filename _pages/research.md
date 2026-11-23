---
permalink: /
title: "Research Projects"
excerpt: "research"
permalink: /research/
author_profile: true
---

{% include base_path %}


## Cyber Threat Detection and Investigation {#cyber-threat-detection-and-investigation}

<img alt="" src="https://xusheng-xiao.github.io/images/depimpact.png" style="width:850px" />

RISE lab developes system security techniques that **monitors software behaviors using system auditing** and **model the causality among software behaviors** to provide contextual information of cyber threats, assisting cyber threat investigation. Specifically, to address the fundamental limitations of causality analysis in system auditing, we have develop data reduction techniques, attack behavior query and detection techniques with domain-specific language support, and causality analysis techniques to analyze system auditing logs. 
* Our work in attack investigation was selected as one of the top ten finalists for ***[CSAW Best Applied Security Paper Award 2018](https://csaw.engineering.nyu.edu/)***. 
* The security intelligence solution built by our team won first place in the ***[Town Life and Society Innovation Category at CEATEC Award](http://www.ceatec.com/en/award/award01_02.html)***. Check out our project websites at [AIQL](https://sites.google.com/site/aiqlsystem/), [SAQL](https://sites.google.com/site/saqlsystem/). 
* See our papers at [VLDB'16](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/behaviorquery-vldb2016.pdf), [CCS'16](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/reduction-ccs.pdf), [USENIX ATC'18](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/aiql-usenix_atc2018_0.pdf), [USENIX Security'18](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/sec18-final146.pdf), [CCS' 18](http://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/nodemerge-ccs2018.pdf), [ICDE'20](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/aptrace-camera-ready.pdf), [ICDE'21](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/threatraptor-icde21_0.pdf), [USENIX Security'22](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/sec22summer_fang.pdf), [IEEE S&P'22](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/depcomm-ieeesp2022.pdf).


**Recent publications**

* **ProGQL: A Provenance Graph Query System for Cyber Attack Investigation** — [ICDE'26](https://xusheng-xiao.github.io/papers/progql_icde2026.pdf), [arXiv](https://arxiv.org/abs/2510.22400).
* **CTIKG: LLM-Powered Knowledge Graph Construction from Cyber Threat Intelligence** — [COLM'24](https://xusheng-xiao.github.io/papers/ctikg-colm2024.pdf).
* **NODLINK: An Online System for Fine-Grained APT Attack Detection and Investigation** — [NDSS'24](https://xusheng-xiao.github.io/papers/nodlink-ndss.pdf).
* **Are we there yet? An Industrial Viewpoint on Provenance-based Endpoint Detection and Response Tools** — [CCS'23](https://xusheng-xiao.github.io/papers/provenance_study_ccs_2023.pdf).
* **DISTDET: A Cost-Effective Distributed Cyber Threat Detection System** — [USENIX Security'23](https://xusheng-xiao.github.io/papers/usenixsecurity23-distdet.pdf).

**NSF awards**

* [NSF #2613277](https://www.nsf.gov/awardsearch/show-award?AWD_ID=2613277): CICI: TCR: Cyber Threat Triage and Investigation for Scientific Institutions via Adaptive Deployable Provenance Analysis and Agentic AI-Based Threat Intelligence.
* [NSF #2438197](https://www.nsf.gov/awardsearch/show-award?AWD_ID=2438197): SaTC: CORE: Small: Scalable Cyber Attack Investigation using Declarative Queries and Interrogative Analysis.


## Online Scam/Fraud and Cyber Deception {#online-scam-fraud-and-cyber-deception}

RISE lab develops AI-driven techniques to **detect and understand online scams, fraud, and cyber deception**. We combine large language models with insights from psychology to analyze how scammers manipulate victims and how deceptive interactions evolve over time. Specifically, we develop benchmarks for identifying psychological techniques in real-world scams and predicting scam progression from early conversations. We also study cryptocurrency fraud by detecting and characterizing scam tokens on decentralized exchanges.

**Recent publications**

* **PreScam** benchmarks scam progression in multi-turn conversations, including real-time risk estimation and prediction of scammers' next actions. See our paper at [COLM'26](https://xusheng-xiao.github.io/papers/prescam_colm2026.pdf) and [arXiv](https://arxiv.org/abs/2605.12243).
* **PsyScam** benchmarks psychological techniques in real-world scams and evaluates language models on scam detection and generation. See our paper at [EMNLP'25](https://xusheng-xiao.github.io/papers/psyscam_emnlp_2025.pdf) and [arXiv](https://arxiv.org/abs/2505.15017).
* **Trade or Trick?** detects and characterizes scam tokens on the Uniswap decentralized exchange using transaction analysis and machine learning. See our paper at [SIGMETRICS'22](https://xusheng-xiao.github.io/papers/uniswap.pdf) and [arXiv](https://arxiv.org/abs/2109.00229).


## Mobile App Analysis {#mobile-app-analysis}

<img alt="" src="https://xusheng-xiao.github.io/images/mobile.png" style="width:650px" />

RISE lab combines program analysis and machine learning techniques to model both **program semantics** and **behavior intention** for detecting *undesired software behaviors* that cannot be justified by software applications' functionality. Specifically, we have developed a series of techniques to improve mobile app security. First, we combined program analysis techniques, computer vision techniques, and text analysis techniques to analyze the images and the text in the GUIs of mobile apps to understand behavior intention of mobile apps. Second, we combine program analysis techniques and machine learning techniques to train a model using a large number of apps, and use the model to detect undesired behaviors that cannot be justified by apps’ functionality. Also, existing techniques only tell the users what private data the apps want to use, but do not explain why the apps use users’ private data. Third, to address this problem, we combine program analysis techniques and machine learning techniques to train a model that can synthesize natural-language descriptions to describe the program behaviors that use users’ private data, which can be used to explain why the apps use users’ private data. 
* Our work in mobile security was selected as one of the top ten finalists for ***[CSAW Best Applied Security Paper Award 2015](https://csaw.engineering.nyu.edu/)***, and produced a static analysis tool that was deployed in TouchDevelop of Microsoft Research.  
* Check out our open sourced tools for AppContext, WHYPER. See our papers at [ASE'12](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/xusheng-ase2012.pdf), [USENIX Security'13](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/whyper-usenix2013.pdf), [ICSE'15](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/appcontext-icse2015_0.pdf), [ASEJ'15](https://link.springer.com/article/10.1007/s10515-014-0166-y), [USENIX Security'15](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/supor-usenix2015.pdf), [ICSE’19](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/iconintent-icse2019.pdf), [CCS'19](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/deepintent-optimize.pdf), [ICSE'21](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/champ_icse2021_cr-submit3.pdf), [ICSE'22-a](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/describectx_cr.pdf), [ICSE'22-b](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/promal_icse_cr.pdf). 
* The recent work DeepIntent (CCS'19) that detects intention-behavior discrepancies using the synergy of program analysis and deep learning releases the code and the complete dataset (including example dataset) at [Github](https://github.com/deepintent-ccs/DeepIntent/).


**Recent publications**

* **An Empirical Study of Data Access Practice in Android AR Apps to Understand User Privacy Risks** — [ASE'26](https://xusheng-xiao.github.io/papers/ar_study_ase2026.pdf). <span aria-hidden="true">🏆</span> **ACM SIGSOFT Distinguished Paper Award**.
* **AppBDS: LLM-Powered Description Synthesis for Sensitive Behaviors in Mobile Apps** — [ASE'25](https://xusheng-xiao.github.io/papers/appbds-ase2025.pdf).
* **Careful About What App Promotion Ads Recommend! Detecting and Explaining Malware Promotion via App Promotion Graph** — [NDSS'25](https://xusheng-xiao.github.io/papers/adgpe_ndss2025.pdf).
* **MalCertain: Enhancing Deep Neural Network Based Android Malware Detection by Tackling Prediction Uncertainty** — [ICSE'24](https://xusheng-xiao.github.io/papers/uncertainty_icse_cr.pdf).
* **WeMinT: Tainting Sensitive Data Leaks in WeChat Mini-Programs** — [ASE'23](https://xusheng-xiao.github.io/papers/wemint-ase2023.pdf).

**NSF awards**

* [NSF #2318483](https://www.nsf.gov/awardsearch/show-award?AWD_ID=2318483): CAREER: Enhancing Mobile Application Security through Contextual Integrity and User Awareness.
* [NSF #2318486](https://www.nsf.gov/awardsearch/show-award?AWD_ID=2318486): Collaborative Research: EAGER: Enhancing Security and Privacy of Augmented Reality Mobile Applications through Software Behavior Analysis.
* [NSF #1755772](https://www.nsf.gov/awardsearch/show-award?AWD_ID=1755772): CRII: SaTC: Enhancing Mobile App Security by Detecting Icon-Behavior Contradiction.


## Blockchain and Smart Contract {#blockchain-and-smart-contract}

RISE lab develops software analysis and system analysis techniques for blockchain systems and smart contracts. Specifically, we have developed Hyper Service ([CCS' 19](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/hyperservice.pdf)), the ***first interoperability blockchain platform with programmability and strong security guarantees***. 
* It is open sourced at [Github](https://github.com/HyperService-Consortium). 
* Our recent work also studies digital asset trading platforms ([SIGMETRICS'22](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/uniswap.pdf)).

**Recent publications**

* **vFix: Facilitating Software Maintenance of Smart Contracts via Automatically Fixing Vulnerabilities** — [ICSME'24](https://xusheng-xiao.github.io/papers/vFix_ICSME2024.pdf).
* **iSyn: Semi-Automated Smart Contract Synthesis from Legal Financial Agreements** — [ISSTA'23](https://xusheng-xiao.github.io/papers/iSyn_issta.pdf).
* **Making Web 3.0 Connected - A Perspective from Interoperability and Programmability across Blockchains** — [IEEE TDSC'22](https://xusheng-xiao.github.io/papers/hyperservice-tdsc21.pdf).
* **Trade or Trick? Detecting and Characterizing Scam Tokens on Uniswap Decentralized Exchange** — [SIGMETRICS'22](https://xusheng-xiao.github.io/papers/uniswap.pdf), [arXiv](https://arxiv.org/abs/2109.00229).

## Software Testing and Program Analysis {#software-testing-and-program-analysis}

RISE lab develops static program analysis techniques and dynamic symbolic execution techniques to improve software testing ([ICSE'2011](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/covana-icse2011.pdf), [ASE'13](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/xusheng-ase2013.pdf), [ICSE'16 Edu](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/icse16seet-similarity.pdf), [DSN'18](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/dsn18-preinfer.pdf), [HotMobile' 19](http://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/hotm068-maa.pdf)), bug detection ([ISSTA'14](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/cilppa-issta2014.pdf), [FSE Demo'17](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/fse17demo.pdf)), and software performance ([ISSTA'13](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/deltainfer-issta2013.pdf), [RTAS'19](http://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/rtas2019-final29.pdf)). Our lab also develops text analysis techniques to improve access control policy extraction ([FSE'12](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/text2policy-fse2012.pdf), [ACSAC'14](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/xusheng-acsac2014.pdf)) and precondition extraction from API documents ([ICSE'12](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/xusheng-icse2012.pdf)). 
* Our work in software testing received ***[ICSE SRC Best Project Representing an Innovative Use of Microsoft Technology](https://www.csc.ncsu.edu/news/1347)*** at [ACM SRC Grand Final 2012](https://src.acm.org/grand-finalists/2012). 
* Check out the open sourced tools for [Covana](http://pexase.codeplex.com/wikipage?title=Covana&referringTitle=Home), [APIInfer](https://research.csc.ncsu.edu/ase/projects/pint/).


**Recent publications**

* **Specification-Guided Detection of ISA Conformance Bugs in RISC-V Emulators** — [ICSE'27](/publications/#2027).
* **Agent+P: Guiding UI Agents via Symbolic Planning** — [AACL-IJCNLP'26](/publications/#2026).
* **Your Harness is Not Secure: Benchmarking Real-world Threat of Command Line Interface Agent** — [EMNLP'26](/publications/#2026).
* **WebEvo: Taming Web Application Evolution via Detecting Semantic Structure Change** — [ISSTA'21](https://xusheng-xiao.github.io/papers/webevo-cr.pdf).
* **DroidMutator: An Effective Mutation Analysis Tool for Android Applications** — [ICSE'20 Demo](https://xusheng-xiao.github.io/papers/icse_tooldemo_2020_droidmutator_1.pdf).
