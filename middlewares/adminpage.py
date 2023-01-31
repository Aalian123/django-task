from django.urls import reverse

from django.shortcuts import redirect, render


def admin_page_middleware(get_response):
    # One-time configuration and initialization.
    def admin_page(request):
        user = request.user

        if user.is_superuser:
            return redirect('/admin/')
        else:
            return render(request, 'home.html')
        response = get_response(request)
        return response

    return admin_page

# class AdminPageMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#
#         response = self.get_response(request)
#         user = request.user
#         if user.is_authenticated:
#             return redirect('/admin/')
#         else:
#             return redirect('/signup/')
#         return response

# class AdminPageMiddleware(MiddlewareMixin):
#     # import pdb
#     # pdb.set_trace()
#     def process_view(self, request, Signup, *view_arg, **kwargs):
#         # import pdb
#         # pdb.set_trace()
#         user = request.user
#
#         if user.is_superuser:
#             while not (request.path == reverse('Elearning_platform:inherit')):
#                 return redirect(reverse('Elearning_platform:inherit'))
#         else:
#             while not (request.path == reverse('Elearning_platform:login')):
#                 return redirect(reverse('Elearning_platform:login'))
