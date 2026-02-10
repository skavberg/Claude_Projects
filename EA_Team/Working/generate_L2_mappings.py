#!/usr/bin/env python3
"""
Generate L2 Business Capability Mappings for Enterprise, Shared Services, Cybersecurity, OT, and AI Applications
"""

import csv
import re
from typing import Dict, List, Set, Tuple

# Read BCM Hierarchy
def load_bcm_hierarchy(filepath: str) -> Dict[int, Dict]:
    """Load BCM L1 and L2 hierarchy"""
    bcm = {}
    l1_to_l2 = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            l1_id = int(row['L1_id'])
            l1_name = row['L1_name']
            l2_id = int(row['L2_id'])
            l2_name = row['L2_name']
            l2_desc = row['L2_description']

            if l1_id not in l1_to_l2:
                l1_to_l2[l1_id] = {'name': l1_name, 'l2s': []}

            l1_to_l2[l1_id]['l2s'].append({
                'id': l2_id,
                'name': l2_name,
                'description': l2_desc
            })

            bcm[l2_id] = {
                'l1_id': l1_id,
                'l1_name': l1_name,
                'l2_name': l2_name,
                'l2_description': l2_desc
            }

    return bcm, l1_to_l2

# Read Apps List
def load_apps(filepath: str) -> List[Dict]:
    """Load application list"""
    apps = []

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            apps.append({
                'id': int(row['id']),
                'name': row['name'],
                'business_unit': row['business_unit'],
                'short_description': row['short_description'],
                'vendor': row['vendor'],
                'current_L1_mapping': row['current_L1_mapping']
            })

    return apps

def escape_sql_string(s: str) -> str:
    """Escape single quotes for SQL"""
    return s.replace("'", "''")

def map_app_to_l2(app: Dict, bcm: Dict, l1_to_l2: Dict) -> List[Tuple[int, str]]:
    """
    Map an application to L2 capabilities
    Returns list of (l2_id, justification) tuples
    """
    mappings = []

    app_name = app['name'].lower()
    app_desc = app['short_description'].lower()
    app_vendor = app['vendor'].lower()
    business_unit = app['business_unit']
    current_l1 = app['current_L1_mapping']

    # Helper function to find L2 by name pattern
    def find_l2_by_name(pattern: str, l1_constraint: str = None) -> List[int]:
        results = []
        for l2_id, info in bcm.items():
            if l1_constraint and info['l1_name'] != l1_constraint:
                continue
            if pattern.lower() in info['l2_name'].lower():
                results.append(l2_id)
        return results

    # Helper to check if keyword in app name or description
    def has_keyword(*keywords) -> bool:
        combined = f"{app_name} {app_desc} {app_vendor}"
        return any(kw.lower() in combined for kw in keywords)

    # === SHARED SERVICES APPS (Apps - Shared Services) ===
    if business_unit == "Apps - Shared Services":

        # Active Directory, Identity, Access Management
        if has_keyword('active directory', 'ad recovery', 'adaudit', 'azure ad', 'entra', 'identity', 'iam', 'pim', 'privileged', 'access management', 'beyondid'):
            # Identity Management, Authentication and Access Control
            l2_ids = find_l2_by_name("Identity Management, Authentication and Access Control")
            if l2_ids:
                mappings.append((l2_ids[0], "Identity and access management platform"))

        # Communication tools (Exchange, Jabber, Unified Communications)
        if has_keyword('exchange', 'jabber', 'unified communication', 'email', 'cisco jabber'):
            l2_ids = find_l2_by_name("Unified Communications")
            if l2_ids:
                mappings.append((l2_ids[0], "Enterprise communication platform"))

        # Collaboration tools (SharePoint, Teams, Office)
        if has_keyword('sharepoint', 'office', 'collaboration', 'productivity'):
            l2_ids = find_l2_by_name("Collaboration")
            if l2_ids:
                mappings.append((l2_ids[0], "Collaboration and productivity tool"))
            l2_ids = find_l2_by_name("Office Productivity")
            if l2_ids:
                mappings.append((l2_ids[0], "Office productivity suite"))

        # Device Management
        if has_keyword('device', 'endpoint', 'mobile device', 'mdm'):
            l2_ids = find_l2_by_name("Device Management")
            if l2_ids:
                mappings.append((l2_ids[0], "Device lifecycle and configuration management"))

        # Backup and Recovery
        if has_keyword('backup', 'commvault', 'recovery', 'airgap', 'cloudendure'):
            l2_ids = find_l2_by_name("IT Service Continuity")
            if l2_ids:
                mappings.append((l2_ids[0], "Backup and disaster recovery"))

        # Automation tools (Ansible, Chocolatey, etc.)
        if has_keyword('ansible', 'automation', 'chocolatey', 'workflow'):
            l2_ids = find_l2_by_name("Workflow Automation")
            if l2_ids:
                mappings.append((l2_ids[0], "IT automation and orchestration"))

        # Development/Build tools
        if has_keyword('codecommit', 'git', 'build', 'ci/cd', 'cast'):
            l2_ids = find_l2_by_name("Build & Automation Tools")
            if l2_ids:
                mappings.append((l2_ids[0], "Software development and build tooling"))

        # Cloud services (AWS, Azure)
        if has_keyword('aws', 'azure', 'cloud'):
            l2_ids = find_l2_by_name("Cloud Services")
            if l2_ids:
                mappings.append((l2_ids[0], "Cloud infrastructure and services"))

        # Network and connectivity
        if has_keyword('network', 'aruba', 'cisco transport', 'f5', 'loadbalancer', 'vpn'):
            l2_ids = find_l2_by_name("Network Connectivity")
            if l2_ids:
                mappings.append((l2_ids[0], "Network infrastructure and connectivity"))

        # Printing services
        if has_keyword('print', 'cups', 'jetadmin'):
            l2_ids = find_l2_by_name("Office Productivity")
            if l2_ids:
                mappings.append((l2_ids[0], "Print services management"))

        # Certificate services
        if has_keyword('certificate', 'pki', 'key management'):
            l2_ids = find_l2_by_name("Cyber Protection")
            if l2_ids:
                mappings.append((l2_ids[0], "Certificate and key management"))

        # Remote access (Citrix, VPN)
        if has_keyword('citrix', 'remote access', 'virtual app'):
            l2_ids = find_l2_by_name("Mobility")
            if l2_ids:
                mappings.append((l2_ids[0], "Remote access and virtual desktop"))

        # Monitoring and operations
        if has_keyword('monitoring', 'insight', 'operations'):
            l2_ids = find_l2_by_name("IT Operations")
            if l2_ids:
                mappings.append((l2_ids[0], "IT infrastructure monitoring"))

        # Wiki and documentation
        if has_keyword('wiki', 'documentation', 'docuwiki'):
            l2_ids = find_l2_by_name("Content Management")
            if l2_ids:
                mappings.append((l2_ids[0], "Knowledge management and documentation"))

    # === CYBERSECURITY APPS (Cyber Security Operations) ===
    elif business_unit == "Cyber Security Operations":

        # Threat detection and response
        if has_keyword('threat', 'falcon', 'crowdstrike', 'endace', 'cribl'):
            l2_ids = find_l2_by_name("Cyber Detection")
            if l2_ids:
                mappings.append((l2_ids[0], "Threat detection and monitoring"))
            l2_ids = find_l2_by_name("Cyber Response")
            if l2_ids:
                mappings.append((l2_ids[0], "Incident response and analysis"))

        # Antivirus and endpoint protection
        if has_keyword('antivirus', 'clam', 'endpoint', 'bit9', 'carbon black'):
            l2_ids = find_l2_by_name("Cyber Protection")
            if l2_ids:
                mappings.append((l2_ids[0], "Endpoint security and protection"))

        # Authentication and MFA
        if has_keyword('mfa', 'multi-factor', 'authentication', 'duo'):
            l2_ids = find_l2_by_name("Cyber Protection")
            if l2_ids:
                mappings.append((l2_ids[0], "Multi-factor authentication"))

        # Password management
        if has_keyword('password', 'self-service password'):
            l2_ids = find_l2_by_name("Cyber Protection")
            if l2_ids:
                mappings.append((l2_ids[0], "Password lifecycle management"))

        # VPN and remote access security
        if has_keyword('vpn', 'global protect', 'secure connector', 'private network'):
            l2_ids = find_l2_by_name("Cyber Protection")
            if l2_ids:
                mappings.append((l2_ids[0], "Secure remote access"))

        # Network security (firewalls, access control)
        if has_keyword('firewall', 'access control', 'external dynamic list', 'forescout'):
            l2_ids = find_l2_by_name("Cyber Protection")
            if l2_ids:
                mappings.append((l2_ids[0], "Network security controls"))

        # Data protection (AIP, encryption)
        if has_keyword('information protection', 'aip', 'encryption', 'data security'):
            l2_ids = find_l2_by_name("Cyber Protection")
            if l2_ids:
                mappings.append((l2_ids[0], "Data classification and protection"))

        # Conditional access and access control
        if has_keyword('conditional access', 'access control'):
            l2_ids = find_l2_by_name("Cyber Protection")
            if l2_ids:
                mappings.append((l2_ids[0], "Conditional access policies"))

        # Security monitoring tools
        if has_keyword('httpwatch', 'web', 'traffic'):
            l2_ids = find_l2_by_name("Cyber Detection")
            if l2_ids:
                mappings.append((l2_ids[0], "Web traffic analysis and monitoring"))

        # Risk assessment
        if has_keyword('risk', 'assessment', 'vulnerability'):
            l2_ids = find_l2_by_name("Cyber Risk Identification")
            if l2_ids:
                mappings.append((l2_ids[0], "Cyber risk assessment"))

    # === OT / INFRASTRUCTURE APPS (Business - OT (BST/LOB), Business - HMGP (BST/LOB)) ===
    elif business_unit in ["Business - OT (BST/LOB)", "Business - HMGP (BST/LOB)"]:

        # SCADA and control systems
        if has_keyword('scada', 'controlwave', 'deltav', 'cygnet', 'factorytalk', 'geifix', 'system 1'):
            l2_ids = find_l2_by_name("Equipment Monitoring & Control")
            if l2_ids:
                mappings.append((l2_ids[0], "Process control and SCADA systems"))

        # Pipeline management
        if has_keyword('pipeline', 'dss', 'bss', 'decision support'):
            l2_ids = find_l2_by_name("Pipeline Operations")
            if l2_ids:
                mappings.append((l2_ids[0], "Pipeline monitoring and control"))

        # Equipment maintenance and reliability
        if has_keyword('vibration', 'equipment', 'maintenance', 'bentley nevada'):
            l2_ids = find_l2_by_name("Asset Reliability Management")
            if l2_ids:
                mappings.append((l2_ids[0], "Equipment reliability monitoring"))

    # === ENTERPRISE APPS (Apps - Enterprise) ===
    elif business_unit == "Apps - Enterprise":

        # BI and Analytics (Databricks, Crystal Reports, Spotfire)
        if has_keyword('databricks', 'bi', 'crystal reports', 'analytics', 'spotfire', 'datamart'):
            l2_ids = find_l2_by_name("BI, Analytics & Data Science")
            if l2_ids:
                mappings.append((l2_ids[0], "Business intelligence and analytics"))

        # Data Management and Integration
        if has_keyword('data query', 'edq', 'fds database', 'data integration', 'cpi-ds'):
            l2_ids = find_l2_by_name("Data & Knowledge Management")
            if not l2_ids:
                l2_ids = find_l2_by_name("Master Data & Data Quality Management")
            if l2_ids:
                mappings.append((l2_ids[0], "Master data and data integration"))

        # SAP integration and middleware
        if has_keyword('cpi-ds', 'sap', 'hana', 'eim'):
            l2_ids = find_l2_by_name("Integration Architecture")
            if l2_ids:
                mappings.append((l2_ids[0], "SAP integration services"))

        # Travel and Expense (Concur)
        if has_keyword('concur', 'travel', 'expense'):
            if 'travel' in app_name.lower() or 'accommodation' in app_desc.lower():
                l2_ids = find_l2_by_name("Corporate Commerical Travel & Fleet Management")
                if l2_ids:
                    mappings.append((l2_ids[0], "Corporate travel management"))
            l2_ids = find_l2_by_name("General Accounting & Budgeting")
            if l2_ids:
                mappings.append((l2_ids[0], "Expense reporting and processing"))

        # Procurement and Supply Chain (Ariba, Cortex)
        if has_keyword('ariba', 'procurement', 'sourcing'):
            l2_ids = find_l2_by_name("Sourcing")
            if l2_ids:
                mappings.append((l2_ids[0], "Strategic sourcing and procurement"))

        if has_keyword('cortex', 'supplier', 'vendor', 'edi'):
            l2_ids = find_l2_by_name("Supplier Lifecycle Management")
            if l2_ids:
                mappings.append((l2_ids[0], "Supplier relationship and data exchange"))
            l2_ids = find_l2_by_name("Procure")
            if l2_ids:
                mappings.append((l2_ids[0], "Purchase order processing"))

        # HR and Talent (FieldGlass, Enable Now)
        if has_keyword('fieldglass', 'contingent', 'contractor'):
            l2_ids = find_l2_by_name("Recruitment")
            if l2_ids:
                mappings.append((l2_ids[0], "Contingent workforce management"))
            l2_ids = find_l2_by_name("Resource Allocation")
            if l2_ids:
                mappings.append((l2_ids[0], "Contractor resource scheduling"))

        if has_keyword('enable now', 'training', 'learning'):
            l2_ids = find_l2_by_name("Learning Management")
            if l2_ids:
                mappings.append((l2_ids[0], "Learning and training delivery"))

        # Security and threat detection (SAP ETD)
        if has_keyword('threat detection', 'etd', 'security event'):
            l2_ids = find_l2_by_name("Cyber Detection")
            if l2_ids:
                mappings.append((l2_ids[0], "SAP security monitoring"))

    # === DATA AND AI GOVERNANCE (Apps - Data and AI Goverance) ===
    elif business_unit == "Apps - Data and AI Goverance":

        # AI and chatbot tools
        if has_keyword('askit', 'ai', 'chatbot', 'chat interface'):
            l2_ids = find_l2_by_name("AI Creation")
            if l2_ids:
                mappings.append((l2_ids[0], "AI-enabled support interface"))
            l2_ids = find_l2_by_name("IT Operations")
            if l2_ids:
                mappings.append((l2_ids[0], "Self-service IT support"))

        # Corporate Data Platform (CDP)
        if has_keyword('cdp', 'corporate data platform', 'databricks'):
            l2_ids = find_l2_by_name("Data Governance")
            if l2_ids:
                mappings.append((l2_ids[0], "Enterprise data governance"))
            l2_ids = find_l2_by_name("Master Data & Data Quality Management")
            if l2_ids:
                mappings.append((l2_ids[0], "Master data management"))
            l2_ids = find_l2_by_name("BI, Analytics & Data Science")
            if l2_ids:
                mappings.append((l2_ids[0], "Advanced analytics platform"))

    # === FALLBACK: Use current_L1_mapping if exists and no mappings found yet ===
    if not mappings and current_l1:
        # Find L2s under this L1
        for l1_id, l1_info in l1_to_l2.items():
            if l1_info['name'] == current_l1:
                # Pick the first L2 as a fallback
                if l1_info['l2s']:
                    first_l2 = l1_info['l2s'][0]
                    mappings.append((first_l2['id'], f"Mapped to {first_l2['name']} under existing L1 {current_l1}"))
                break

    # === FINAL FALLBACK: Map to a generic IT capability if still nothing ===
    if not mappings:
        # Default to IT Operations or Application Service Delivery
        l2_ids = find_l2_by_name("IT Operations")
        if l2_ids:
            mappings.append((l2_ids[0], "General IT operations support"))

    return mappings


def generate_sql(apps: List[Dict], bcm: Dict, l1_to_l2: Dict, output_path: str):
    """Generate SQL mapping file"""

    total_inserts = 0
    processed_apps = set()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("-- =====================================================\n")
        f.write("-- L2 Business Capability Mappings\n")
        f.write("-- Enterprise, Shared Services, Cybersecurity, OT, AI Apps\n")
        f.write("-- =====================================================\n")
        f.write("-- Total apps to process: TBD\n")
        f.write("-- Total INSERT statements: TBD\n")
        f.write("--\n")
        f.write("-- Generated by: Enterprise Applications Portfolio Architect\n")
        f.write("-- Date: 2026-02-09\n")
        f.write("-- =====================================================\n\n")

        for app in apps:
            app_id = app['id']
            app_name = app['name']

            # Skip duplicate app IDs (same app may appear multiple times with different L1 mappings)
            if app_id in processed_apps:
                continue
            processed_apps.add(app_id)

            # Get L2 mappings
            l2_mappings = map_app_to_l2(app, bcm, l1_to_l2)

            # Write comment header
            f.write(f"-- ==========================================\n")
            f.write(f"-- App ID: {app_id}\n")
            f.write(f"-- App Name: {app_name}\n")
            f.write(f"-- Business Unit: {app['business_unit']}\n")
            f.write(f"-- Current L1: {app['current_L1_mapping'] if app['current_L1_mapping'] else 'None'}\n")
            f.write(f"-- ==========================================\n")

            # Write INSERT statements
            for l2_id, justification in l2_mappings:
                l2_info = bcm.get(l2_id)
                if l2_info:
                    f.write(f"-- L2: {l2_info['l2_name']} (under L1: {l2_info['l1_name']})\n")

                safe_justification = escape_sql_string(justification)
                sql = f"INSERT OR IGNORE INTO app_business_capability (application_id, business_capability_id, capability_role, notes)\n"
                sql += f"VALUES ({app_id}, {l2_id}, 'Primary', '{safe_justification}');\n"
                f.write(sql)
                f.write("\n")
                total_inserts += 1

        f.write(f"\n-- =====================================================\n")
        f.write(f"-- SUMMARY\n")
        f.write(f"-- Total unique apps processed: {len(processed_apps)}\n")
        f.write(f"-- Total INSERT statements: {total_inserts}\n")
        f.write(f"-- =====================================================\n")

    return len(processed_apps), total_inserts


def main():
    bcm_file = r"C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\bcm_L1_L2_hierarchy.csv"
    apps_file = r"C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\apps_for_L2_mapping_other.csv"
    output_file = r"C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\L2_mapping_other.sql"

    print("Loading BCM hierarchy...")
    bcm, l1_to_l2 = load_bcm_hierarchy(bcm_file)
    print(f"Loaded {len(bcm)} L2 capabilities")

    print("Loading applications...")
    apps = load_apps(apps_file)
    print(f"Loaded {len(apps)} app entries")

    print("Generating SQL mappings...")
    num_apps, num_inserts = generate_sql(apps, bcm, l1_to_l2, output_file)

    print(f"\nDONE!")
    print(f"Processed {num_apps} unique applications")
    print(f"Generated {num_inserts} INSERT statements")
    print(f"Output file: {output_file}")


if __name__ == "__main__":
    main()
