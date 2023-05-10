// Bind events to buttons
document.getElementById('translate_button').onclick = process_translation;
document.getElementById('random_text_button').onclick = random_text;
document.getElementById('random_language_button').onclick = random_language;

// Get the text element and the language element
let text_element = document.getElementById('source_text');
let language_element = document.getElementById('target_language');

// Check if input string is null or empty or whitespace(s)
function isNullOrEmpty(str) {
    return str == null || str.trim() === '';
}

// Cancel submission if either the text or the language is empty
function process_translation() {
    if (isNullOrEmpty(language_element.value) || isNullOrEmpty(text_element.value)) {
        document.getElementById('result').innerHTML = '<h3>Text and language cannot be empty</h3>';
        document.getElementById('result').style.visibility = 'visible';
        return false;
    } else {
        document.getElementById('result').innerHTML = '<h3>Generating Translation...</h3>';
        document.getElementById('result').style.visibility = 'visible';
        return true;
    }
}

// Get a random line from the text file at the given file path
async function get_random_line(path) {
    try {
        const response = await fetch(path);
        const text = await response.text();
        const lines = text.split('\r\n');
        return lines[Math.floor(Math.random() * lines.length)];
    } catch (err) {
        console.error(err);
    }
}

// Fill in a random quote into the text field
async function random_text() {
    text_element.value = await get_random_line('static/res/quotes.txt');
}

// Fill in a random langauge into the language field
async function random_language() {
    language_element.value = await get_random_line('static/res/languages.txt');
}
