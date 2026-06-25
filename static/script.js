const dropzone = document.getElementById('dropzone');
const fileInput = document.getElementById('image-input');
const uploadForm = document.getElementById('upload-form');
const loader = document.getElementById('loader');
const uploadContent = document.getElementById('upload-content');
const localPreviewContainer = document.getElementById('local-preview-container');
const localPreviewImg = document.getElementById('local-preview-img');
const removeImgBtn = document.getElementById('remove-img-btn');
const submitBtn = document.getElementById('submit-btn');
const columnRight = document.getElementById('column-right');

// Drag and drop styles
['dragenter', 'dragover'].forEach(eventName => {
  dropzone.addEventListener(eventName, (e) => {
    e.preventDefault();
    dropzone.classList.add('dragover');
  }, false);
});

['dragleave', 'drop'].forEach(eventName => {
  dropzone.addEventListener(eventName, (e) => {
    e.preventDefault();
    dropzone.classList.remove('dragover');
  }, false);
});

// Handle file drop manually to show local preview
dropzone.addEventListener('drop', (e) => {
  const dt = e.dataTransfer;
  const files = dt.files;
  if (files.length > 0) {
    fileInput.files = files;
    handleFileSelect(files[0]);
  }
}, false);

// Show loader on form submission
uploadForm.addEventListener('submit', () => {
  loader.style.display = 'flex';
});

// Local preview handler
function handleFileSelect(file) {
  if (file) {
    const reader = new FileReader();
    reader.onload = function(e) {
      localPreviewImg.src = e.target.result;
      uploadContent.style.display = 'none';
      localPreviewContainer.style.display = 'flex';
      fileInput.removeAttribute('required');
      
      // Enable analyze button
      submitBtn.disabled = false;
      submitBtn.style.opacity = '1';
      submitBtn.style.cursor = 'pointer';
    }
    reader.readAsDataURL(file);
  }
}

// Input change listener (triggers preview instead of submission)
fileInput.addEventListener('change', () => {
  if(fileInput.files.length > 0) {
    handleFileSelect(fileInput.files[0]);
  }
});

// Remove image handler
removeImgBtn.addEventListener('click', (e) => {
  e.preventDefault();
  e.stopPropagation(); // Prevent file upload dialog from opening
  
  fileInput.value = '';
  localPreviewImg.src = '';
  localPreviewContainer.style.display = 'none';
  uploadContent.style.display = 'flex';
  fileInput.setAttribute('required', 'true');
  
  // Disable analyze button
  submitBtn.disabled = true;
  submitBtn.style.opacity = '0.6';
  submitBtn.style.cursor = 'not-allowed';

  // Revert right side to awaiting state
  columnRight.innerHTML = `
    <div class="placeholder-card" id="report-placeholder">
      <div class="placeholder-icon">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
          <polyline points="14 2 14 8 20 8"></polyline>
          <line x1="16" y1="13" x2="8" y2="13"></line>
          <line x1="16" y1="17" x2="8" y2="17"></line>
          <polyline points="10 9 9 9 8 9"></polyline>
        </svg>
      </div>
      <h3>Awaiting Analysis</h3>
      <p>Upload a skin lesion image on the left and click <strong>Analyze Lesion</strong> to generate a diagnostic report.</p>
    </div>
  `;
});
