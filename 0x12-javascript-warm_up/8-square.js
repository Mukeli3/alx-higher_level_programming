#!/usr/bin/node
const { argv } = require('process');
const x = parseInt(argv[2]);

if (isNaN(x)) {
        console.log('Missing size');
}
else {
        for (i = 0; i < x; i++) {
                console.log('X'.repeat(x));
        }
}
