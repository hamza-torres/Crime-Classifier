data = {
    "incident_types": [
        "Threat",
        "Security Breach",
        "Phishing"
    ],
    "communication_types": [
        "Communication",
        "Communication",
        "Cyberbullying"
    ],
    "user_activities": [
        "Data Manipulation",
        "Internet Activity",
        "Data Encryption"
    ],
    "data_categories": [
        "PII Exposure",
        "Financial Data",
        "Trade Secret Breach"
    ],
    "attack_techniques": [
        "Malware Attack",
        "SQL Injection",
        "Brute-force Attack"
    ],
    "investigation_steps": [
        "Evidence Collection",
        "Digital Forensic Analysis",
        "Reporting and Documentation"
    ]
}


texts = [
    # Incident Types
    "Unauthorized access attempt detected from IP address 123.456.789.0",
    "Data breach reported in company database.",
    "Email phishing scam targeting employees.",
    
    # Communication Types
    "Chat conversation related to the case.",
    "Email exchange discussing sensitive information.",
    "Social media post indicating potential cyberbullying.",
    
    # User Activities
    "File deletion activity on suspect's computer.",
    "Suspicious browsing history found on the device.",
    "Evidence of encrypted files on external storage device.",
    
    # Data Categories
    "Disclosure of personal identifiable information (PII).",
    "Financial records found on suspect's computer.",
    "Discovery of confidential business documents on an unauthorized device.",
    
    # Attack Techniques
    "Malware detected in the system.",
    "Evidence of SQL injection attack in the web server logs.",
    "Brute-force login attempts on the network server.",
    
    # Investigation Steps
    "Digital evidence collection and preservation process.",
    "Forensic analysis of hard drive for deleted files.",
    "Documentation and reporting of forensic findings."
]

labels = [
    # Incident Types
    "Threat",
    "Security Breach",
    "Phishing",
    
    # Communication Types
    "Communication",
    "Communication",
    "Cyberbullying",
    
    # User Activities
    "Data Manipulation",
    "Internet Activity",
    "Data Encryption",
    
    # Data Categories
    "PII Exposure",
    "Financial Data",
    "Trade Secret Breach",
    
    # Attack Techniques
    "Malware Attack",
    "SQL Injection",
    "Brute-force Attack",
    
    # Investigation Steps
    "Evidence Collection",
    "Digital Forensic Analysis",
    "Reporting and Documentation"
]

labels = [
    # Data Breach and Customer Information Theft
    "Data Breach and Customer Information Theft",
    "Data Breach and Customer Information Theft",
    "Data Breach and Customer Information Theft",
    "Data Breach and Customer Information Theft",
    "Data Breach and Customer Information Theft",
    
    # Ransomware Attack on Hospitals
    "Ransomware Attack on Hospitals",
    "Ransomware Attack on Hospitals",
    "Ransomware Attack on Hospitals",
    "Ransomware Attack on Hospitals",
    "Ransomware Attack on Hospitals",
    
    # Intellectual Property Theft and Corporate Espionage
    "Intellectual Property Theft and Corporate Espionage",
    "Intellectual Property Theft and Corporate Espionage",
    "Intellectual Property Theft and Corporate Espionage",
    "Intellectual Property Theft and Corporate Espionage",
    "Intellectual Property Theft and Corporate Espionage",
    
    # Online Fraud Schemes: Phishing and Identity Theft
    "Online Fraud Schemes: Phishing and Identity Theft",
    "Online Fraud Schemes: Phishing and Identity Theft",
    "Online Fraud Schemes: Phishing and Identity Theft",
    "Online Fraud Schemes: Phishing and Identity Theft",
    "Online Fraud Schemes: Phishing and Identity Theft",
    
    # Insider Trading and Securities Fraud
    "Insider Trading and Securities Fraud",
    "Insider Trading and Securities Fraud",
    "Insider Trading and Securities Fraud",
    "Insider Trading and Securities Fraud",
    "Insider Trading and Securities Fraud",
    
    # Online Harassment and Stalking
    "Online Harassment and Stalking",
    "Online Harassment and Stalking",
    "Online Harassment and Stalking",
    "Online Harassment and Stalking",
    "Online Harassment and Stalking",
    
    # Insider Threat and Information Leak
    "Insider Threat and Information Leak",
    "Insider Threat and Information Leak",
    "Insider Threat and Information Leak",
    "Insider Threat and Information Leak",
    "Insider Threat and Information Leak",
    
    # Cyberbullying and Harassment
    "Cyberbullying and Harassment",
    "Cyberbullying and Harassment",
    "Cyberbullying and Harassment",
    "Cyberbullying and Harassment",
    "Cyberbullying and Harassment",
    
    # Cryptocurrency Fraud Scheme
    "Cryptocurrency Fraud Scheme",
    "Cryptocurrency Fraud Scheme",
    "Cryptocurrency Fraud Scheme",
    "Cryptocurrency Fraud Scheme",
    "Cryptocurrency Fraud Scheme",
    
    # Involvement in Dark Web Marketplaces
    "Involvement in Dark Web Marketplaces",
    "Involvement in Dark Web Marketplaces",
    "Involvement in Dark Web Marketplaces",
    "Involvement in Dark Web Marketplaces",
    "Involvement in Dark Web Marketplaces",
    
    # Compromised IoT Device in DDoS Attacks
    "Compromised IoT Device in DDoS Attacks",
    "Compromised IoT Device in DDoS Attacks",
    "Compromised IoT Device in DDoS Attacks",
    "Compromised IoT Device in DDoS Attacks",
    "Compromised IoT Device in DDoS Attacks",
    
    # Unauthorized Access and Theft of Classified Information
    "Unauthorized Access and Theft of Classified Information",
    "Unauthorized Access and Theft of Classified Information",
    "Unauthorized Access and Theft of Classified Information",
    "Unauthorized Access and Theft of Classified Information",
    "Unauthorized Access and Theft of Classified Information",
    
    # Piracy and Copyright Infringement
    "Piracy and Copyright Infringement",
    "Piracy and Copyright Infringement",
    "Piracy and Copyright Infringement",
    "Piracy and Copyright Infringement",
    "Piracy and Copyright Infringement",
    
    # Counterfeit Product Scam
    "Counterfeit Product Scam",
    "Counterfeit Product Scam",
    "Counterfeit Product Scam",
    "Counterfeit Product Scam",
    "Counterfeit Product Scam",
    
    # Distributed Intrusion Campaign
    "Distributed Intrusion Campaign",
    "Distributed Intrusion Campaign",
    "Distributed Intrusion Campaign",
    "Distributed Intrusion Campaign",
    "Distributed Intrusion Campaign",
    
    # Online Grooming and Child Exploitation
    "Online Grooming and Child Exploitation",
    "Online Grooming and Child Exploitation",
    "Online Grooming and Child Exploitation",
    "Online Grooming and Child Exploitation",
    "Online Grooming and Child Exploitation",
    
    # Drug Trafficking and Communication with Suppliers
    "Drug Trafficking and Communication with Suppliers",
    "Drug Trafficking and Communication with Suppliers",
    "Drug Trafficking and Communication with Suppliers",
    "Drug Trafficking and Communication with Suppliers",
    "Drug Trafficking and Communication with Suppliers",
    
    # Business Email Compromise (BEC) Scam
    "Business Email Compromise (BEC) Scam",
    "Business Email Compromise (BEC) Scam",
    "Business Email Compromise (BEC) Scam",
    "Business Email Compromise (BEC) Scam",
    "Business Email Compromise (BEC) Scam",
    
    # Terrorist Activities and Extremist Communication
    "Terrorist Activities and Extremist Communication",
    "Terrorist Activities and Extremist Communication",
    "Terrorist Activities and Extremist Communication",
    "Terrorist Activities and Extremist Communication",
    "Terrorist Activities and Extremist Communication",
    
    # Unauthorized Access and Personal Information Theft
    "Unauthorized Access and Personal Information Theft",
    "Unauthorized Access and Personal Information Theft",
    "Unauthorized Access and Personal Information Theft",
    "Unauthorized Access and Personal Information Theft",
    "Unauthorized Access and Personal Information Theft"
]