from django.db import models

# Create your models here.


# class MyModelName(models.Model):
    
#     # Fields
#     my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
#     ...

#     # Metadata
#     class Meta: 
#         ordering = ['-my_field_name']

#     # Methods
#     def get_absolute_url(self):
#         """Returns the url to access a particular instance of MyModelName."""
#         return reverse('model-detail-view', args=[str(self.id)])
    
#     def __str__(self):
#         """String for representing the MyModelName object (in Admin site etc.)."""
#         return self.my_field_name

    # # Create a new record using the model's constructor.
    # record = MyModelName(my_field_name="Instance #1")

    # # Save the object into the database.
    # record.save()