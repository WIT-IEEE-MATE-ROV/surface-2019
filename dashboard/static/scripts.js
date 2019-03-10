const socket = io.connect('http://localhost');
const imgDirectory = '/static/lib/indicators/img/';
let attitude, heading, vectorMotors, depthMotors;
// set up all the indicators
$(document).ready(() => {
    attitude = $.flightIndicator('#attitude', 'attitude', {
        size: 300,
        showBox: true,
        img_directory: imgDirectory
    });
    heading = $.flightIndicator('#heading', 'heading', {
        size: 300,
        showBox: true,
        img_directory: imgDirectory
    });
    vectorMotors = [ $('#LF'), $('#RF'), $('#LB'), $('#RB') ];
    depthMotors = [ $('#F'), $('#B') ];

    // do some button listeners
    $('#connect').click(() => socket.emit('connectToBot'));
    $('#disconnect').click(() => socket.emit('disconnectFromBot'));
    $('#PIDTuneSend').click(() => socket.emit('PIDTune', {
        zKp: $('#zKp').val(),
        zKi: $('#zKi').val(),
        zKd: $('#zKd').val()
    }));
    $('#specialDeliveryButton').click(() => socket.emit('specialDelivery', {
        type: $('#specialDeliveryType').val(),
        payload: $('#specialDeliveryPayload').val()
    }));
});
// ye olde socket listeners
socket.on('magData', data => {
    attitude.setPitch(data.pitch);
    attitude.setRoll(data.roll);
    heading.setHeading(data.heading)
});
socket.on('piTempData', data => $('#piTemp').val(data));
socket.on('motorData', data => {
    console.log(data);
    if (data.hasOwnProperty('vector')) data.vector.map((value, index) => vectorMotors[index].val((value - 1550) / 400));
    if (data.hasOwnProperty('depth')) data.depth.map((value, index) => depthMotors[index].val((value - 1550) / 400));
    if (data.hasOwnProperty('manip')) $('#MAN').val((data.manip - 1550) / 400);
});
socket.on('PIDTuneData', data => {
    console.log(data);
    $('#zKp-ROV').val(data.zKp);
    $('#zKi-ROV').val(data.zKi);
    $('#zKd-ROV').val(data.zKd);
});
socket.on('specialDeliveryResponse', data => $('#specialDeliveryResponse').val(data));
