import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Book
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

@login_required
@require_http_methods(["GET", "POST"])
def list_or_add_books(request):
    if request.method == 'GET':
        response = []
        books = Book.objects.all()
        for book in books:
            response.append(
                {
                    "title": book.title,
                    "author": book.author,
                    "status": book.status,
                    "id": book.id
                }
            )
        return JsonResponse({
            "books": response
        })
    else:
        content = json.loads(request.body)
        user = request.user
        content["user"] = user
        book = Book.objects.create(**content)
        return JsonResponse({
            "title": book.title,
            "author": book.author,
            "status": book.status,
            "id": book.id
        })


@login_required
@require_http_methods(["GET", "DELETE", "PUT"])
def show_delete_edit_book(request, id):
    if request.method == 'GET':
        book = Book. objects.get(id=id)
        return JsonResponse({
            "title": book.title,
            "author": book.author,
            "status": book.status,
            "description": book.description,
            "genre": book.genre
        })
    elif request.method == 'DELETE':
        count, _ = Book.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)

        Book.objects.filter(id=id).update(**content)
        book = Book.objects.get(id=id)

        return JsonResponse({
            "title": book.title,
            "author": book.author,
            "status": book.status
        })
