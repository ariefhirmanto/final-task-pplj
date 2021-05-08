const authJwt = require("./authJwt");
const verifySignUp = require("./verifySignUp");
const verifyUsername = require("./verifyUsername");
const serviceOTP = require("./serviceOTP");

module.exports = {
  authJwt,
  verifySignUp,
  verifyUsername,
  serviceOTP
};