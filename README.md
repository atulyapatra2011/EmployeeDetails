<h2>Employee Information Project to BUILD OWN APIs using Django RestFramework</h2>
<ul>
	<li>Simple Get Api is created to make new user feel comfortable</li>
	<li>Entire project is based on Python Django Framework</li>
	<li>To access API online, we deployed it on HEROKU</li>
	<li>How to deploy on HEROKU see below:</li>
</ul>
<h2>Deploy Django Project on HEROKU</h2>
<ul>
	<li>create Github user account: https://github.com/</li>
	<li>create repository on Github</li>
	<li>create Heroku user account: https://id.heroku.com/login</li>
	<li>install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli</li>
	<li>create new APP on Heroku</li>
	<li>under Deploy => Deployment method => Connect to Github => Search Github Repository</li>
	<li>install Gunicorn pip install gunicorn</li>
	<li>create 'Procfile' without extension</li>
	<li>add below line in 'Procfile', replace myproject with your project name<br/>
		<span>web: gunicorn myproject.wsgi</span>
	</li>
	<li>pip install django-heroku</li>
	<li>pip install waitress</li>
	<li>pip install witenoise :- for django static file
		<span>STATIC_ROOT = os.path.join(BASE_DIR,'static')</span>
		<span> 'whitenoise.middleware.WhiteNoiseMiddleware' </span>
	</li>
	<li>pip freeze</li>
	<li>create requirments file using following command<br/>
		<span>pip freeze > requirements.txt</span>
	</li>
	<li>add import statement at the top of settings.py<br/>
		<span>import django_heroku</span>
	</li>
	<li>at the bottom of settings.py add below<br/>
		<span>django_heroku.settings(locals())</span>
	</li>
	<li>change debug setting in settings.py<br/>
		<span> DEBUG = False OR DEBUG =True use below code</span><br/>
		<span>
			if (len(sys.argv) >= 2 and sys.argv[1] == 'runserver'):
   					DEBUG = True
 			else:
   					DEBUG = False
		</span>
	</li>
	<li>add import statement at the top of settings.py otherwise, 'sys.argv' will not work<br/>
		<span>import sys</span>
	</li>
	<li>git add .</li>
	<li>git commite -m 'second commit"</li>
	<li>git push</li>
	<li>Logout heroku :- heroku logout</li>
	<li>Login heroku :- heroku login </li>
	<li>run below for heroku:-cd "go to your project folder":- <br/>heroku run -app <name of heroku app> python manage.py migrate</li>
	<li>create super user for heroku:-cd "go to your project folder":-<br/> heroku run -app <name of heroku app> python manage.py createsuperuser</li>
	
</ul>
