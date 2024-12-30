urlPrefix = $("#urlPrefix").attr("data-url");

$(document).ready(function () {
	//Hired candididates recruitment wise chart


	//onboarding started candidate chart
	$.ajax({
		type: "GET",
		url: `/${urlPrefix}onboarding/onboard-candidate-chart`,
		success: function (response) {
			const ctx = document.getElementById("onboardCandidate");
			if (ctx) {
				new Chart(ctx, {
					type: "bar",
					data: {
						labels: response.labels,
						datasets: [
							{
								label: "#onboarding candidates",
								data: response.data,
								backgroundColor: response.background_color,
								borderColor: response.border_color,
								borderWidth: 1,
							},
						],
						// message:response.message,
						// emptyImageSrc:'/static/images/ui/sunbed.png'
					},
					options: {
						responsive: true,

						scales: {
							y: {
								beginAtZero: true,
							},
						},
						onClick: (e, activeEls) => {
							let datasetIndex = activeEls[0].datasetIndex;
							let dataIndex = activeEls[0].index;
							let datasetLabel = e.chart.data.datasets[datasetIndex].label;
							let value = e.chart.data.datasets[datasetIndex].data[dataIndex];
							let label = e.chart.data.labels[dataIndex];
							localStorage.removeItem("savedFilters");
							window.location.href =
								`/${urlPrefix}recruitment/candidate-view` +
								"?recruitment=" +
								label +
								"&start_onboard=true";
						},
					},
					plugins: [
						{
							afterRender: (chart) => emptyChart(chart),
						},
					],
				});
			}
		},
	});
});
