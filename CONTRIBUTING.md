
<img src="HacktoberFest2023_Resources/05_logo_set/hf10_horizontal_logos/cmyk/hf10_horz_fcl_cmyk.png" alt="My Image">


<h1>Python Hunt Hacktoberfest 2023 Contribution Guidelines 💙</h1>
   <p>Hello open-source enthusiasts! Welcome to Python Hunt, a platform dedicated to making learning Python even more accessible. This Django project provides a space for contributors to create web pages explaining various Python concepts, as outlined in the existing issues. To maintain a consistent design, please ensure that your templates follow the established style guide. Refer to the documentation below for instructions on running the website on your local system.</p>
    <p>Don't forget to show your support by leaving a ⭐ if you find this repository helpful!</p>
    <h2>Prerequisites</h2>
    <p>Before you proceed with the installation, make sure you have the following prerequisites installed on your system:</p>
    <ul>
        <li>Python (version 3.6 or higher)</li>
        <li>pip (Python package installer)</li>
    </ul>
    <h2>Installation Steps</h2>
    <h3>Create a Virtual Environment (Optional)</h3>
    <p>It's recommended to create a virtual environment to isolate your Django project's dependencies. Open your terminal or command prompt and execute the following command:</p>
    <code>python3 -m venv myenv</code>
    <p>Replace <code>myenv</code> with your desired name for the virtual environment.</p>
    <h3>Activate the Virtual Environment (Optional)</h3>
    <p>Activate the virtual environment based on your operating system:</p>
    <p><strong>Windows:</strong></p>
    <code>myenv\Scripts\activate</code>
    <p><strong>Unix or Linux:</strong></p>
    <code>source myenv/bin/activate</code>
    <h3>Install Django</h3>
    <p>With your virtual environment activated, install Django using pip:</p>
    <code>pip install django</code>
    <p>This command will download and install the latest stable version of Django.</p>
    <h3>Verify the Installation</h3>
    <p>To verify that Django is successfully installed, run the following command:</p>
    <code>django-admin --version</code>
    <p>You should see the installed Django version printed in the console.</p>
    <p>Congratulations! You have successfully installed Django on your system. You are now ready to start building your Django web applications.</p>
    <h2>Running the System on Your Local System</h2>
    <ol>
        <li>Fork this repository and move inside it:</li>
        <code>git clone https://github.com/X-Evolve/Python_Hunt.git &amp;&amp; cd Python_Hunt/producthunt_pro</code>
        <li>Migrate the necessary data for the models:</li>
        <code>python manage.py migrate</code>
        <li>Run the website on your local host:</li>
        <code>python manage.py runserver</code>
        <li>Click on the URL produced, and it will open in your default browser.</li>
    </ol>
    <p>Congratulations! You have successfully set up your Django Web Server on your local host. You are now ready to contribute!</p>
    <h2>Getting Started with Contribution</h2>
    <ol>
        <li>Create a new branch to work on an issue:</li>
        <code>git checkout -b new_work</code>
        <li>Once you have completed your code, open a Pull Request (PR).</li>
        <p>From the root of the project, run the following commands:</p>
        <code>git add .</code>
        <code>git commit -m "Description of your work (short one is preferred)"</code>
        <code>git push origin new_work</code>
        <li>Open your forked repository in your browser and then raise a Pull Request (PR) to the main branch of this repository!</li>
    </ol>
    <h2>How to Add Your Files in the Project</h2>
    <p>If you want to add CSS, JavaScript, or image files to this project, place them in the static folder:</p>
    <code>producthunt_pro/producthunt/static/</code>
    <p>Import them into the code using the following:</p>
    <p>(At the top of the HTML File)</p>
    <code>{% load static %}</code>
    <p>(To use your CSS / JavaScript file)</p>
    <code>href="{% static 'name of the file' %}"</code>
    <p>(To use your image file)</p>
    <code>src="{% static 'name of the file' %}"</code>
    <h2>Additional Resources</h2>
    <ul>
        <li><a href="https://docs.djangoproject.com/">Django Official Documentation</a>: The official Django documentation provides comprehensive information and tutorials for learning Django.</li>
        <li><a href="https://www.djangoproject.com/">Django Project Website</a>: The official website of the Django project offers news, updates, and additional resources.</li>
        <li><a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django">Django Tutorial by Mozilla</a>: This tutorial by Mozilla provides a beginner-friendly introduction to Django.</li>
    </ul>
    <p>Happy coding with Django! 🐍💙</p>
    <br>

<img src="HacktoberFest2023_Resources/06_banners/hf10_logo_wall/hf10_logo_wall_1920x1080.png" alt="My Image">

