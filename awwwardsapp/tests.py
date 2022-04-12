# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Project, Profile,Rating


class ProfileTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="Sharp"
        )

        self.profile = Profile(
            bio="Full-stack dev",
            user=user,
            contact="0796042110",
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_update_method(self):
        self.profile.update_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)


    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_create_method(self):
        self.profile.create_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
class ProjectTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
               username="Sharp"
        )

        self.project = Project(
            title="pizza-joint",
            description="This a website for rating projects",
            image="",
            user=user,
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)
    

    def test_update_project(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_method(self):
        self.project.save_project()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)

   
class ProfileTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="test_user"
        )

        self.profile = Profile(
            bio="Test Profile_photo",
            user=user,
            contact="Test Contact",
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_update_method(self):
        self.profile.update_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)


    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_create_method(self):
        self.profile.create_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
class RatingTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
               username="Sharp"
        )

        self.rating = Rating(
            user=user,
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))
