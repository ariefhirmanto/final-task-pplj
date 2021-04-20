const mongoose = require('mongoose');
mongoose.Promise = global.Promise;

const db = {};

db.mongoose = mongoose;

db.user = require("./user.model");
db.role = require("./role.model");
db.bill = require("./bill.model");

db.ROLES = ["user", "merchant", "admin"];

module.exports = db;