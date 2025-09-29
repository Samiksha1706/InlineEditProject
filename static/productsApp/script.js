$(document).ready(function () {
  // Initialize DataTable
  $("#products-table").DataTable({
  });

  // Enable editing
  $(document).on("click", ".edit-btn", function () {
    const row = $(this).closest("tr");

    const name = row.find(".PR_NAME").text().trim();
    const price = row.find(".PR_PRICE").text().trim();
    const available = row.find(".PR_AVAILABLE").text().trim() === "✅";

    // Store old values for cancel
    row.data("old-name", name);
    row.data("old-price", price);
    row.data("old-available", available ? "True" : "False");

    // Replace with inputs
    row.find(".PR_NAME").html(
      `<input type="text" class="form-control" name="PR_NAME" value="${name}">`
    );
    row.find(".PR_PRICE").html(
      `<input type="number" class="form-control" step="0.01" name="PR_PRICE" value="${price}">`
    );
    row.find(".PR_AVAILABLE").html(`
      <select class="form-select" name="PR_AVAILABLE">
        <option value="">Select</option>
        <option value="True" ${available ? "selected" : ""}>Yes</option>
        <option value="False" ${!available ? "selected" : ""}>No</option>
      </select>
    `);

    row.find(".edit-btn").addClass("d-none");
    row.find(".save-btn, .cancel-btn").removeClass("d-none");
  });

  // Cancel editing
  $(document).on("click", ".cancel-btn", function () {
    const row = $(this).closest("tr");

    const oldName = row.data("old-name");
    const oldPrice = row.data("old-price");
    const oldAvailable = row.data("old-available");

    row.find(".PR_NAME").text(oldName);
    row.find(".PR_PRICE").text(oldPrice);
    row.find(".PR_AVAILABLE").html(oldAvailable === "True" ? "✅" : "❌");

    row.find(".save-btn, .cancel-btn").addClass("d-none");
    row.find(".edit-btn").removeClass("d-none");
  });

  // Save via AJAX
  $(document).on("click", ".save-btn", function () {
    const row = $(this).closest("tr");
    const productId = row.data("id");

    const data = {
      PR_NAME: row.find('input[name="PR_NAME"]').val(),
      PR_PRICE: row.find('input[name="PR_PRICE"]').val(),
      PR_AVAILABLE: row.find('select[name="PR_AVAILABLE"]').val(),
      csrfmiddlewaretoken: window.CSRF_TOKEN, // CSRF token global 
    };

    $.ajax({
      url: `/update/${productId}/`,
      type: "POST",
      data: data,
      success: function (response) {
        row.find(".error-msg").remove();

        if (response.success) {
          row.find(".PR_NAME").text(response.product.PR_NAME);
          row.find(".PR_PRICE").text(response.product.PR_PRICE);
          row.find(".PR_AVAILABLE").html(
            response.product.PR_AVAILABLE ? "✅" : "❌"
          );

          row.find(".save-btn, .cancel-btn").addClass("d-none");
          row.find(".edit-btn").removeClass("d-none");
        } else {
          for (let field in response.errors) {
            const msg = `<div class="text-danger error-msg small">${response.errors[field]}</div>`;
            row.find(`[name='${field}']`).after(msg);
          }
        }
      },
      error: function () {
        alert("Something went wrong while saving.");
      },
    });
  });
});
