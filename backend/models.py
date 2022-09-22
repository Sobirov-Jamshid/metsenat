from django.db import models


class Sponsor(models.Model):
    STATUS_CHOICES = (
        ('new', 'Yangi'),
        ('processing', 'Moderatsiyada'),
        ('complated', 'Tasdiqlangan'),
        ('canceled', 'Bekor qilingan')
    )
    PERSON_CHOICES = (
        ('physical', 'Jismoniy shaxs'),
        ('juridic', 'Yuridik shaxs')
    )
    full_name = models.CharField(max_length=70, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    money = models.BigIntegerField(null=True)
    person_type = models.CharField(max_length=50, choices=PERSON_CHOICES, null=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class University(models.Model):
    name = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'


class Student(models.Model):
    DEGREE_CHOICES = (
        ('bachelor', 'Bakalavr'),
        ('master', 'Magistr'),
        ('phd', 'phd')
    )
    full_name = models.CharField(max_length=70, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    university = models.ForeignKey(University, related_name='students', on_delete=models.SET_NULL, null=True)
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES, null=True)
    contract = models.BigIntegerField(null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class SponsorShip(models.Model):
    sponsor = models.ForeignKey(Sponsor, related_name='sponsorships', on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, related_name='sponsorships', on_delete=models.CASCADE, null=True)
    money = models.BigIntegerField(null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.sponsor.full_name} -> {self.student.full_name} : {self.money} so\'m'

    class Meta:
        verbose_name = 'Sponsorship'
        verbose_name_plural = 'Sponsorships'
