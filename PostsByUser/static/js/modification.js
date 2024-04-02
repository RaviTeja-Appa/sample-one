var toggleButton = document.getElementById("toggleButton");
var container = document.getElementById("container");
var emptybox = document.getElementById("emptybox");
toggleButton.addEventListener("click", function () {
  if (container.style.display === "none") {
    container.style.display = "block";
    emptybox.style.display = "none";
    container.style.opacity = 1; // Show the container
  } else {
    container.style.display = "none";
    emptybox.style.display = "block";
    // Hide the container
  }
});

document.getElementById("commentholder").addEventListener("input", (event) => {
  const input = event.target;
  var comment = document.getElementById("maindiv");
  const form = document.getElementById("commentForm"); // Corrected form ID
  const send = document.getElementById("send-comment");
  if (input.value.trim() !== "") {
    form.style.backgroundColor = "white"; // Apply background color to the form instead of 'form'
    document.getElementById("commentholder").style.width = "95%";
    send.style.display = "block";
    comment.style.backgroundColor = "white";
    comment.style.border = "1px solid #c9c9c9";
    input.style.backgroundColor = "white"; // Change background color if input has value
  } else {
    comment.style.backgroundColor = "#e9e9e9";
    comment.style.border = "none";
    form.style.backgroundColor = "transparent"; // Reset form background color
    document.getElementById("commentholder").style.width = "100%";
    send.style.display = "none";
    // Reset background color if input is empty
  }
});

var like = document.getElementById("love"); // Assuming the element has ID "love"

like.addEventListener("click", function (event) {
  // Use a more robust color comparison function
  function colorMatches(expectedColor) {
    const computedStyle = window.getComputedStyle(like);
    const actualColor = computedStyle.backgroundColor;
    return actualColor.toLowerCase() === expectedColor.toLowerCase();
  }

  const defaultColor = "rgb(233, 233, 233)"; // Use a consistent format
  const likedColor = "rgba(255, 224, 224, 1)";

  if (colorMatches(defaultColor)) {
    like.style.backgroundColor = likedColor;
    like.style.color = "red";
  } else {
    like.style.backgroundColor = defaultColor;
    like.color = "black";
  }

  // Prevent default form submission behavior (if desired)
  // event.preventDefault();

  // Submit the form using the form's submit() method
  // You might need to adjust the form element selector if it has a different ID
  const form = document.getElementById("likeform");
  form.submit();
});

document
  .getElementById("send-comment")
  .addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default form submission behavior
    document.getElementById("commentForm").submit(); // Submit the form
  });

// follow unfollowing the persons
// Follow/unfollow functionality
document.addEventListener("DOMContentLoaded", function () {
  var unfollow = document.getElementById("unfollow");
  if (unfollow) {
    document.getElementById("unfollow").addEventListener("click", (event) => {
      event.preventDefault();
      console.log("clicked unfollow");
      document.getElementById("unfollower").submit();
    });
  } else {
    document.getElementById("follow").addEventListener("click", (event) => {
      event.preventDefault();
      console.log("clicked follow");
      document.getElementById("follower").submit();
    });
  }
});

// toggling the content

document.getElementById("toggling").addEventListener("click", (event) => {
  event.preventDefault();
  document.getElementById("sideone").style.display =
    document.getElementById("sideone").style.display === "block"
      ? "none"
      : "block";
});
