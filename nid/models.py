from django.db import models
from cloudinary.models import CloudinaryField

# Create a model named Nid that has a primary key named id which is 10 digit number gerated serially

class Nid(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    id = models.CharField(max_length=10,primary_key=True, editable=False, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Male")
    present_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    father = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='father_child', null=True, blank=True)
    father_name = models.CharField(max_length=100)
    mother = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='mother_child', null=True, blank=True)
    mother_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    photo = CloudinaryField('nid_photo', blank=True)
    signature = CloudinaryField('nid_signature', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.id} - {self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generate_id()
        super(Nid, self).save(*args, **kwargs)

    def generate_id(self):
        last_id = Nid.objects.all().order_by('id').last()
        if not last_id:
            return '0000000001'
        nid = str(int(last_id.id) + 1)
        return nid.zfill(10)

    

    class Meta:
        ordering = ['-created_at']

