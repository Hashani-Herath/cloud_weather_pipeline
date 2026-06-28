# Serverless Global Weather Data Lake (Cloud-Native Infrastructure)

## 📌 Project Overview
This project implements a fully automated, **Cloud-Native Data Ingestion Pipeline** that tracks climate indices across major global cities. 

Instead of relying on local hardware, this solution is **6-month free-tier compliant** and engineered entirely in the cloud. It leverages serverless computing runtimes to fetch public environmental metrics daily, converts unstructured responses into high-performance columnar files, and streams them securely into an enterprise cloud storage lake layer.

---

## 🏗️ System Architecture & Data Flow
1. **Serverless Orchestration (GitHub Actions):** Triggered daily via a serverless cron container environment, removing the need for dedicated on-premise local server hardware.
2. **Data Extraction:** A Python ingestion component connects to the Open-Meteo REST API, capturing localized global variables.
3. **Storage Optimization (Apache Parquet):** Raw arrays are systematically formatted into compressed, columnar **Parquet** binaries using PyArrow, drastically lowering cloud storage capacity costs.
4. **Data Lake Storage (Amazon S3):** Files are uploaded securely via encrypted network pipelines into automated partitions within an Amazon Web Services S3 data store layer.

---

## 🛠️ Tech Stack & Core Tools
* **Cloud Infrastructure Provider:** Amazon Web Services (AWS S3)
* **Serverless Compute Runtime:** GitHub Actions CI/CD Engines
* **File Format Architecture:** Apache Parquet
* **Languages & Core SDKs:** Python 3.x, Boto3 (AWS SDK), Pandas, PyArrow

---

## 🚀 How to Run and Deploy

### 1. Configure Cloud Infrastructure
* Create an account within the AWS Management Console framework.
* Initialize an S3 Bucket instance to establish your physical Cloud Data Lake boundary.
* Generate an IAM user profile to secure programmatic access credentials.

### 2. Configure CI/CD Cloud Secrets
Within your public GitHub source repository layout, navigate through settings to register your secure environment credentials safely:
* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`

### 3. Manual Workflow Dispatch Trigger
Navigate directly to the **Actions** layout tab within this GitHub user interface framework, select the active workflow pipeline, and select **Run workflow** to force immediate end-to-end processing execution.