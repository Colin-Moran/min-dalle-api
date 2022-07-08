# min-dalle-api

 This is a simple python API for AI image generation using min-dalle and FastAPI. This API uses the dalle-mini model by default. You can use the dalle-mega model by changing the `isMega = False` line at the top of the main.py file to `isMega = True`

#### Hardware Requirements
You do not need a GPU to run the dalle-mini model, although it is much faster with one. It takes about ~100 seconds to generate a 2x2 grid running on my Ryzen 5600X. To run on a GPU you will likely need a minimum of 4GB VRAM for the mini model and 12GB VRAM for the mega model.

## Install

`pip install -r requirements.txt`

## Usage
Navigate to the "app" directory : `cd app`

Start the server: `uvicorn main:app --reload`

If everything goes as planned you will see an output in the console similar to this:

`
Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit) 
`

Your server is now running at that address. You can navigate to http://127.0.0.1:8000/docs to see and test the available endpoints. 

![image](https://user-images.githubusercontent.com/37432040/177916767-334c0a26-564d-4584-b3b1-60b95e29aab1.png)

![image](https://user-images.githubusercontent.com/37432040/177916843-0738c0e4-444e-4f74-bb42-36bdeebe2741.png)

## Deployment

I have included a Dockerfile for easy deployment. 

NOTE: Must use a Windows container.

