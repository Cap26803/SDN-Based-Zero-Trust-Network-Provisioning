var nodes = new vis.DataSet([
    {id: 38, label: 's1\n(Switch)', color: '#FFB347', font: {color: '#000000', size: 18}},
    {id: 39, label: 's2\n(Switch)', color: '#FFB347', font: {color: '#000000', size: 18}},
    {id: 40, label: 's3\n(Switch)', color: '#FFB347', font: {color: '#000000', size: 18}},

    {id: 1, label: 'h1\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 2, label: 'h2\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 3, label: 'h3\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 4, label: 'h4\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 5, label: 'h5\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 6, label: 'h6\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 7, label: 'h7\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 8, label: 'h8\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 9, label: 'h9\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 10, label: 'h10\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 11, label: 'h11\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 12, label: 'h12\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 13, label: 'h13\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 14, label: 'h14\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 15, label: 'h15\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 16, label: 'h16\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 17, label: 'h17\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 18, label: 'h18\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 19, label: 'h19\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 20, label: 'h20\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 21, label: 'h21\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 22, label: 'h22\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 23, label: 'h23\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 24, label: 'h24\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},
    {id: 25, label: 'h25\n(Student)', color: '#A3D977', font: {color: '#000000', size: 16}},

    {id: 26, label: 'f1\n(Faculty)', color: '#7FB3D5', font: {color: '#000000', size: 16}},
    {id: 27, label: 'f2\n(Faculty)', color: '#7FB3D5', font: {color: '#000000', size: 16}},
    {id: 28, label: 'f3\n(Faculty)', color: '#7FB3D5', font: {color: '#000000', size: 16}},
    {id: 29, label: 'f4\n(Faculty)', color: '#7FB3D5', font: {color: '#000000', size: 16}},
    {id: 30, label: 'f5\n(Faculty)', color: '#7FB3D5', font: {color: '#000000', size: 16}},
    {id: 31, label: 'f6\n(Faculty)', color: '#7FB3D5', font: {color: '#000000', size: 16}},
    {id: 32, label: 'f7\n(Faculty)', color: '#7FB3D5', font: {color: '#000000', size: 16}},
    {id: 33, label: 'f8\n(Faculty)', color: '#7FB3D5', font: {color: '#000000', size: 16}},

    {id: 34, label: 'admin\n(Admin)', color: '#F39C12', font: {color: '#000000', size: 18}},
    {id: 35, label: 'attacker1\n(Attacker)', color: '#E57373', font: {color: '#000000', size: 16}},
    {id: 36, label: 'attacker2\n(Attacker)', color: '#E57373', font: {color: '#000000', size: 16}},
    {id: 37, label: 'attacker3\n(Attacker)', color: '#E57373', font: {color: '#000000', size: 16}}
]);

var edges = new vis.DataSet([
    {from: 1, to: 38},
    {from: 2, to: 38},
    {from: 3, to: 38},
    {from: 4, to: 38},
    {from: 5, to: 39},
    {from: 6, to: 39},
    {from: 7, to: 40},
    {from: 8, to: 40},
    {from: 9, to: 38},
    {from: 10, to: 38},
    {from: 11, to: 39},
    {from: 12, to: 39},
    {from: 13, to: 39},
    {from: 14, to: 39},
    {from: 15, to: 40},
    {from: 16, to: 40},
    {from: 17, to: 40},
    {from: 18, to: 40},
    {from: 19, to: 40},
    {from: 20, to: 40},
    {from: 21, to: 40},
    {from: 22, to: 40},
    {from: 23, to: 40},
    {from: 24, to: 40},
    {from: 25, to: 40},

    // Connecting faculty nodes to switches
    {from: 26, to: 38},
    {from: 27, to: 38},
    {from: 28, to: 39},
    {from: 29, to: 39},
    {from: 30, to: 40},
    {from: 31, to: 40},
    {from: 32, to: 38},
    {from: 33, to: 39},

    {from: 38, to: 39},
    {from: 39, to: 40},
    {from: 34, to: 38},
    {from: 35, to: 38},
    {from: 36, to: 38},
    {from: 37, to: 38}
]);

var container = document.getElementById('network');

var data = { nodes: nodes, edges: edges };

var options = {
    physics: {
        stabilization: true
    },
    interaction: { hover: true },
    layout: { improvedLayout: true },
    edges: { color: { color: '#999999' }, width: 1.5 }
};

var network = new vis.Network(container, data, options);

