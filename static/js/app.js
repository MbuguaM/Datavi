
down vote
accepted
Resolved inserting a script tag in the html with the javascript function as follow

  <script>
  function respScreen() {
      var x = document.getElementById("navbar");
      if (x.className === "new") {
          x.className += " responsive";
      } else {
          x.className = "new";
      }
  }
  </script>
