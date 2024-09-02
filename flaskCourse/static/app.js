document.getElementById('splash_art').addEventListener('change', function(e){
  const file = this.files[0];
  if (file.type && file.type == 'image/jpeg' || file.type == 'image/png') {
    const reader = new FileReader();
    reader.onload = function(e) {
      const img = document.getElementById('splash_art_preview');
      img.src = e.target.result;
    }
    reader.readAsDataURL(file);
  }
})