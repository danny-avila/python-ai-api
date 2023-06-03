the app is: RESTful API in Python using Flask for AI utility libraries

the files we have decided to generate are: app.py, requirements.txt, Dockerfile, docker-compose.yaml, test_app.py, README.md

Shared dependencies:
1. Exported variables:
   - OPENAI_API_KEY

2. Data schemas:
   - Input payload schema:
     {
       "input": string,
       "envs": {
         "OPENAI_API_KEY": string
       }
     }
   - Response data schema:
     {
       "result": string,
       "error": string,
       "stdout": string
     }

3. ID names of DOM elements: None (no frontend involved)

4. Message names:
   - Error messages for invalid input, failed requests, and other errors

5. Function names:
   - sentiment_analysis (example function for AI utility)
   - Other functions corresponding to AI utility libraries' features