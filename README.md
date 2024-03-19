# Capstone Project 1
# TrueCare Hospital Patient Data Management Application

This application is the result of a Python project created as part of Module 1 Capstone Project at Purwadhika Digital School in the Data Science program. It aims to implement basic CRUD (Create, Read, Update, Delete) functions for managing hospital patient data. 

## Introduction

The application uses dummy data and not connected to a database, serving purely as a programming exercise to understand the basics of Python. Additionally, it utilizes two Python libraries:
- **Tabulate:** for displaying data in structured table form.
- **PyInputPlus:** for taking user input while validating and handling various input errors.
![Alt text](https://github.com/fatikasanjaya/Capstone_Project1/blob/8bddb4996a7c1b6f49a0e85cc4589148914ddcba/image/library.png)

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

![Alt text](https://github.com/fatikasanjaya/Capstone_Project1/blob/8bddb4996a7c1b6f49a0e85cc4589148914ddcba/image/main_menu.png)
- When the user selects option "1" from the main menu, the application displays a submenu to view patient data.
![Alt text](https://github.com/fatikasanjaya/Capstone_Project1/blob/main/image/read_menu.png)
- Submenu 2 displays specific data based on user input, such as patient ID.
![Alt text](https://github.com/fatikasanjaya/Capstone_Project1/blob/main/image/read%20data%20by%20id.png)
### Data Addition (Create Menu)
- Adding Inpatient Patient Data
  Users are prompted to fill in the primary key / patient ID and proceed by entering new patient information.
![Alt text](https://github.com/fatikasanjaya/Capstone_Project1/blob/main/image/create_menu.png)

### Data Deletion (Delete Menu)
#### Deleting Patient Data
- Users can delete patient data by entering the patient ID. 
![Alt text](https://github.com/fatikasanjaya/Capstone_Project1/blob/main/image/delete_menu.png)
- Additionally, there is a feature for data restoration.
![Alt text](https://github.com/fatikasanjaya/Capstone_Project1/blob/main/image/restore_data.png)

### Data Editing (Update Menu)
- For editing patient data, users can edit patient data based on the column they want to change.
![Alt text](https://github.com/fatikasanjaya/Capstone_Project1/blob/main/image/update_menu.png)


## Conclusion
The development of this patient data management application is an important step in improving operational efficiency and data integrity at TrueCare Hospital. By providing user-friendly tools to manage patient records, this application empowers healthcare institutions to provide optimal care while maintaining careful attention to patient data management.
