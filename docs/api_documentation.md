# AI Utility API Documentation

## Overview

This API provides an interface to various AI utility libraries, handling user credentials securely for accessing these AI services.

## Base URL

All API requests should be made to the base URL:

```
http://localhost:8080
```

## Endpoints

### POST /ask

This endpoint accepts a question and returns an AI-generated answer.

#### Request Headers

- `accept: application/json`
- `Content-Type: application/json`

#### Request Body

```json
{
  "input": "How many people live in canada as of 2023?",
  "envs": {
    "OPENAI_API_KEY": "your_openai_api_key"
  }
}
```

#### Response

The response will be a JSON object with the following format:

```json
{
  "result": "Arrr, there be 38,645,670 people livin' in Canada as of 2023!",
  "error": "",
  "stdout": "Answer the following questions as best you can, but speaking as a pirate might speak...Final Answer: Arrr, there be 38,645,670 people livin' in Canada as of 2023!"
}
```

#### Possible Errors

- `400 Bad Request`: Invalid input or missing required parameters
- `500 Internal Server Error`: An error occurred while processing the request

### POST /sentiment_analysis

This endpoint accepts text data and returns the sentiment score.

#### Request Headers

- `accept: application/json`
- `Content-Type: application/json`

#### Request Body

```json
{
  "input": "I love this product!",
  "envs": {
    "OPENAI_API_KEY": "your_openai_api_key"
  }
}
```

#### Response

The response will be a JSON object with the following format:

```json
{
  "result": "positive",
  "error": "",
  "stdout": "Sentiment analysis result: positive"
}
```

#### Possible Errors

- `400 Bad Request`: Invalid input or missing required parameters
- `500 Internal Server Error`: An error occurred while processing the request