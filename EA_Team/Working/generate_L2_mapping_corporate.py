#!/usr/bin/env python3
"""
Generate L2 business capability mappings for Corporate Applications
"""
import csv
import re
from collections import defaultdict
from pathlib import Path

# File paths
BCM_FILE = r"C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\bcm_L1_L2_hierarchy.csv"
APPS_FILE = r"C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\apps_for_L2_mapping_corporate.csv"
OUTPUT_FILE = r"C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\L2_mapping_corporate.sql"

# Load BCM hierarchy
bcm_hierarchy = {}  # L1_name -> [(L2_id, L2_name, L2_description), ...]
l1_to_id = {}  # L1_name -> L1_id
l2_lookup = {}  # L2_name -> L2_id
all_l2_by_id = {}  # L2_id -> (L1_name, L2_name, L2_description)

print("Loading BCM hierarchy...")
with open(BCM_FILE, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        l1_id = row['L1_id']
        l1_name = row['L1_name']
        l2_id = row['L2_id']
        l2_name = row['L2_name']
        l2_desc = row['L2_description']

        if l1_name not in bcm_hierarchy:
            bcm_hierarchy[l1_name] = []
            l1_to_id[l1_name] = l1_id

        bcm_hierarchy[l1_name].append((l2_id, l2_name, l2_desc))
        l2_lookup[l2_name] = l2_id
        all_l2_by_id[l2_id] = (l1_name, l2_name, l2_desc)

print(f"Loaded {len(l1_to_id)} L1 capabilities and {len(l2_lookup)} L2 capabilities")

# Load apps
apps_data = []
print("Loading corporate applications...")
with open(APPS_FILE, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        apps_data.append(row)

print(f"Loaded {len(apps_data)} app entries")

# Mapping rules: app name patterns/keywords -> L2 capability names
# This is where the domain expertise comes in
def map_app_to_l2(app_id, app_name, app_desc, vendor, current_l1):
    """
    Map an application to one or more L2 capabilities.
    Returns list of (L2_id, justification) tuples
    """
    mappings = []
    app_lower = app_name.lower()
    desc_lower = app_desc.lower() if app_desc else ""
    vendor_lower = vendor.lower() if vendor else ""

    # SAP and ERP systems
    if 'sap' in app_lower or 'sap' in vendor_lower:
        if 'ecc' in app_lower or 'r/3' in app_lower or 's/4hana' in app_lower:
            # SAP ECC/S4HANA - map to multiple capabilities
            mappings.extend([
                (l2_lookup.get("Perform Transaction Processing"), "SAP ECC core transaction processing"),
                (l2_lookup.get("Reporting Analysis, Consolidation"), "SAP ECC financial reporting and consolidation"),
                (l2_lookup.get("Maintain Master Data (including JV)"), "SAP ECC master data management"),
            ])
        elif 'ariba' in app_lower:
            mappings.append((l2_lookup.get("Procure"), "SAP Ariba procurement platform"))
            mappings.append((l2_lookup.get("Sourcing"), "SAP Ariba sourcing capabilities"))
        elif 'concur' in app_lower:
            mappings.append((l2_lookup.get("Corporate Commerical Travel & Fleet Management"), "SAP Concur for travel and expense management"))
        elif 'successfactors' in app_lower:
            mappings.append((l2_lookup.get("Performance Management"), "SAP SuccessFactors performance management"))
            mappings.append((l2_lookup.get("Recruitment"), "SAP SuccessFactors recruiting"))

    # Microsoft 365 and Office suite
    if 'microsoft' in vendor_lower or 'office 365' in app_lower or 'm365' in app_lower or 'sharepoint' in app_lower:
        if 'sharepoint' in app_lower:
            mappings.append((l2_lookup.get("Content Management"), "SharePoint document and content management"))
        elif 'teams' in app_lower:
            mappings.append((l2_lookup.get("Collaboration"), "Microsoft Teams collaboration platform"))
        elif 'office' in app_lower or 'excel' in app_lower or 'word' in app_lower:
            mappings.append((l2_lookup.get("Office Productivity"), "Microsoft Office productivity suite"))
        elif 'exchange' in app_lower or 'outlook' in app_lower:
            mappings.append((l2_lookup.get("Unified Communications"), "Microsoft Exchange email and communications"))

    # HR and People systems
    if 'workday' in app_lower or 'workday' in vendor_lower:
        mappings.append((l2_lookup.get("Performance Management"), "Workday HCM performance management"))
        mappings.append((l2_lookup.get("Payroll"), "Workday payroll processing"))
        mappings.append((l2_lookup.get("Compensation"), "Workday compensation management"))
        mappings.append((l2_lookup.get("Recruitment"), "Workday talent acquisition"))

    if 'adp' in app_lower or 'adp' in vendor_lower:
        mappings.append((l2_lookup.get("Payroll"), "ADP payroll processing"))
        mappings.append((l2_lookup.get("Benefits"), "ADP benefits administration"))

    # Learning and development
    if 'learning' in app_lower or 'training' in app_lower or 'lms' in app_lower:
        mappings.append((l2_lookup.get("Learning Management"), "Learning management system"))
        if 'safety' in desc_lower or 'hse' in desc_lower:
            mappings.append((l2_lookup.get("Training & Qualification"), "Safety training and qualification tracking"))

    # Risk and compliance
    if 'risk' in app_lower:
        if 'cyber' in app_lower or 'security' in app_lower:
            mappings.append((l2_lookup.get("Cyber Risk Identification"), "Cybersecurity risk assessment"))
        else:
            mappings.append((l2_lookup.get("Monitor Risk Policy Compliance"), "Enterprise risk monitoring"))

    if 'compliance' in app_lower or 'regulatory' in app_lower:
        mappings.append((l2_lookup.get("Manage Regulatory Compliance & Regulations"), "Regulatory compliance management"))
        if 'audit' in app_lower or 'audit' in desc_lower:
            mappings.append((l2_lookup.get("Manage Regulatory & Environmental Audits"), "Compliance audit management"))

    # Financial and accounting
    if 'accounting' in desc_lower or 'finance' in app_lower:
        if 'asset' in app_lower or 'capital' in app_lower:
            mappings.append((l2_lookup.get("Perform Fixed Asset Accounting"), "Fixed asset and capital accounting"))
        elif 'tax' in app_lower:
            mappings.append((l2_lookup.get("Income Taxes"), "Tax planning and compliance"))
        elif 'treasury' in app_lower or 'cash' in app_lower:
            mappings.append((l2_lookup.get("Manage Cash Accounts"), "Treasury and cash management"))
        else:
            mappings.append((l2_lookup.get("Perform Transaction Processing"), "Financial transaction processing"))

    # Supply chain and procurement
    if 'procurement' in desc_lower or 'purchasing' in app_lower or 'supplier' in app_lower:
        mappings.append((l2_lookup.get("Procure"), "Procurement execution"))
        if 'contract' in app_lower or 'contracting' in desc_lower:
            mappings.append((l2_lookup.get("Contracting"), "Contract management"))

    if 'inventory' in app_lower or 'warehouse' in app_lower or 'materials' in app_lower:
        mappings.append((l2_lookup.get("Inventory Management (Materials)"), "Materials inventory management"))

    # Data and analytics
    if 'power bi' in app_lower or 'powerbi' in app_lower or 'tableau' in app_lower or 'spotfire' in app_lower:
        mappings.append((l2_lookup.get("BI, Analytics & Data Science"), "Business intelligence and analytics"))

    if 'data warehouse' in app_lower or 'data lake' in desc_lower:
        mappings.append((l2_lookup.get("Data Management Technology"), "Data warehousing and analytics infrastructure"))

    # Document and content management
    if 'document' in app_lower or 'content management' in desc_lower or 'ecm' in app_lower:
        mappings.append((l2_lookup.get("Content Management"), "Document and content management"))

    if 'archive' in app_lower:
        mappings.append((l2_lookup.get("Content Management"), "Data archiving and retention"))

    # Security and access control
    if 'security' in app_lower or 'access control' in desc_lower:
        if 'cyber' in app_lower or 'threat' in app_lower:
            mappings.append((l2_lookup.get("Cyber Detection"), "Cybersecurity monitoring and detection"))
        elif 'physical' in desc_lower or 'badge' in desc_lower or 'gate' in desc_lower:
            mappings.append((l2_lookup.get("Safe Operations"), "Physical security and access control"))

    # Environmental and HSE
    if 'environmental' in desc_lower or 'emission' in app_lower or 'hse' in app_lower:
        if 'water' in app_lower:
            mappings.append((l2_lookup.get("Manage Water"), "Water management and compliance"))
        elif 'air' in app_lower or 'emission' in app_lower:
            mappings.append((l2_lookup.get("Manage Air Emissions"), "Air quality and emissions management"))
        elif 'waste' in app_lower:
            mappings.append((l2_lookup.get("Manage Waste"), "Waste management"))
        else:
            mappings.append((l2_lookup.get("Manage Regulatory Compliance & Regulations"), "Environmental compliance management"))

    # Safety
    if 'safety' in app_lower or 'incident' in app_lower:
        if 'incident' in app_lower:
            mappings.append((l2_lookup.get("Safe Operations"), "Safety incident management"))
        else:
            mappings.append((l2_lookup.get("Safe Operations"), "Safety operations and monitoring"))

    # Legal
    if 'legal' in app_lower or 'contract' in app_lower:
        if 'contract' in app_lower and 'procurement' not in desc_lower:
            mappings.append((l2_lookup.get("Contracting"), "Legal contract management"))

    # IT and technology
    if 'azure' in app_lower or 'aws' in app_lower or 'cloud' in app_lower:
        mappings.append((l2_lookup.get("Cloud Services"), "Cloud infrastructure services"))

    if 'automation' in app_lower or 'rpa' in app_lower:
        mappings.append((l2_lookup.get("Workflow Automation"), "Robotic process automation"))

    if 'service desk' in app_lower or 'servicenow' in app_lower or 'itsm' in app_lower:
        mappings.append((l2_lookup.get("IT Operations"), "IT service management and operations"))

    # Travel and accommodation
    if 'travel' in app_lower or 'accommodation' in app_lower:
        mappings.append((l2_lookup.get("Corporate Commerical Travel & Fleet Management"), "Corporate travel management"))

    # Communication and engagement
    if 'communication' in desc_lower or 'stakeholder' in app_lower:
        mappings.append((l2_lookup.get("Manage Corporate Communications"), "Corporate communications"))

    # Remove None mappings
    mappings = [(l2_id, just) for l2_id, just in mappings if l2_id is not None]

    # If we have a current_L1 mapping but no L2 mappings yet, try to find a default L2 under that L1
    if not mappings and current_l1 and current_l1 in bcm_hierarchy:
        # Get the first L2 under this L1 as a fallback
        l2_options = bcm_hierarchy[current_l1]
        if l2_options:
            first_l2 = l2_options[0]
            mappings.append((first_l2[0], f"Mapped to {first_l2[1]} under existing L1: {current_l1}"))

    return mappings

# Process apps and generate SQL
sql_statements = []
app_count = 0
insert_count = 0
processed_apps = set()

for row in apps_data:
    app_id = row['id']
    app_name = row['name']
    app_desc = row['short_description']
    vendor = row['vendor']
    current_l1 = row['current_L1_mapping']

    # Skip if we've already processed this app ID
    if app_id in processed_apps:
        continue

    processed_apps.add(app_id)
    app_count += 1

    # Get L2 mappings
    l2_mappings = map_app_to_l2(app_id, app_name, app_desc, vendor, current_l1)

    if not l2_mappings:
        # Fallback: try to map based on current_L1
        if current_l1 and current_l1 in bcm_hierarchy:
            l2_options = bcm_hierarchy[current_l1]
            if l2_options:
                # Just pick the first one as a placeholder
                l2_mappings = [(l2_options[0][0], f"Default mapping under {current_l1}")]

    if l2_mappings:
        # Generate SQL for this app
        sql_statements.append(f"-- {app_name} (ID: {app_id})")
        for l2_id, justification in l2_mappings:
            # Escape single quotes in justification
            safe_just = justification.replace("'", "''")
            sql = f"INSERT OR IGNORE INTO app_business_capability (application_id, business_capability_id, capability_role, notes) VALUES ({app_id}, {l2_id}, 'Primary', '{safe_just}');"
            sql_statements.append(sql)
            insert_count += 1
        sql_statements.append("")  # Blank line for readability

# Write SQL file
print(f"\nGenerating SQL file: {OUTPUT_FILE}")
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("-- ========================================\n")
    f.write("-- L2 Business Capability Mapping for Corporate Applications\n")
    f.write("-- ========================================\n")
    f.write(f"-- Total Applications Processed: {app_count}\n")
    f.write(f"-- Total INSERT Statements: {insert_count}\n")
    f.write("-- ========================================\n\n")

    for stmt in sql_statements:
        f.write(stmt + "\n")

print(f"✓ Generated {insert_count} INSERT statements for {app_count} applications")
print(f"✓ SQL file written to: {OUTPUT_FILE}")
