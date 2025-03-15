# Doctor Survey Prediction

This project is a Doctor Availability Prediction System that helps users estimate doctor availability based on input time. It is built using Flask, Pandas, and Machine Learning to process survey data and generate predictions.

## Features

* Predict doctor availability based on survey data
* Download predictions as a CSV file
* Deployed using Railway for easy access

## Outline

I used a dataset of collections of dummy NPIs. NPIs are basically a unique ID given to each doctor in the US. This dataset contains a list of NPIs along with their details like Speciality, Region, Login Time, Logout out Time, Time spent, Count of Attempts etc.

The idea is to have an app which conducts survey for doctors. Let's assume that I have to send a campaign like an email to the doctors to invite them for this survey. Instead of sending mails to everyone, I would want to target the doctors who are more likely to attend the survey.

given the details about the Doctors along with their survey data through the dataset, I have to get the time like 6:00 as an input from the user and then return the best list of doctors(the NPIs) who is more likely to attend the survey at this particular time as a csv export through any AI/ML algorithm. So now, I can send mail to these doctors only.

## Tech Stack

* Backend: Flask
* Frontend: HTML, CSS, JavaScript
* Deployment: Railway

## How to Use

* Enter the desired time in the input field.
* Click the Predict button to generate doctor availability.
* Download the CSV file to view all the doctors available at that time.

## Deployment

[Public URL from Railway app](doctor-survey-predictor-production.up.railway.app)
