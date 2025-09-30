A serverless AWS Lambda function that provides real-time temperature data for Mumbai, India. Built with full CI/CD pipeline automation using AWS CodePipeline, CodeBuild, and API Gateway.

![AWS](https://img.shields.io/badge/AWS-Lambda-orange?logo=amazonaws)
![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![CI/CD](https://img.shields.io/badge/CI/CD-CodePipeline-success)

--------------------------------------------------------------------------
## 🚀 Features

- **Real-time Weather Data** - Current temperature, humidity, and weather conditions for Mumbai
- **Serverless Architecture** - Built on AWS Lambda for cost efficiency and scalability
- **RESTful API** - Clean JSON API endpoint via API Gateway
- **Automated CI/CD** - Zero-touch deployments via GitHub integration
- **Monitoring Ready** - Integrated with CloudWatch for logging and metrics

----------------------------------------------------------------------------
## 📊 API Response
{
  "city": "Mumbai",
  "country": "India",
  "temperature_celsius": 25.99,
  "feels_like_celsius": 25.99,
  "humidity_percent": 89,
  "weather_description": "Mist",
  "timestamp": 1727692800
}

-----------------------------------------------------------------------------
Architecture ->>>>>>>

GitHub → CodePipeline → CodeBuild → Lambda → API Gateway
  
Source   >   Orchestrate  >  Build  >  Execute  >  Expose

Repository -> Pipeline -> Package -> Function -> API

-----------------------------------------------------------------------------

🛠️ Technology Stack
AWS Lambda - Serverless compute

API Gateway - REST API management

CodePipeline - CI/CD orchestration

CodeBuild - Build and package automation

S3 - Artifact storage

Python 3.9 - Runtime environment

OpenWeatherMap API - Weather data source

-----------------------------------------------------------------------------
