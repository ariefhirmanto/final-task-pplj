const { authJwt } = require("../middlewares");
const { serviceOTP } = require("../middlewares");
const controller = require("../controllers/otp.controller");

module.exports = function(app) {
  app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header(
      "Access-Control-Allow-Headers",
      "x-access-token, Origin, Content-Type, Accept"
    );
    next();
  });
  app.get("/api/processing", [authJwt.verifyToken, serviceOTP.generateOTP]);
};