// Automatically hide flash messages after 3 seconds
document.addEventListener('DOMContentLoaded', () => {
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(msg => {
        setTimeout(() => {
            msg.style.display = 'none';
        }, 3000); // 3 seconds
    });
});

// Optional: Prevent negative input values in attendance form
document.addEventListener('input', function (e) {
    if (e.target.type === 'number') {
        if (parseInt(e.target.value) < 0) {
            e.target.value = 0;
        }
    }
});

// Copy week total classes to all rows
document.addEventListener('DOMContentLoaded', function() {
    const totalClassInputs = document.querySelectorAll('input[id^="total_"]');
    
    totalClassInputs.forEach(input => {
        input.addEventListener('input', function() {
            const value = this.value;
            if (value && value > 0) {
                // Copy to all other total class inputs
                totalClassInputs.forEach(otherInput => {
                    if (otherInput !== this) {
                        otherInput.value = value;
                        // Trigger percentage update for the other row
                        const studentId = otherInput.id.replace('total_', '');
                        updatePercentage(studentId);
                    }
                });
                
                // Update percentage for current row
                const currentStudentId = this.id.replace('total_', '');
                updatePercentage(currentStudentId);
            }
        });
    });
    
    // Clear form when subject changes
    const subjectSelect = document.getElementById('subject');
    if (subjectSelect) {
        subjectSelect.addEventListener('change', function() {
            // Clear all attendance inputs
            const attendanceInputs = document.querySelectorAll('input[id^="total_"], input[id^="attended_"]');
            attendanceInputs.forEach(input => {
                input.value = '';
            });
            
            // Clear all percentage previews
            const percentagePreviews = document.querySelectorAll('[id^="percent_preview_"]');
            percentagePreviews.forEach(preview => {
                preview.textContent = '';
            });
            
            // Clear week number if subject is deselected
            if (!this.value) {
                const weekInput = document.getElementById('week');
                if (weekInput) {
                    weekInput.value = '';
                }
            }
        });
    }
    
    // Disable number input arrows and enable row navigation
    const attendanceInputs = document.querySelectorAll('input[id^="total_"], input[id^="attended_"]');
    attendanceInputs.forEach(input => {
        // Disable default number input arrow behavior
        input.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowUp' || e.key === 'ArrowDown') {
                e.preventDefault();
                
                // Find current row
                const currentRow = this.closest('tr');
                const currentInputs = currentRow.querySelectorAll('input[id^="total_"], input[id^="attended_"]');
                const currentIndex = Array.from(currentInputs).indexOf(this);
                
                // Find all rows
                const allRows = document.querySelectorAll('tbody tr');
                const currentRowIndex = Array.from(allRows).indexOf(currentRow);
                
                let targetRow, targetInput;
                
                if (e.key === 'ArrowUp') {
                    // Move to previous row
                    if (currentRowIndex > 0) {
                        targetRow = allRows[currentRowIndex - 1];
                        targetInput = targetRow.querySelectorAll('input[id^="total_"], input[id^="attended_"]')[currentIndex];
                    }
                } else if (e.key === 'ArrowDown') {
                    // Move to next row
                    if (currentRowIndex < allRows.length - 1) {
                        targetRow = allRows[currentRowIndex + 1];
                        targetInput = targetRow.querySelectorAll('input[id^="total_"], input[id^="attended_"]')[currentIndex];
                    }
                }
                
                // Focus on target input if found
                if (targetInput) {
                    targetInput.focus();
                    targetInput.select();
                }
            }
        });
        
        // Also handle left/right arrow keys for column navigation
        input.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
                e.preventDefault();
                
                // Find current row
                const currentRow = this.closest('tr');
                const currentInputs = currentRow.querySelectorAll('input[id^="total_"], input[id^="attended_"]');
                const currentIndex = Array.from(currentInputs).indexOf(this);
                
                let targetInput;
                
                if (e.key === 'ArrowLeft') {
                    // Move to previous column
                    if (currentIndex > 0) {
                        targetInput = currentInputs[currentIndex - 1];
                    }
                } else if (e.key === 'ArrowRight') {
                    // Move to next column
                    if (currentIndex < currentInputs.length - 1) {
                        targetInput = currentInputs[currentIndex + 1];
                    }
                }
                
                // Focus on target input if found
                if (targetInput) {
                    targetInput.focus();
                    targetInput.select();
                }
            }
        });
    });
});

// Optional: Real-time percentage preview (if you implement it in update form)
function updatePercentage(studentId) {
    const total = parseInt(document.getElementById(`total_${studentId}`).value) || 0;
    const attended = parseInt(document.getElementById(`attended_${studentId}`).value) || 0;
    const preview = document.getElementById(`percent_preview_${studentId}`);

    if (total > 0 && attended >= 0) {
        const percent = ((attended / total) * 100).toFixed(2);
        preview.textContent = `(${percent}%)`;
    } else {
        preview.textContent = '';
    }
}

// Show/hide password toggle for login page
if (document.getElementById('show-password')) {
    document.getElementById('show-password').addEventListener('change', function() {
        const pwd = document.getElementById('password');
        if (this.checked) {
            pwd.type = 'text';
        } else {
            pwd.type = 'password';
        }
    });
}
