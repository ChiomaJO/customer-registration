# Customer Registration Application

A cloud-based customer registration application built with HTML, CSS, JavaScript, Amazon S3, Amazon API Gateway, and AWS Lambda.

## Project Overview

This project provides a simple customer registration form that collects basic customer information and sends the registration request to an AWS backend for validation.

## Features

- Customer registration form
- Full name validation
- Email validation
- Phone number validation
- Date of birth collection
- Gender selection
- Address collection
- API-based registration processing
- AWS Lambda backend validation
- CORS-enabled API communication

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- AWS Lambda

### Cloud Services
- Amazon S3
- Amazon API Gateway
- AWS Lambda

## Architecture

Customer  
↓  
Web Frontend  
↓  
Amazon S3  
↓  
Amazon API Gateway  
↓  
AWS Lambda  
↓  
Validation & Response

## AWS Components

### Amazon S3
Stores the frontend files:

- `index.html`
- `style.css`
- `script.js`

### Amazon API Gateway

Provides the API endpoint:

`POST /register`

### AWS Lambda

Processes the registration request and validates the submitted customer information.

## Testing

The application was tested successfully using:

- AWS Lambda test event
- API Gateway
- Frontend registration form

The Lambda test returned a successful `200` status code, and the frontend successfully communicated with the AWS backend.

## Security and Cost Considerations

- No AWS access keys or credentials are included in the source code.
- The local customer database is excluded from version control.
- S3 public access remains restricted.
- AWS resources were kept to the minimum required for the project.

## Project Status

Completed and tested.

## Author

Chioma JO