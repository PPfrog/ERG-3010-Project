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
  y: ['0.01920825', '0.0188891', '0.0199509', '0.01995213', '0.01867667', '0.01878362', '0.01963265', '0.01973971', '0.01952807', '0.01973926'], 
  boxmean: true, 
  boxpoints: 'all', 
  marker: {
    color: '#440154', 
    symbol: 'circle-open'
  }, 
  name: '1', 
  type: 'box', 
  uid: 'fb3b44', 
  ysrc: 'PPfrog:28:c1bb63'
};
trace2 = {
  y: ['0.02355956', '0.02409046', '0.02387781', '0.02472797', '0.02440702', '0.02281646', '0.02525605', '0.0240908', '0.02483345', '0.02525808'], 
  boxmean: true, 
  boxpoints: 'all', 
  marker: {
    color: '#482878', 
    symbol: 'circle-open'
  }, 
  name: '2', 
  type: 'box', 
  uid: '1fb9c9', 
  ysrc: 'PPfrog:28:7691ee'
};
trace3 = {
  y: ['0.02217963', '0.02111817', '0.02101235', '0.02090732', '0.02154156', '0.02079925', '0.02133015', '0.0218624', '0.0210137', '0.02228601'], 
  boxmean: true, 
  boxpoints: 'all', 
  marker: {
    color: '#3e4989', 
    symbol: 'circle-open'
  }, 
  name: '3', 
  type: 'box', 
  uid: '799eb9', 
  ysrc: 'PPfrog:28:78e6c6'
};
trace4 = {
  y: ['0.02345329', '0.02292273', '0.02334747', '0.02387848', '0.02408866', '0.02302799', '0.02260347', '0.02334759', '0.02292397', '0.02366628'], 
  boxmean: true, 
  boxpoints: 'all', 
  marker: {
    color: '#31688e', 
    symbol: 'circle-open'
  }, 
  name: '4', 
  type: 'box', 
  uid: '239882', 
  ysrc: 'PPfrog:28:b5dc43'
};
trace5 = {
  y: ['0.02430187', '0.02398419', '0.02504542', '0.02472763', '0.02408888', '0.02430187', '0.02408956', '0.02324165', '0.02462158', '0.02451509'], 
  boxmean: true, 
  boxpoints: 'all', 
  marker: {
    color: '#26828e', 
    symbol: 'circle-open'
  }, 
  name: '5', 
  type: 'box', 
  uid: '1291fe', 
  ysrc: 'PPfrog:28:e1655f'
};
trace6 = {
  y: ['0.02440769', '0.02515079', '0.02642513', '0.02557655', '0.02525616', '0.02515124', '0.02504385', '0.02653151', '0.02610699', '0.02546983'], 
  boxmean: true, 
  boxpoints: 'all', 
  marker: {
    color: '#1f9e89', 
    symbol: 'circle-open'
  }, 
  name: '6', 
  type: 'box', 
  uid: '135166', 
  ysrc: 'PPfrog:28:880613'
};
trace7 = {
  y: ['0.02578751', '0.02684919', '0.02748659', '0.02578886', '0.02621113', '0.02674326', '0.02621158', '0.0266371', '0.02716823', '0.02695535'], 
  boxmean: true, 
  boxpoints: 'all', 
  marker: {
    color: '#35b779', 
    symbol: 'circle-open'
  }, 
  name: '7', 
  type: 'box', 
  uid: 'f9388c', 
  ysrc: 'PPfrog:28:94bd93'
};
trace8 = {
  y: ['0.02780393', '0.02759173', '0.02822957', '0.02801748', '0.02843964', '0.02780382', '0.02748501', '0.02865353', '0.02854861', '0.02833517'], 
  boxmean: true, 
  boxpoints: 'all', 
  marker: {
    color: '#6ece58', 
    symbol: 'circle-open'
  }, 
  name: '8', 
  type: 'box', 
  uid: '25c7fb', 
  ysrc: 'PPfrog:28:94a41b'
};
trace9 = {
  y: ['0.02939573', '0.02950222', '0.02907827', '0.02929092', '0.02939449', '0.02992651', '0.02950121', '0.02897234', '0.03056469', '0.02939618'], 
  boxmean: true, 
  boxpoints: 'all', 
  marker: {
    color: '#b5de2b', 
    symbol: 'circle-open'
  }, 
  name: '9', 
  type: 'box', 
  uid: '9e6240', 
  ysrc: 'PPfrog:28:e07143'
};
trace10 = {
  y: ['0.03066939', '0.03066984', '0.0303517', '0.03013973', '0.03056143', '0.03056368', '0.03013759', '0.03088283', '0.03130757', '0.0301386'], 
  boxmean: true, 
  boxpoints: 'all', 
  marker: {
    color: '#fde725', 
    symbol: 'circle-open'
  }, 
  name: '10', 
  type: 'box', 
  uid: '5bca86', 
  ysrc: 'PPfrog:28:27ab69'
};
data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10];
layout = {
  boxmode: 'group', 
  hovermode: 'closest', 
  showlegend: true, 
  title: 'K vs. CV Error Rate', 
  xaxis: {
    autorange: true, 
    range: [0.304, 10.5], 
    type: 'linear'
  }, 
  yaxis: {
    autorange: true, 
    range: [0.0179749533333, 0.0320092866667], 
    title: 'CV Error Rate', 
    type: 'linear'
  }
};
Plotly.plot('plotly-div', {
  data: data,
  layout: layout
});