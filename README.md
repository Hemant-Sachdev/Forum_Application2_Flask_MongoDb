# Forum_Application2_Flask_MongoDb
A simple Forum Application built with Flask, featuring user login functionality, account management, and a user dashboard and Like management per post. The application leverages MongoDB as its database.

## Features
 - User registration and login
 - Account management with real-time data interactions
 - User dashboard displaying various posts and likes
 - Error handling with user-friendly feedback
 - Like Management per post (one user can like atmost once)

## Technologies Used
 - **Flask**: Backend framework
 - **MongoDB**: NoSQL database
 - **PyMongo**: MongoDB driver for Python
 - **HTML**: Templates
 - **Bootstrap@5.3.3**: Styling the templates

## Installation Guide
Follow these steps to set up and run the application:

### 1. Create a New Virtual Environment
Create and activate a virtual environment to manage dependencies:
```bash
# Create a virtual environment named 'forumapp'
python -m venv forumapp

# Activate the virtual environment
# Windows
.\forumapp\Scripts\activate

# macOS/Linux
source forumapp/bin/activate
```

### 2. Install Required Libraries
Install necessary packages using pip:
```bash
pip install -r requirements.txt
```

### 3. Set Up app.py
Ensure app.py includes your unique security key:
```bash
app.secret_key = 'add_your_unique_key_here'  # Replace with your unique key
```

### 4. Run the Application
Use the following command in the terminal to start the Flask server:
```bash
python app.py
```
The application will be accessible at http://127.0.0.1:5000/.

## File Structure
### Main Code File
 - app.py: Contains the main application logic and route setup.

### Template Files
 - **base.htm**l: Base template with reusable HTML structure.
 - **home.html**: Homepage template with login and signup forms.
 - **dashboard.html**: Dashboard template showing user data.
 - **login.html**: Login page template.
 - **profile.html**: User Profile page template.


## Screenshot of Web APP
![image](https://github.com/user-attachments/assets/b50f6a6c-0773-4ae0-b0c1-451a478dfafa)
![image](https://github.com/user-attachments/assets/8aa115f2-3744-4cfa-a0ff-333fa3814d53)
![image](https://github.com/user-attachments/assets/2d6232ba-34e4-45f4-bbbf-1ce071f77ccc)
![image](https://github.com/user-attachments/assets/e38f77bf-ad33-4ddb-839a-7e9823cd114a)





