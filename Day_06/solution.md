# DevOps SRE Daily Challenge - Custom AMI Creation & Resource Management

## Overview

This challenge focuses on creating a custom Amazon Machine Image (AMI) from an EC2 instance, applying security hardening, copying the AMI and snapshots across AWS regions, and managing resources efficiently for scalability and disaster recovery.

---

## Steps to Complete the Challenge

### Step 1: Create a Custom AMI

#### 1.1 Launch an EC2 Instance

- Go to the **AWS Management Console** and navigate to the **EC2 Dashboard**.
- Click on **Launch Instance**.
- **AMI:** Choose **Ubuntu 22.04 LTS**.
- **Instance Type:** Select **t2.micro**.
- **Key Pair:** Create/select a key pair for SSH access.
- **Security Group:** Open ports `22` (SSH) and `80` (HTTP).

#### 1.2 Install Nginx and Security Tools

SSH into the instance:

```bash
ssh -i <your-key.pem> ubuntu@<ec2-public-ip>

Install Nginx:
    
    sudo apt update
    sudo apt install nginx -y

Start and enable Nginx:

    sudo systemctl start nginx
    sudo systemctl enable nginx

Install AWS Inspector Agent (for security hardening):

    curl -O https://inspector-agent.amazonaws.com/linux/latest/install
    sudo bash install

Apply Security Hardening:

    Disable root login:
        
        sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
        sudo systemctl restart ssh

Configure firewall to allow Nginx:

    sudo ufw allow 'Nginx HTTP'
    sudo ufw enable

Enforce password policies: Edit /etc/pam.d/common-password:

    sudo nano /etc/pam.d/common-password


    Add the following line:

    password requisite pam_pwquality.so retry=3 minlen=12 dcredit=-1 ucredit=-1 ocredit=-1 lcredit=-1


Create the Custom AMI
    
    Stop the EC2 instance:

    aws ec2 stop-instances --instance-ids <instance-id>

    Create the custom AMI:

    aws ec2 create-image --instance-id <instance-id> --name "Ubuntu-Nginx-Custom-AMI"


Step 2: Copy the Custom AMI to Another Region

Copy the AMI to Target Region

    Get the AMI ID:

        aws ec2 describe-images --owners self

    Copy the AMI to the target region:

        aws ec2 copy-image --source-image-id <ami-id> --source-region us-east-1 --region us-west-2 --name "Ubuntu-Nginx-Custom-AMI-Copy"


Step 3 :Launch a New Instance from the Copied AMI

    Launch a New Instance in the Target Region:

        aws ec2 run-instances --image-id <ami-id> --count 1 --instance-type t2.micro --key-name <key-name> --security-group-ids <sg-id> --subnet-id <subnet-id>

Step 4: Prepare a Volume Snapshot
        
    Create a Snapshot of an Existing Volume

        Identify the volume ID attached to your EC2 instance:

            aws ec2 describe-volumes --filters Name=attachment.instance-id,Values=<instance-id>

        Create a snapshot:

            aws ec2 create-snapshot --volume-id <volume-id> --description "Nginx volume snapshot"

        Copy the Snapshot to the Target Region:

            aws ec2 copy-snapshot --source-region us-east-1 --source-snapshot-id <snapshot-id> --region us-west-2

Step 5: Create and Attach a Volume from the Copied Snapshot

Create a Volume in the Target Region:

    aws ec2 create-volume --snapshot-id <snapshot-id> --availability-zone us-west-2a --volume-type gp3

Attach the Volume to the Instance:

    aws ec2 attach-volume --volume-id <volume-id> --instance-id <instance-id> --device /dev/xvdf



---

Now you have the entire content in a single block that you can copy and paste into your `README.md` file! Let me know if you need anything else!

