const db = require("../models");
const Bill = db.bill;

exports.findAllBill = (req, res) => {
  Bill.find()
    .then(data => {
        res.send(data);
    }).catch(err => {
        res.status(500).send({
            message: err.message || "Some error occurred while retrieving notes."
        });
    });
};

// Find a single Bill with an id
exports.findBill = (req, res) => {  
  Bill.find({ bill_id: req.params.bill_id })
  .then(data => {
      if(!data) {
          return res.status(404).send({
              message: "Bill not found " + req.params.bill_id
          });            
      }
      res.send(data);
  }).catch(err => {
      if(err.kind === 'ObjectId') {
          return res.status(404).send({
              message: "Bill not found with id " + req.params.bill_id
          });                
      }
      return res.status(500).send({
          message: "Error retrieving Bill with id " + req.params.bill_id
      });
  });
};

// Create and Save a new Bill
exports.create = (req, res) => {
  // Validate request
  if (!req.body.bill_id) {
    res.status(400).send({ message: "Content can not be empty!" });
    return;
  }

  // Create a Tutorial
  const bill = new Bill({
    bill_name: req.body.bill_name,
    bill_id: req.body.bill_id,
    bill_owner: req.body.bill_owner,
    bill_sender: req.body.bill_sender,
    amount: req.body.amount,
    description: req.body.description,
    isPaid: false
  });

  // Save Bill in the database
  bill
    .save(bill)
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while creating the Bill."
      });
    });
};

// Update a Bill by the id in the request
exports.updatePaid = (req, res) => {
  if (!req.body) {
    return res.status(400).send({
      message: "Data to update can not be empty!"
    });
  }

  const id = req.params.bill_id;

  Bill.findOneAndUpdate(id, { isPaid: true } , { new: true, useFindAndModify: false })
    .then(data => {
      if (!data) {
        res.status(404).send({
          message: `Cannot update bill with id=${id}. Maybe Bill was not found!`
        });
      } else {
        res.send({ message: "Bill has been paid!" });
      }
    })
    .catch(err => {
      res.status(500).send({
        message: "Error updating Bill with id=" + id
      });
    });
};

// Delete a Bill with the specified id in the request
exports.delete = (req, res) => {
  const id = req.params.bill_id;
  Bill.findOneAndRemove({ bill_id:id })
    .then(data => {
      if (!data) {
        res.status(404).send({
          message: `Cannot delete bill with id=${id}. Maybe Bill was not found!`
        });
      } else {
        res.send({
          message: "Bill was deleted successfully!"
        });
      }
    })
    .catch(err => {
      res.status(500).send({
        message: "Could not delete Bill with id = " + id
      });
    });
};


