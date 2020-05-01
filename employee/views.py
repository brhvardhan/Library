from django.shortcuts import render,redirect
from .forms import AddBookForm
from .models import Books
# Create your views here.

def Index(request):
    if request.user.is_authenticated:
        return render(request,'emp_home.html',context={'user':request.user})
    else:
        return redirect('emploginview')

def AddBookView(request):
    # add_book = AddBookForm()
    # return render(request,'addbook.html',context={'form1':add_book})
    add_book = AddBookForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            user1 = request.user
            bookform = AddBookForm(request.POST)
            # print(bookform['Total_quantity'])
            if bookform.is_valid():
                b = Books(Name=request.POST['Name'],Author=request.POST['Author'],
                    Total_quantity=int(request.POST['Total_quantity']),Stock_quantity=int(request.POST['Total_quantity']))
                b.save()
                message = "Successfully Added"
            else:
                message = "Not added please, please retry"
            return render(request,'addbook.html',context={'user1':user1, 'form1':add_book, 'message':message })
        else:
            return render(request,'addbook.html',context={'form1':add_book})
    
    return redirect('/')

def ShowBookView(request):
    message = None
    if request.GET.get('message'):
        message = request.GET.get('message')
    if request.user.is_authenticated:
        books_all = Books.objects.all()
        # print(books_all[0])
        return render(request,'showbooks.html',context={'books_all':books_all,'fields':Books._meta.get_fields(),'message':message})

    else:
        return redirect('/')

def DeleteBookView(request, id=None):
    if not id:
        return redirect('/emp/showbooks')
    try:
        book = Books.objects.get(id=id)
        book.delete()
        message = "Deleted Book"
    except Exception as e:
        print(e)
        message = "Unable to Delete Book"
    finally:
        return redirect('/emp/showbooks?{}'.format('message='+message))

def Header(request):
    return render(request,'header_emp.html')

def EditBookView(request,id=None):
    if not id:
        return redirect('emp/showbook')
    if request.method == 'GET':
        try:
            book = Books.objects.get(id=id)
            message = None 
        except Exception as e:
            print(e)
            message = "Book do not Exist"
        return render(request,'edit_book.html',context={'message':message,'book':book})
    elif request.method == 'POST':
        # print(dir(Books))
        book = Books.objects.get(id=id)
        book.Name = request.POST['Name']
        book.Author = request.POST['author']
        book.Total_quantity = request.POST['tquantity']
        book.Stock_quantity = request.POST['squantity']
        book.save()
        message = 'Successfully Updated '+book.Name
        print(message)
        return redirect('/emp/showbooks?{}'.format('message='+message))