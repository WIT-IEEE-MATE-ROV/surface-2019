/**
 * Nugget Industries
 * 2017
 */

// dependencies
const http = require('http');
const yargs = require('yargs');
const express = require('express');
const io = require('socket.io');
const { nugLog } = require('nugget-logger');
const { socket } = require('nugget-comms');
const JoystickMapper = require('./joystick-mapper');

// set up logger
const logger = new nugLog('debug', 'surface.log');

// socket.io dashboard port
const dashPort = 80;

const args = yargs
    .usage('Usage: $0 [options]')
    .version(false)
    .option('l', {
        alias: 'local',
        desc: 'connect to the robot on localhost',
        type: 'boolean'
    })
    .option('P', {
        alias: 'pi-address',
        desc: 'connect to the robot at this address',
        type: 'string',
        default: 'deepfriednug.local',
        nargs: 1
    })
    .alias('h', 'help')
    .argv;

// address to look for robot at
const botAddress = args.local ? '127.0.0.1' : args.piAddress;
// port to look for robot on
const piPort = 8080;
// robot connection options
const options = {
    host: botAddress,
    port: piPort
};

// so that the dashboard doesn't blow up in our face when we leave or try to re-load
const dummySocket = {
    reset: () => {
        this.notified = false;
        return dummySocket;
    },
    // overload emit, be annoying if you try to send stuff to a dashboard that isn't there
    emit: () => {
        if (this.notified)
            return;

        logger.w('dashboard', 'dashboard disconnected WHAT HAVE YOU DONE OPEN IT BACK UP');
        this.notified = true;
    }
};

// BotSocket!!!!
const botSocket = new socket();
const mapper = new JoystickMapper(17);

// socket.io stuff
const app = express();
const server = http.Server(app);
const dashboard = io(server);

let _dashSocket = dummySocket;
let toggleDepthLock = false;

// express/webserver stuff
app.use('/static', express.static(__dirname + '/dashboard/static'));

// GET renderer
app.get('/', (request, response) => response.sendFile(__dirname + '/dashboard/index.html'));

// http server shit
server.listen(dashPort, () => logger.i('dashboard', `dashboard running on localhost:${dashPort}`));

/*
 * 1. controller
 * 2. app (express)
 * 3. server
 * 4. dashSocket
 * 5. BotSocket
 */
async function main() {

    mapper.on('data', async data => {
        try {
            _dashSocket.emit('motorData', (await botSocket.sendControllerData(data)).body);
        }
        catch (error) {
            if (error instanceof TypeError)
                return;
            throw error;
        }
    });
    mapper.on('setDepthLock', value => {
        toggleDepthLock = value;
        botSocket.setDepthLock(toggleDepthLock);
    });
    mapper.on('specialDelivery', data => {
        botSocket.specialDelivery(data.type, data.body);
    });

    // convert radians to degrees
    botSocket.on('magData', data => {
        Object.keys(data).map(k => data[k] *= 180 / Math.PI);
        _dashSocket.emit('magData', data);
    });
    botSocket.on('piTempData', data => {
        _dashSocket.emit('piTempData', data);
    });
    botSocket.on('motorData', data => {
        _dashSocket.emit('motorData', data);
    });

    // set us up some dashboard listeners
    dashboard.on('connection', socket => {
        _dashSocket = socket;

        logger.i('dashboard', 'the dashboard awakens');
        _dashSocket.on('connectToBot', async () => {
            await botSocket.connect(options);
            await botSocket.startPiTempStream(1000);
        });

        _dashSocket.on('PIDTune', async data => {
            logger.d('PID tuning', 'SEND IT button pressed');
            socket.emit('PIDTuneData', (await botSocket.tunePIDLoop(data.zKp, data.zKi, data.zKd)).body);
        });
        _dashSocket.on('specialDelivery', async data => _dashSocket.emit('specialDeliveryResponse', (await botSocket.specialDelivery(data.type, data.payload)).body));
        _dashSocket.on('disconnectFromBot', () => botSocket.disconnect());

        // actual socket.io disconnect event from dashboard
        _dashSocket.on('disconnect', () => {
            logger.i('dashboard', 'dashboard connection closed');
            _dashSocket = dummySocket.reset()
        });
    });

}

main().catch(error => console.error(error));
