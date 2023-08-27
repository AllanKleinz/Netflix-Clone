const videoEl = document.querySelector('video');
const movie_data = JSON.parse(document.getElementById('movie_data').textContent);
const url = new URL(location.href);
const video_param = parseInt(url.searchParams.get('epi')) || 0;  // Use || instead of ?:
videoEl.setAttribute('src', `http://localhost:8000/media/${movie_data[video_param].file}`);