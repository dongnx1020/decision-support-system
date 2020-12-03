// Global Variable

window.chartColors = {
    red: 'rgb(255, 99, 132)',
    orange: 'rgb(255, 159, 64)',
    yellow: 'rgb(255, 205, 86)',
    green: 'rgb(75, 192, 192)',
    blue: 'rgb(54, 162, 235)',
    purple: 'rgb(153, 102, 255)',
    grey: 'rgb(201, 203, 207)'
};

var colors = [
    '#e040fb',
    '#2196f3',
    '#66bb6a',
    '#fdd835',
    '#ff5722',
    '#4dd0e1',
    '#f44336',
    '#26a69a',
    '#ec407a',
    '#ffb300',
    '#e91e63',
    '#8d6e63',
];

_options = function(type) {
    options = null;
    if (type == 'line') {
        options = {
            responsive: true,
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: false
                }],
                yAxes: [{
                    display: false
                }]
            },
            legend: {
                display: false
            },
            tooltips: {
                callbacks: {
                    label: function (tooltipItem) {
                        return tooltipItem.yLabel;
                    }
                }
            }
        };
        
    } else if (type == 'bar') {
        options = {
            responsive: true,
            legend: {
                display: false,
                position: 'right',
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
        };
    } else {
        options = {
            responsive: true,
            legend: {
                display: true,
                position: 'right',
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
        };
    };
    return options;
};

_dataTable = function(table) {
    var result = [];
    for (var i = 1; i < table.rows.length; i++) {
        var row = [];
        for (var j = 1; j < table.rows[i].cells.length; j++) {
            row.push(table.rows[i].cells[j].innerHTML);
        };
        result.push(row);
    };
    return result;
};

_datasets = function(type, label, data) {
    var result = [];
    if (type == 'doughnut') {
        var item = {
            label: label[0],
            backgroundColor: colors,
            borderColor: colors,
            data: data[0],
            fill: false
        };
        result.push(item);
    } else {
        for (var i = 0; i < data.length; i++) {
            var item = {
                label: label[i],
                backgroundColor: colors[i],
                borderColor: colors[i],
                data: data[i],
                fill: false
            };
            result.push(item);
        };
    }
    return result;
};

_config = function(type, xlabels, ylabels, datatable) {
    var result = {
        type: type,
        data: {
            labels: xlabels,
            datasets: _datasets(type, ylabels, datatable),
        },
        options: _options(type),
    };
    return result;
};

// Display Chart

window.onload = function() {
    var xlabelsLine = ['Drink', 'Rice', 'Spice', 'Conv', 'Fruit', 'Other', 'Nonfood', 'Vegetable', 'Meat', 'Fish', 'Tea', 'Count'];
    var ylabelsLine = ['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5']
    
    var tableLinePre = document.querySelector('#tableClusterPre');
    var dataTableLinePre = _dataTable(tableLinePre)
    var ctxLinePre = document.getElementById('myLineChartPre').getContext('2d');
    var linePreConfig = _config('line', xlabelsLine, ylabelsLine, dataTableLinePre)
    window.myLinePre = new Chart(ctxLinePre, linePreConfig);

    var tableLineNow = document.querySelector('#tableClusterNow');
    var dataTableLineNow = _dataTable(tableLineNow)
    var ctxLineNow = document.getElementById('myLineChartNow').getContext('2d');
    var lineNowConfig = _config('line', xlabelsLine, ylabelsLine, dataTableLineNow)
    window.myLineNow = new Chart(ctxLineNow, lineNowConfig);
    
    var xlabelsBar = ['Drink', 'Rice', 'Spice', 'Conv', 'Fruit', 'Other', 'Nonfood', 'Vegetable', 'Meat', 'Fish', 'Tea']
    var ylabelsBar = ['Previous', 'Current']

    var tableBar = document.querySelector('#tableTotalMoney');
    var dataTableBar = _dataTable(tableBar)
    var ctxBar = document.getElementById('myBarChart').getContext('2d');
    var barConfig = _config('bar', xlabelsBar, ylabelsBar, dataTableBar)
    window.myBar = new Chart(ctxBar, barConfig);
    
    var xlabelsPie = ['Drink', 'Rice', 'Spice', 'Conv', 'Fruit', 'Other', 'Nonfood', 'Vegetable', 'Meat', 'Fish', 'Tea']
    var ylabelsPie = ['Previous', 'Current']
    
    var tablePieNow = document.querySelector('#tablePercent');
    var dataTablePieNow = _dataTable(tablePieNow)
    var ctxPie = document.getElementById('myPieChartPre').getContext('2d');
    var pieConfig = _config('doughnut', xlabelsPie, ylabelsPie, [dataTablePieNow[0]])
    window.myPie = new Chart(ctxPie, pieConfig);
    
    var tablePiePre = document.querySelector('#tablePercent');
    var dataTablePiePre = _dataTable(tablePiePre)
    var ctxPie = document.getElementById('myPieChartNow').getContext('2d');
    var pieConfig = _config('doughnut', xlabelsPie, ylabelsPie, [dataTablePiePre[1]])
    window.myPie = new Chart(ctxPie, pieConfig);
};
