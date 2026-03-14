from django.contrib.auth.mixins import UserPassesTestMixin

class ProfesseurRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_professeur
