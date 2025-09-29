# InlineEditProject

A small Django app demonstrating 'inline editing of products' with AJAX, CSRF protection, server-side validation, and a search/filter box via DataTables.


## Features

**Implemented (Hard Requirements)**

- One model: 'Product' with fields:
  - `PR_NAME` (Text)
  - `PR_PRICE` (Decimal ≥ 0)
  - `PR_AVAILABLE` (Boolean)
- Table view listing products (3 sample records)
- Inline editing of a single row
- AJAX-based save (no page reload)
- Server-side validation with inline error display
- CSRF handled correctly for AJAX
- Search/filter box above the table (via DataTables)
- Basic Bootstrap styling

**Nice-to-have (Optional)**

- Simple auth / identify by email  ❌ 
- Django Admin enabled  ✅ 
- Guard against double-click/double-submit on Save ❌
- Unit tests for update view/validation  ❌ 
- Docker / Docker Compose  ❌ 


# InlineEditProject

A small Django app demonstrating **inline editing of products** with AJAX, CSRF protection, server-side validation, and a search/filter box via DataTables.

---

## Features

### Implemented (Hard Requirements)

* One model: `Product` with fields:

  * `PR_NAME` (Text)
  * `PR_PRICE` (Decimal ≥ 0)
  * `PR_AVAILABLE` (Boolean)
* Table view listing products (3 sample records)
* Inline editing of a single row
* AJAX-based save (no page reload)
* Server-side validation with inline error display
* CSRF handled correctly for AJAX
* Search/filter box above the table (via DataTables)
* Basic Bootstrap styling

### Nice-to-have (Optional)

* Simple auth / identify by email ❌
* Django Admin enabled ✅
* Guard against double-click/double-submit on Save ❌
* Unit tests for update view/validation ❌
* Docker / Docker Compose ❌


## Setup & Run Instructions

1. **Clone the repo**


   git clone https://github.com/Samiksha1706/InlineEditProject.git
   cd InlineEditProject


2. **Create and activate a virtual environment**

   python -m venv env
   source env/bin/activate   # On Mac/Linux
   env\Scripts\activate      # On Windows
   

3. **Install dependencies**

   pip install -r requirements.txt
 

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Insert sample data (via Django shell)**

   python manage.py shell
   
   from productsApp.models import Product

   Product.objects.create(PR_NAME="Laptop", PR_PRICE=50000, PR_AVAILABLE=True)
   Product.objects.create(PR_NAME="Phone", PR_PRICE=20000, PR_AVAILABLE=True)
   Product.objects.create(PR_NAME="Headphones", PR_PRICE=2000, PR_AVAILABLE=False)
   
   exit()

6. **Run the development server**

   python manage.py runserver
  

7. **Access the app in browser**

   * Root: http://127.0.0.1:8000/


## AJAX + CSRF + Validation Handling

* **AJAX**: Implemented via jQuery `$.ajax()` for updating rows.
* **CSRF**: Token is injected into AJAX headers via Django template tag `{% csrf_token %}`.
* **Validation**: On server-side in Django view; if invalid, JSON response contains error messages that display inline in the table row.


