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
        $("#id").text(data.data.id);
        $("#temperature").text(data.data.temperature);
        $("#light").text(data.data.light);
        $("#humidity").text(data.data.humidity);
        $("#heat_index").text(data.data.heat_index);
        $("#ground_temperature").text(data.data.ground_temperature);
        $("#timestamp").text(data.data.timestamp);
        $("#microcontroller_id").text(data.data.microcontroller_id);
        $("#microcontroller_user_id").text(data.data.microcontroller_user_id);
      },
    });
  }
});
