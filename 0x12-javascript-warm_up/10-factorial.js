#!/usr/bin/node
const { argv } = require('process');
const i = parseInt(argv[2]);

function fact (i) {
	if (i === 0 || isNaN(i)) {
		return (1);
	}
	else {
		return (i * fact(i - 1));
	}
}
console.log(fact(i));
