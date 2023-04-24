## MRPC Sentence Simillarity
In this repository, I am trying to train a bert model which can predict whether two sentences are paraphrased or not. The model is then inferenced using Fast API. The whole model and inference script are also dockerised and tested. Some basic unit testing is also done in the Fast API by using Pytest.

### Repository structure
    .
    ├── Model_2                                        # Bert model directory
    ├── Screenshots                                    # Various screenshots of different checks
    ├── __init.py__                                    # init file 
    ├── data_download.py                               # script to download the MRPC dataset and upload it to GDrive
    ├── Dockerfile                                     # Docker file for model inference
    ├── main.py                                        # inference script for Fast API 
    ├── MRPC_Notebook.ipynb                            # Jupyter notebook for model training
    ├── README.md                                              
    ├── requirements.txt                               # Python package requirement for docker image
    └──test_main.py                                    # Basic unit testing script

### License
```
Copyright 2022
```