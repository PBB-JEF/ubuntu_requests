![alt text](image.png)
![alt text](image-2.png)
![alt text](image-3.png)


markdown
# 🌍 Ubuntu-Inspired Image Fetcher

> _"I am because we are."_ — Ubuntu Philosophy

This project is a Python-based tool that respectfully connects to the global web community to fetch and organize shared images. Inspired by the Ubuntu principles of **community**, **respect**, **sharing**, and **practicality**, this script allows users to mindfully collect images from the internet and store them locally for appreciation and reuse.

---

## 🧠 Project Purpose

The Ubuntu Image Fetcher is designed to:
- Strengthen digital connection through shared resources
- Handle errors gracefully, respecting the unpredictability of the web
- Organize images for later sharing and community enrichment
- Serve as a practical tool for ethical image collection

---

## 🚀 Features

- ✅ Accepts one or multiple image URLs
- ✅ Creates a `Fetched_Images/` directory automatically
- ✅ Downloads and saves images in binary mode
- ✅ Extracts filenames from URLs or generates defaults
- ✅ Checks for valid image content via HTTP headers
- ✅ Prevents duplicate downloads using hash comparison
- ✅ Handles network and runtime errors respectfully

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
requirements.txt includes:
Code
requests
🛠️ How to Run
Clone the repository:


cd Ubuntu_Requests
Run the script:

bash
python3 ubuntu_fetcher.py
Enter one or more image URLs when prompted:

Code
Please enter image URLs separated by commas:
https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/keybord-kingshuk-de.jpg, https://pixels.com/images/homepage/ourProductsPrints001.jpg
🖼️ Sample Image URLs for Testing
https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg




📁 Folder Structure
Code
Ubuntu_Requests/
├── ubuntu_fetcher.py
├── requirements.txt
├── README.md
└── .gitignore
Note: The Fetched_Images/ folder is created at runtime and excluded from version control.

🔒 .gitignore
To keep your repository clean and respectful of bandwidth and copyright, the following is included in .gitignore:

Code
Fetched_Images/
🧘 Ubuntu Principles in Action
Principle	Implementation
Community	Connects to the global web to fetch shared resources
Respect	Handles errors gracefully without crashing
Sharing	Organizes images for later appreciation and reuse
Practicality	Provides a real-world tool for ethical image collection
📬 Submission
Submit this repository URL for your assignment:

Code
https://https://github.com/PBB-JEF/ubuntu_requests


🙌 Acknowledgments
This project is inspired by the Ubuntu philosophy: "A person is a person through other persons." It honors the spirit of connection, collaboration, and ethical technology.



