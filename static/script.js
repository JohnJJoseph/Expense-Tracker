document.addEventListener('DOMContentLoaded', function() {
    // Form validation for adding a category
    const categoryForm = document.getElementById('categoryForm');
    if (categoryForm) {
        categoryForm.addEventListener('submit', function(event) {
            const nameInput = document.getElementById('name');
            const descriptionInput = document.getElementById('description');
            
            if (!nameInput.value.trim()) {
                alert('Please enter a category name.');
                event.preventDefault();
            } else if (!descriptionInput.value.trim()) {
                alert('Please enter a description.');
                event.preventDefault();
            }
        });
    }

    // Form validation for adding an expense
    const expenseForm = document.getElementById('expenseForm');
    if (expenseForm) {
        expenseForm.addEventListener('submit', function(event) {
            const amountInput = document.getElementById('amount');
            
            if (!amountInput.value.trim()) {
                alert('Please enter an amount.');
                event.preventDefault();
            } else if (isNaN(parseFloat(amountInput.value))) {
                alert('Please enter a valid numeric amount.');
                event.preventDefault();
            }
        });
    }
});
