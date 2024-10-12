import os
import sys
import django

if __name__ == '__main__':
    # Set the environment variable to your Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exam_form.settings')
    
    # Initialize Django
    django.setup()
    
    # Run the Django command
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
