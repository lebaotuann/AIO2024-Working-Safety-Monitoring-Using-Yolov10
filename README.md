# AIO2024 - Project Module 1: [YOLOv10](https://github.com/THU-MIG/yolov10)

## Image Project: Working Safety Monitoring Using YOLOv10
We will train a custom YOLOv10 model ([YOLOv10-N](https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10n.pt)) with the Safety Helmet Dataset. 
Then, we use the pre-trained weight to detect images with the safety helmet.

## Installation
### 1. Clone the repository
```commandline
git clone https://github.com/lebaotuann/AIO2024-Working-Safety-Monitoring-Using-Yolov10.git aio2024_wsmuy_project
cd aio2024_wsmuy_project
```

### 2. (Optional) Create and activate a python virtual environment
- For Ubuntu:
```commandline
sudo apt-get install python3.9-venv
python3 -m venv myvenv
source myvenv/bin/activate
```
- For Windows:
```commandline
py -m venv myvenv
myvenv\Scripts\activate
```
or
```commandline
python -m venv myvenv
myvenv\Scripts\activate
```

### 3. Install the required dependencies

```commandline
pip install -r requirements.txt
```

## Run the Application
You can start the application by the following command :
```shell
streamlit run app.py
```
