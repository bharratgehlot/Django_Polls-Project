import os
import django
from django.utils import timezone

# Set up Django Environment 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "polls_project.settings")
django.setup()

from polls.models import Question, Choice

questions_and_choice = [
  
  
  
     {
        "question_text": "1. You have a Django view that displays a list of products that is rarely updated.  Which caching strategy would be MOST beneficial for performance?",
        "choices": [
          "A. Cache the entire view function output",
          "B. Cache individual product objects",
          "C. Don't use caching, database access is fast enough",    
          "D. Use a custom cache backend with in-memory storage"   
        ]
        
    },
    
    
    {
        "question_text": "2. You're building a user registration form in Django. Which approach would be MOST secure for storing passwords?",
        "choices": [
          "A. Store passwords as plain text in the database",     
          "B. Use a simple hashing algorithm like MD5",     
          "C. Hash passwords with a strong algorithm like bcrypt and store the hash",
          "D. Encrypt passwords before storing them in the database"
        ]
        
    },
    
    
    {
        
        "question_text": "3. You're writing unit tests for a Django view that takes an optional query parameter. How can you effectively test different scenarios for the parameter?",
        "choices": [
          "A. Hardcode the parameter value in the test code", 
"B. Use a mocking framework to simulate different parameter values",     
"C. Write separate tests for each possible parameter value",
"D. Unit tests shouldn't handle request parameters"
        ]
        
    },
    
    
    {
        
        "question_text": "4. You want to perform an action (like sending an email notification) whenever a new user is created in Django.  Which approach is the BEST way to achieve this?",
        "choices": [
          "A. Modify the User model's save method directly",    
"B. Override the default behavior of the create_user function",
"C. Use Django signals to listen for user creation events",
"D. Use a custom middleware to intercept user creation requests"
        ]
        
    },
    
    
    {
        "question_text": "5. What is the main advantage of using Class-Based Views (CBVs) in Django compared to function-based views?",
        "choices": [
          "A. CBVs provide a cleaner separation of concerns",
"B. CBVs offer built-in functionality for handling HTTP methods",
"C. CBVs are always more performant than function-based views",
"D. CBVs are required for using generic views like ListView"
        ]
    },
    
    
    {

        "question_text": "6. You're building an API with Django REST framework. Which approach is the recommended way to define serializers for nested data models?",
        "choices": [
          "A. Use a single serializer for the entire data structure",
"B. Define nested serializer classes for each level of the data model",
"C. Manually handle nested data serialization in the view code",
"D. Django REST framework doesn't support nested data serialization"
        ]
    },
    
    
    {

        "question_text": "7. You're deploying a Django application to a production server. Which factor should receive the HIGHEST priority for security purposes?",
        "choices": [
          "A. Optimizing the application for the fastest possible load times",
"B. Exposing the Django debug toolbar for easier troubleshooting",
"C. Keeping all dependencies up-to-date with the latest versions",
"D. Restricting access to sensitive data and functionalities"
        ]
    },
    
    
    {

        "question_text": "8. You need to periodically clean up old and unused data from your Django database. Which approach is the BEST way to achieve this?",
        "choices": [
          "A. Write a script that directly interacts with the database outside of Django",
"B. Create a custom Django management command to handle the cleanup logic",
"C. Modify the existing model deletion logic to automatically remove old data",
"D. Use a third-party library for database cleanup tasks"
        ]
    },
    
    
    {

        "question_text": "9. Your Django application is experiencing high traffic and needs to be scaled horizontally. Which approach would be MOST effective?",
        "choices": [
          "A. Increase the server resources (CPU, RAM) for the existing server",
"B. Use a load balancer to distribute traffic across multiple Django instances",
"C. Implement caching mechanisms for frequently accessed data",
"D. All of the above (A, B, and C)"
        ]
    },
    
    
    {

        "question_text": "10. You have a model for \"Courses\" and another for \"Students.\"  A student can enroll in multiple courses, and a course can have multiple enrolled students. How can you represent this many-to-many rela",
        "choices": [
          "A. Define a foreign key field in both models referencing each other",
"B. Create a separate model with a foreign key to both Course and Student models",
"C. Use a custom field type to store a list of enrolled student IDs in the Course model",
"D. Django models don't support many-to-many relationships"

        ]
    },
  
     {
        "question_text": "11.  What is the primary purpose of middleware in Django?",
        "choices": [
                "A. To handle database interactions for models",
    "B. To intercept and modify HTTP requests and responses",
    "C. To define custom template tags for dynamic content generation",
    "D. To manage user authentication and authorization logic"
        ]
    },
    {
        
        "question_text": "12. You're building a Django project with a consistent base layout. Which approach is the BEST way to achieve this layout reuse?",
        "choices": [
            "A. Copy and paste the common layout code into each template",
"B. Use a separate template for the base layout and include it in all other templates",
"C. Define a custom template tag to dynamically generate the base layout",
"D. Django templates don't support layout inheritance"
        ]
    },
    {
        
        "question_text": "13. You need to extend the default Django User model with additional profile fields. What is the recommended approach?",
        "choices": [
                "A. Modify the existing User model directly",
    "B. Create a custom user model inheriting from AbstractBaseUser",
    "C. Use a one-to-one relationship with a separate profile model",
    "D. Option B and C are valid approaches"
        ]
    },
    {
        
        "question_text": "14. What is the advantage of using Django's built-in form validation features?",
        "choices": [
                "A. Improves code readability by separating validation logic from views",
    "B. Provides a consistent way to handle user input errors with error messages",
    "C. Offers automatic data sanitization to prevent security vulnerabilities",
    "D. All of the above (A, B, and C)"
        ]
    },
    {
        
        "question_text": "15. Your Django application needs to send a large number of confirmation emails after user registration. What is the best approach to handle this efficiently?",
        "choices": [
               "A. Process all email sending logic within the registration view",
    "B. Use a background task queue like Celery to send emails asynchronously",
    "C. Implement multithreading within the view to send emails concurrently",
    "D. Django doesn't offer functionalities for asynchronous tasks"
        ]
    },
    {
        
        "question_text": "16. You want to customize the display of a specific field in the Django admin interface. How can you achieve this?",
        "choices": [
                "A. Modify the model definition for the field",
    "B. Override the model's admin class and define a custom method for the field",
    "C. Use JavaScript within the admin templates to manipulate the field display",
    "D. You cannot customize field display in the Django admin interface"
        ]
    },
    {
        
        "question_text": "17. What is the main benefit of using Django's generic class-based views like ListView or CreateView?",
        "choices": [
                "A. They automatically handle complex database queries",
    "B. They reduce boilerplate code for common CRUD (Create, Read, Update, Delete) operations",
    "C. They offer built-in functionalities for user authentication",
    "D. They are always more performant than custom views"
        ]
    },
    {
       
        "question_text": "18. You're building a Django application that needs to support multiple languages. How can you manage translations for your templates and user interface?",
        "choices": [
                "A. Hardcode translations directly within the templates",
    "B. Use a third-party library for translation management",
    "C. Leverage Django's built-in i18n features with translation files",
    "D. Django doesn't offer functionalities for internationalization"
        ]
    },
    {
        
        "question_text": "19. What is the best practice for managing static files (like CSS, JavaScript) in Django?",
        "choices": [
                "A. Store them directly within the templates folder",
    "B. Use a separate static folder outside the project directory and configure Django to serve them",
    "C. Inline all static files within the HTML templates",
    "D. Upload static files directly to the web server"
        ]
    },
    {
       
        "question_text": "20. The default Django permission system doesn't meet your specific application's needs. How can you implement custom permissions for user roles?",
        "choices": [
                "A. Modify the existing permission classes provided by Django",
    "B. Create custom permission classes and integrate them with the Django permission framework",
    "C. Use a third-party library for managing custom user permissions",
    "D. Django doesn't allow for custom permission logic"
        ]
    },    
   
  
  
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
    