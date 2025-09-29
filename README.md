# InlineEditProject


A small Django app demonstrating 'inline editing of products' with AJAX, CSRF protection, server-side validation, and a search/filter box via DataTables.

---

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

---

# Setup & Run Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/InlineEditProject.git
   cd InlineEditProject
