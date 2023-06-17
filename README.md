<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Django Installation Guide</title>
</head>
<body>
  <h1>Django Installation Guide</h1>

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
  </ul>

  <p>Happy coding with Django!</p>
</body>
</html>
