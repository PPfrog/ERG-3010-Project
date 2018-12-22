// You can reproduce this figure in plotly.js with the following code!

// Learn more about plotly.js here: https://plot.ly/javascript/getting-started

/* Here's an example minimal HTML template
 *
 * <!DOCTYPE html>
 *   <head>
 *     <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
 *   </head>
 *   <body>
 *   <!-- Plotly chart will be drawn inside this div -->
 *   <div id="plotly-div"></div>
 *     <script>
 *     // JAVASCRIPT CODE GOES HERE
 *     </script>
 *   </body>
 * </html>
 */

trace1 = {
  direction: 'clockwise', 
  hole: 0, 
  labels: ['US', 'China', 'European Union', 'Russian Federation', 'Brazil', 'India', 'Rest of World'], 
  labelssrc: 'plotly2_demo:405:3e02d0', 
  marker: {line: {width: 0}}, 
  name: 'Global CO2 Emission', 
  opacity: 1, 
  pull: 0, 
  rotation: 0, 
  sort: false, 
  textinfo: 'percent', 
  type: 'pie', 
  values: [27, 11, 25, 8, 1, 3, 25], 
  valuessrc: 'plotly2_demo:405:3da60a'
};
data = [trace1];
layout = {
  autosize: true, 
  title: '<b>Global CO</b><sub><b>2</b></sub><b> Emissions</b>', 
  xaxis: {
    autorange: true, 
    range: [-0.36109260493, 6.36109260493], 
    type: 'category'
  }, 
  yaxis: {
    autorange: true, 
    range: [-0.655373831776, 28.6553738318], 
    type: 'linear'
  }
};
Plotly.plot('plotly-div', {
  data: data,
  layout: layout
});