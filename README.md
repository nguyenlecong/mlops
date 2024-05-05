# mlflow
---
- **mlflow** is an open-source platform and a great tool for managing the end-to-enf machine learning cycle
- **mlflow components:**
  - **mlflow tracking:**
    - Record metrics and params from training runs
    - Store models, artifacts and code
  - **mlflow models:**
    - Standardize models for deployments
    - Build customized models
  - **mlflow projects:**
    - Package ML code for reproducibility
    - Package ML code for repeatability
  - **mlflow model registry:**
    - Store and version ML models
    - Load and deploy ML models
---
- **mlflow and kubeflow:**

|mlflow|kubeflow|
|------|--------|
|dự án mã nguồn mở được tạo ra bởi Databrricks, những người tạo ra Spark|tạo ra bởi google năm 2018, dựa trên **k8s**|
|tập trung nhiều hơn vào việc theo dõi thí nghiệm|tập trung vào điều phối và quản lý pipeline|
|experiment tracking, model versioning/deployment|make it easy to develop, deploy, manage portable, scalable ml workflows|