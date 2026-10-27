from django.contrib import admin
from .models import Message, ContactUs
from .models import (
    Country,
    State,
    City,
    User,
    FreelancerProfile,
    JobCategory,
    Project,
    Proposal,
    Hire,
)

@admin.register(Country)
class ShowCountry(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(State)
class ShowState(admin.ModelAdmin):
    list_display = ('id', 'country', 'name')



@admin.register(City)
class ShowCity(admin.ModelAdmin):
    list_display = ('id', 'state', 'name')


# -------------------- User --------------------

@admin.register(User)
class ShowUser(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'profile_image',
        'role',
        'date_joined',
    )


# -------------------- Freelancer Profile --------------------

@admin.register(FreelancerProfile)
class ShowFreelancerProfile(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'skills',
        'experience',
        'hourly_rate',
        'phone_no',
        'city',
        'state',
        'country',
    )


# -------------------- Job Category --------------------

@admin.register(JobCategory)
class ShowJobCategory(admin.ModelAdmin):
    list_display = (
        'id',
        'category_name',
        'description',
    )


# -------------------- Project --------------------

@admin.register(Project)
class ShowProject(admin.ModelAdmin):
    list_display = (
        'id',
        'client',
        'category',
        'title',
        'budget',
        'deadline',
        'status',
        'created_at',
    )


# -------------------- Proposal --------------------

@admin.register(Proposal)
class ShowProposal(admin.ModelAdmin):
    list_display = (
        'id',
        'project',
        'freelancer',
        'bid_amount',
        'delivery_days',
        'status',
        'created_at',
    )


# -------------------- Hire --------------------

@admin.register(Hire)
class ShowHire(admin.ModelAdmin):
    list_display = (
        'id',
        'project',
        'freelancer',
        'hired_date',
        'status',
    )

# -------------------- Message --------------------

@admin.register(Message)
class ShowMessage(admin.ModelAdmin):
    list_display = [
        'id',
        'sender',
        'receiver',
        'message',
        'created_at'
    ]


# -------------------- Contact Us --------------------

@admin.register(ContactUs)
class ShowContactUs(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'phone',
        'message',
        'created_at'
    ]