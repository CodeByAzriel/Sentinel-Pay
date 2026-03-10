## ☁️ Sentinel-Pay: AWS Transaction Dashboard

A serverless cloud solution for financial data observability. Built an automated pipeline that ingests banking transaction data into **AWS S3**, triggers **AWS Lambda** for real-time processing, and visualizes trends through an interactive **Streamlit** dashboard. Focuses on high-availability architecture and secure cloud data handling.

**Key Features:**
- Real-time transaction ingestion from CSV/JSON
- Fraud detection rules: High Value & Impossible Travel alerts
- Streamlit dashboard for monitoring transactions
- Serverless architecture using AWS S3 + Lambda
- Secure handling of credentials and sensitive data (no secrets committed to repo)

**Tech Stack:**  
Python · AWS Lambda · AWS S3 · Boto3 · Streamlit · JSON · Data Automation · Serverless Architecture  

**Setup Instructions:**  
1. Clone the repo.  
2. Create an `.env` file (or use AWS Secrets Manager) to store your credentials securely.  
3. Install dependencies: `pip install -r requirements.txt`.  
4. Run the Streamlit dashboard: `streamlit run Processing/dashboard.py`.  

> **Note:** All sensitive keys and passwords have been removed. Configure your own AWS access keys in environment variables or AWS Secrets Manager.

