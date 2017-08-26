# app/admin.py

from import_export import resources
from core.models import Book

# class BookResource(resources.ModelResource):

#     class Meta:
#         model = Book
#         # fields = ('id', 'name', 'price',)
#         # exclude = ('imported', )
#         fields = ('id', 'name', 'author', 'price',)
#         export_order = ('id', 'price', 'author', 'name')

from import_export import fields

class BookResource(resources.ModelResource):
    published = fields.Field(column_name='published_date')
    myfield = fields.Field(column_name='myfield')

    class Meta:
        model = Book

    def dehydrate_full_title(self, book):
        return '%s by %s' % (book.name, book.author.name)
    widgets = {
                'published': {'format': '%d.%m.%Y'},
                }

    delete = fields.Field(widget=widgets.BooleanWidget())

    def for_delete(self, row, instance):
        return self.fields['delete'].clean(row)

# app/admin.py
from import_export.admin import ImportExportActionModelAdmin

# class BookAdmin(ImportExportActionModelAdmin):
#     pass
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

