document.addEventListener('DOMContentLoaded', function() {
    let checkboxes = document.querySelectorAll('.service-checkbox');
    let deleteButton = document.getElementById('btn-item-delete');
    let notifyButton = document.getElementById('btn-item-notify')

    function isAnyCheckboxChecked() {
        return Array.from(checkboxes).some(checkbox => checkbox.checked);
    }

    function updateDeleteButton() {
        deleteButton.disabled = !isAnyCheckboxChecked();
        notifyButton.disabled = !isAnyCheckboxChecked();
    }

    function handleDeleteButtonClick(event) {
        if (!isAnyCheckboxChecked()) {
            alert('Please select at least one item before deleting.');
            event.preventDefault();
        } else if (!confirm('Are you sure you want to delete the selected service(s)?')) {
            event.preventDefault();
        }
    }

    function handleNotifyButtonClick(event) {
        if (!isAnyCheckboxChecked()) {
            alert('Please select at least one item before notifying.');
            event.preventDefault();
        } else if (!confirm('Are you sure you want to notify the selected service(s)?')) {
            event.preventDefault();
        }
    }

    function attachEventListeners() {
        deleteButton.addEventListener('click', handleDeleteButtonClick);
        notifyButton.addEventListener('click', handleNotifyButtonClick);

        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', updateDeleteButton);
        });
    }

    // Initialize
    updateDeleteButton();
    attachEventListeners();
});
