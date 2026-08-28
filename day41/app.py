# Program 3 — First FastAPI App
# 
# Create:
# 
# app.py
# 
# Build:
# 
# GET /
# 
# Return:
# 
# {
  # "message": "Student ML API is running"
# }
# 
# Run using:
# 
# uvicorn app:app --reload
# 
# Then test:
# 
# /docs

from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {
        "message":"Student ML API is running."
    }