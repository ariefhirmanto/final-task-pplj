const db = require("../models");
const User = db.user;

checkUsernameExist = (req, res, next) => {
    User.findOne({
        username: req.body.username
        }).exec((err, user) => {
        if (err) {
            res.status(500).send({ message: err });
            return;
        }

        if (!user) {
            res.status(400).send({ message: "Failed! Username didn't exist!" });
            return;
        }

        next();
    });
}

const verifyUsername = {
    checkUsernameExist
  };
  
  module.exports = verifyUsername;