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
  y: [90, 88, 55, 88, 72, 100, 88, 25, 92, 100, 82, 82, 90, 68, 85, '', 82, 40, 100, 92, 82, 55, 62, 85, 100, 75, 88, 78, 80, '', 92, 100, 88, 72, 95, 80, 90, 72, 100, '', 100, 75, 82, 60, 90, 85, 90, 38, 78, 82, 100, 90, 80, '', 80, 100, 70, 100, 82, 62, 92, '', 100, 80, '', 100, 88, 85], 
  boxmean: 'sd', 
  boxpoints: 'all', 
  fillcolor: '#c8e6c0', 
  jitter: 0.5, 
  line: {color: '#1c9099'}, 
  marker: {
    color: '#c8e6c0', 
    line: {
      color: '#FFFFFF', 
      width: 1
    }, 
    size: 10
  }, 
  name: 'Homeworks', 
  pointpos: -2, 
  type: 'box', 
  ysrc: 'PPfrog:33:e9bcd5'
};
trace2 = {
  y: [70, 65, 85, 75, 72, 75, 90, 88, 85, 80, 92, 85, 85, 75, 72, '', 80, 42, 80, 95, 90, 62, 65, 65, 82, 68, 48, 57, 95, 70, 100, 80, 95, 78, 80, 80, 85, 90, 100, 52, 85, 72, 70, 45, 75, 85, 95, 65, 70, 85, 70, 85, 35, '', 90, 95, 95, 65, 62, 48, 60, '', 85, 85, '', 90, 70, 68], 
  boxmean: 'sd', 
  boxpoints: 'all', 
  fillcolor: '#84cba0', 
  jitter: 0.5, 
  line: {color: '#1c9099'}, 
  marker: {
    color: '#84cba0', 
    line: {
      color: '#FFFFFF', 
      width: 1
    }, 
    size: 10
  }, 
  name: 'Midterm Exam', 
  pointpos: -2, 
  type: 'box', 
  ysrc: 'PPfrog:33:f5a44a'
};
trace3 = {
  y: [95, 75, 70, 72, 52, 70, 82, 90, 95, 80, 68, 88, 82, 52, 80, '', 78, 57, 88, 88, 100, 50, 65, 78, 92, 65, 50, 60, 88, '', 100, 50, 90, 70, 60, 72, 75, 95, 100, 45, 68, 72, 45, 60, 78, 85, 92, 45, 68, 70, 85, 82, 62, '', 75, 100, 80, 65, 52, 48, 57, '', 100, 72, '', 100, 80, 65], 
  boxmean: 'sd', 
  boxpoints: 'all', 
  fillcolor: '#56a999', 
  jitter: 0.5, 
  line: {color: '#1c9099'}, 
  marker: {
    color: '#56a999', 
    line: {
      color: '#FFFFFF', 
      width: 1
    }, 
    size: 10
  }, 
  name: 'Final Exam', 
  pointpos: -2, 
  type: 'box', 
  ysrc: 'PPfrog:33:e4e846'
};
trace4 = {
  y: [86, 75.9, 70, 77.7, 64, 80.5, 86.2, 69.9, 91.1, 86, 79.4, 85.3, 85.3, 63.7, 79.1, '', 79.8, 47.4, 89.2, 91.3, 91.6, 55.1, 64.1, 76.2, 91.4, 68.9, 60.8, 64.5, 87.7, 21, 97.6, 74, 90.9, 73, 76.5, 76.8, 82.5, 86.6, 100, 33.6, 82.7, 72.9, 63.6, 55.5, 80.7, 85, 92.3, 48.9, 71.6, 78.1, 85, 85.3, 59.3, '', 81, 98.5, 81.5, 75.5, 64, 52.2, 68.4, '', 95.5, 78.3, '', 97, 79.4, 71.9], 
  boxmean: 'sd', 
  boxpoints: 'all', 
  fillcolor: '#408494', 
  jitter: 0.5, 
  line: {color: '#1c9099'}, 
  marker: {
    color: '#408494', 
    line: {
      color: '#FFFFFF', 
      width: 1
    }, 
    size: 10
  }, 
  name: 'Course Grade', 
  pointpos: -2, 
  type: 'box', 
  ysrc: 'PPfrog:33:630272'
};
data = [trace1, trace2, trace3, trace4];
layout = {
  autosize: false, 
  height: 500, 
  plot_bgcolor: '#EFECEA', 
  showlegend: false, 
  title: 'Fig 4.4c: Course Grade Distributions', 
  width: 530, 
  xaxis: {
    autorange: true, 
    gridcolor: '#FFFFFF', 
    range: [-0.8675, 3.5], 
    showgrid: true, 
    ticklen: 8, 
    ticks: 'outside', 
    tickwidth: 1.5, 
    type: 'category', 
    zeroline: false
  }, 
  yaxis: {
    autorange: true, 
    gridcolor: '#FFFFFF', 
    range: [16.6111111111, 104.388888889], 
    showgrid: true, 
    ticklen: 8, 
    ticks: 'outside', 
    tickwidth: 1.5, 
    title: 'Grade [%]', 
    type: 'linear', 
    zeroline: false
  }
};
Plotly.plot('plotly-div-1', {
  data: data,
  layout: layout
});