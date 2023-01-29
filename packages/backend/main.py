from fastapi import FastAPI
from transformers import pipeline
import tensorflow as tf
import asyncio
from pydantic import BaseModel

app = FastAPI()

#TODO:
# summarization
# clasification
#    find commities based on classification
#    who to contact?
#    
# likelyness to pass
# similar bills?
# 

class Data(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/summerize")
async def summerize(data: Data):
    """
    Model type: Tensorflow
    returns a summerization of message that is provided
    """

    summarizer = pipeline(
        "summarization", model="philschmid/bart-large-cnn-samsum")

    return summarizer(data.message)


@app.post("/billCassification")
async def billCassification(message):
    """
    provide a summarization of the bill in which you would like to classify

    Model type: TensorFlow
    
    **NOTE: this model is case sensative

    returns JSON with classification groups, along with 'percent' classified to each group

    """

    classifier = pipeline(
        "text-classification", model="z-dickson/CAP_coded_US_Congressional_bills")
    
    return classifier(message)


# for testing
# msg = "a bill proposal that addresses an increase in escaped convicts, and lowing the number of escapees"

# output = asyncio.run(billCassification(msg))
# print(output)



