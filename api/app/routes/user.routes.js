const { authJwt } = require("../middlewares");
const controller = require("../controllers/user.controller");
const { verifyUsername } = require("../middlewares");
const { serviceOTP } = require("../middlewares");

module.exports = function(app) {
  app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header(
      "Access-Control-Allow-Headers",
      "x-access-token, Origin, Content-Type, Accept"
    );
    next();
  });
  app.get("/api/user", [authJwt.verifyToken], controller.findOne);
  app.put("/api/user/transfer", [authJwt.verifyToken, verifyUsername.checkUsernameExist, serviceOTP.verifyOTP], controller.updateAmount); // ceklis
  app.put("/api/user/bill", [authJwt.verifyToken, verifyUsername.checkUsernameExist, serviceOTP.verifyOTP], controller.updateBill);
  app.get("/api/user/transfer/:username", [authJwt.verifyToken], controller.findTransferHistOwner); //ceklis
};