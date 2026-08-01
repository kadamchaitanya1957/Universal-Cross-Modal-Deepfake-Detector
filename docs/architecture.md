# Universal Cross-Modal Deepfake Detector

## Objective

Build an AI-powered web application capable of analyzing Images, Videos and PDF documents for authenticity using pretrained AI models.

This project is an Ideathon MVP.

The focus is a professional working prototype rather than building new AI models.

---

## Tech Stack

Frontend

- React
- Vite
- JavaScript
- CSS

Backend

- FastAPI
- Python

AI

- Pretrained Models
- EasyOCR
- OpenCV

Version Control

- Git
- GitHub

IDE

- Cursor

---

## Supported Media

- Image
- Video
- PDF

---

## Backend Workflow

Upload

↓

Detect Media Type

↓

Route

↓

Image Service

Video Service

Document Service

↓

Return JSON

---

## Frontend Workflow

Landing Page

↓

Upload

↓

Loading

↓

Results Dashboard

---

## API Contract

POST

/api/v1/analyze

Response

{
    "status":"success",
    "mediaType":"image",
    "authenticityScore":95,
    "confidence":90,
    "summary":"Dummy response"
}

---

## Rules

Never train models.

Always use pretrained models.

Backend owns all AI logic.

Frontend only displays data.

API contract must never change without updating this document.
