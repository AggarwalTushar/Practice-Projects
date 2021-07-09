let likeBtn = document.getElementById("likeBtn");
let dislikeBtn = document.getElementById("dislikeBtn");
let commentButton = document.getElementById("commentBtn");
let likedBtn = document.getElementById("liked");
let dislikedBtn = document.getElementById("disliked");

let showCommentCheckbox = document.getElementById("flexSwitchCheckChecked");
let showCommentBoxContainer = document.getElementById("comment-box-section");
let insideCommentBoxContainer = document.getElementById("inside-comment-box-section");
let commentForm = document.getElementById("comment-form");
let commentName = document.getElementById("name");
let commentText = document.getElementById("comment-box");
let commentWarning = document.getElementById("comment-warning");
let nameWarning = document.getElementById("name-warning");
let commentCounter = document.getElementById("commentCounter");
let counter = 4;
let ord = 0;

//Like and dislike
likeBtn.addEventListener("click", function(event) {
    likeBtn.classList.toggle("d-none");
    likedBtn.classList.toggle("d-none");
    dislikeBtn.classList.remove("d-none");
    dislikedBtn.classList.add("d-none");
});

likedBtn.addEventListener("click", function(event) {
    likeBtn.classList.toggle("d-none");
    likedBtn.classList.toggle("d-none");
});

dislikeBtn.addEventListener("click", function(event) {
    dislikeBtn.classList.toggle("d-none");
    dislikedBtn.classList.toggle("d-none");
    likedBtn.classList.add("d-none");
    likeBtn.classList.remove("d-none");
});

dislikedBtn.addEventListener("click", function(event) {
    dislikeBtn.classList.toggle("d-none");
    dislikedBtn.classList.toggle("d-none");
});


// Show Comment Method
showCommentCheckbox.addEventListener("click", function(event) {
    showCommentBoxContainer.classList.toggle("d-none");
});


