#!/usr/bin/node

let executions = 0;
exports.logMe = function (item) {
  executions += 1;
  console.log(executions + ':' + item);
};
