
function changeIndex(offset) {
    // Access the current_index value from the hidden input
    var current_index = parseInt(document.getElementById('current_index').value);
    
    // Calculate the new index
    var newIndex = current_index + offset;

    // Ensure the index stays within the valid range
    if (newIndex >= 0 && newIndex < diary_pages.length) {
        current_index = newIndex;

        // Update the content on the page
        document.querySelector('h3').innerText = diary_pages[current_index].title;
        document.querySelector('#category').innerText = diary_pages[current_index].category;
        document.querySelector('#date').innerText = diary_pages[current_index].date;
        document.querySelector('#content').innerText = diary_pages[current_index].content;

        // Update the hidden input with the new index value
        document.getElementById('current_index').value = current_index;
    }
}