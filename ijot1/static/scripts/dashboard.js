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

const getNotes = (e) => {
	console.log(e.target.id);
	fetch('/note', {body: JSON.stringify({id: e.target.id}), method: 'POST', header: {'Content-Type': 'application/json'}}).catch((err) => console.log(err));
}