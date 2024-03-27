from django.db import models


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length = 50,null=True)
    pic = models.FileField(upload_to="media/",default="media/user_image.jpg",blank=True, null=True)
 
    def __str__(self):
        return f"{self.name}"


class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    sender_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender')
    receiver_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='receiver')
    time = models.TimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.receiver_name} From: {self.sender_name}"

    class Meta:
        ordering = ('timestamp',)


class Friends(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    friend = models.IntegerField()

    def __str__(self):
        return f"{self.friend}"

