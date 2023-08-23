document.addEventListener("DOMContentLoaded", function() {
  var btnScrollDown = document.getElementById("btnScrollDown");

  btnScrollDown.addEventListener("click", function() {
    var currentPosition = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
    var targetPosition = document.body.scrollHeight;

    var animationInterval = 10; // O intervalo de tempo entre cada quadro da animação (em milissegundos)
    var scrollDistance = (targetPosition - currentPosition) / (1000 / animationInterval); // A distância a ser percorrida a cada quadro

    var scrollInterval = setInterval(function() {
      var newPosition = Math.min(currentPosition + scrollDistance, targetPosition);
      window.scrollTo(0, newPosition);
      currentPosition = newPosition;

      if (currentPosition >= targetPosition) {
        clearInterval(scrollInterval);
      }
    }, animationInterval);
  });
});