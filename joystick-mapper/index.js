const EventEmitter = require('events');
const gamepad = require('gamepad');

// true if platform is windows
const win = require('os').platform().indexOf('win32') > -1;

let FBAxis;
let LRAxis;
let dickspinAxis;
let smolLeftRightAxis;
let smolUpDownAxis;
let throttleAxis;
let rightBumper;
let leftBumper;
let rightTrigger;
let leftTrigger;
let rightThumbUD;
let upOnDPad;
let downOnDPad;
let A;
let B;
let X;
let Y;

if (win) {
    FBAxis = 0;
    LRAxis = 1;
    dickspinAxis = 4;
    smolLeftRightAxis = 2;
    smolUpDownAxis = 3;
    throttleAxis = 5;
    rightBumper = 9;
    leftBumper = 8;
    rightTrigger = 5;
    leftTrigger = 4;
    rightThumbUD = 3;
    upOnDPad = 0;
    downOnDPad = 1;
    A = 10;
    B = 11;
    X = 12;
    Y = 13;
}
else {
    FBAxis = 1;
    LRAxis = 0;
    dickspinAxis = 2;
    smolLeftRightAxis = 4;
    smolUpDownAxis = 5;
    throttleAxis = 3;
    rightBumper = 5;
    leftBumper = 4;
    rightTrigger = 5;
    leftTrigger = 2;
    rightThumbUD = 4;
    upOnDPad = 6;
    downOnDPad = 7;
    A = 0;
    B = 1;
    X = 2;
    Y = 3;
}

gamepad.init();
setInterval(gamepad.processEvents, 17);
setInterval(gamepad.detectDevices, 500);

module.exports = class extends EventEmitter {

    constructor(interval, deadzone = 0.15) {
        super();
        this.deadzone = deadzone;

        this.axes = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ];
        this.axes[1][rightTrigger] = -1;
        this.axes[1][leftTrigger] = -1;
        this.buttons = [
            [false, false, false, false, false, false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false, false, false, false, false, false]
        ];

        this.directions = {};

        gamepad.on('down', (id, num) => this.buttonDown(id, num));
        gamepad.on('up', (id, num) => this.buttonUp(id, num));
        gamepad.on('move', (id, num, val) => this.joystickMove(id, num, val));
        setInterval(() => this.checkValues(), interval);
    }

    buttonDown(id, num) {
        this.buttons[id][num] = true;
        this.emit('rawData', this.buttons);
        if (id === 1 && num === rightBumper)
            this.emit('setDepthLock', true);
        if (id === 1 && num === leftBumper)
            this.emit('setDepthLock', false);
        if (id === 1 && num === Y)
            this.emit('specialDelivery', {
                type: 'electromag',
                body: true
            });
        if (id === 1 && num === X)
            this.emit('specialDelivery', {
                type: 'electromag',
                body: false
            });
    }

    buttonUp(id, num) {
        this.buttons[id][num] = false;
        this.emit('rawData', this.buttons);
    }

    joystickMove(id, axis, val) {
        if (Math.abs(val) < this.deadzone) {
            this.axes[id][axis] = 0;
            return;
        }

        this.axes[id][axis] = val;
        this.emit('rawData', this.axes);
    }

    checkValues() {
        let newVals = {
            FB: !this.buttons[0][6] && -this.axes[0][FBAxis],
            turn: !this.buttons[0][6] &&  this.axes[0][dickspinAxis],
            strafe: !this.buttons[0][6] &&  this.axes[0][LRAxis],
            pitch: !this.buttons[0][6] &&  this.axes[1][rightThumbUD],
            depth: !this.buttons[0][6] && (this.axes[1][leftTrigger] - this.axes[1][rightTrigger]) / 2,
            manip: !this.buttons[0][6] && this.axes[0][smolUpDownAxis],
            leveler: !this.buttons[0][6] && this.buttons[1][A] * 1 + this.buttons[1][B] * -1,
            picamControl: this.buttons[1][upOnDPad] * 1 + this.buttons[1][downOnDPad] * -1,
            electromagControl: this.buttons[1][Y] * 1

        };
        Object.keys(newVals).map(key => {
            if (newVals[key] === this.directions[key])
                delete newVals[key];
        });
        if (Object.keys(newVals).length === 0) return;

        this.emit('data', newVals);
        this.directions = Object.assign(this.directions, newVals);
    }

};

if (require.main === module) {
    const mapper = new module.exports(17, 0.15);
    mapper.on('rawData', console.log);
}
