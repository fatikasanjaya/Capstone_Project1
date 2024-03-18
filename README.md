# Capstone Project 1
# TrueCare Hospital Patient Data Management Application

This application is the result of a Python project created as part of Module 1 Capstone Project at Purwadhika Digital School in the Data Science program. It aims to implement basic CRUD (Create, Read, Update, Delete) functions for managing hospital patient data. 

## Introduction

The application uses dummy data and not connected to a database, serving purely as a programming exercise to understand the basics of Python. Additionally, it utilizes two Python libraries:
- **Tabulate:** for displaying data in structured table form.
- **PyInputPlus:** for taking user input while validating and handling various input errors.

## Features

Data Display (Read Menu)
- Users can view detailed information of all patient records or retrieve specific patient data based on unique identification such as patient ID.

Data Addition (Create Menu)
- Administrators can easily add new inpatient patient information to the system, ensuring the accuracy and completeness of the hospital database.

Data Deletion (Delete Menu)
- The application facilitates the deletion of irrelevant or incorrect inpatient patient information, with options for permanent deletion or data recovery if needed.

Data Editing (Update Menu)
- Users have the flexibility to edit existing patient information/data, allowing them to update information as needed.

## Implementation

### Data Display (Read Menu)

Main Menu View
- When the user selects option "1" from the main menu, the application displays a submenu to view patient data.
  

#### Read Menu Feature
- Submenu 2 displays specific data based on user input, such as patient ID.

### Data Addition (Create Menu)

#### Adding Inpatient Patient Data
- Users are prompted to fill in the primary key / patient ID and proceed by entering new patient information.

### Data Deletion (Delete Menu)

#### Deleting Patient Data
- Users can delete patient data by entering the patient ID. Additionally, there is a feature for data restoration.

### Data Editing (Update Menu)

#### Editing Patient Data
- Users can edit patient data based on the column they want to change.

## Conclusion

The development of this patient data management application is an important step in improving operational efficiency and data integrity at TrueCare Hospital. By providing user-friendly tools to manage patient records, this application empowers healthcare institutions to provide optimal care while maintaining careful attention to patient data management.
