// Get references to the boardslist element
var boardslist = document.getElementById("boardslist");
var boarddisplay = document.getElementById("boarddisplay");

// Define URLs

// Fetch the boards list on page load

boarddisplay.addEventListener("click", function () {
  fetchBoards(boards_url);
});

function fetchBoards(boards_url) {
  fetch(boards_url)
    .then((response) => response.text())
    .then((html) => {
      boardslist.innerHTML = html;
      boardslist.style.display = "block";
    })
    .catch((error) => console.error("Error fetching boards:", error));
}

// Get reference to the fetch create board form button
let fetchCreateBoardFormButton = document.getElementById(
  "fetchCreateBoardForm"
);
// Add event listener to the fetch create board form button
fetchCreateBoardFormButton.addEventListener("click", function (event) {
  event.preventDefault(); // Prevent default behavior of button click

  fetch(createboardurl)
    .then((response) => response.text())
    .then((html) => {
      let createboard = document.getElementById("createboard");
      createboard.innerHTML = html;
      createboard.style.display = "block";

      // Set the action attribute of the form to point to the create_board URL
      let createBoardForm = createboard.querySelector("form");
      createBoardForm.setAttribute("action", createboardurl);
    })
    .catch((error) =>
      console.error("Error fetching create board form:", error)
    );
});

// For fecting the images and displaying on home page

// Fetch and display images on the home page
function fetchAndDisplayImages(imagesUrl) {
  fetch(imagesUrl)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      console.log(data);
      const container = document.querySelector(".container");
      data.images.forEach((image) => {
        const box = document.createElement("div");
        box.classList.add("box");

        const anchor = document.createElement("a");
        anchor.href = `posts/post/${image.pk}/`; // Assuming you have a URL pattern for post_detail view

        const img = document.createElement("img");
        img.src = image.url; // Using image URL from the response
        img.alt = `Image ${image.pk}`; // Using image primary key for alt text

        anchor.appendChild(img);
        box.appendChild(anchor);
        container.appendChild(box);
      });
    })
    .catch((error) => console.error("Error fetching images:", error));
}

// Call the function to fetch and display images on page load
fetchAndDisplayImages(imagesurl);

// sidebar event
document.getElementById("toggling").addEventListener("click", () => {
  event.preventDefault();
  document.getElementById("sideone").style.display =
    document.getElementById("sideone").style.display === "block"
      ? "none"
      : "block";
});
