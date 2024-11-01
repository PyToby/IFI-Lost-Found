# The _IFILAF_ Project
### [Overview](#overview)
This repository contains the code for a Lost & Found web application designed for GJK. This platform allows students, staff, and faculty to report lost and found items, making it easier to track and retrieve personal belongings within the school campus.
<br>
_Disclaimer: This website is currently hosted on a temporary domain, indicating that it is still in the development phase._
<br>
<br>
<p align="center">
  <a href="#overview"><img src="https://img.shields.io/badge/📄-Overview-blue?style=for-the-badge" alt="Overview"></a>
  <a href="#features"><img src="https://img.shields.io/badge/✨-Features-green?style=for-the-badge" alt="Features"></a>
  <a href="#screenshots"><img src="https://img.shields.io/badge/📷-Screenshots-lightgrey?style=for-the-badge" alt="Screenshots"></a>
  <a href="#tech-stack"><img src="https://img.shields.io/badge/🔧-Tech_Stack-blueviolet?style=for-the-badge" alt="Tech Stack"></a>
  <a href="#getting-started"><img src="https://img.shields.io/badge/🚀-Getting_Started-orange?style=for-the-badge" alt="Getting Started"></a>
  <a href="#project-structure"><img src="https://img.shields.io/badge/📂-Project_Structure-red?style=for-the-badge" alt="Project Structure"></a>
  <!-- <a href="#contributing"><img src="https://img.shields.io/badge/🤝-Contributing-yellowgreen?style=for-the-badge" alt="Contributing"></a>
  <a href="#license"><img src="https://img.shields.io/badge/📜-License-9cf?style=for-the-badge" alt="License"></a> -->
  <a href="#acknowledgments"><img src="https://img.shields.io/badge/🙏-Acknowledgments-ff69b4?style=for-the-badge" alt="Acknowledgments"></a>
</p>

## ✨ [Features](#features)

Our Lost & Found Website for [School Name] includes a variety of user-friendly and powerful features, designed to make item management easy and efficient:

| 🌟 Feature                    | 💻 Description                                                                 |
|-------------------------------|------------------------------------------------------------------------------|
| **Lost Item Reporting**       | Users can submit detailed descriptions and images of lost items, helping others identify and track items more easily. |
| **Found Item Reporting**      | Report found items with detailed descriptions and photos, making it simple for owners to identify their belongings. |
| **Search & Filter**           | Filter items by category, location, and date to quickly find specific lost or found items. |
| **User Authentication**       | Secure login and authentication through your gjk.cz email. |

## 📷 [Screenshots](#screenshots)

No screenshots yet due to the project being in development.

## 🔧 [Tech-Stack](#tech-stack)

| Usage                         | Language                                                                      |
|-------------------------------|------------------------------------------------------------------------------|
| **Frontend**                  | HTML, Tailwind CSS |
| **Backend**                   | Python - Flask |
| **Database**                  | MySQL |
| **Authentication**            | Google API |

## 🚀 [Getting started](#getting-started)

**In your web browser of choice, open [Temporary IFILAF site](https://ifilaf.onrender.com/)**
<br>
<br>

_Disclaimer: This website is currently hosted on a temporary domain, indicating that it is still in the development phase._ 


## 📂 [Project Structure](#project-structure)
```plaintext
📦 lost-and-found-website
 ┣ 📂 instance                # MySQL Database
 ┃ ┃ ┣ 🗄️database.db
 ┃ 📂 website                 #Folder containing websites functionality                        
 ┃ ┣ 📂 __pycache__
 ┃ ┣ 📂 templates
 ┃ ┃ ┃ ┣ base.html            #The structure of the site (other html files extend it)
 ┃ ┣ 📜 __init__.py          #Creates the backend and site    
 ┃ ┣ 📜 auth.py              #All authentication code
 ┃ ┣ 📜 models.py            #Database models     
 ┃ ┗ 📜 views.js             #Websites' views               
 ┣ 📜 .gitignore    
 ┣ 📜 README.md               
 ┣ 📜 main.py                #Starts the website
 ┗ 📜 requirements.txt
```

## 🙏 [Acknowledgments](#acknowledgments)

Special thanks to [@jeohan19](https://www.github.com/jeohan19) and [@Onkvisu](https://www.github.com/onkvisu) for being able to develop this project. _Can be found in collaborators tab._
