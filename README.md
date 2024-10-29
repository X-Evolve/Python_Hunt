<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Hunt - OpenSource Website</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            color: #333;
        }
        header {
            text-align: center;
            padding: 20px;
            background: #007acc;
            color: white;
        }
        img {
            max-width: 100%;
            height: auto;
        }
        h1, h2, h3 {
            margin: 20px 0;
        }
        ul, ol {
            margin: 10px 0;
            padding-left: 20px;
        }
        a {
            color: #007acc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background: white;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        pre {
            background: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        footer {
            text-align: center;
            padding: 20px;
            background: #007acc;
            color: white;
            position: relative;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>

<header>
    <img src="HacktoberFest2023_Resources/05_logo_set/hf10_horizontal_logos/cmyk/hf10_horz_fcl_cmyk.png" alt="My Image"/>
    <h1>Python Hunt is an OpenSource Website 💙</h1>
</header>

<div class="container">
    <p>Hello opensource developers! We have initiated a website called Python Hunt to make learning Python even easier. This is a Django project where you can contribute web pages explaining various concepts in Python as mentioned in issues. Make sure that the templates maintain the same kind of design everywhere to ensure uniformity. Please refer to the documentation below for running the website on your system.</p>

    <p>Add your HTML Pages here:</p>
    <pre><code>producthunt_pro/products/templates/products/</code></pre>
    <p>[To know more about how to add the pages, <a href="#how-to-add-your-files-in-the-project">click here!</a>]</p>
    <p>Kindly consider leaving a ⭐ if you like the repository.</p>
    <p>Happy Coding!</p>

    <h2>Prerequisites</h2>
    <p>Before installing Django, ensure that you have the following prerequisites installed on your system:</p>
    <ul>
        <li>Python (version 3.6 or higher)</li>
        <li>pip (Python package installer)</li>
    </ul>

    <h2>Installation Steps</h2>
    <ol>
        <li>
            <h3>Create a virtual environment (optional)</h3>
            <p>It's recommended to create a virtual environment to isolate your Django project's dependencies. Open your terminal or command prompt and execute the following command:</p>
            <pre><code>python3 -m venv myenv</code></pre>
            <p>Replace <code>myenv</code> with the desired name for your virtual environment.</p>
        </li>
        <li>
            <h3>Activate the virtual environment (optional)</h3>
            <p>Activate the virtual environment by running the appropriate command for your operating system:</p>
            <h4>Windows:</h4>
            <pre><code>myenv\Scripts\activate</code></pre>
            <h4>Unix or Linux:</h4>
            <pre><code>source myenv/bin/activate</code></pre>
        </li>
        <li>
            <h3>Install Django</h3>
            <p>With your virtual environment activated, execute the following command to install Django using pip:</p>
            <pre><code>pip install django</code></pre>
            <p>This command will download and install the latest stable version of Django.</p>
        </li>
        <li>
            <h3>Verify the installation</h3>
            <p>To verify that Django is successfully installed, run the following command:</p>
            <pre><code>django-admin --version</code></pre>
            <p>You should see the installed Django version printed in the console.</p>
        </li>
    </ol>

    <p>Congratulations! You have successfully installed Django on your system. You are now ready to start building your Django web applications.</p>

    <h2>Running this system on your local machine</h2>
    <ol>
        <li>
            <h3>Fork this repository and move inside it</h3>
            <pre><code>git clone https://github.com/X-Evolve/Python_Hunt.git && cd producthunt_pro</code></pre>
        </li>
        <li>
            <h3>Next, use this command for migrating changes to the models</h3>
            <pre><code>python manage.py migrate</code></pre>
        </li>
        <li>
            <h3>Running the Website on your Local Host</h3>
            <p>To run the website on your local host, use the following command:</p>
            <pre><code>python manage.py runserver</code></pre>
        </li>
        <li>
            <h3>Last Step</h3>
            <p>Click on the URL produced to open it in your default browser.</p>
        </li>
    </ol>

    <p>Congratulations! You have successfully set up your Django Web Server on your local host. You are now ready to contribute!</p>

    <h2>Getting Started with Contributions</h2>
    <ol>
        <li>
            <h3>Checkout to a new branch to work on an issue</h3>
            <pre><code>git checkout -b new_work</code></pre>
        </li>
        <li>
            <h3>Once you have completed coding, then open a Pull Request (PR)</h3>
            <p>From the root of the project, run the following commands:</p>
            <ul>
                <li>
                    <p>Add your contributions to the branch</p>
                    <pre><code>git add .</code></pre>
                </li>
                <li>
                    <p>Commit the contributions you made to the branch</p>
                    <pre><code>git commit -m "prefix: Description of your work (short one is preferred)"</code></pre>
                    <p>Add the following prefixes depending on your contributions:</p>
                    <ul>
                        <li>fix: A bug fix</li>
                        <li>feat: A new feature</li>
                        <li>docs: Documentation changes</li>
                        <li>chore: Miscellaneous changes that do not match any of the above.</li>
                    </ul>
                </li>
                <li>
                    <p>Push your contributions to your branch:</p>
                    <pre><code>git push origin new_work</code></pre>
                </li>
            </ul>
            <p>Open your forked repository in your browser and then raise a Pull Request (PR) to the main branch of this repository!</p>
        </li>
    </ol>

    <h2>How to Add your files in the project</h2>
    <p>If you want to add CSS, JavaScript, or image files in this project, add them in the static folder:</p>
    <pre><code>producthunt_pro/producthunt/static/</code></pre>
    <p>Import them into the code by using this:</p>

    <p>(On the top of the HTML File)</p>
    <pre><code>{% extends 'base.html' %}</code></pre>
    <pre><code>{% block content %}</code></pre>
    <pre><code>{% load static %}</code></pre>
    
    <p>(When you want to use your CSS / JavaScript file)</p>
    <pre><code>href = "{% static 'name of the file' %}"</code></pre> 

    <p>(When you want to use your image file)</p>
    <pre><code>src = "{% static 'name of the file' %}"</code></pre> 

    <p>(After you have finished your HTML page, add the below code at the end of the file)</p>
    <pre><code>{% endblock %}</code></pre> 
    <b>Notes: 
    <ul>
        <li>Design your HTML pages with respect to the base template.<br>
        For more reference, check the other pages designed so far.</li>
        <li>The importance of including the base

  
