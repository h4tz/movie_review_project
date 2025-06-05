Django Movie Review Application
This is a Django-based web application for searching movies, submitting reviews, and viewing existing reviews. Users can log in, search for movies, rate them from 1 to 5 stars, and leave comments.

Features
User Authentication: Users can register, log in, and log out.

Movie Search: Search for movies using an external API (e.g., OMDB API).

Movie Listing: Display search results in a card-based layout with Tailwind CSS.

Movie Details & Review Submission: View movie details and submit/update reviews.

Review Display: See your own review for a specific movie, including a star rating visualization.

REST API for Reviews: (Optional, based on ReviewViewSet) Programmatic access to review data.

Responsive Design: Styled with Tailwind CSS for a modern and mobile-friendly interface.

Technologies Used
Backend: Python, Django, Django REST Framework (for API)

Frontend: HTML, CSS (Tailwind CSS), JavaScript

Database: SQLite (default for development)

External API: OMDB API (or similar, for movie data)

What I Learned
Throughout the development of this project, I gained practical experience and a deeper understanding of:

Django Fundamentals:

Setting up Django projects and applications.

Defining models and understanding ForeignKey relationships.

Working with views (function-based and class-based for REST API).

Configuring URL patterns and using the {% url %} template tag for dynamic URL generation.

Managing templates and passing context data to them.

Implementing User Authentication and using @login_required decorators.

Utilizing Django's messages framework for user feedback.

Handling form submissions and data validation with Django Forms.

Performing database migrations (makemigrations, migrate).

External API Integration:

Making HTTP requests to external web services (like OMDB API).

Parsing JSON responses from APIs.

Strategies for saving and updating data fetched from external sources into Django models.

Frontend Development with Tailwind CSS:

Applying Tailwind CSS utility classes for rapid and responsive styling.

Creating modern, card-based layouts using CSS Grid and Flexbox.

Styling forms and interactive elements for a better user experience.

Implementing dynamic content rendering in templates (e.g., star ratings with SVG).

Debugging and Error Resolution:

Interpreting Django Tracebacks to pinpoint code errors (NameError, TypeError, NoReverseMatch, ValueError).

Using the dbshell to inspect and modify database contents directly.

Understanding the importance of correct data types and argument passing in both Python views and Django templates.

Troubleshooting template rendering issues.

Version Control:

Basic Git workflow (add, commit, push) for managing project changes and collaborating.

Setup and Installation
Follow these steps to get the project up and running on your local machine.

Prerequisites
Python 3.8+

pip (Python package installer)

sqlite3 command-line tool (for default development database)

1. Clone the repository
git clone https://github.com/YourUsername/your-repo-name.git
cd your-repo-name

(Replace YourUsername and your-repo-name with your actual GitHub details.)

2. Create and activate a virtual environment
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

3. Install dependencies
First, create the requirements.txt file by listing all installed Python packages:

pip freeze > requirements.txt

Then, install them (useful if you've cloned the repo or are setting up on a new machine):

pip install -r requirements.txt

4. Database Setup
python manage.py makemigrations
python manage.py migrate

5. Create a Superuser (for Django Admin)
python manage.py createsuperuser

Follow the prompts to create an admin user.

6. Configure API Key
You'll need an API key for a movie database service (e.g., OMDB API).
Create a .env file in the root of your project or add the key directly to your settings.py (for development only, for production use environment variables).

In movie_review_project/settings.py:

# settings.py
# ...
OMDB_API_KEY = 'YOUR_OMDB_API_KEY' # Replace with your actual OMDB API key
# ...

7. Run the Development Server
python manage.py runserver

The application will be available at http://localhost:8000/.

8. Access Django Admin
You can access the Django administration panel at http://localhost:8000/admin/ using the superuser credentials you created.

Project Structure (Example)
movie_review_project/
├── movie_review_project/  # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── reviews/             # Your reviews application
│   ├── migrations/
│   ├── templates/
│   │   └── reviews/
│   │       ├── review_form.html
│   │       ├── review_detail.html
│   │       └── review_success.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── core/                # Your core application (if it exists)
│   ├── templates/
│   │   └── core/
│   │       └── index.html # Movie listing page
│   ├── models.py
│   └── views.py
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md

Contributing
Feel free to fork the repository, make changes, and submit pull requests.
