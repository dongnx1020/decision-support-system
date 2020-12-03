// Global
var COLOR = [
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

var OPTIONS = {
    responsive: true,
    hover: {
        mode: 'nearest',
        intersect: true
    },
    scales: {
        xAxes: [{
            display: true,
            scaleLabel: {
                display: true,
                labelString: 'Category'
            }
        }],
        yAxes: [{
            display: true,
            scaleLabel: {
                display: true,
                labelString: 'Total Money'
            }
        }]
    },
    tooltips: {
        callbacks: {
            label: function (tooltipItem) {
                return tooltipItem.yLabel;
            }
        }
    }
};

GetDataTable = function (id_table) {
    var _table = document.querySelector(id_table);
    var _data_table = [];
    for (var i = 1; i < _table.rows.length; i++) {
        var _row = [];
        for (var j = 1; j < _table.rows[i].cells.length; j++) {
            _row.push(_table.rows[i].cells[j].innerHTML);
        };
        _data_table.push(_row);
    };
    return _data_table;
};

CreateDataSet = function (type, ylabel, data_table) {
    var _data_set = [];
    if (type == 'line') {
        for (var i = 0; i < data_table.length; i++) {
            var _item = {
                label: ylabel[i],
                backgroundColor: COLOR[i],
                borderColor: COLOR[i],
                data: data_table[i],
                fill: false
            };
            _data_set.push(_item);
        };
    };
    return _data_set;
};

CreateConfig = function (type, xlabel, ylabel, data_table) {
    var _config = {
        type: type,
        data: {
            labels: xlabel,
            datasets: CreateDataSet(type, ylabel, data_table)
        },
        options: OPTIONS
    }
    return _config;
};


window.onload = function () {
    var _xlabel = ['Drink', 'Rice', 'Spice', 'Conv', 'Fruit', 'Other', 'Nonfood', 'Vegetable', 'Meat', 'Fish', 'Tea', 'Count'];
    var _ylabel = ['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5'];
    var _data_table = GetDataTable('#dataTable');
    var _config = CreateConfig('line', _xlabel, _ylabel, _data_table);
    var _ctx = document.getElementById('myLineChart').getContext('2d');
    window.myLine = new Chart(_ctx, _config);
};