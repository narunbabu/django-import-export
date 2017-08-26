# The workflow
https://django-import-export.readthedocs.io/en/latest/import_workflow.html
git push -u origin master

# And run in shell
from app.admin import BookResource
dataset = BookResource().export()
print (dataset.csv)


import tablib
from import_export import resources
from core.models import Book
book_resource = resources.modelresource_factory(model=Book)()
dataset = tablib.Dataset(['', 'New book'], headers=['id', 'name'])
result = book_resource.import_data(dataset, dry_run=True)
print (result.has_errors())

result = book_resource.import_data(dataset, dry_run=False)


django-admin inspectdb db_tut.sqlite3

Create a database using firefox sqlite manager and keep the resulted db in main django project.

# edit settings.py for databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'final_db.sqlite'),
    }
}
and run
python manage.py inspectdb > myapp/models.py

echo "# django-import-export" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/narunbabu/django-import-export.git
git push -u origin master


