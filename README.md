<body>
<img src="HacktoberFest2023_Resources/05_logo_set/hf10_horizontal_logos/cmyk/hf10_horz_fcl_cmyk.png" alt="My Image"/>
  <h1>Python Hunt is an OpenSoure Website 💙</h1>
   <p>Hello opensource developers! We have initiated a website called Python Hunt to make learning python even more easier. This is a Django project where you can contribute web pages explaining various concepts in python as mentioned in issues. Make sure that the templates must have same kind of design everywhere to maintain uniformity. Please refer the below documentation for running the website on your system.</p>
 
  <p>Add your HTML Pages here: </p>
   <pre><code>producthunt_pro/products/templates/products/</code></pre>
   
 [To know more about how to add the pages, click here!](#how-to-add-your-files-in-the-project)
 <p>Kindly consider leaving a ⭐ if you like the repository</p>
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
  
  <h2>Running this system in your local system</h2>
  
  <ol>
    <li>
      <h3>Fork this repository and move inside it</h3>
      <pre><code>git clone https://github.com/X-Evolve/Python_Hunt.git && producthunt_pro</code></pre>
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
      <p>Click on the url produced and it opens in your default browser</p>
    </li>
  </ol>
  
  <p>Congratulations! You have successfully setup your Django Web Server on your local host. You are now ready to contribute!</p>

 <h2>Getting Started with Contributions</h2>
  <ol>
    <li>
      <h3>Checkout to a new branch to work on an issue</h3>
      <pre><code>git checkout -b new_work</code></pre>
    </li>
     <li>
      <h3>Once you have completed coding, then open a Pull Request(PR)</h3>
       <p>From the root of the project, Run the following commands:</p>
        <ul>
                <li>
                        <p> Add your contributions to the branch</p>
                        <pre><code>git add .</code></pre>
                </li>
                <li>
                        <p> Commit the contributions you made to the branch</p>
                        <pre><code>git commit -m "prefix: Description of your work (short one is preferred)"</code></pre>
                        <p>
                          Add the following prefixes depending on your contributions:
                          <ul>
                            <li>fix: A bug fix</li>
                            <li>feat: A new feature</li>
                            <li>docs: Documentation changes</li>
                            <li>chore: Miscellaneous changes that do not match any of the above.</li>
                          </ul>
                        </p>
                </li>
                <li> 
                        <p> Push your contributions to your branch:</p>
                        <pre><code>git push origin new_work</code></pre>
                </li>
        </ul>
       <p>Open your forked repository in your browser and then raise a Pull Request (PR) to the main branch of this repository!</p>
    </li>
  </ol>

  
  <h2>How to Add your files in the project</h2>
  <p>If you want to add CSS or Javascript or Image files in this project, add it in static folder:</p>
  <div class="contrainer">
  <pre><code>producthunt_pro/producthunt/static/</code></pre>
  <p>Import them into the code by using this: </p>
  
  (On the top of the HTML File)
  <pre><code>#Imports the base template
{% extends 'base.html' %} 
{% block content %} 
    
#Load the static files added in the folder above
{% load static %}</code></pre>
  (When you want to use your CSS / Javascript file)
  <pre><code>href = "{% static 'name of the file' %}"</code></pre> 
  
  (When you want to use your image file)
  <pre><code>src = "{% static 'name of the file' %}"</code></pre> 

  (After you have finished your HTML page, add the below code at the end of the file)
  <pre><code>{% endblock %}</code></pre> 
  <b>Notes: 
  <ul>
   <li> Do design your HTML pages with respect to the base template.<br>
  For more reference, check the other pages designed so far.</li>
    <li> The importance of including the base template is that it has the default navbar and footer which makes it easier to navigate through the pages.</li>
  </ul></b>
  </div>


  <h2>Additional Resources</h2>

  <ul>
    <li>
      <a href="https://docs.djangoproject.com/">Django Official Documentation</a>: The official Django documentation provides comprehensive information and tutorials for learning Django.
    </li>
    <li>
      <a href="https://www.djangoproject.com/">Django Project Website</a>: The official website of the Django project offers news, updates, and additional resources.
    </li>
    <li>
      <a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django">Django Tutorial by Mozilla</a>: This tutorial by Mozilla provides a beginner-friendly introduction to Django.
    </li>
    <li>
      <a href="https://www.conventionalcommits.org/en/v1.0.0/">Conventional Commits</a>: This website provides a detailed description of how to write proper commits.
    </li>
  </ul>

  <p>Happy coding with Django!</p>
</body>
