# Day 2 of SRE Challenge  
## Challenge 2: Cloud Storage Optimization  

### Problem Statement  
Using a provided JSON file (`buckets.json`), create a Python script to analyze, modify, and optimize S3 bucket metadata.

### Requirements  

Using the provided JSON file, implement the following:  

1. **Print a Summary of Each Bucket**  
   - Name  
   - Region  
   - Size (in GB)  
   - Versioning status  

2. **Identify Buckets Larger Than 80 GB**  
   - Identify and list buckets larger than 80 GB from every region that have been unused for 90+ days.  

3. **Generate a Cost Report**  
   - Calculate the total S3 bucket cost grouped by region and department, using the cost rate of $0.023 per GB.  

4. **Highlight Buckets with the Following Characteristics**  
   - **Size > 50 GB**: Recommend cleanup operations.  
   - **Size > 100 GB and not accessed in 20+ days**: Add these buckets to a deletion queue.  

5. **Provide a Final List of Buckets to Delete**  
   - From the deletion queue, provide a list of buckets marked for deletion.  
   - For archival candidates, suggest moving to **Glacier**.

---

### How to Run the Script  

1. **Prerequisites**  
   - Python 3.x installed.  
   - A `buckets.json` file containing metadata about S3 buckets.

2. **Setup**  
   - Clone or download this repository.  
   - Place the `buckets.json` file in the same directory as the Python script.

3. **Run the Script**  
   - Run the Python script by executing:  
     ```bash
     python <script_name>.py
     ```

4. **Outputs**  
   The script will print the following:  
   - A **bucket summary** including name, region, size, and versioning status.  
   - A **list of large unused buckets** (larger than 80 GB and unused for 90+ days).  
   - A **cost report** showing total storage costs grouped by region and department.  
   - **Recommendations** for cleanup, deletion, and archival for relevant buckets.

---

### Example Outputs  

![2.](/home/onkar/Desktop/Material/Devops_Sre_Mega_Challenge/Day_02/Output/Day_02_Output.png)
---
