var ids = ["Lname", "Tname", "Title", "stack", "Theme", "Achievement", "desc"];
for (key in ids) {
  
  document.getElementById(ids[key]).disabled = true;
}

function unlock() {
    for (key in ids) {
        
        document.getElementById(ids[key]).disabled = false;
  }
}