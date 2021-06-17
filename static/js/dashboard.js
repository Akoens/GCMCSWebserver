$(document).ready(function () {
  const container = document.querySelector(".live-data");

  const humidity_dougnut = document.getElementById("humidity_dougnut");
  const humidity_dougnut_ctx = humidity_dougnut.getContext("2d");
  const humidity_dougnut_chart = new Chart(humidity_dougnut_ctx, {
    type: "doughnut",
    responsive: true,
    animation: {
      animateScale: true,
      animateRotate: true,
    },
  });

  const moisture_dougnut = document.getElementById("moisture_dougnut");
  const moisture_dougnut_ctx = moisture_dougnut.getContext("2d");
  const moisture_dougnut_chart = new Chart(moisture_dougnut_ctx, {
    type: "doughnut",
    responsive: true,
    animation: {
      animateScale: true,
      animateRotate: true,
    },
  });

  const temperature_line = document.getElementById("temperature_line");
  const temperature_line_ctx = temperature_line.getContext("2d");
  const temperature_line_chart = new Chart(temperature_line_ctx, {
    type: "line",
    responsive: true,
    animation: {
      animateScale: true,
      animateRotate: true,
    },
    options: {
      scales: {
        y: {
          ticks: {
            callback: function (value, index, values) {
              return value + " °C";
            },
          },
        },
        x: {
          reverse: true,
        },
      },
    },
  });

  const light_line = document.getElementById("light_line");
  const light_line_ctx = light_line.getContext("2d");
  const light_line_chart = new Chart(light_line_ctx, {
    type: "line",
    responsive: true,
    animation: {
      animateScale: true,
      animateRotate: true,
    },
    options: {
      scales: {
        y: {
          ticks: {
            callback: function (value, index, values) {
              return value + " Lux";
            },
          },
        },
        x: {
          reverse: true,
        },
      },
    },
  });

  const humidity_line = document.getElementById("humidity_line");
  const humidity_line_ctx = humidity_line.getContext("2d");
  const humidity_line_chart = new Chart(humidity_line_ctx, {
    type: "line",
    responsive: true,
    animation: {
      animateScale: true,
      animateRotate: true,
    },
    options: {
      scales: {
        y: {
          ticks: {
            callback: function (value, index, values) {
              return value + " %";
            },
          },
        },
        x: {
          reverse: true,
        },
      },
    },
  });

  const heat_index_line = document.getElementById("heat_index_line");
  const heat_index_line_ctx = heat_index_line.getContext("2d");
  const heat_index_line_chart = new Chart(heat_index_line_ctx, {
    type: "line",
    responsive: true,
    animation: {
      animateScale: true,
      animateRotate: true,
    },
    options: {
      scales: {
        y: {
          ticks: {
            callback: function (value, index, values) {
              return value + " °C";
            },
          },
        },
        x: {
          reverse: true,
        },
      },
    },
  });

  const ground_temperature_line = document.getElementById(
    "ground_temperature_line"
  );
  const ground_temperature_line_ctx = ground_temperature_line.getContext("2d");
  const ground_temperature_line_chart = new Chart(ground_temperature_line_ctx, {
    type: "line",
    responsive: true,
    animation: {
      animateScale: true,
      animateRotate: true,
    },
    options: {
      scales: {
        y: {
          ticks: {
            callback: function (value, index, values) {
              return value + " °C";
            },
          },
        },
        x: {
          reverse: true,
        },
      },
    },
  });

  const ground_moisture_line = document.getElementById("ground_moisture_line");
  const ground_moisture_line_ctx = ground_moisture_line.getContext("2d");
  const ground_moisture_line_chart = new Chart(ground_moisture_line_ctx, {
    type: "line",
    responsive: true,
    animation: {
      animateScale: true,
      animateRotate: true,
    },
    options: {
      scales: {
        y: {
          ticks: {
            callback: function (value, index, values) {
              return value + " %";
            },
          },
        },
        x: {
          reverse: true,
        },
      },
    },
  });

  loadLatestResults();

  window.setInterval(function () {
    loadLatestResults();
  }, 30000);

  function createElementHtml(id, data, unit) {
    let paragraph = document.createElement("p");
    let text = document.createTextNode(id + ": " + data + unit);
    paragraph.id = id;
    paragraph.appendChild(text);
    return paragraph;
  }

  // Live view
  function updateLiveView(values) {
    container.innerHTML = "";

    container.appendChild(
      createElementHtml("Temperature", values.temperature, " °C")
    );
    container.appendChild(createElementHtml("Humidity", values.humidity, "%"));
    container.appendChild(
      createElementHtml("Heat Index", values.heat_index, " °C")
    );
    container.appendChild(createElementHtml("Light", values.light, " Lux"));
    container.appendChild(
      createElementHtml("Ground Temperature", values.ground_temperature, " °C")
    );
    container.appendChild(
      createElementHtml("Ground Moisture", values.ground_moisture, "%")
    );
    container.appendChild(createElementHtml("Timestamp", values.timestamp, ""));
  }

  //Dougnuts
  function updateHumidityDougnut(humidity) {
    humidity_dougnut_chart.data = {
      datasets: [
        {
          data: [humidity, 100 - humidity],
          backgroundColor: ["#03A9F4", "#9E9E9E"],
        },
      ],
      labels: ["Humidity (%)"],
    };
    humidity_dougnut_chart.update();
    document.getElementById("humidity").innerText = humidity + "%";
  }

  function updateMoistureDougnut(moisture) {
    moisture_dougnut_chart.data = {
      datasets: [
        {
          data: [moisture, 100 - moisture],
          backgroundColor: ["#03A9F4", "#9E9E9E"],
        },
      ],
      labels: ["Ground Moisture (%)"],
    };

    moisture_dougnut_chart.update();
    document.getElementById("moisture").innerText = moisture + "%";
  }

  //Charts
  function updateTemperature(data) {
    temperature_line_chart.data = {
      labels: data.labels,
      datasets: [
        {
          label: "Temperature",
          data: data.values,
          fill: false,
          borderColor: "#8bc34a",
          tension: 0.1,
        },
      ],
    };
    temperature_line_chart.update();
  }

  function updateLight(data) {
    light_line_chart.data = {
      labels: data.labels,
      datasets: [
        {
          label: "Light",
          data: data.values,
          fill: false,
          borderColor: "#8bc34a",
          tension: 0.1,
        },
      ],
    };
    light_line_chart.update();
  }

  function updateHumidity(data) {
    humidity_line_chart.data = {
      labels: data.labels,
      datasets: [
        {
          label: "Humidity",
          data: data.values,
          fill: false,
          borderColor: "#8bc34a",
          tension: 0.1,
        },
      ],
    };
    humidity_line_chart.update();
  }

  function updateHeatIndex(data) {
    heat_index_line_chart.data = {
      labels: data.labels,
      datasets: [
        {
          label: "Heat index",
          data: data.values,
          fill: false,
          borderColor: "#8bc34a",
          tension: 0.1,
        },
      ],
    };
    heat_index_line_chart.update();
  }

  function updateGroundTemperature(data) {
    ground_temperature_line_chart.data = {
      labels: data.labels,
      datasets: [
        {
          label: "Ground temperature",
          data: data.values,
          fill: false,
          borderColor: "#8bc34a",
          tension: 0.1,
        },
      ],
    };
    ground_temperature_line_chart.update();
  }

  function updateGroundMoisture(data) {
    ground_moisture_line_chart.data = {
      labels: data.labels,
      datasets: [
        {
          label: "Ground moisture",
          data: data.values,
          fill: false,
          borderColor: "#8bc34a",
          tension: 0.1,
        },
      ],
    };
    ground_moisture_line_chart.update();
  }

  //Ajax
  function loadLatestResults() {
    $.ajax({
      url: "/api/receive",
      type: "POST",
      data: {
        json: JSON.stringify({ id: 1 }),
      },
      cache: false,
      success: function (response) {
        let data = response.data;
        updateLiveView(data);
        updateHumidityDougnut(data.humidity);
        updateMoistureDougnut(data.ground_moisture);
      },
    });

    $.ajax({
      url: "/api/temperature",
      type: "POST",
      data: {
        json: JSON.stringify({ id: 1, amount: 20 }),
      },
      cache: false,
      success: function (response) {
        let data = response.data;
        console.log(JSON.stringify(data));
        updateTemperature(data);
      },
    });

    $.ajax({
      url: "/api/light",
      type: "POST",
      data: {
        json: JSON.stringify({ id: 1, amount: 20 }),
      },
      cache: false,
      success: function (response) {
        let data = response.data;
        console.log(JSON.stringify(data));
        updateLight(data);
      },
    });

    $.ajax({
      url: "/api/humidity",
      type: "POST",
      data: {
        json: JSON.stringify({ id: 1, amount: 20 }),
      },
      cache: false,
      success: function (response) {
        let data = response.data;
        console.log(JSON.stringify(data));
        updateHumidity(data);
      },
    });

    $.ajax({
      url: "/api/heat_index",
      type: "POST",
      data: {
        json: JSON.stringify({ id: 1, amount: 20 }),
      },
      cache: false,
      success: function (response) {
        let data = response.data;
        console.log(JSON.stringify(data));
        updateHeatIndex(data);
      },
    });

    $.ajax({
      url: "/api/ground_temperature",
      type: "POST",
      data: {
        json: JSON.stringify({ id: 1, amount: 20 }),
      },
      cache: false,
      success: function (response) {
        let data = response.data;
        console.log(JSON.stringify(data));
        updateGroundTemperature(data);
      },
    });

    $.ajax({
      url: "/api/ground_moisture",
      type: "POST",
      data: {
        json: JSON.stringify({ id: 1, amount: 20 }),
      },
      cache: false,
      success: function (response) {
        let data = response.data;
        console.log(JSON.stringify(data));
        updateGroundMoisture(data);
      },
    });
  }

  document.querySelector(".scroll-up").addEventListener("click", (e) => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
});
