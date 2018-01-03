
function handleClicks() {
  var clickCount = 0;

  // this line sets the inner text
  $('.js-click-counter').text(clickCount);

  // this line says when the
  // `.js-clicker` element is
  // clicked, run the instructions
  // inside the anonymous function
  // (that is, the instructions
  // between the {...} brackets).
  $('.js-clicker').click(function(event) {

    // any time the user clicks,
    // we add 1 to the value of
    // `clickCount ...
    clickCount += 1;

    // ...and display the updated
   // click count in the
   // `.js-click-count` element.
   $('.js-click-counter').text(clickCount);
 });
}

// this code just says that when
// the browser is done loading the
// page, it should run the
// `handleClicks` function
// we've defined above.
$(handleClicks);
