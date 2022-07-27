import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from catalog.forms import RenewBookForm
from catalog.models import Author
# Create your views here.


"""
from django.contrib.auth.decorators import permission_required

@permission_required('catalog.can_mark_returned')
@permission_required('catalog.can_edit')
For functions-based views


from django.contrib.auth.mixins import PermissionRequiredMixin

class MyView(PermissionRequiredMixin, View):
    permission_required = 'catalog.can_mark_returned'
    
    # or for multiple permissions
    permission_required = ('catalog.can_mark_returned','catalog.can_edit',)


"""
@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Count of genres
    num_genres = Genre.objects.count()

    # Count of books that contain a particular word(case insensitive)
    num_particular_books = Book.objects.filter(title__icontains="wind").count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_particular_books': num_particular_books,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 2
    context_object_name = 'book_list'
    # your own name for the list as a template variable.

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

    queryset = Book.objects.filter(title__icontains = 'a')[:5]
    # Get me five books that contain 'a'.
    def get_queryset(self):
        return self.queryset

    template_name = 'books/book_list.html'
    # Specify your own template name/location


class BookDetailView(LoginRequiredMixin, generic.DetailView):       # Use this or...
    model = Book
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


@login_required
def book_detail_view(request, primary_key):     # Use this
    try:
        book = Book.objects.get(id=primary_key)
    except Book.DoesNotExist:
        raise Http404('Book does not exist!')

    return render(request, 'catalog/book_detail.html', context={'book': book})


class AuthorListView(LoginRequiredMixin,generic.ListView):
    model = Author
    context_object_name = 'author_list'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    
    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['some_data'] = "This is just some data"
        return context
    
    def get_queryset(self):
        return Author.objects.filter(last_name__startswith = 'A')

    template_name = 'authors/author_list.html'


class AuthorDetailView(LoginRequiredMixin,generic.DetailView):
    model = Author
    login_url = '/login/'
    redirect_field_name = 'redirect_to'



@login_required
def author_detail_view(request, primary_key):
    try:
        author = Author.objects.get(pk=primary_key)
    except Author.DoesNotExist:
        raise Http404('Author does not exist!')

    return render(request, 'catalog/author_detail.html', context={'author': author})


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 2

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


@permission_required('catalog.can_mark_returned')
def all_borrowed_book_list_view(request, primary_key):
    try:
        all_borrowed_book = BookInstance.objects.filter(status__exact='o')
    except BookInstance.DoesNotExist:
        raise Http404('No borrowed books!')
    
    return render(request,'catalog/bookinstance_list_all-borrowed.html', context={'all-borrowed-book':all_borrowed_book})

class AllBorrowedBooksListView(PermissionRequiredMixin,generic.ListView):
    """Generic class-based view listin all borrowed books to the librarian"""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_all_borrowed.html'
    paginate_by = 2
    permission_required = 'catalog.can_mark_returned'

    def get_queryset(self):
        return BookInstance.objects.all().filter(status__exact='o').order_by('due_back')
    


@login_required
@permission_required('catalog.can_mark_returned',raise_exception=True)
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # process the data in form.cleaned_data as required(here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))

    # If this is a GET (or any method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date':proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


# To delete, create and update Authors
class AuthorCreate(CreateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']
    initial = {'date_of_death': '11/06/2020'}


class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__' # Not recommended (potential security issue if more fields added)


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')