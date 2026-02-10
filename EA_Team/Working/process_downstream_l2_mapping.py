import csv
import re

# Read BCM hierarchy
bcm_dict = {}
l1_to_l2 = {}

with open(r'C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\bcm_L1_L2_hierarchy.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        l1_id = row['L1_id']
        l1_name = row['L1_name']
        l2_id = row['L2_id']
        l2_name = row['L2_name']

        bcm_dict[l2_id] = {
            'l1_id': l1_id,
            'l1_name': l1_name,
            'l2_id': l2_id,
            'l2_name': l2_name,
            'l2_description': row.get('L2_description', '')
        }

        if l1_name not in l1_to_l2:
            l1_to_l2[l1_name] = []
        l1_to_l2[l1_name].append({'l2_id': l2_id, 'l2_name': l2_name})

# Read apps
apps = []
with open(r'C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\apps_for_L2_mapping_downstream.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        apps.append({
            'id': row['id'],
            'name': row['name'],
            'description': row['short_description'],
            'vendor': row['vendor'],
            'current_L1_mapping': row['current_L1_mapping']
        })

# Count unique apps
unique_apps = {}
for app in apps:
    app_id = app['id']
    if app_id not in unique_apps:
        unique_apps[app_id] = {
            'id': app_id,
            'name': app['name'],
            'description': app['description'],
            'vendor': app['vendor'],
            'l1_mappings': []
        }
    if app['current_L1_mapping'] and app['current_L1_mapping'].strip():
        if app['current_L1_mapping'] not in unique_apps[app_id]['l1_mappings']:
            unique_apps[app_id]['l1_mappings'].append(app['current_L1_mapping'])

print(f"Total app rows: {len(apps)}")
print(f"Unique apps: {len(unique_apps)}")
print("\nSample unique apps with L1 mappings:")
for i, (app_id, app_info) in enumerate(list(unique_apps.items())[:10]):
    print(f"{app_id}: {app_info['name']} -> L1: {app_info['l1_mappings']}")
