// Store student IDs for JavaScript use
var studentIds = [];

function updatePercentage(studentId) {
    var totalInput = document.getElementById('total_' + studentId);
    var attendedInput = document.getElementById('attended_' + studentId);
    var previewSpan = document.getElementById('percent_preview_' + studentId);
    
    var total = parseInt(totalInput.value) || 0;
    var attended = parseInt(attendedInput.value) || 0;
    
    if (total > 0) {
        var percentage = Math.round((attended / total) * 100 * 100) / 100;
        previewSpan.textContent = percentage + '%';
        
        if (percentage < 75) {
            previewSpan.style.color = 'red';
        } else {
            previewSpan.style.color = 'green';
        }
    } else {
        previewSpan.textContent = '';
    }
}

// Update current attendance when subject is selected
function initializeAttendanceForm() {
    var subjectSelect = document.getElementById('subject');
    if (subjectSelect) {
        subjectSelect.addEventListener('change', function() {
            var subjectId = this.value;
            if (subjectId) {
                // This would typically fetch current attendance data via AJAX
                // For now, we'll just show placeholder data
                for (var i = 0; i < studentIds.length; i++) {
                    var studentId = studentIds[i];
                    var currentTotal = document.getElementById('current_total_' + studentId);
                    var currentAttended = document.getElementById('current_attended_' + studentId);
                    var currentPercent = document.getElementById('current_percent_' + studentId);
                    
                    if (currentTotal) currentTotal.textContent = '0';
                    if (currentAttended) currentAttended.textContent = '0';
                    if (currentPercent) currentPercent.textContent = '0%';
                }
            }
        });
    }
    
    // Add event listeners for attendance inputs
    var attendanceInputs = document.querySelectorAll('.attendance-input');
    attendanceInputs.forEach(function(input) {
        input.addEventListener('input', function() {
            var studentId = this.getAttribute('data-student-id');
            if (studentId) {
                updatePercentage(parseInt(studentId));
            }
        });
    });
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeAttendanceForm();
}); 