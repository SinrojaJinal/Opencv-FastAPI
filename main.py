from fastapi import FastAPI, UploadFile, File
import cv2 as cv
import uvicorn
import os
from bgrtogray import GrayScale

app = FastAPI()

@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    try:
        os.mkdir("files")
        print(os.getcwd()) # os.getcwd() method tells us the location of current working directory (CWD).
    except Exception as e:
        print(e) 
    file_name = os.getcwd()+"/files/"+file.filename.replace(" ", "-")
    with open(file_name,'wb+') as f:
        f.write(file.file.read())
        f.close()
    obj = GrayScale()
    obj.GrayScaling(file_name)  
    return {"filename": file_name}

if __name__ =="__main__":
    uvicorn.run(app, host = '0.0.0.0', port=8001)
