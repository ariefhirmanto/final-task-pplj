const db = require("../models");
const User = db.user;

// Update a Bill by the id in the request
exports.updateAmount = (req, res) => {
  if (!req.body) {
    return res.status(400).send({
      message: "Data to update can not be empty!"
    });
  }

  const username = req.params.username;
  const new_amount = req.body.amount_credit;

  User.findOneAndUpdate(username, { amount_credit: new_amount } , { new: true, useFindAndModify: false })
    .then(data => {
      if (!data) {
        res.status(404).send({
          message: `Cannot update user data with username=${username}. Maybe User was not found!`
        });
      } else {
        res.send({ message: "Credits changed!" });
      }
    })
    .catch(err => {
      res.status(500).send({
        message: "Error updating User with username=" + username
      });
    });
};

exports.findOne = (req, res) => {  
  User.find({ username: req.body.username })
  .then(data => {
      if(!data) {
          return res.status(404).send({
              message: "User not found " + req.body.username
          });            
      }
      res.send(data);
  }).catch(err => {
      if(err.kind === 'ObjectId') {
          return res.status(404).send({
              message: "User not found with username " + req.body.username
          });                
      }
      return res.status(500).send({
          message: "Error retrieving node with id " + req.body.username
      });
  });
};