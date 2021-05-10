const db = require("../models");
const User = db.user;
const Transfer = db.transfer;

// Update a Bill by the id in the request
exports.updateAmount = (req, res) => {
  if (!req.body) {
    return res.status(400).send({
      message: "Data to update can not be empty!"
    });
  }

  const username = req.body.username;
  const new_amount = req.body.amount_credit;
  const category = req.body.category;

  if (category == "transfer" || category == "pay bill") {
    const transfer = new Transfer({
      username: username,
      change_balance: new_amount,
      category: category
    });

  User.findOneAndUpdate({username: username}, {$inc: { amount_credit: new_amount }} , { new: true, useFindAndModify: false })
    .then(data => {
      if (!data) {
        res.status(404).send({
          message: `Cannot update user data with username=${username}. Maybe User was not found!`
        });
      } else {
        transfer
        .save(transfer)
        .then(data => {
          res.send({ message: "Credits changed!" });
        });
      }
    })
    .catch(err => {
      res.status(500).send({
        message: "Error updating User with username=" + username
      });
    });
}};

exports.findOne = (req, res) => {  
  User.find({ username: req.body.username })
  .then(data => {
      if(!data || data == "") {
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
          message: "Error retrieving username with id " + req.body.username
      });
  });
};

exports.updateBill = (req, res) => {
  const username = req.body.username;
  const new_bill = req.body.bill_id;
  User.findOneAndUpdate({ username: username}, { $push: { bill_id: new_bill}}, {new: true, upsert: true, useFindAndModify: false })
  .then(data => {
    if (!data || data == "") {
      res.status(404).send({
        message: `Cannot update user with username=${username}`
      });
    } else {
      res.send({ message: "User bill has been updated!" });
    }
  })
  .catch(err => {
    res.status(500).send({
      message: "Error updating user bill with id=" + new_bill
    });
  });
}

exports.findTransferHistOwner = (req, res) => {  
  Transfer.find({ username: req.params.username })
  .then(data => {
      if(!data) {
          return res.status(404).send({
              message: "Transfer history not found " + req.params.username
          });            
      }
      res.send(data);
  }).catch(err => {
      if(err.kind === 'ObjectId') {
          return res.status(404).send({
              message: "Transfer hist not found with username " + req.params.username
          });                
      }
      return res.status(500).send({
          message: "Transfer history retrieving Bill with username " + req.params.username
      });
  });
};