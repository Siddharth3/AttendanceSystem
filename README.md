# AttendanceSystem (OpenCV + Python)


https://github.com/user-attachments/assets/11ca8bc2-a1e6-46e4-b950-f1e7e8481e33


### 1. Overview
#### Purpose:
This attendance system is designed to automate the process of recording attendance using facial recognition technology. By leveraging OpenCV with Python, the system captures an image of each individual through a camera and compares it against a pre-existing database of photos. If a match is found, the individual's attendance is logged with their name in a CSV file for the current day. This streamlined approach eliminates the need for traditional, time-consuming attendance methods and enhances accuracy by minimizing manual errors. 

#### Audience:
This system is ideal for organizations, schools, and businesses that require reliable and efficient attendance tracking. Typical users may include:

- Administrators: Responsible for setting up and maintaining the photo database, as well as managing and retrieving attendance records as needed.
- Staff Members or Instructors: Individuals who monitor attendance and ensure records are accurate.
- Employees or Students: End-users whose attendance is tracked automatically by the system.

This attendance system offers a user-friendly and efficient solution for daily attendance management, ensuring a secure and streamlined record-keeping process.

### 2. Resources
- Dataset (This is the folder which we are using to save our picture for the system to identify)
- templates (This folder is used to keep our webpage code separate from our other files)
- GUI_FR.py (This is the main file with all python code which is doing all backend work) 
- haarcascade_frontalface_default.xml (This is the opencv file which is using to detect the face from image)

### 3. Instructions to Use
- Firstly we need to open terminal in the project folder and run "python GUI_FR.py" command.
- After succesfully started python code, you need to open http://127.0.0.1:5000/ in your browser.
- Now, you are ready to go for marking attendance if you have dataset already in folder. Otherwise you can start adding data/picture manually or through portal.
##### *** Maybe you will face some errors if you don't have 'cmake' or 'dlib' library in your syatem. If this case you can simply install through commands.
##### *** Some are the sample csv files are already in code, if you want to get the idea for result.

### 4. Contact Information
For any questions or issues related to the code, please contact:

#### Developer: Siddharth Sahni
#### Email: sidd.sahni3@gmail.com
#### LinkedIn: [Siddharth Sahni](https://www.linkedin.com/in/er-siddharth-sahni-36b227103/)
#### Website: [TheDataMan.github.io/](https://siddharth3.github.io/TheDataMan.github.io/)
