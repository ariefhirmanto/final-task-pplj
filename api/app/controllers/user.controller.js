const db = require("../models");
const User = db.user;

// exports.allAccess = (req, res) => {
//     res.status(200).send("Public Content.");
//   };
  
//   exports.userBoard = (req, res) => {
//     res.status(200).send("User Content.");
//   };
  
//   exports.adminBoard = (req, res) => {
//     res.status(200).send("Admin Content.");
//   };
  
//   exports.merchantBoard = (req, res) => {
//     res.status(200).send("Merchant Content.");
//   };

// Update a Bill by the id in the request
exports.updateAmount = (req, res) => {
  if (!req.body) {
    return res.status(400).send({
      message: "Data to update can not be empty!"
    });
  }

  const id = req.params.id;
  const new_amount = req.body.amount_credit;

  User.findOneAndUpdate(id, { amount_credit: new_amount } , { new: true, useFindAndModify: false })
    .then(data => {
      if (!data) {
        res.status(404).send({
          message: `Cannot update user data with id=${id}. Maybe User was not found!`
        });
      } else {
        res.send({ message: "Credits changed!" });
      }
    })
    .catch(err => {
      res.status(500).send({
        message: "Error updating User with id=" + id
      });
    });
};