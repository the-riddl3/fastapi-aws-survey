import csv
import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas import BaseSurvey

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.post("/survey/cu")
async def fill_survey_cu(survey: BaseSurvey):
    qa = survey.questionsAndAnswers

    data_to_append = [qa['fullName'], qa['email'], qa['cuGraduate'], qa['programStudied'], qa['enrollMasters']]

    # Open the CSV file in append mode and write the data
    with open('data/survey_cu.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_to_append)

    return "thank you for participating!"

@app.get("/survey/cu", response_class=HTMLResponse)
async def get_survey_cu(request: Request):
    return templates.TemplateResponse("survey_cu.html", {"request": request})