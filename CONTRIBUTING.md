<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Hunt Hacktoberfest 2023 Contribution Guidelines</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f0f0f0;
            color: #333;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #3498db;
        }
        code {
            background-color: #f4f4f4;
            padding: 0.2em 0.4em;
            border-radius: 5px;
            font-size: 1em;
            color: #d14;
        }
        ul, ol {
            margin-left: 20px;
        }
        img {
            display: block;
            max-width: 100%;
            margin: 20px 0;
        }
    </style>
</head>
<body>

    <img src="HacktoberFest2023_Resources/05_logo_set/hf10_horizontal_logos/cmyk/hf10_horz_fcl_cmyk.png" alt="Hacktoberfest 2023 Logo">

    <h1>Python Hunt Hacktoberfest 2023 Contribution Guidelines 💙</h1>
    <p>Welcome, open-source enthusiasts! This Django-based <strong>Python Hunt</strong> project provides a platform to create web pages explaining various Python concepts, as outlined in the issues. Follow the guidelines below to contribute effectively!</p>

    <h2>Prerequisites</h2>
    <ul>
        <li>Python (version 3.6 or higher)</li>
        <li>pip (Python package installer)</li>
    </ul>

    <h2>Installation Steps</h2>
    <h3>1. Create a Virtual Environment (Optional)</h3>
    <p>It's recommended to create a virtual environment to isolate dependencies:</p>
    <code>python3 -m venv myenv</code>
    <p>Replace <code>myenv</code> with your chosen environment name.</p>

    <h3>2. Activate the Virtual Environment (Optional)</h3>
    <p>Activate based on your OS:</p>
    <ul>
        <li><strong>Windows:</strong> <code>myenv\Scripts\activate</code></li>
        <li><strong>Unix/Linux:</strong> <code>source myenv/bin/activate</code></li>
    </ul>

    <h3>3. Install Django</h3>
    <p>Run this command to install Django:</p>
    <code>pip install django</code>
    <p>Verify installation with:</p>
    <code>django-admin --version</code>

    <h2>Running the System Locally</h2>
    <ol>
        <li>Fork this repository, then clone it locally and move into the directory:</li>
        <code>git clone https://github.com/X-Evolve/Python_Hunt.git && cd Python_Hunt/producthunt_pro</code>
        <li>Run migrations:</li>
        <code>python manage.py migrate</code>
        <li>Start the server:</li>
        <code>python manage.py runserver</code>
        <li>Open the provided URL to view the site.</li>
    </ol>

    <h2>Getting Started with Contribution</h2>
    <ol>
        <li>Create a new branch for your work:</li>
        <code>git checkout -b new_work</code>
        <li>Stage and commit changes:</li>
        <code>git add .</code>
        <code>git commit -m "Description of your work"</code>
        <code>git push origin new_work</code>
        <li>Open your forked repository in your browser, then submit a Pull Request (PR) to the main branch.</li>
    </ol>

    <h2>Adding Files</h2>
    <p>To add CSS, JavaScript, or images, place them in the static folder:</p>
    <code>producthunt_pro/producthunt/static/</code>
    <p>To use these files, import them as follows:</p>
    <p>Load static files at the top of HTML:</p>
    <code>{% load static %}</code>
    <p>CSS/JavaScript file:</p>
    <code>href="{% static 'filename' %}"</code>
    <p>Image file:</p>
    <code>src="{% static 'filename' %}"</code>

    <h2>Additional Resources</h2>
    <ul>
        <li><a href="https://docs.djangoproject.com/">Django Documentation</a></li>
        <li><a href="https://www.djangoproject.com/">Django Project Website</a></li>
        <li><a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django">Mozilla Django Tutorial</a></li>
    </ul>
    
    <p>Happy coding with Django! 🐍💙</p>
    <img src="HacktoberFest2023_Resources/06_banners/hf10_logo_wall/hf10_logo_wall_1920x1080.png" alt="Hacktoberfest 2023 Banner">

</body>
</html>