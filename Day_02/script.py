import json
from datetime import datetime, timedelta


with open('buckets.json') as f:
    data = json.load(f)['buckets']

COST_PER_GB = 0.023
ninety_days_ago = datetime.now() - timedelta(days=90)
twenty_days_ago = datetime.now() - timedelta(days=20)


def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

print("Bucket Summary:")
for bucket in data:
    print(f"Name: {bucket['name']}, Region: {bucket['region']}, Size: {bucket['sizeGB']} GB, Versioning: {bucket['versioning']}")

large_unused_buckets = [
    bucket for bucket in data
    if bucket['sizeGB'] > 80 and parse_date(bucket['createdOn']) < ninety_days_ago
]

print("\nLarge Unused Buckets (Size > 80 GB and unused for 90+ days):")
for bucket in large_unused_buckets:
    print(f"{bucket['name']} in {bucket['region']} - {bucket['sizeGB']} GB")

cost_by_region_dept = {}
cleanup_buckets = []
deletion_queue = []

for bucket in data:
    region = bucket['region']
    department = bucket['tags'].get('team', 'unknown')
    cost = bucket['sizeGB'] * COST_PER_GB
    key = (region, department)
    cost_by_region_dept[key] = cost_by_region_dept.get(key, 0) + cost

    if bucket['sizeGB'] > 50:
        cleanup_buckets.append(bucket)
    if bucket['sizeGB'] > 100 and parse_date(bucket['createdOn']) < twenty_days_ago:
        deletion_queue.append(bucket)

print("\nCost by Region and Department:")
for (region, department), total_cost in cost_by_region_dept.items():
    print(f"{region} - {department}: ${total_cost:.2f}")

print("\nBuckets Recommended for Cleanup (Size > 50 GB):")
for bucket in cleanup_buckets:
    print(f"{bucket['name']} - {bucket['sizeGB']} GB")

print("\nBuckets in Deletion Queue (Size > 100 GB, not accessed in 20+ days):")
for bucket in deletion_queue:
    print(f"{bucket['name']} - {bucket['sizeGB']} GB")


print("\nFinal List of Buckets for Deletion:")
for bucket in deletion_queue:
    print(f"{bucket['name']} in {bucket['region']} - {bucket['sizeGB']} GB (Consider moving to Glacier)")
