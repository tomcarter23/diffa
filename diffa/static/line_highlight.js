document.addEventListener('DOMContentLoaded', () => {
	let rows = document.querySelectorAll('.diff_content');
	rows.forEach(row => {
		row.addEventListener('mouseover', () => {
			row.classList.add('highlight');
		});
		row.addEventListener('mouseout', () => {
			row.classList.remove('highlight');
		});
	});
});
