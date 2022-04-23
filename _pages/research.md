---
permalink: /
title: "Research Projects"
excerpt: "research"
permalink: /research/
author_profile: true
---

{% include base_path %}


## Cyber Threat Detection and Investigation


<img alt="" src="https://xusheng-xiao.github.io/images/mobile.png" style="width:400px" />
RISE lab developes system security techniques that **monitors software behaviors using system auditing** and **model the causality among software behaviors** to provide contextual information of cyber threats, assisting cyber threat investigation. Specifically, to address the fundamental limitations of causality analysis in system auditing, we have develop data reduction techniques, attack behavior query and detection techniques with domain-specific language support, and causality analysis techniques to analyze system auditing logs. 
* Our work in attack investigation was selected as one of the top ten finalists for ***[CSAW Best Applied Security Paper Award 2018](https://csaw.engineering.nyu.edu/)***. 
* The security intelligence solution built by our team won first place in the ***[Town Life and Society Innovation Category at CEATEC Award](http://www.ceatec.com/en/award/award01_02.html)***. Check out our project websites at [AIQL](https://sites.google.com/site/aiqlsystem/), [SAQL](https://sites.google.com/site/saqlsystem/). 
* See our papers at VLDB'16, CCS'16, USENIX ATC'18, USENIX Security'18, CCS' 18, ICDE'20, ICDE'21, USENIX Security'22, IEEE S&P'22.


## Mobile App Analysis 

RISE lab combines program analysis and machine learning techniques to model both **program semantics** and **behavior intention** for detecting *undesired software behaviors* that cannot be justified by software applications' functionality. Specifically, we have developed a series of techniques to improve mobile app security. First, we combined program analysis techniques, computer vision techniques, and text analysis techniques to analyze the images and the text in the GUIs of mobile apps to understand behavior intention of mobile apps. Second, we combine program analysis techniques and machine learning techniques to train a model using a large number of apps, and use the model to detect undesired behaviors that cannot be justified by apps’ functionality. Also, existing techniques only tell the users what private data the apps want to use, but do not explain why the apps use users’ private data. Third, to address this problem, we combine program analysis techniques and machine learning techniques to train a model that can synthesize natural-language descriptions to describe the program behaviors that use users’ private data, which can be used to explain why the apps use users’ private data. 
* Our work in mobile security was selected as one of the top ten finalists for ***[CSAW Best Applied Security Paper Award 2015](https://csaw.engineering.nyu.edu/)***, and produced a static analysis tool that was deployed in TouchDevelop of Microsoft Research.  
* Check out our open sourced tools for AppContext, WHYPER. See our papers at ASE'12, USENIX Security'13, ICSE'15, ASEJ'15, USENIX Security'15, ICSE’19, CCS'19, ICSE'21, ICSE'22-a, ICSE'22-b. 
* The recent work DeepIntent (CCS'19) that detects intention-behavior discrepancies using the synergy of program analysis and deep learning releases the code and the complete dataset (including example dataset) at [Github](https://github.com/deepintent-ccs/DeepIntent/).


## Blockchain and Smart Contract 

RISE lab develops software analysis and system analysis techniques for blockchain systems and smart contracts. Specifically, we have developed Hyper Service ([CCS' 19](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/hyperservice.pdf)), the ***first interoperability blockchain platform with programmability and strong security guarantees***. 
* It is open sourced at [Github](https://github.com/HyperService-Consortium). 
* Our recent work also studies digital asset trading platforms ([SIGMETRICS'22](https://engineering.case.edu/groups/xusheng-xiao/sites/engineering.case.edu.groups.xusheng-xiao/files/docs/uniswap.pdf)).

## Software Testing and Program Analysis

RISE lab develops static program analysis techniques and dynamic symbolic execution techniques to improve software testing (ICSE'2011, ASE'13, ICSE'16 Edu, DSN'18, HotMobile' 19), bug detection (ISSTA'14, FSE Demo'17), and software performance (ISSTA'13, RTAS'19). Our lab also develops text analysis techniques to improve access control policy extraction (FSE'12, ACSAC'14) and precondition extraction from API documents (ICSE'12). 
* Our work in software testing received ***[ICSE SRC Best Project Representing an Innovative Use of Microsoft Technology](https://www.csc.ncsu.edu/news/1347)*** at [ACM SRC Grand Final 2012](https://src.acm.org/grand-finalists/2012). 
* Check out the open sourced tools for [Covana](http://pexase.codeplex.com/wikipage?title=Covana&referringTitle=Home), [APIInfer](https://research.csc.ncsu.edu/ase/projects/pint/).


