function fetchAttackLogs(){
    $.get('/api/attack_logs', function(data){
        var tb = '';
        data.forEach(row => {
            tb += `<tr><td>${row[0]}</td><td>${row[1]}</td><td>${row[2]}</td><td>${row[3]}</td></tr>`;
        });
        $("#attackLogs tbody").html(tb);
    });
}

function fetchLoginLogs(){
    $.get('/admin/login_logs.json', function(data){
        let roleCount = {admin:0, faculty:0, student:0};
        let tb = '';

        data.forEach(row => {
            roleCount[row.role]++;
            tb += `<tr><td>${row.username}</td><td>${row.role}</td><td>${row.time}</td></tr>`;
        });

        $("#loginTable tbody").html(tb);

        const ctx = document.getElementById('loginChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Admin','Faculty','Student'],
                datasets: [{
                    label: 'Login Count',
                    data: [roleCount.admin, roleCount.faculty, roleCount.student],
                    backgroundColor: ['red', 'blue', 'green']
                }]
            }
        });
    });
}

function fetchLoginHeatmap(){
    $.get('/api/login_heatmap', function(data){
        const heatmap = new CalHeatmap();
        heatmap.paint({
            range: 6,  // 6 months view
            domain: "month",
            subDomain: "day",
            data: data,
            start: new Date(),
            scale: {
                color: {
                    scheme: "Blues"  // Clean soothing colors
                }
            },
            tooltip: true,
        });
    });
}

function fetchPasswordAlerts(){
    $.get('/api/password_reset_alerts', function(data){
        let tb = '';
        if (data.length === 0){
            tb = `<tr><td colspan="3">✅ No Alerts</td></tr>`;
        } else {
            data.forEach(row => {
                tb += `<tr><td>${row.username}</td><td>${row.alert}</td><td>${row.time}</td></tr>`;
            });
        }
        $("#resetAlerts tbody").html(tb);
    });
}

fetchAttackLogs();
fetchLoginLogs();
fetchLoginHeatmap();
fetchPasswordAlerts();
setInterval(fetchAttackLogs, 3000);
setInterval(fetchPasswordAlerts, 5000);

