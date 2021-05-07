const { authJwt } = require("../middlewares");
const controller = require("../controllers/bill.controller");
const userController = require("../controllers/user.controller");

module.exports = function(app) {
  app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header(
      "Access-Control-Allow-Headers",
      "x-access-token, Origin, Content-Type, Accept"
    );
    next();
  });

  app.get("/api/bill/", [authJwt.verifyToken], controller.findAllBill); //ceklis
  app.get("/api/bill/:bill_owner", [authJwt.verifyToken], controller.findBillBasedOwner); //ceklis
  app.post("/api/bill/", [authJwt.verifyToken], controller.create, userController.updateBill); //ceklis
  app.put("/api/bill/:bill_id",[authJwt.verifyToken], controller.updatePaid); //ceklis
  app.delete("/api/bill/:bill_id",[authJwt.verifyToken], controller.delete); //ceklis

};