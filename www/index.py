def get_context(context):
    context.hero = {
        "badge": "New • ERPNext-native",
        "title": "System Expert for ERPNext",
        "subtitle": "Automate routine ops, get instant answers, and boost throughput across finance, inventory, and fulfillment.",
        "primary_label": "Get Started",
        "primary_href": "#get-started",
        "secondary_label": "See Features",
        "secondary_href": "#features",
        "image": None,
        "kpis": [
            {"num": "98%", "label": "Request auto-resolution"},
            {"num": "10x", "label": "Faster insights"},
            {"num": "0 code", "label": "Admin setup"},
        ],
    }
    context.logos = {
        "heading": "Trusted by modern teams",
        "items": [
            {"src": "/assets/system_expert_site/images/logo1.svg", "alt": "Logo 1"},
            {"src": "/assets/system_expert_site/images/logo2.svg", "alt": "Logo 2"},
            {"src": "/assets/system_expert_site/images/logo3.svg", "alt": "Logo 3"},
            {"src": "/assets/system_expert_site/images/logo4.svg", "alt": "Logo 4"},
        ]
    }
    context.features = {
        "title": "Everything you need to move fast",
        "subtitle": "Modular capabilities that snap into your ERPNext workflows.",
        "items": [
            {"title": "Natural language queries", "desc": "Ask questions across ledgers, inventory, CRM, and projects; get precise answers with citations."},
            {"title": "Automated approvals", "desc": "Route POs, leave requests, and expenses to the right approvers with policy-aware checks."},
            {"title": "Exception detection", "desc": "Surface anomalies in payments, stock, and receivables before they become issues."},
            {"title": "Workflow builder", "desc": "Compose no-code automations triggered by forms, webhooks, or schedules."},
            {"title": "Secure by design", "desc": "Respects ERPNext roles & permissions. Full audit trail."},
            {"title": "Extensible", "desc": "Bring your own models, connect external data sources via REST."},
        ]
    }
    context.how = {
        "title": "How it works",
        "subtitle": "Three steps to value.",
        "steps": [
            {"title": "Connect your ERPNext", "desc": "Install the app, enable website, and authenticate."},
            {"title": "Choose modules", "desc": "Turn on features like approvals, insights, or automations."},
            {"title": "Refine policies", "desc": "Set thresholds, exceptions, and escalation rules."},
        ]
    }
    context.testimonials = {
        "title": "Loved by operators",
        "subtitle": "What teams say about System Expert.",
        "items": [
            {"quote": "We cut cycle time on approvals by 70% in two weeks.", "author": "Alex Chen", "role": "Ops Lead, Northwind"},
            {"quote": "Finally, answers across modules without exports.", "author": "Maya Al-Fulan", "role": "Finance Manager"},
            {"quote": "Setup took minutes; results showed the same day.", "author": "Omar Rahman", "role": "COO"},
        ]
    }
    context.pricing = {
        "title": "Simple pricing",
        "subtitle": "Start free, grow with your team.",
        "plans": [
            {"name":"Starter","price":"$0","period":"Free forever","features":["Basic insights","Up to 3 workflows","Community support"],"cta_label":"Start free","cta_href":"#get-started"},
            {"name":"Pro","price":"$49","period":"per user / mo","features":["Advanced queries","Unlimited workflows","Role-based governance"],"cta_label":"Start Pro","cta_href":"#get-started"},
            {"name":"Enterprise","price":"Contact","period":"Custom","features":["SSO & SAML","On-prem support","Dedicated SLA"],"cta_label":"Contact Sales","cta_href":"/contact"},
        ]
    }
    context.cta = {
        "title": "Ready to try System Expert?",
        "subtitle": "Install the app, connect your ERPNext, and ship faster.",
        "href": "/contact",
        "label": "Contact sales"
    }
