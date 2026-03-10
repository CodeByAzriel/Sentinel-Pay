## ☁️ Sentinel-Pay: AWS Fraud Monitoring Dashboard

A secure, serverless financial data pipeline designed for **real-time transaction monitoring and fraud detection**. Sentinel-Pay **ingests banking transaction data into AWS S3**, triggers **AWS Lambda functions** to process transactions automatically, and **visualizes anomalies** through an interactive **Streamlit dashboard**. Features include high-value transaction alerts, impossible travel detection, and data-driven summaries to support decision-making.

### Key Highlights
- Real-time fraud monitoring for financial transactions  
- High-availability serverless architecture with AWS S3 and Lambda  
- Secure handling of sensitive financial data (no secrets stored in code)  
- Interactive Streamlit dashboard for analytics and operational insight  

### Tech Stack
Python · Pandas · AWS Lambda · AWS S3 · Boto3 · Streamlit · JSON · Data Automation · Serverless Architecture

**Setup Instructions:**  
1. Clone the repo.  
2. Create an `.env` file (or use AWS Secrets Manager) to store your credentials securely.  
3. Install dependencies: `pip install -r requirements.txt`.  
4. Run the Streamlit dashboard: `streamlit run Processing/dashboard.py`.  

> **Note:** All sensitive keys and passwords have been removed. Configure your own AWS access keys in environment variables or AWS Secrets Manager.


