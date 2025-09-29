from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.middleware.csrf import get_token
from productsApp.models import Product

def product_list(request):
    products = Product.objects.all()
    csrf_token = get_token(request)
    return render(request, "productsApp/products/list.html", {"products": products, "csrf_token": csrf_token})

@require_POST
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    name = request.POST.get("PR_NAME")
    price = request.POST.get("PR_PRICE")
    available = request.POST.get("PR_AVAILABLE")

    errors = {}

    if not name:
        errors["PR_NAME"] = "Name is required."

    try:
        price = float(price)
        if price < 0:
            errors["PR_PRICE"] = "Price must be greater than or equal to 0."
    except (TypeError, ValueError):
        errors["PR_PRICE"] = "Invalid price."

    if available not in ["True", "False"]:
        errors["PR_AVAILABLE"] = "Invalid choice."

    if errors:
        return JsonResponse({"success": False, "errors": errors})

    # Save updated values
    product.PR_NAME = name
    product.PR_PRICE = price
    product.PR_AVAILABLE = (available == "True")
    product.save()

    return JsonResponse(
        {
            "success": True,
            "product": {
                "id": product.id,
                "PR_NAME": product.PR_NAME,
                "PR_PRICE": str(product.PR_PRICE),
                "PR_AVAILABLE": product.PR_AVAILABLE,
            },
        }
    )




















# """Views for listing and updating products via AJAX."""
# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST
# from django.middleware.csrf import get_token
# from productsApp.models import Product
# from .forms import ProductForm


# def product_list(request):
#     """Render table of products with CSRF token in template."""
#     products = Product.objects.all()
#     csrf_token = get_token(request)  # send CSRF for JS fetch
#     return render(request, "productsApp/products/list.html", {"products": products, "csrf_token": csrf_token})


# @require_POST
# def update_product(request, pk):
#     """Handle AJAX inline update."""
#     product = get_object_or_404(Product, pk=pk)
#     form = ProductForm(request.POST, instance=product)
#     if form.is_valid():
#         form.save()
#         return JsonResponse(
#             {
#                 "success": True,
#                 "product": {
#                     "id": product.id,
#                     "name": product.PR_NAME,
#                     "price": str(product.PR_PRICE),
#                     "available": product.PR_AVAILABLE,
#                 },
#             }
#         )
#     else:
#         return JsonResponse({"success": False, "errors": form.errors})
