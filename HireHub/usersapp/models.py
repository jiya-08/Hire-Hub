from django.db import models


# -----------------------------
# Country Model
# -----------------------------
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# -----------------------------
# State Model
# -----------------------------
class State(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="states"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# -----------------------------
# City Model
# -----------------------------
class City(models.Model):
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name="cities"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# -----------------------------
# User Model
# -----------------------------
class User(models.Model):

    ROLE_CHOICES = [
        ('Client', 'Client'),
        ('Freelancer', 'Freelancer'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    profile_image = models.ImageField(
        upload_to="profile_images/",
        blank=True,
        null=True
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


# -----------------------------
# Freelancer Profile
# -----------------------------
class FreelancerProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.CharField(max_length=255)
    experience = models.IntegerField()
    hourly_rate = models.FloatField()
    portfolio_link = models.URLField(blank=True, null=True)
    bio = models.TextField()
    phone_no = models.CharField(max_length=15)
    address = models.TextField()

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


# -----------------------------
# Job Category
# -----------------------------
class JobCategory(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name


# -----------------------------
# Project
# -----------------------------
class Project(models.Model):

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.FloatField()
    deadline = models.DateField()
    skills_required = models.CharField(max_length=255)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='open'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# -----------------------------
# Proposal
# -----------------------------
class Proposal(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE)

    proposal_text = models.TextField()
    bid_amount = models.FloatField()
    delivery_days = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.freelancer.first_name


# -----------------------------
# Hire
# -----------------------------
class Hire(models.Model):

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE)

    hired_date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Active'
    )

    def __str__(self):
        return self.freelancer.first_name

# -----------------------------
# Message Model
# -----------------------------
class Message(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )

    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"

# -----------------------------
# Contact Us Model
# -----------------------------
class ContactUs(models.Model):
    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name