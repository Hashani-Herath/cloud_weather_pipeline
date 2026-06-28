import os
import requests
import pandas as pd
from datetime import datetime, UTC  # Updated to use modern UTC features
import boto3

def load_env_file(file_path=".env"):
    if not os.path.exists(file_path):
        return

    with open(file_path, "r", encoding="utf-8") as env_file:
        for raw_line in env_file:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value


def require_env(name):
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value

def run_weather_pipeline():
    load_env_file()

    # 1. FETCH LIVE WEATHER DATA
    print("Fetching live global weather records...")
    cities = {
        "Colombo": {"lat": 6.9271, "lon": 79.8612},
        "New York": {"lat": 40.7128, "lon": -74.0060},
        "London": {"lat": 51.5074, "lon": -0.1278}
    }
    
    weather_records = []
    for city_name, coords in cities.items():
        url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current_weather=true"
        response = requests.get(url).json()
        current = response["current_weather"]
        
        weather_records.append({
            "recorded_at": datetime.now(UTC).strftime('%Y-%m-%d %H:%M:%S'),
            "city": city_name,
            "temperature_c": current["temperature"],
            "windspeed_kmh": current["windspeed"]
        })
    
    # 2. TRANSFORM DATA INTO COMPRESSED PARQUET FORMAT
    df = pd.DataFrame(weather_records)
    file_name = f"weather_{datetime.now(UTC).strftime('%Y%m%d_%H%M%S')}.parquet"
    df.to_parquet(file_name, index=False)
    print(f"✔ Transformed data saved locally as: {file_name}")
    
    # 3. UPLOAD THE FILE DIRECTLY TO AMAZON S3 CLOUD
    print("Uploading file to Amazon S3 Cloud Data Lake...")

    aws_access_key = require_env("AWS_ACCESS_KEY_ID")
    aws_secret_key = require_env("AWS_SECRET_ACCESS_KEY")
    bucket_name = "my-weather-data-lake-2026-975050334884-eu-north-1-an" 
    
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )
    
    try:
        s3_client.upload_file(file_name, bucket_name, f"raw_zone/{file_name}")
        print("✔ Cloud Upload Complete! File is safely stored in the cloud data lake.")
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        
    # Clean up local file
    if os.path.exists(file_name):
        os.remove(file_name)

if __name__ == "__main__":
    run_weather_pipeline()