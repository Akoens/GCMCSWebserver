$(document).ready(function () {
  window.setInterval(function () {
    loadLatestResults();
  }, 5000);

  function loadLatestResults() {
    $.ajax({
      url: "/api/receive",
      type: "POST",
      cache: false,
      success: function (data) {
        $("#ldr").text(data.data.ldr);
        $("#tmp").text(data.data.tmp);
        $("#dht").text(data.data.dht);
        $("#ds20b18").text(data.data.ds20b18);

      },
    });
  }
});
