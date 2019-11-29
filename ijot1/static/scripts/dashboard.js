const newNoteBtn = document.getElementById('add-btn')
const container = document.getElementById('container')

// EVent listener
newNoteBtn.addEventListener('click',() =>
container.classList.add('note-panel-active'));

const noteNextbtn = document.getElementById('next-note-btn')
const noteform = document.getElementById('note-form')

// Event listener 
noteNextbtn.addEventListener('click',() => 
noteform.classList.add('note-field-active'));

