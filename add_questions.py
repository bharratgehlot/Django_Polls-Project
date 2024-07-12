import os
import django
from django.utils import timezone

# Set up Django Environment 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "polls_project.settings")
django.setup()

from polls.models import Question, Choice

questions_and_choice = [
  
    {
        "question_text": "21. When using Django ModelForms, what is the purpose of the cleaned_data dictionary?",
        "choices": ["A. It stores the raw form data submitted by the user.","B. It contains the validated and processed form data after cleaning.","C. It defines the layout and fields of the form in the template.","D. It manages the authorization rules for accessing model instances."]
    },

{
"question_text": "22. Within a Django template, how can you iterate over a list of objects retrieved from the context?",
"choices": [
"A. Using a standard for loop with the object list directly.",
"B. Employing a custom template tag specifically designed for iteration.",
"C. Accessing objects one by one using their index within the context.",
"D. Django templates don't support looping through context data."
]
},

{
"question_text": "23. In Django REST framework, what is the role of a serializer class?",
"choices": [
"A. It defines the authentication mechanism for API requests.",
"B. It controls the caching behavior for API endpoints.",
"C. It specifies the format (JSON, XML) for data serialization and deserialization.",
"D. It handles permission checks for accessing API resources."
]
},

{
"question_text": "24. Which Django signal is emitted when a user successfully logs in to the application?",
"choices": [
"A. user_registered",
"B. user_authenticated",
"C. user_logged_in (Django doesn't provide this specific signal)",
"D. request_login"
]
},

{
"question_text": "25. How can you implement a custom authentication backend in Django?",
"choices": [
"A. By modifying the default User model directly.",
"B. By inheriting from the AuthenticationBackend class and defining custom logic.",
"C. By using a third-party library specifically designed for authentication.",
"D. Django doesn't allow for custom authentication backends."
]
},

{
"question_text": "26. What is the primary benefit of using Django's built-in development server for local development?",
"choices": [
"A. It offers high performance and scalability for production use.",
"B. It provides a convenient way to test applications without complex setup.",
"C. It integrates seamlessly with deployment tools for easy server management.",
"D. It enforces strict security measures for development environments."
]
},

{
"question_text": "27. When using Django's ORM (Object-Relational Mapper), what is the purpose of a model manager?",
"choices": [
"A. It defines the database schema and table structure for the model.",
"B. It manages the relationships between different models in your application.",
"C. It provides methods for querying and interacting with model instances in the database.",
"D. It handles user authentication and authorization logic for model access."
]
},

{
"question_text": "28. What is the difference between a Django URL pattern and a view function?",
"choices": [
"A. URL patterns define database queries, while view functions handle user requests.",
"B. URL patterns map incoming URLs to specific view functions for handling logic.",
"C. View functions manage user authentication, while URL patterns define permissions.",
"D. URL patterns are for static content, while view functions handle dynamic content."
]
},

{
"question_text": "29. How can you leverage Django's built-in form rendering capabilities to display a form in a template?",
"choices": [
"A. By directly writing HTML code for the form within the template.",
"B. By using a custom template tag specifically designed for form rendering.",
"C. By employing the {{ form }} template tag with the appropriate form instance.",
"D. Django templates don't offer functionalities for form rendering."
]
},

{
"question_text": "30. Hardcoding environment variables directly within the application code is discouraged. What is a more secure approach?",
"choices": [
"A. Storing environment variables in a separate configuration file on the server.",
"B. Including environment variables as part of the deployment script.",
"C. Prompting the user for environment variables during application startup.",
"D. Storing environment variables in the Django settings module (not recommended for production)."
]
}

]

for items in questions_and_choice:
  question = Question.objects.create(
    question_text=items["question_text"],
    pub_date=timezone.now()
  )
  
  for choices in items["choices"]:
    Choice.objects.create(
      question=question,
      choice_text=choices,
      votes=0
    )
    
print("Questions and choices added successfully!")   
    